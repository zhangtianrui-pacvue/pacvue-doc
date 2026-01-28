"""
自定义工具模块

提供给 Agent 使用的工具：
1. search_docs - 在文档中搜索相关内容（支持跨语言搜索）
2. list_docs - 列出所有可用文档
3. read_doc - 读取指定文档的完整内容
4. refresh_docs - 刷新文档索引
"""

from langchain_core.documents.base import Document


import os
from typing import Optional
from langchain_core.tools import tool
from pydantic import BaseModel, Field
from typing import Any, Dict, List, Optional
from doc_loader import get_doc_loader, DocLoader
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()


# 获取当前脚本目录
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS_DIR = os.path.join(SCRIPT_DIR, "docs")


class SearchDocsInput(BaseModel):
    """文档搜索工具的输入模型"""
    query: str = Field(description="搜索查询内容，可以是问题或关键词（支持中英文）")
    num_results: int = Field(default=3, description="返回结果数量，默认为3")


@tool(args_schema=SearchDocsInput)
def search_docs(query: str, num_results: int = 3) -> str:
    """在 Pacvue 文档库中搜索相关内容
    
    根据用户的问题或关键词，在文档库中查找最相关的内容片段。
    适用于回答关于组件方面的问题。
    
    Args:
        query: 搜索查询内容（支持中英文）
        num_results: 返回结果数量
        
    Returns:
        搜索结果的文本内容
    """
    try:
        loader = get_doc_loader(docs_dir=DOCS_DIR)
        results = loader.search(query, k=num_results)
        print("DEBUG search_docs:", "query=", query, "k=", num_results, "len(results)=", len(results))
        for idx, doc in enumerate[Document](results):
            if idx == 0:
                print("DEBUG first doc type=", type(doc), "metadata=", getattr(doc, "metadata", None))
        
        if not results:
            return {
                "results": [],
                "citations": [],
                "message": "未找到相关文档内容。请尝试使用不同的关键词搜索。"
            }
        
        # 格式化输出：将 Document 列表转换为结构化字典
        structured_results: List[Dict[str, Any]] = []
        for doc in results:
            meta = doc.metadata or {}
            structured_results.append({
                "content": doc.page_content,
                "title": meta.get("title", meta.get("filename", "")),
                "url": meta.get("url", ""),
                "source": meta.get("source", "local"),
            })
        
        # 生成 citations（按文档去重，取前 3 个）
        citations: List[Dict[str, Any]] = []
        seen = set()
        for r in structured_results:
            key = (r.get("title"), r.get("url"))
            if key in seen:
                continue
            seen.add(key)
            citations.append({
                "title": r.get("title"),
                "url": r.get("url"),
                "source": r.get("source"),
            })
            if len(citations) >= 3:
                break

        return {
            "results": structured_results,
            "citations": citations
        }
        
    except Exception as e:
        return f"搜索出错: {str(e)}"


@tool
def list_docs() -> str:
    """列出所有可用的 Pacvue 文档
    
    显示文档库中所有已索引的 Markdown 文档文件名。
    
    Returns:
        文档列表
    """
    try:
        loader = get_doc_loader(docs_dir=DOCS_DIR)
        docs = loader.list_documents()
        
        if not docs:
            return "文档库为空。请在 docs 目录下添加 Markdown 文档。"
        
        output_parts = [f"文档库中共有 {len(docs)} 个文档：\n"]
        
        for i, doc_name in enumerate(docs, 1):
            output_parts.append(f"{i}. {doc_name}")
        
        return "\n".join(output_parts)
        
    except Exception as e:
        return f"获取文档列表出错: {str(e)}"


class ReadDocInput(BaseModel):
    """读取文档工具的输入模型"""
    filename: str = Field(description="要读取的文档文件名，例如 'Transfer.md'")


@tool(args_schema=ReadDocInput)
def read_doc(filename: str) -> str:
    """读取指定文档的完整内容
    
    根据文件名直接读取文档的全部内容。
    当通过 list_docs 发现目标文档后，可以用此工具获取完整内容。
    
    Args:
        filename: 文档文件名，如 'Transfer.md'
        
    Returns:
        文档的完整内容
    """
    try:
        # 构建文件路径
        filepath = os.path.join(DOCS_DIR, filename)
        
        # 检查文件是否存在
        if not os.path.exists(filepath):
            return f"文档 '{filename}' 不存在。请使用 list_docs 查看可用文档。"
        
        # 读取文件内容
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 如果内容过长，截断并提示
        max_length = 8000
        if len(content) > max_length:
            content = content[:max_length]
            content += f"\n\n... 文档内容过长，已截断。完整文档共 {len(content)} 字符。"
        
        return f"【{filename}】的内容：\n\n{content}"
        
    except Exception as e:
        return f"读取文档出错: {str(e)}"


@tool
def refresh_docs() -> str:
    """刷新文档索引
    
    重新加载 docs 目录下的所有 Markdown 文档，并更新向量索引。
    当添加、修改或删除文档后，需要调用此工具来更新索引。
    
    Returns:
        刷新结果信息
    """
    try:
        loader = get_doc_loader(docs_dir=DOCS_DIR)
        loader.refresh()
        
        docs = loader.list_documents()
        return f"文档索引刷新完成！共索引 {len(docs)} 个文档。"
        
    except Exception as e:
        return f"刷新文档索引出错: {str(e)}"


# 导出所有工具
all_tools = [search_docs, list_docs, read_doc, refresh_docs]


def get_tools():
    """获取所有可用工具"""
    return all_tools


if __name__ == "__main__":
    # 测试工具
    print("=== 测试工具 ===\n")
    
    print("1. 列出文档:")
    print(list_docs.invoke({}))
    print()
    
    print("2. 搜索文档:")
    print(search_docs.invoke({"query": "Pacvue 是什么", "num_results": 2}))
    print()
    
    print("3. 工具信息:")
    for t in all_tools:
        print(f"  - {t.name}: {t.description[:50]}...")

