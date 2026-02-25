import os
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_graph_retriever.transformers import ShreddingTransformer

from connectors.confluence_client import ConfluenceLoader
from ingest.manifest_store import ManifestStore
from ingest.scanner import scan_local_markdown
from indexing.chroma_store import ChromaStore
from retrieve.search_service import SearchService
from retrieve.splitter import DocumentSplitter
from runtime.settings import (
    DEFAULT_CHUNK_STRATEGY_VERSION,
    DEFAULT_INDEX_VERSION,
)


class DocLoader:
    """
    文档服务门面：负责 ingest/index/retrieve 编排。
    """

    def __init__(
        self,
        docs_dir: str = "./docs",
        persist_directory: str = "./chroma_db",
        embedding_model: str = "BAAI/bge-small-zh-v1.5",
        source_repo: Optional[str] = None,
        chunk_strategy_version: str = DEFAULT_CHUNK_STRATEGY_VERSION,
        index_version: str = DEFAULT_INDEX_VERSION
    ):
        self.docs_dir = docs_dir
        self.persist_directory = persist_directory
        self.embedding_model = embedding_model
        self.source_repo = source_repo or Path(self.docs_dir).resolve().parent.name
        self.chunk_strategy_version = chunk_strategy_version
        self.index_version = index_version
        self.manifest_path = os.path.join(self.persist_directory, "manifest.jsonl")
        self._local_ingested_once = False

        self.embeddings = HuggingFaceEmbeddings(
            model_name=embedding_model,
            model_kwargs={"device": "cpu"},
            encode_kwargs={"normalize_embeddings": True}
        )
        self.splitter = DocumentSplitter()
        self.vector_store: Optional[Chroma] = None
        self.search_service: Optional[SearchService] = None
        self.manifest_store = ManifestStore(self.manifest_path)

    def load_documents(self) -> List[Document]:
        return scan_local_markdown(self.docs_dir, self.source_repo)

    def split_documents(self, documents: List[Document]) -> List[Document]:
        splits = self.splitter.split_documents(documents)
        print(f"文档分割完成，共 {len(splits)} 个片段")
        return splits

    def create_vector_store(self, documents: List[Document]) -> Chroma:
        print("正在创建向量存储...")
        shredder = ShreddingTransformer()
        processed_docs = list(shredder.transform_documents(documents))
        self.vector_store = Chroma.from_documents(
            documents=processed_docs,
            embedding=self.embeddings,
            persist_directory=self.persist_directory,
            collection_name="pacvue_docs"
        )
        self.search_service = SearchService(self.vector_store, self.embeddings)
        return self.vector_store

    def load_vector_store(self) -> Optional[Chroma]:
        if not os.path.exists(self.persist_directory):
            return None
        try:
            self.vector_store = Chroma(
                persist_directory=self.persist_directory,
                embedding_function=self.embeddings,
                collection_name="pacvue_docs"
            )
            self.search_service = SearchService(self.vector_store, self.embeddings)
            return self.vector_store
        except Exception as e:
            print(f"[错误] 加载向量存储失败: {e}")
            return None

    def _create_empty_vector_store(self) -> Chroma:
        self.vector_store = Chroma(
            persist_directory=self.persist_directory,
            embedding_function=self.embeddings,
            collection_name="pacvue_docs"
        )
        self.search_service = SearchService(self.vector_store, self.embeddings)
        return self.vector_store

    def _chroma_store(self) -> ChromaStore:
        if self.vector_store is None:
            self.get_or_create_vector_store()
        return ChromaStore(
            vector_store=self.vector_store,
            splitter=self.splitter,
            manifest_store=self.manifest_store,
            source_repo=self.source_repo,
            chunk_strategy_version=self.chunk_strategy_version,
            index_version=self.index_version,
        )

    def get_or_create_vector_store(self) -> Chroma:
        vector_store = self.load_vector_store()
        if vector_store is None:
            print("[信息] 未找到现有向量存储，正在创建空集合...")
            vector_store = self._create_empty_vector_store()
        if not self._local_ingested_once:
            self.ingest_local_documents()
            self._local_ingested_once = True
        return vector_store

    def search(self, query: str, k: int = 1) -> List[Document]:
        if self.vector_store is None:
            self.get_or_create_vector_store()
        return self.search_service.search(query, k=k)

    def graph_search(self, query: str, k: int = 5) -> List[Document]:
        if self.vector_store is None:
            self.get_or_create_vector_store()
        return self.search_service.graph_search(query, k=k)

    def hybrid_search(self, query: str, k: int = 5) -> List[Document]:
        if self.vector_store is None:
            self.get_or_create_vector_store()
        return self.search_service.hybrid_search(query, k=k)

    def list_documents(self) -> List[str]:
        docs_path = Path(self.docs_dir)
        if not docs_path.exists():
            return []
        return [f.name for f in docs_path.glob("**/*.md")]

    def refresh(self) -> None:
        print("正在刷新向量存储...")
        if os.path.exists(self.persist_directory):
            shutil.rmtree(self.persist_directory)
            print("已删除旧的向量存储")
        self.vector_store = None
        self.search_service = None
        self._local_ingested_once = False
        self.get_or_create_vector_store()
        print("[OK] 向量存储刷新完成")

    def add_documents(self, chunks: List[Document], ids: List[str]) -> None:
        self._chroma_store().add_documents(chunks, ids)
        print(f"[OK] 已添加 {len(chunks)} 个文档片段")

    def _delete_by_doc_id(self, doc_id: str) -> int:
        return self._chroma_store().delete_by_doc_id(doc_id)

    def upsert_by_doc_id(self, docs: List[Document], source_scope: Optional[Tuple[str, str]] = None) -> Dict[str, int]:
        summary = self._chroma_store().upsert_by_doc_id(docs, source_scope=source_scope)
        print(
            "[OK] ingest 完成："
            f"新增={summary['added']} 更新={summary['updated']} "
            f"跳过={summary['skipped']} 删除={summary['deleted']}"
        )
        return summary

    def ingest_local_documents(self) -> Dict[str, int]:
        docs = self.load_documents()
        if not docs:
            print("[警告] 本地 docs 目录为空，跳过 ingest")
            return {"added": 0, "updated": 0, "skipped": 0, "deleted": 0}
        return self.upsert_by_doc_id(docs, source_scope=("local", self.source_repo))

    def upsert_documents(self, chunks: List[Document], ids: List[str]) -> None:
        if self.vector_store is None:
            self.get_or_create_vector_store()
        collection = self.vector_store._collection
        existing_ids: Set[str] = set(collection.get()["ids"])
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
        if to_update_chunks:
            embeddings_list = self.embeddings.embed_documents([c.page_content for c in to_update_chunks])
            metadatas = [c.metadata for c in to_update_chunks]
            collection.update(
                ids=to_update_ids,
                embeddings=embeddings_list,
                documents=[c.page_content for c in to_update_chunks],
                metadatas=metadatas
            )
        if to_add_chunks:
            self.vector_store.add_documents(to_add_chunks, ids=to_add_ids)

    def add_confluence_docs(self, docs: List[Document]) -> None:
        if not docs:
            print("[警告] 没有 Confluence 文档需要添加")
            return
        self.upsert_by_doc_id(docs)


