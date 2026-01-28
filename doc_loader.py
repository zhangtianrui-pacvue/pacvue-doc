"""
Markdown 文档加载和向量化处理模块

负责：
1. 加载指定目录下的所有 Markdown 文档
2. 对文档进行分割处理
3. 使用 HuggingFace Embeddings 进行向量化（默认使用 bge-m3 多语言模型）
4. 存储到 ChromaDB 向量数据库
5. 支持 Confluence 文档的集成
6. 支持中英文混合搜索
7. 支持跨语言搜索（英文查询 -> 中文文档）

注意：
- 如果更换 embedding 模型，需要删除 chroma_db 目录并重新构建向量存储
- 不同模型产生的向量空间不同，无法混用
"""

import os
import re
import shutil
import hashlib
from typing import List, Optional, Set, Tuple
from pathlib import Path

from langchain_community.document_loaders import TextLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_text_splitters import (
    MarkdownHeaderTextSplitter,
    RecursiveCharacterTextSplitter
)

# GraphRAG - 图增强检索
from langchain_graph_retriever import GraphRetriever
from graph_retriever.strategies import Eager
from langchain_graph_retriever.transformers import ShreddingTransformer


class DocLoader:
    """
    Markdown 文档加载器
    
    负责加载、分割、向量化和存储文档。
    支持本地 Markdown 文件和 Confluence 文档。
    支持中英文混合搜索（使用 bge-small-zh-v1.5 多语言 embedding 模型）。
    """
    
    # Markdown 标题分割配置
    HEADERS_TO_SPLIT = [
        ("#", "h1"),
        ("##", "h2"),
        ("###", "h3"),
        ("####", "h4"),
    ]
    
    def __init__(
        self,
        docs_dir: str = "./docs",
        persist_directory: str = "./chroma_db",
        embedding_model: str = "BAAI/bge-small-zh-v1.5"
    ):
        """
        初始化文档加载器
        
        Args:
            docs_dir: Markdown 文档目录路径
            persist_directory: ChromaDB 持久化目录
            embedding_model: HuggingFace Embedding 模型名称，默认使用 bge-small-zh-v1.5 多语言模型
                            支持中英文混合搜索
        """
        self.docs_dir = docs_dir
        self.persist_directory = persist_directory
        self.embedding_model = embedding_model
        
        # 初始化 Embeddings
        self.embeddings = HuggingFaceEmbeddings(
            model_name=embedding_model,
            model_kwargs={'device': 'cpu'},
            encode_kwargs={'normalize_embeddings': True}
        )
        
        # Markdown 标题分割器（用于本地 Markdown 文件）
        self.text_splitter = MarkdownHeaderTextSplitter(
            headers_to_split_on=self.HEADERS_TO_SPLIT,
            strip_headers=False
        )
        
        # 通用文本分割器（用于 Confluence 等非结构化文档）
        # chunk_size=1000 适合中英文混合文档
        # chunk_overlap=200 保留上下文连贯性
        self.general_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
            separators=[
                "\n\n",      # 段落
                "\n",        # 换行
                ". ",        # 英文句号（带空格）
                "。",        # 中文句号
                "; ",        # 英文分号
                "；",        # 中文分号
                ", ",        # 英文逗号
                "，",        # 中文逗号
                " ",         # 空格
                ""           # 字符
            ]
        )
        
        # 向量存储
        self.vector_store: Optional[Chroma] = None
    
    def load_documents(self) -> List[Document]:
        """
        加载目录下所有 Markdown 文档
        
        Returns:
            Document 列表
        """
        docs_path = Path(self.docs_dir)
        
        if not docs_path.exists():
            print(f"[警告] 文档目录不存在: {self.docs_dir}")
            return []
        
        documents = []
        
        # 遍历目录下所有 .md 文件
        for md_file in docs_path.glob("**/*.md"):
            try:
                loader = TextLoader(str(md_file), encoding='utf-8')
                docs = loader.load()
                
                # 添加文件名到 metadata
                for doc in docs:
                    doc.metadata['source'] = str(md_file)
                    doc.metadata['filename'] = md_file.name
                
                documents.extend(docs)
                print(f"[OK] 已加载: {md_file.name}")
                
            except Exception as e:
                print(f"[错误] 加载失败 {md_file.name}: {str(e)}")
        
        print(f"\n共加载 {len(documents)} 个文档")
        return documents
    
    def split_documents(self, documents: List[Document]) -> List[Document]:
        """
        对文档进行分割
        
        Args:
            documents: 原始文档列表
            
        Returns:
            分割后的文档列表
        """
        all_splits = []
        for doc in documents:
            # MarkdownHeaderTextSplitter.split_text 接受字符串，返回 Document 列表
            chunks = self.text_splitter.split_text(doc.page_content)
            # 将原始文档的 metadata 合并到每个 chunk
            for chunk in chunks:
                chunk.metadata.update(doc.metadata)
            all_splits.extend(chunks)
        
        print(f"文档分割完成，共 {len(all_splits)} 个片段")
        return all_splits
    
    def create_vector_store(self, documents: List[Document]) -> Chroma:
        """
        创建向量存储
        
        使用 ShreddingTransformer 扁平化 metadata，
        确保与 GraphRAG 兼容（ChromaDB 不支持嵌套 metadata）。
        
        Args:
            documents: 文档列表
            
        Returns:
            Chroma 向量存储实例
        """
        print("正在创建向量存储...")
        
        # 使用 ShreddingTransformer 扁平化 metadata
        # ChromaDB 不支持嵌套 metadata，这是 GraphRAG 的要求
        shredder = ShreddingTransformer()
        processed_docs = list(shredder.transform_documents(documents))
        print(f"[信息] 已使用 ShreddingTransformer 处理 {len(processed_docs)} 个文档")
        
        self.vector_store = Chroma.from_documents(
            documents=processed_docs,
            embedding=self.embeddings,
            persist_directory=self.persist_directory,
            collection_name="pacvue_docs"
        )
        
        print(f"[OK] 向量存储创建完成，保存在: {self.persist_directory}")
        return self.vector_store
    
    def load_vector_store(self) -> Optional[Chroma]:
        """
        加载已存在的向量存储
        
        Returns:
            Chroma 向量存储实例，如果不存在则返回 None
        """
        if not os.path.exists(self.persist_directory):
            return None
        
        try:
            self.vector_store = Chroma(
                persist_directory=self.persist_directory,
                embedding_function=self.embeddings,
                collection_name="pacvue_docs"
            )
            print(f"[OK] 已加载现有向量存储: {self.persist_directory}")
            return self.vector_store
        except Exception as e:
            print(f"[错误] 加载向量存储失败: {str(e)}")
            return None
    
    def get_or_create_vector_store(self) -> Chroma:
        """
        获取或创建向量存储
        
        如果向量存储已存在则加载，否则创建新的
        
        Returns:
            Chroma 向量存储实例
        """
        # 尝试加载已有的向量存储
        vector_store = self.load_vector_store()
        
        if vector_store is not None:
            return vector_store
        
        # 创建新的向量存储
        print("未找到现有向量存储，正在创建...")
        documents = self.load_documents()
        
        if not documents:
            raise ValueError("没有找到任何文档，请在 docs 目录下添加 Markdown 文件")
        
        splits = self.split_documents(documents)
        return self.create_vector_store(splits)
    
    def search(self, query: str, k: int = 1) -> List[Document]:
        """
        搜索相关文档（纯向量搜索）
        
        Args:
            query: 搜索查询
            k: 返回结果数量
            
        Returns:
            相关文档列表
        """
        if self.vector_store is None:
            self.get_or_create_vector_store()
        
        results = self.vector_store.similarity_search(query, k=k)
        return results
    
    def create_graph_retriever(
        self,
        k: int = 5,
        start_k: int = 1,
        max_depth: int = 2
    ) -> GraphRetriever:
        """
        创建 GraphRAG 检索器
        
        GraphRAG 通过文档的 metadata 属性建立图关系，
        在向量搜索的基础上进行图遍历，找到更相关的文档。
        
        Args:
            k: 返回结果数量
            start_k: 初始向量搜索返回的文档数
            max_depth: 图遍历的最大深度
            
        Returns:
            GraphRetriever 实例
        """
        if self.vector_store is None:
            self.get_or_create_vector_store()
        
        # 定义图边关系：基于 metadata 属性建立文档间的连接
        # - ("source", "source"): 相同来源的文档片段
        # - ("filename", "filename"): 相同文件名的片段（本地文档）
        # - ("title", "title"): 相同标题的片段（Confluence 文档）
        edges = [
            ("source", "source"),
            ("filename", "filename"),
            ("title", "title"),
        ]
        
        # 使用 Eager 策略进行图遍历
        strategy = Eager(k=k, start_k=start_k, max_depth=max_depth)
        
        retriever = GraphRetriever(
            store=self.vector_store,
            edges=edges,
            strategy=strategy,
        )
        
        return retriever
    
    def graph_search(self, query: str, k: int = 5) -> List[Document]:
        """
        使用 GraphRAG 进行图遍历搜索
        
        Args:
            query: 搜索查询
            k: 返回结果数量
            
        Returns:
            相关文档列表
        """
        retriever = self.create_graph_retriever(k=k)
        results = retriever.invoke(query)
        return results
    
    def hybrid_search(self, query: str, k: int = 5) -> List[Document]:
        """
        混合搜索：结合向量搜索和 GraphRAG 图遍历
        
        同时执行向量搜索和图遍历搜索，合并并去重结果，
        以获得更全面和相关的文档。
        
        Args:
            query: 搜索查询
            k: 返回结果数量
            
        Returns:
            去重后的相关文档列表
        """
        if self.vector_store is None:
            self.get_or_create_vector_store()
        
        # 执行向量搜索
        vector_results = self.search(query, k=k)
        
        # 执行图遍历搜索
        try:
            graph_results = self.graph_search(query, k=k)
        except Exception as e:
            print(f"[警告] GraphRAG 搜索失败，回退到向量搜索: {e}")
            return vector_results
        
        # 合并结果并去重（基于文档内容的哈希值）
        seen_hashes: Set[str] = set()
        merged_results: List[Document] = []
        
        # 先添加向量搜索结果（优先级更高）
        for doc in vector_results:
            content_hash = hashlib.sha1(doc.page_content.encode()).hexdigest()
            if content_hash not in seen_hashes:
                seen_hashes.add(content_hash)
                merged_results.append(doc)
        
        # 再添加图遍历结果
        for doc in graph_results:
            content_hash = hashlib.sha1(doc.page_content.encode()).hexdigest()
            if content_hash not in seen_hashes:
                seen_hashes.add(content_hash)
                merged_results.append(doc)
        
        # 返回前 k 个结果
        return merged_results[:k]
    
    def list_documents(self) -> List[str]:
        """
        列出所有已加载的文档
        
        Returns:
            文档文件名列表
        """
        docs_path = Path(self.docs_dir)
        
        if not docs_path.exists():
            return []
        
        return [f.name for f in docs_path.glob("**/*.md")]
    
    def refresh(self) -> None:
        """
        刷新向量存储（重新加载所有文档）
        """
        print("正在刷新向量存储...")
        
        # 删除旧的向量存储
        if os.path.exists(self.persist_directory):
            shutil.rmtree(self.persist_directory)
            print("已删除旧的向量存储")
        
        # 重新创建
        self.vector_store = None
        self.get_or_create_vector_store()
        print("[OK] 向量存储刷新完成")

    def add_documents(self, chunks: List[Document], ids: List[str]) -> None:
        """
        添加文档片段到向量存储
        
        使用 ShreddingTransformer 扁平化 metadata（GraphRAG 要求）。
        
        Args:
            chunks: Document 片段列表
            ids: 每个片段对应的唯一 ID 列表
        """
        if self.vector_store is None:
            self.get_or_create_vector_store()
        
        # 使用 ShreddingTransformer 扁平化 metadata
        shredder = ShreddingTransformer()
        processed_chunks = list(shredder.transform_documents(chunks))
        
        # 添加到向量存储
        self.vector_store.add_documents(processed_chunks, ids=ids)
        print(f"[OK] 已添加 {len(processed_chunks)} 个文档片段")

    def upsert_documents(self, chunks: List[Document], ids: List[str]) -> None:
        """
        更新或插入文档到向量存储（upsert）
        
        如果 ID 已存在则更新，否则插入新文档。
        使用 ShreddingTransformer 扁平化 metadata（GraphRAG 要求）。
        
        Args:
            chunks: Document 片段列表（已经过 ShreddingTransformer 处理）
            ids: 每个片段对应的唯一 ID 列表
        """
        if self.vector_store is None:
            self.get_or_create_vector_store()
        
        # 获取已存在的 ID
        collection = self.vector_store._collection
        existing_ids: Set[str] = set(collection.get()["ids"])
        
        # 分离需要更新和需要添加的文档
        to_update_chunks = []
        to_update_ids = []
        to_add_chunks = []
        to_add_ids = []
        
        for chunk, doc_id in zip(chunks, ids):
            if doc_id in existing_ids:
                to_update_chunks.append(chunk)
                to_update_ids.append(doc_id)
            else:
                to_add_chunks.append(chunk)
                to_add_ids.append(doc_id)
        
        # 更新已存在的文档
        if to_update_chunks:
            # ChromaDB 的 update 需要重新计算 embeddings
            embeddings_list = self.embeddings.embed_documents(
                [c.page_content for c in to_update_chunks]
            )
            metadatas = [c.metadata for c in to_update_chunks]
            
            collection.update(
                ids=to_update_ids,
                embeddings=embeddings_list,
                documents=[c.page_content for c in to_update_chunks],
                metadatas=metadatas
            )
            print(f"[OK] 已更新 {len(to_update_chunks)} 个文档片段")
        
        # 添加新文档
        if to_add_chunks:
            self.vector_store.add_documents(to_add_chunks, ids=to_add_ids)
            print(f"[OK] 已添加 {len(to_add_chunks)} 个新文档片段")

    def add_confluence_docs(self, docs: List[Document]) -> None:
        """
        添加 Confluence 文档到向量存储
        
        对文档进行分割后，使用 ShreddingTransformer 扁平化 metadata，
        然后使用 upsert 方式添加到向量存储。
        
        Args:
            docs: Confluence 文档列表
        """
        if not docs:
            print("[警告] 没有 Confluence 文档需要添加")
            return
        
        # 分割文档
        chunks = self.split_documents(docs)
        
        # 使用 ShreddingTransformer 扁平化 metadata（GraphRAG 要求）
        shredder = ShreddingTransformer()
        processed_chunks = list(shredder.transform_documents(chunks))
        print(f"[信息] 已使用 ShreddingTransformer 处理 {len(processed_chunks)} 个 Confluence 文档片段")
        
        # 生成稳定的 ID
        ids = self._generate_confluence_ids(processed_chunks)
        
        # 使用 upsert 方式添加
        self.upsert_documents(processed_chunks, ids)
    
    @staticmethod
    def _generate_confluence_ids(chunks: List[Document]) -> List[str]:
        """
        为 Confluence 文档片段生成稳定的唯一 ID
        
        Args:
            chunks: 文档片段列表
            
        Returns:
            ID 列表
        """
        ids = []
        for chunk in chunks:
            page_id = chunk.metadata.get("id", "unknown")
            content_hash = hashlib.sha1(
                chunk.page_content.encode("utf-8")
            ).hexdigest()[:16]
            ids.append(f"confluence:{page_id}:{content_hash}")
        return ids


