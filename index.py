"""
Pacvue 智能文档助手

基于 LangChain + DeepSeek 的智能文档问答 Agent
支持对 Markdown 文档进行语义搜索和智能问答
"""

import os
import sys
import io
import json

# 设置 Windows 控制台编码为 UTF-8
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import InMemorySaver
from tools import get_tools
from typing import Any, Dict, List
from doc_loader import get_doc_loader, init_with_confluence
from constant import online_docs_Ids

# FastAPI 和 SSE 相关
from fastapi import FastAPI
from pydantic import BaseModel
from sse_starlette.sse import EventSourceResponse

# 加载环境变量
load_dotenv()

# 获取当前脚本目录，用于定位 docs 目录
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS_DIR = os.path.join(SCRIPT_DIR, "docs")

# 检查 API Key
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
if not DEEPSEEK_API_KEY:
    print("[警告] 未找到 DEEPSEEK_API_KEY 环境变量")
    print("请在 .env 文件中设置：")
    print("DEEPSEEK_API_KEY=your_api_key_here\n")


# 系统提示词
SYSTEM_PROMPT = """你是 Pacvue 智能文档助手，专门帮助用户查询和理解 Pacvue 相关的文档内容。

你的职责：
1. 根据用户的问题，使用 search_docs 工具在文档库中搜索相关内容
2. 基于搜索结果，用清晰、准确的语言回答用户的问题
3. 如果搜索结果不足以回答问题，可以用 list_docs 查看文档列表，然后用如果metadata["source"] !== "confluence"，则使用 read_doc 直接读取相关文档
4. 当用户要求刷新文档时，使用 refresh_docs 工具

回答规范：
- 使用中文回答
- 回答要简洁明了，重点突出
- 引用文档内容时，注明来源
- 如果不确定，不要编造信息

可用工具：
- search_docs: 在文档中搜索相关内容（语义搜索）
- list_docs: 列出所有可用文档
- read_doc: 读取指定文档的完整内容（当知道文档名时直接使用）
- refresh_docs: 刷新文档索引
"""


def create_agent(use_memory: bool = False):
    """
    创建智能文档助手 Agent
    
    Args:
        use_memory: 是否启用本地内存记忆（CLI 模式用 True，LangGraph Studio 用 False）
    """
    
    # 初始化 DeepSeek 模型
    model = ChatDeepSeek(
        model="deepseek-chat",
        temperature=0.1,
        max_tokens=2048,
    )
    
    # 获取工具列表
    tools = get_tools()
    
    # 创建 ReAct Agent
    if use_memory:
        # CLI 本地运行：使用内存检查点保存对话历史
        checkpointer = InMemorySaver()
        graph = create_react_agent(
            model=model,
            tools=tools,
            prompt=SYSTEM_PROMPT,
            checkpointer=checkpointer
        )
    else:
        # LangGraph Studio/API：平台自动处理持久化，不传 checkpointer
        graph = create_react_agent(
            model=model,
            tools=tools,
            prompt=SYSTEM_PROMPT
        )
    
    return graph

# 给 LangGraph Studio 导出（不带自定义 checkpointer）
agent = create_agent(use_memory=False)

# ========== FastAPI 应用 ==========
app = FastAPI(title="Pacvue 智能文档助手 API")


@app.on_event("startup")
async def startup_event():
    """
    应用启动时初始化文档加载器
    
    加载本地 Markdown 文档和 Confluence 文档
    """
    print("\n" + "=" * 60)
    print("正在初始化文档加载器...")
    print("=" * 60)
    
    try:
        # 使用新的初始化函数，同时加载本地文档和 Confluence 文档
        init_with_confluence(
            page_ids=online_docs_Ids,
            docs_dir=DOCS_DIR
        )
        print("[OK] 文档加载器初始化完成")
    except Exception as e:
        print(f"[警告] 文档加载器初始化时出现问题: {e}")
        # 即使 Confluence 加载失败，也尝试只加载本地文档
        try:
            loader = get_doc_loader(docs_dir=DOCS_DIR)
            loader.get_or_create_vector_store()
            print("[OK] 已加载本地文档")
        except Exception as inner_e:
            print(f"[错误] 本地文档加载也失败: {inner_e}")
    
    print("=" * 60 + "\n")


class ChatRequest(BaseModel):
    query: str

