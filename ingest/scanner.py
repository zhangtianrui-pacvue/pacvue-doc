from datetime import datetime, timezone
from pathlib import Path
from typing import List

from langchain_community.document_loaders import TextLoader
from langchain_core.documents import Document

from ingest.identity import normalize_title


def scan_local_markdown(docs_dir: str, source_repo: str) -> List[Document]:
    docs_path = Path(docs_dir)
    if not docs_path.exists():
        print(f"[警告] 文档目录不存在: {docs_dir}")
        return []

    documents: List[Document] = []
    for md_file in docs_path.glob("**/*.md"):
        try:
            loader = TextLoader(str(md_file), encoding="utf-8")
            docs = loader.load()
            for doc in docs:
                rel_path = str(md_file.relative_to(docs_path)).replace("\\", "/")
                title = md_file.stem
                normalized_title = normalize_title(title)
                # 极短标题容易碰撞，禁用跨文档 title 连边
                if len(normalized_title) < 3:
                    normalized_title = ""
                updated_at = datetime.fromtimestamp(
                    md_file.stat().st_mtime,
                    tz=timezone.utc
                ).isoformat()
                doc.metadata["source"] = str(md_file)
                doc.metadata["filename"] = md_file.name
                doc.metadata["title"] = title
                doc.metadata["normalized_title"] = normalized_title
                doc.metadata["source_type"] = "local"
                doc.metadata["source_repo"] = source_repo
                doc.metadata["path"] = rel_path
                doc.metadata["updated_at"] = updated_at
            documents.extend(docs)
            print(f"[OK] 已加载: {md_file.name}")
        except Exception as e:
            print(f"[错误] 加载失败 {md_file.name}: {e}")

    print(f"\n共加载 {len(documents)} 个文档")
    return documents

