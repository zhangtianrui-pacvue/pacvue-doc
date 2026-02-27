from datetime import datetime, timezone
from typing import Dict, Optional

from connectors.repo_sync import RepoSyncManager
from ingest.source_doc_generator import SourceDocGenerator
from runtime.doc_service import DocLoader
from runtime.settings import (
    REMOTE_REPO_LOCAL_PATH,
    REMOTE_REPO_SYNC_DAYS,
    REMOTE_REPO_URL,
)

_LAST_REPO_SYNC_TIME_KEY = "last_repo_sync_time"
_LAST_REPO_SYNC_COMMIT_KEY = "last_repo_sync_commit"


def _get_meta_collection(persist_directory: str = "./chroma_db"):
    try:
        import chromadb

        client = chromadb.PersistentClient(path=persist_directory)
        return client.get_or_create_collection(name="pacvue_meta")
    except Exception as e:
        print(f"[错误] 获取 meta collection 失败: {e}")
        return None


def get_last_repo_sync_time(persist_directory: str = "./chroma_db") -> Optional[datetime]:
    meta = _get_meta_collection(persist_directory)
    if meta is None:
        return None
    try:
        result = meta.get(ids=[_LAST_REPO_SYNC_TIME_KEY])
        if result and result["documents"] and result["documents"][0]:
            return datetime.fromisoformat(result["documents"][0])
    except Exception as e:
        print(f"[警告] 读取上次 Repo 同步时间失败: {e}")
    return None


def get_last_repo_sync_commit(persist_directory: str = "./chroma_db") -> Optional[str]:
    meta = _get_meta_collection(persist_directory)
    if meta is None:
        return None
    try:
        result = meta.get(ids=[_LAST_REPO_SYNC_COMMIT_KEY])
        if result and result["documents"] and result["documents"][0]:
            return str(result["documents"][0])
    except Exception as e:
        print(f"[警告] 读取上次 Repo commit 失败: {e}")
    return None


def set_repo_sync_meta(persist_directory: str, commit_sha: str) -> None:
    meta = _get_meta_collection(persist_directory)
    if meta is None:
        return
    now_str = datetime.now(timezone.utc).isoformat()
    try:
        meta.upsert(ids=[_LAST_REPO_SYNC_TIME_KEY], documents=[now_str])
        meta.upsert(ids=[_LAST_REPO_SYNC_COMMIT_KEY], documents=[commit_sha or ""])
    except Exception as e:
        print(f"[错误] 写入 Repo 同步 meta 失败: {e}")


def should_sync_repo(last_sync_time: Optional[datetime], sync_days: int) -> bool:
    if last_sync_time is None:
        return True
    now = datetime.now(timezone.utc)
    return (now - last_sync_time).days >= sync_days


class RepoSyncService:
    def __init__(
        self,
        *,
        doc_loader: DocLoader,
        repo_url: str = REMOTE_REPO_URL,
        repo_local_path: str = REMOTE_REPO_LOCAL_PATH,
        sync_days: int = REMOTE_REPO_SYNC_DAYS,
    ):
        self.doc_loader = doc_loader
        self.repo_url = repo_url
        self.repo_local_path = repo_local_path
        self.sync_days = sync_days
        self.repo_sync = RepoSyncManager(repo_url=repo_url, local_path=repo_local_path)
        self.generator = SourceDocGenerator(
            source_root=repo_local_path,
            docs_root=doc_loader.docs_dir,
        )

    def run(self, force: bool = False) -> Dict[str, object]:
        last_sync_time = get_last_repo_sync_time(self.doc_loader.persist_directory)
        if not force and not should_sync_repo(last_sync_time, self.sync_days):
            return {
                "status": "skipped",
                "reason": "not_due",
                "last_sync_time": last_sync_time.isoformat() if last_sync_time else None,
                "sync_days": self.sync_days,
            }

        sync_result = self.repo_sync.sync()
        repo_changed = str(sync_result.get("changed", "false")).lower() == "true"
        should_regenerate = force or repo_changed

        if should_regenerate:
            generation = self.generator.generate()
            ingest_summary = self.doc_loader.ingest_local_documents()
        else:
            generation = {"generated_files": [], "count": 0, "skipped": True}
            ingest_summary = {"added": 0, "updated": 0, "skipped": 0, "deleted": 0}

        new_commit = str(sync_result.get("new_commit") or "")
        set_repo_sync_meta(self.doc_loader.persist_directory, new_commit)

        return {
            "status": "ok",
            "force": force,
            "sync": sync_result,
            "generation": generation,
            "ingest_summary": ingest_summary,
        }
