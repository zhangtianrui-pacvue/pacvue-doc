"""
Pacvue 文档搜索服务

支持对 Markdown 文档进行语义搜索
"""

import os
import sys
import io

# 设置 Windows 控制台编码为 UTF-8
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace', line_buffering=True)
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace', line_buffering=True)

import threading
from datetime import datetime, timezone

from dotenv import load_dotenv
from doc_loader import get_doc_loader, init_with_confluence, get_last_confluence_update
from constant import confluence_folder_ids

# FastAPI 相关
from fastapi import FastAPI
from pydantic import BaseModel

# 加载环境变量
load_dotenv()

# 获取当前脚本目录，用于定位 docs 目录
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS_DIR = os.path.join(SCRIPT_DIR, "docs")
CHROMA_DIR = os.path.join(SCRIPT_DIR, "chroma_db")

# Confluence 更新间隔（天）
CONFLUENCE_UPDATE_INTERVAL_DAYS = 7


def _do_confluence_update(force=False):
    """
    执行 Confluence 文档更新
    
    Args:
        force: 是否强制更新（忽略内存中的已初始化标志）
    """
    try:
        init_with_confluence(
            folder_ids=confluence_folder_ids,
            docs_dir=DOCS_DIR,
            force=force
        )
        print("[OK] Confluence 文档更新完成")
    except Exception as e:
        print(f"[错误] Confluence 文档更新失败: {e}")


def _key_listener():
    """
    后台监听键盘输入，按 r 键触发 Confluence 文档手动更新
    
    使用 msvcrt（Windows 内置模块）进行非阻塞键盘检测
    """
    try:
        import msvcrt
    except ImportError:
        print("[警告] msvcrt 模块不可用（仅 Windows 支持），按键监听已禁用")
        return
    
    import time
    print("[信息] 按 r 键可手动触发 Confluence 文档更新")
    
    while True:
        try:
            if msvcrt.kbhit():
                key = msvcrt.getch().decode('utf-8', errors='ignore').lower()
                if key == 'r':
                    print("\n" + "=" * 60)
                    print("[手动触发] 正在重新加载 Confluence 文档...")
                    print("=" * 60)
                    _do_confluence_update(force=True)
                    print("=" * 60 + "\n")
            else:
                # 避免 CPU 空转，短暂休眠
                time.sleep(0.1)
        except Exception as e:
            print(f"[错误] 按键监听异常: {e}")
            time.sleep(1)


# ========== FastAPI 应用 ==========
app = FastAPI(title="Pacvue 智能文档助手 API")

@app.on_event("startup")
async def startup_event():
    """
    应用启动时初始化文档加载器
    
    - 始终加载本地 Markdown 文档和已有向量存储
    - 检查距上次 Confluence 更新是否超过 7 天，超过则自动更新
    - 启动后台线程监听按 r 键手动触发更新
    """
    print("\n" + "=" * 60)
    print("正在初始化文档加载器...")
    print("=" * 60)
    
    try:
        # 先加载本地文档和已有向量存储
        loader = get_doc_loader(docs_dir=DOCS_DIR)
        loader.get_or_create_vector_store()
        print("[OK] 本地文档和向量存储已就绪")
        
        # 检查是否需要更新 Confluence 文档
        last_update = get_last_confluence_update(CHROMA_DIR)
        
        if last_update is None:
            print("[信息] 从未同步过 Confluence 文档，正在执行首次同步...")
            _do_confluence_update()
        else:
            now = datetime.now(timezone.utc)
            days_since = (now - last_update).days
            print(f"[信息] 上次 Confluence 同步时间: {last_update.strftime('%Y-%m-%d %H:%M:%S UTC')}")
            print(f"[信息] 距今 {days_since} 天")
            
            if days_since >= CONFLUENCE_UPDATE_INTERVAL_DAYS:
                print(f"[信息] 超过 {CONFLUENCE_UPDATE_INTERVAL_DAYS} 天未更新，正在同步 Confluence 文档...")
                _do_confluence_update()
            else:
                remaining = CONFLUENCE_UPDATE_INTERVAL_DAYS - days_since
                print(f"[信息] Confluence 文档仍在有效期内，{remaining} 天后自动更新")
                
    except Exception as e:
        print(f"[警告] 文档加载器初始化时出现问题: {e}")
        # 即使 Confluence 加载失败，也尝试只加载本地文档
        try:
            loader = get_doc_loader(docs_dir=DOCS_DIR)
            loader.get_or_create_vector_store()
            print("[OK] 已加载本地文档")
        except Exception as inner_e:
            print(f"[错误] 本地文档加载也失败: {inner_e}")
    
    print("=" * 60)
    print("[信息] 按 r 键可随时手动触发 Confluence 文档更新")
    print("=" * 60 + "\n")
    
    # 启动按键监听后台线程
    listener_thread = threading.Thread(target=_key_listener, daemon=True)
    listener_thread.start()


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
