"""
Pacvue 文档搜索服务

支持对 Markdown 文档进行语义搜索
"""

import os
import sys
import io

# 设置 Windows 控制台编码为 UTF-8
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

from dotenv import load_dotenv
from doc_loader import get_doc_loader, init_with_confluence
from constant import confluence_folder_ids

# FastAPI 相关
from fastapi import FastAPI
from pydantic import BaseModel

# 加载环境变量
load_dotenv()

# 获取当前脚本目录，用于定位 docs 目录
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS_DIR = os.path.join(SCRIPT_DIR, "docs")

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
            folder_ids=confluence_folder_ids,
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