def _try_parse_tool_payload(content: Any) -> Dict[str, Any]:
    """兼容 ToolMessage.content 可能是 dict / JSON 字符串 / 其它类型"""
    if isinstance(content, dict):
        return content
    if isinstance(content, str):
        try:
            return json.loads(content)
        except Exception:
            return {"raw": content}
    return {"raw": content}


@app.post("/chat/stream")
async def chat_stream_api(req: ChatRequest):
    """
    流式聊天接口（SSE）
    
    逐 token 返回 Agent 回答
    """
    async def event_generator():
        for chunk in chat_stream(agent, req.query):
            yield {"data": chunk}
        yield {"data": "[DONE]"}
    return EventSourceResponse(event_generator())


@app.post("/chat")
def chat_api(req: ChatRequest):
    """
    非流式聊天接口
    
    返回完整的 Agent 回答
    """
    answer = chat(agent, req.query)

    return answer

# 不创建agent 
@app.post("/chat_no_agent")
def chat_no_agent_api(req: ChatRequest):
    doc_loader = get_doc_loader(docs_dir=DOCS_DIR)
    search_results = doc_loader.search(req.query, k=5)
    
    # 转换为与 chat 函数一致的返回格式
    results = []
    citations = []
    print(search_results, 'search_results', flush=True)
    
    for doc in search_results:
        result_item = {
            "content": doc.page_content,
            "metadata": doc.metadata
        }
        results.append(result_item)
        
        # 生成引用信息
        citation = {
            "source": doc.metadata.get("source", ""),
            "filename": doc.metadata.get("filename", "")
        }
        if citation["source"] or citation["filename"]:
            citations.append(citation)
    
    return {
        "answer": "",  # 无 agent 处理，无回答
        "results": results,
        "citations": citations
    }
    

def chat_stream(agent, user_input: str, thread_id: str = "default"):
    """
    与 Agent 进行流式对话，逐 token 输出最终结果
    
    使用 stream_mode="messages" 实现真正的流式输出（打字机效果）
    只输出最终回复，过滤掉工具调用等中间过程
    
    Args:
        agent: ReAct Agent 实例
        user_input: 用户输入
        thread_id: 会话ID，用于区分不同对话（实现记忆）
        
    Yields:
        逐 token 的文本片段
    """
    try:
        # 配置 thread_id 用于记忆，recursion_limit 防止无限循环
        config = {
            "configurable": {"thread_id": thread_id},
            "recursion_limit": 15
        }
        
        # 使用 messages 模式获取 token 级别的流式输出
        for message_chunk, metadata in agent.stream(
            {"messages": [{"role": "user", "content": user_input}]},
            config=config,
            stream_mode="messages"
        ):
       
            # metadata 包含 langgraph_node 等信息
            # 只输出来自 agent 节点的 AIMessageChunk 内容
            # 过滤掉工具调用和工具返回的消息
            if (
                metadata.get("langgraph_node") == "agent"  # 来自 agent 节点
                and hasattr(message_chunk, 'content')       # 有内容
                and message_chunk.content                   # 内容非空
                and not getattr(message_chunk, 'tool_call_chunks', None)  # 不是工具调用
            ):
                yield message_chunk.content
                
    except Exception as e:
        yield f"处理请求时出错: {str(e)}"


