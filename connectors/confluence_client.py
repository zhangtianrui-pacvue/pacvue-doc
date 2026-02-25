"""
Confluence 文档加载模块（拆分自 confluence_get.py）。
"""

import os
import base64
import hashlib
from typing import List, Dict
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from bs4 import BeautifulSoup
from langchain_core.documents import Document

from ingest.identity import normalize_title


def _get_credentials() -> tuple[str, str]:
    email = os.getenv("CONFLUENCE_EMAIL")
    token = os.getenv("CONFLUENCE_API_TOKEN")
    if not email or not token:
        raise ValueError(
            "请设置 CONFLUENCE_EMAIL 和 CONFLUENCE_API_TOKEN 环境变量。\n"
            "可以在 .env 文件中添加：\n"
            "CONFLUENCE_EMAIL=your-email@example.com\n"
            "CONFLUENCE_API_TOKEN=your-api-token"
        )
    return email, token


def _auth_header() -> Dict[str, str]:
    email, token = _get_credentials()
    encoded = base64.b64encode(f"{email}:{token}".encode()).decode()
    return {
        "Authorization": f"Basic {encoded}",
        "Accept": "application/json"
    }


def _create_session() -> requests.Session:
    session = requests.Session()
    retry_strategy = Retry(
        total=3,
        backoff_factor=0.5,
        status_forcelist=[500, 502, 503, 504],
        allowed_methods=["GET"]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    return session


def html_to_text(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()
    return soup.get_text("\n", strip=True)


class ConfluenceLoader:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")
        self.headers = _auth_header()
        self.session = _create_session()

    def fetch_page(self, page_id: str) -> Document:
        url = f"{self.base_url}/wiki/rest/api/content/{page_id}"
        params = {"expand": "body.view,version,space"}
        response = self.session.get(
            url,
            headers=self.headers,
            params=params,
            timeout=30
        )
        response.raise_for_status()
        page_data = response.json()

        html = page_data.get("body", {}).get("view", {}).get("value", "")
        text = html_to_text(html)

        space = page_data.get("space", {}).get("key", "")
        updated_at = page_data.get("version", {}).get("when")
        page_id_val = page_data.get("id")
        title = page_data.get("title")
        normalized_title = normalize_title(title)
        if len(normalized_title) < 3:
            normalized_title = ""
        metadata = {
            "id": page_id_val,
            "title": title,
            "normalized_title": normalized_title,
            "space": space,
            "lastmodified": updated_at,
            "url": f"{self.base_url}/wiki/spaces/{space}/pages/{page_id_val}",
            "source": "confluence",
            "source_type": "confluence",
            "source_repo": space or "confluence",
            "path": f"{space}/{page_id_val}" if space else str(page_id_val),
            "updated_at": updated_at,
        }
        return Document(page_content=text, metadata=metadata)

    def load_by_page_ids(self, page_ids: List[str]) -> List[Document]:
        documents: List[Document] = []
        for page_id in page_ids:
            try:
                doc = self.fetch_page(page_id)
                documents.append(doc)
                print(f"[OK] 已加载 Confluence 页面: {doc.metadata.get('title')}")
            except requests.HTTPError as e:
                print(f"[错误] 加载页面 {page_id} 失败: {e}")
            except Exception as e:
                print(f"[错误] 处理页面 {page_id} 时出错: {e}")
        return documents

    def load_by_page_ids_concurrent(self, page_ids: List[str], max_workers: int = 10) -> List[Document]:
        if not page_ids:
            return []
        documents: List[Document] = []
        total = len(page_ids)
        loaded_count = 0
        print(f"[信息] 开始并发加载 {total} 个页面（线程数: {max_workers}）")
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_id = {executor.submit(self.fetch_page, pid): pid for pid in page_ids}
            for future in as_completed(future_to_id):
                page_id = future_to_id[future]
                try:
                    doc = future.result()
                    documents.append(doc)
                    loaded_count += 1
                    print(f"[OK] ({loaded_count}/{total}) 已加载: {doc.metadata.get('title')}")
                except requests.HTTPError as e:
                    print(f"[错误] 加载页面 {page_id} 失败: {e}")
                except Exception as e:
                    print(f"[错误] 处理页面 {page_id} 时出错: {e}")
        print(f"[信息] 并发加载完成，成功加载 {len(documents)}/{total} 个页面")
        return documents

    @staticmethod
    def generate_stable_ids(chunks: List[Document]) -> List[str]:
        ids = []
        for chunk in chunks:
            page_id = chunk.metadata.get("id", "unknown")
            content_hash = hashlib.sha1(
                chunk.page_content.encode("utf-8")
            ).hexdigest()[:16]
            ids.append(f"confluence:{page_id}:{content_hash}")
        return ids

    def get_folder_docs_ids(self, folder_id: str, max_depth: int = 20) -> List[str]:
        page_ids: List[str] = []
        visited_pages = set()
        visited_folders = set()
        all_folder_ids: List[str] = []
        self._collect_folder_ids(folder_id, all_folder_ids, visited_folders, depth=0, max_depth=max_depth)
        print(f"[DEBUG] 找到 {len(all_folder_ids)} 个文件夹")

        params = {"start": 0, "limit": 50}
        for fid in all_folder_ids:
            url = f"{self.base_url}/wiki/rest/api/content/{fid}/child/page"
            response = self.session.get(url, headers=self.headers, params=params, timeout=30)
            response.raise_for_status()
            page_list = response.json().get("results", [])
            print(f"[DEBUG] 文件夹 {fid} 下有 {len(page_list)} 个直接页面")
            for page in page_list:
                page_id = page.get("id")
                if page_id and page_id not in visited_pages:
                    self._collect_page_ids(page_id, page_ids, visited_pages, depth=0, max_depth=max_depth)
        return page_ids

    def _collect_folder_ids(self, folder_id: str, folder_ids: List[str], visited: set, depth: int, max_depth: int) -> None:
        if folder_id in visited:
            print(f"[DEBUG] 文件夹 {folder_id} 已访问，跳过")
            return
        if depth > max_depth:
            print(f"[WARN] 达到最大深度 {max_depth}，停止递归")
            return
        visited.add(folder_id)
        folder_ids.append(folder_id)

        params = {"start": 0, "limit": 50}
        url = f"{self.base_url}/wiki/rest/api/content/{folder_id}/child/folder"
        response = self.session.get(url, headers=self.headers, params=params, timeout=30)
        response.raise_for_status()
        sub_folders = response.json().get("results", [])
        for folder in sub_folders:
            sub_id = folder.get("id")
            if sub_id and sub_id not in visited:
                self._collect_folder_ids(sub_id, folder_ids, visited, depth + 1, max_depth)

    def _collect_page_ids(self, page_id: str, page_ids: List[str], visited: set, depth: int, max_depth: int) -> None:
        if page_id in visited:
            print(f"[DEBUG] 页面 {page_id} 已访问，跳过")
            return
        if depth > max_depth:
            print(f"[WARN] 页面递归达到最大深度 {max_depth}，停止")
            return
        visited.add(page_id)
        page_ids.append(page_id)
        print(f"[DEBUG] 添加页面 {page_id}，当前共 {len(page_ids)} 个页面，深度 {depth}")

        url = f"{self.base_url}/wiki/rest/api/content/{page_id}/child/page"
        response = self.session.get(url, headers=self.headers, timeout=30)
        response.raise_for_status()
        page_list = response.json().get("results", [])
        for page in page_list:
            child_id = page.get("id")
            if child_id and child_id not in visited:
                self._collect_page_ids(child_id, page_ids, visited, depth + 1, max_depth)