# 全局文档加载器实例
_doc_loader: Optional[DocLoader] = None
# 标记是否已初始化 Confluence 文档
_confluence_initialized: bool = False


def get_doc_loader(docs_dir: str = "./docs") -> DocLoader:
    """
    获取文档加载器单例
    
    注意：此函数仅创建 DocLoader 实例，不会自动加载 Confluence 文档。
    如需加载 Confluence 文档，请调用 init_with_confluence()。
    
    Args:
        docs_dir: 文档目录路径
        
    Returns:
        DocLoader 实例
    """
    global _doc_loader
    
    if _doc_loader is None:
        _doc_loader = DocLoader(docs_dir=docs_dir)
    
    return _doc_loader


def init_with_confluence(
    page_ids: List[str],
    confluence_base_url: str = "https://pacvue-enterprise.atlassian.net",
    docs_dir: str = "./docs"
) -> DocLoader:
    """
    初始化文档加载器并加载 Confluence 文档
    
    这是完整初始化的入口函数，会：
    1. 创建/获取 DocLoader 单例
    2. 加载本地 Markdown 文档（如果向量存储不存在）
    3. 加载并添加 Confluence 文档
    
    Args:
        page_ids: 要加载的 Confluence 页面 ID 列表
        confluence_base_url: Confluence 实例的基础 URL
        docs_dir: 本地文档目录路径
        
    Returns:
        初始化完成的 DocLoader 实例
    """
    global _confluence_initialized
    
    # 获取或创建 DocLoader
    loader = get_doc_loader(docs_dir=docs_dir)
    
    # 确保向量存储已创建
    loader.get_or_create_vector_store()
    
    # 避免重复加载 Confluence 文档
    if _confluence_initialized:
        print("[信息] Confluence 文档已加载，跳过")
        return loader
    
    # 加载 Confluence 文档
    try:
        from confluence_get import ConfluenceLoader
        
        print("\n正在加载 Confluence 文档...")
        confluence_loader = ConfluenceLoader(base_url=confluence_base_url)
        page_ids = confluence_loader.get_folder_docs_ids(folder_id="2196631")
        confluence_docs = confluence_loader.load_by_page_ids(page_ids)
        
        if confluence_docs:
            loader.add_confluence_docs(confluence_docs)
            _confluence_initialized = True
            print(f"[OK] 已加载 {len(confluence_docs)} 个 Confluence 页面")
        else:
            print("[警告] 未能加载任何 Confluence 文档")
            
    except ValueError as e:
        # 环境变量未设置
        print(f"[警告] 无法加载 Confluence 文档: {e}")
    except Exception as e:
        print(f"[错误] 加载 Confluence 文档时出错: {e}")
    
    return loader


if __name__ == "__main__":
    # 测试代码
    md_text = """## Title

This is content under title.

### Subtitle

More content here.
"""

    header_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=DocLoader.HEADERS_TO_SPLIT,
        strip_headers=False,
    )

    docs = header_splitter.split_text(md_text)

    for d in docs:
        print(f"Metadata: {d.metadata}")
        print(f"Content: {d.page_content[:80]}")
        print("-" * 40)