def chat(agent, user_input: str, thread_id: str = "default") -> str:
    """
    与 Agent 进行对话（非流式）
    
    Args:
        agent: ReAct Agent 实例
        user_input: 用户输入
        thread_id: 会话ID，用于区分不同对话（实现记忆）
        
    Returns:
        Agent 回复
    """
    try:
        # 配置 thread_id 用于记忆，recursion_limit 防止无限循环
        config = {
            "configurable": {"thread_id": thread_id},
            "recursion_limit": 15
        }
        
        result = agent.invoke(
            {"messages": [{"role": "user", "content": user_input}]},
            config=config
        )
        
        # 获取最后一条消息作为回复
        messages = result.get("messages", [])

        for m in messages:
            if getattr(m, "name", None) == "search_docs":
                print("FOUND search_docs tool msg content:", getattr(m, "content", None))
        final_answer = ""
        print(messages[-1])
        if messages:
            last = messages[-1]
            final_answer = getattr(last, "content", "") or (last.get("content") if isinstance(last, dict) else "")

         # 3) 从 tool messages 里捞 search_docs 证据
        results: List[Dict[str, Any]] = []
        citations: List[Dict[str, Any]] = []

        for m in messages:
            name = getattr(m, "name", None) or (m.get("name") if isinstance(m, dict) else None)
            mtype = getattr(m, "type", None) or (m.get("type") if isinstance(m, dict) else None)

            # tool 消息判断：有些实现用 type=="tool"，有些看 name 是否存在
            if name == "search_docs" or (mtype == "tool" and name == "search_docs"):
                content = getattr(m, "content", None) or (m.get("content") if isinstance(m, dict) else None)
                payload = _try_parse_tool_payload(content)

                # 如果 search_docs 返回的是 {"results":..., "citations":...}
                if isinstance(payload, dict):
                    results.extend(payload.get("results", []) or [])
                    citations.extend(payload.get("citations", []) or [])

        # 4) 返回给 GPT Action（最适合你后续在 GPT Instructions 里强制引用）
        return {
            "answer": final_answer,
            "results": results,
            "citations": citations
        }


        
    except Exception as e:
        return f"处理请求时出错: {str(e)}"


def interactive_mode():
    """交互式对话模式（带对话记忆）"""
    
    print("=" * 60)
    print("Pacvue 智能文档助手")
    print("=" * 60)
    print("\n基于 LangChain + DeepSeek 的智能文档问答系统")
    print("支持对话记忆，可以进行多轮对话")
    print("输入问题开始对话，输入 'quit' 或 'exit' 退出\n")
    
    # 为本次交互会话创建唯一的 thread_id
    import uuid
    thread_id = str(uuid.uuid4())
    
    # 检查 API Key
    if not DEEPSEEK_API_KEY:
        print("[错误] 未设置 DEEPSEEK_API_KEY")
        print("请创建 .env 文件并设置 API Key")
        return
    
    # 创建 Agent（CLI 模式启用记忆）
    print("[初始化] 正在初始化 Agent...")
    try:
        agent = create_agent(use_memory=True)
        print("[完成] Agent 初始化完成\n")
    except Exception as e:
        print(f"[错误] Agent 初始化失败: {str(e)}")
        return
    
    # 显示可用文档
    print("[加载] 正在加载文档索引...")
    from tools import list_docs
    print(list_docs.invoke({}))
    print()
    
    # 交互循环
    print("-" * 60)
    while True:
        try:
            user_input = input("你: ").strip()
            
            # 检查退出命令
            if user_input.lower() in ['quit', 'exit', '退出', 'q']:
                print("\n再见！感谢使用 Pacvue 智能文档助手")
                break
            
            # 跳过空输入
            if not user_input:
                continue
            
            # 处理特殊命令
            if user_input.lower() in ['help', '帮助', '?']:
                print_help()
                continue
            
            if user_input.lower() in ['docs', '文档', 'list']:
                print(list_docs.invoke({}))
                continue
            
            # 调用 Agent 处理（流式输出，带记忆）
            print("\n助手: ", end="", flush=True)
            for chunk in chat_stream(agent, user_input, thread_id):
                print(chunk, end="", flush=True)
            print()
            
        except KeyboardInterrupt:
            print("\n\n程序已中断，再见！")
            break
        except Exception as e:
            print(f"\n[错误] 发生错误: {str(e)}\n")

def print_help():
    """打印帮助信息"""
    print("""
帮助信息
-----------
可用命令：
  - help / 帮助 / ?  : 显示此帮助信息
  - docs / 文档 / list: 列出可用文档
  - quit / exit / 退出: 退出程序

使用示例：
  - "Pacvue 是什么？"
  - "Pacvue 支持哪些电商平台？"
  - "如何获取 API 密钥？"
  - "刷新文档索引"
""")


def single_query(query: str):
    """
    单次查询模式
    
    Args:
        query: 查询内容
    """
    if not DEEPSEEK_API_KEY:
        print("[错误] 未设置 DEEPSEEK_API_KEY")
        return
    
    agent = create_agent(use_memory=True)
    for chunk in chat_stream(agent, query):
        print(chunk, end="", flush=True)
    print()


if __name__ == "__main__":
    # 支持命令行参数查询
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
        single_query(query)
    else:
        # 默认进入交互模式
        interactive_mode()

        