import hashlib
import re
from typing import Optional

from runtime.settings import CHUNK_INDEX_WIDTH


def normalize_path(path: str, source_type: str) -> str:
    normalized = path.replace("\\", "/")
    normalized = re.sub(r"/+", "/", normalized)
    normalized = re.sub(r"^\./", "", normalized)
    normalized = normalized.rstrip("/")
    if source_type == "confluence":
        return normalized.lower()
    return normalized


def normalize_title(title: Optional[str]) -> str:
    """
    标题归一化：
    - None/空字符串 -> ""
    - 去前后空格
    - 连续空白折叠为单个空格
    - 全部小写
    """
    if not title:
        return ""
    return re.sub(r"\s+", " ", title.strip()).lower()


def sha1_hex(text: str) -> str:
    return hashlib.sha1(text.encode("utf-8")).hexdigest()


def sha256_hex(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def build_doc_key(source_type: str, source_repo: str, normalized_path: str) -> str:
    return f"{source_type}|{source_repo}|{normalized_path}"


def build_doc_id(source_type: str, source_repo: str, normalized_path: str) -> str:
    return sha1_hex(build_doc_key(source_type, source_repo, normalized_path))


def build_chunk_id(doc_id: str, chunk_index: int) -> str:
    return f"{doc_id}:{chunk_index:0{CHUNK_INDEX_WIDTH}d}"

