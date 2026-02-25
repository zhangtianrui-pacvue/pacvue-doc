from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Set, Tuple

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_graph_retriever.transformers import ShreddingTransformer

from ingest.identity import (
    normalize_path,
    sha256_hex,
    build_doc_key,
    build_doc_id,
    build_chunk_id,
)
from ingest.manifest_store import ManifestStore
from retrieve.splitter import DocumentSplitter
from runtime.settings import MANIFEST_SCHEMA_VERSION


class ChromaStore:
    def __init__(
        self,
        *,
        vector_store: Chroma,
        splitter: DocumentSplitter,
        manifest_store: ManifestStore,
        source_repo: str,
        chunk_strategy_version: str,
        index_version: str,
    ):
        self.vector_store = vector_store
        self.splitter = splitter
        self.manifest_store = manifest_store
        self.source_repo = source_repo
        self.chunk_strategy_version = chunk_strategy_version
        self.index_version = index_version

    @staticmethod
    def _utc_now_iso() -> str:
        return datetime.now(timezone.utc).isoformat()

    def _build_identity(self, doc: Document) -> Dict[str, Any]:
        source_type = doc.metadata.get("source_type", "local")
        source_repo = doc.metadata.get("source_repo", self.source_repo)
        raw_path = doc.metadata.get("path", doc.metadata.get("source", "unknown"))
        normalized_path = normalize_path(str(raw_path), source_type)
        updated_at = doc.metadata.get("updated_at")
        content_hash = sha256_hex(doc.page_content)
        doc_key = build_doc_key(source_type, source_repo, normalized_path)
        doc_id = build_doc_id(source_type, source_repo, normalized_path)
        return {
            "doc_id": doc_id,
            "doc_key": doc_key,
            "source_type": source_type,
            "source_repo": source_repo,
            "path": normalized_path,
            "updated_at": updated_at,
            "content_hash": content_hash,
        }

    def _build_manifest_record(
        self,
        *,
        doc_id: str,
        doc_key: str,
        source_type: str,
        source_repo: str,
        path: str,
        updated_at: Optional[str],
        content_hash: str,
        ingested_at: str,
        is_deleted: bool,
        ingest_status: str
    ) -> Dict[str, Any]:
        return {
            "schema_version": MANIFEST_SCHEMA_VERSION,
            "doc_id": doc_id,
            "doc_key": doc_key,
            "source_type": source_type,
            "source_repo": source_repo,
            "path": path,
            "updated_at": updated_at,
            "content_hash": content_hash,
            "ingested_at": ingested_at,
            "chunk_strategy_version": self.chunk_strategy_version,
            "index_version": self.index_version,
            "is_deleted": is_deleted,
            "ingest_status": ingest_status,
        }

    def add_documents(self, chunks: List[Document], ids: List[str]) -> None:
        shredder = ShreddingTransformer()
        processed_chunks = list(shredder.transform_documents(chunks))
        self.vector_store.add_documents(processed_chunks, ids=ids)

    def delete_by_doc_id(self, doc_id: str) -> int:
        collection = self.vector_store._collection
        try:
            existing = collection.get(where={"doc_id": doc_id})
            ids = existing.get("ids", []) if existing else []
            if ids:
                collection.delete(ids=ids)
            return len(ids)
        except Exception as e:
            print(f"[警告] 删除 doc_id={doc_id} 失败: {e}")
            return 0

    def upsert_by_doc_id(self, docs: List[Document], source_scope: Optional[Tuple[str, str]] = None) -> Dict[str, int]:
        summary = {"added": 0, "updated": 0, "skipped": 0, "deleted": 0}
        ingest_ts = self._utc_now_iso()
        manifest_latest = self.manifest_store.load_latest()
        records: List[Dict[str, Any]] = []
        seen_doc_ids: Set[str] = set()

        for doc in docs:
            identity = self._build_identity(doc)
            doc_id = identity["doc_id"]
            seen_doc_ids.add(doc_id)
            previous = manifest_latest.get(doc_id)

            doc.metadata.update(identity)
            doc.metadata["chunk_strategy_version"] = self.chunk_strategy_version
            doc.metadata["index_version"] = self.index_version

            same_hash = (
                previous is not None
                and not previous.get("is_deleted", False)
                and previous.get("content_hash") == identity["content_hash"]
                and previous.get("chunk_strategy_version") == self.chunk_strategy_version
                and previous.get("index_version") == self.index_version
            )
            if same_hash:
                summary["skipped"] += 1
                records.append(self._build_manifest_record(
                    **identity,
                    ingested_at=ingest_ts,
                    is_deleted=False,
                    ingest_status="skipped"
                ))
                continue

            existed_before = previous is not None and not previous.get("is_deleted", False)
            self.delete_by_doc_id(doc_id)
            chunks = self.splitter.split_single(doc)
            for idx, chunk in enumerate(chunks):
                chunk.metadata.update(identity)
                chunk.metadata["chunk_index"] = idx
                chunk.metadata["chunk_id"] = build_chunk_id(doc_id, idx)
                chunk.metadata["chunk_strategy_version"] = self.chunk_strategy_version
                chunk.metadata["index_version"] = self.index_version
            ids = [build_chunk_id(doc_id, i) for i in range(len(chunks))]
            if chunks:
                self.add_documents(chunks, ids)

            ingest_status = "updated" if existed_before else "added"
            summary["updated" if existed_before else "added"] += 1
            records.append(self._build_manifest_record(
                **identity,
                ingested_at=ingest_ts,
                is_deleted=False,
                ingest_status=ingest_status
            ))

        if source_scope is not None:
            source_type, source_repo = source_scope
            for doc_id, row in manifest_latest.items():
                if row.get("is_deleted", False):
                    continue
                if row.get("source_type") != source_type or row.get("source_repo") != source_repo:
                    continue
                if doc_id in seen_doc_ids:
                    continue
                self.delete_by_doc_id(doc_id)
                summary["deleted"] += 1
                records.append(self._build_manifest_record(
                    doc_id=doc_id,
                    doc_key=row.get("doc_key", ""),
                    source_type=source_type,
                    source_repo=source_repo,
                    path=row.get("path", ""),
                    updated_at=row.get("updated_at"),
                    content_hash=row.get("content_hash", ""),
                    ingested_at=ingest_ts,
                    is_deleted=True,
                    ingest_status="deleted"
                ))

        self.manifest_store.append_records(records)
        return summary