_doc_loader: Optional[DocLoader] = None
_confluence_initialized: bool = False


def get_doc_loader(docs_dir: str = "./docs") -> DocLoader:
    global _doc_loader
    if _doc_loader is None:
        _doc_loader = DocLoader(docs_dir=docs_dir)
    return _doc_loader


def _get_meta_collection(persist_directory: str = "./chroma_db"):
    try:
        import chromadb
        client = chromadb.PersistentClient(path=persist_directory)
        return client.get_or_create_collection(name="pacvue_meta")
    except Exception as e:
        print(f"[错误] 获取 meta collection 失败: {e}")
        return None


def get_last_confluence_update(persist_directory: str = "./chroma_db") -> Optional[datetime]:
    meta = _get_meta_collection(persist_directory)
    if meta is None:
        return None
    try:
        result = meta.get(ids=["last_confluence_update"])
        if result and result["documents"] and result["documents"][0]:
            timestamp_str = result["documents"][0]
            return datetime.fromisoformat(timestamp_str)
    except Exception as e:
        print(f"[警告] 读取上次更新时间失败: {e}")
    return None


def set_last_confluence_update(persist_directory: str = "./chroma_db") -> None:
    meta = _get_meta_collection(persist_directory)
    if meta is None:
        return
    now_str = datetime.now(timezone.utc).isoformat()
    try:
        meta.upsert(ids=["last_confluence_update"], documents=[now_str])
        print(f"[OK] 已记录 Confluence 更新时间: {now_str}")
    except Exception as e:
        print(f"[错误] 写入更新时间失败: {e}")


def init_with_confluence(
    folder_ids: List[str],
    confluence_base_url: str = "https://pacvue-enterprise.atlassian.net",
    docs_dir: str = "./docs",
    force: bool = False
) -> DocLoader:
    global _confluence_initialized
    loader = get_doc_loader(docs_dir=docs_dir)
    loader.get_or_create_vector_store()
    if _confluence_initialized and not force:
        print("[信息] Confluence 文档已加载，跳过")
        return loader

    try:
        print("\n正在加载 Confluence 文档...")
        confluence_loader = ConfluenceLoader(base_url=confluence_base_url)
        all_page_ids = []
        for folder_id in folder_ids:
            print(f"[信息] 正在获取文件夹 {folder_id} 下的文档...")
            page_ids = confluence_loader.get_folder_docs_ids(folder_id=folder_id)
            all_page_ids.extend(page_ids)
            print(f"[信息] 文件夹 {folder_id} 包含 {len(page_ids)} 个页面")
        all_page_ids = list(set(all_page_ids))
        print(f"[信息] 共获取 {len(all_page_ids)} 个唯一页面")
        confluence_docs = confluence_loader.load_by_page_ids(all_page_ids)
        if confluence_docs:
            loader.add_confluence_docs(confluence_docs)
            _confluence_initialized = True
            set_last_confluence_update(loader.persist_directory)
            print(f"[OK] 已加载 {len(confluence_docs)} 个 Confluence 页面")
        else:
            print("[警告] 未能加载任何 Confluence 文档")
    except ValueError as e:
        print(f"[警告] 无法加载 Confluence 文档: {e}")
    except Exception as e:
        print(f"[错误] 加载 Confluence 文档时出错: {e}")
    return loader

