"""
Confluence 文档加载模块

负责从 Confluence API 获取文档内容，并转换为 LangChain Document 格式。
"""

import os
import base64
import hashlib
from typing import List, Dict, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from bs4 import BeautifulSoup
from langchain_core.documents import Document


def _get_credentials() -> tuple[str, str]:
    """
    从环境变量获取 Confluence 认证凭据
    
    Returns:
        (email, token) 元组
        
    Raises:
        ValueError: 如果环境变量未设置
    """
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
    """
    生成 Confluence API 认证头
    
    Returns:
        包含 Authorization 和 Accept 的请求头字典
    """
    email, token = _get_credentials()
    encoded = base64.b64encode(f"{email}:{token}".encode()).decode()
    return {
        "Authorization": f"Basic {encoded}",
        "Accept": "application/json"
    }


def _create_session() -> requests.Session:
    """
    创建带重试机制的 HTTP Session
    
    Returns:
        配置了重试策略的 requests.Session 实例
    """
    session = requests.Session()
    
    # 配置重试策略：最多重试 3 次，遇到 5xx 错误时重试
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
    """
    将 HTML 内容转换为纯文本
    
    Args:
        html: HTML 字符串
        
    Returns:
        提取的纯文本内容
    """
    soup = BeautifulSoup(html, "html.parser")
    
    # 移除脚本、样式等非内容标签
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()
    
    return soup.get_text("\n", strip=True)

class ConfluenceLoader:
    """
    Confluence 文档加载器
    
    从 Confluence API 获取页面内容，转换为 LangChain Document 格式。
    
    Attributes:
        base_url: Confluence 实例的基础 URL
    """
    
    def __init__(self, base_url: str):
        """
        初始化 Confluence 加载器
        
        Args:
            base_url: Confluence 实例的基础 URL，如 "https://your-domain.atlassian.net"
        """
        self.base_url = base_url.rstrip("/")
        self.headers = _auth_header()
        self.session = _create_session()
    
    def fetch_page(self, page_id: str) -> Document:
        """
        获取单个 Confluence 页面
        
        Args:
            page_id: Confluence 页面 ID
            
        Returns:
            包含页面内容和元数据的 Document 对象
            
        Raises:
            requests.HTTPError: 如果 API 请求失败
        """
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
        
        # 提取页面内容
        html = page_data.get("body", {}).get("view", {}).get("value", "")
        text = html_to_text(html)
        
        # 构建元数据
        space = page_data.get("space", {}).get("key", "")
        metadata = {
            "id": page_data.get("id"),
            "title": page_data.get("title"),
            "space": space,
            "lastmodified": page_data.get("version", {}).get("when"),
            "url": f"{self.base_url}/wiki/spaces/{space}/pages/{page_data.get('id')}",
            "source": "confluence",
        }
        
        return Document(page_content=text, metadata=metadata)
    
    def load_by_page_ids(self, page_ids: List[str]) -> List[Document]:
        """
        批量获取多个 Confluence 页面（串行版本）
        
        Args:
            page_ids: 页面 ID 列表
            
        Returns:
            Document 对象列表
        """
        documents = []
        
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

    def load_by_page_ids_concurrent(
        self,
        page_ids: List[str],
        max_workers: int = 10
    ) -> List[Document]:
        """
        并发加载多个 Confluence 页面
        
        使用线程池并发获取页面，显著提升加载速度。
        
        Args:
            page_ids: 页面 ID 列表
            max_workers: 最大并发线程数（默认 10，建议不超过 20 以避免 API 限流）
            
        Returns:
            Document 对象列表
        """
        if not page_ids:
            return []
        
        documents = []
        total = len(page_ids)
        loaded_count = 0
        
        print(f"[信息] 开始并发加载 {total} 个页面（线程数: {max_workers}）")
        
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # 提交所有任务
            future_to_id = {
                executor.submit(self.fetch_page, pid): pid
                for pid in page_ids
            }
            
            # 收集结果
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
        """
        为文档片段生成稳定的唯一 ID
        
        基于页面 ID 和内容哈希生成，确保相同内容产生相同 ID。
        
        Args:
            chunks: 文档片段列表
            
        Returns:
            对应的 ID 列表
        """
        ids = []
        for chunk in chunks:
            page_id = chunk.metadata.get("id", "unknown")
            content_hash = hashlib.sha1(
                chunk.page_content.encode("utf-8")
            ).hexdigest()[:16]
            ids.append(f"confluence:{page_id}:{content_hash}")
        return ids

    # 获取的文件夹下面所有的IDs
    def get_folder_docs_ids(self, folder_id: str, max_depth: int = 20) -> List[str]:
        """
        获取文件夹下面的所有文档ID
        
        Args:
            folder_id: 根文件夹ID
            max_depth: 最大递归深度，防止无限递归
        """
        page_ids = []
        visited_pages = set()    # 记录已访问的页面
        visited_folders = set()  # 记录已访问的文件夹
        
        # 递归收集所有 folder
        all_folder_ids = []
        self._collect_folder_ids(folder_id, all_folder_ids, visited_folders, depth=0, max_depth=max_depth)
        print(f"[DEBUG] 找到 {len(all_folder_ids)} 个文件夹")
        
        # 获取所有 folder 下面的直接 pages
        params = {'start': 0, 'limit': 50}
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
        """
        递归收集所有文件夹ID
        """
        if folder_id in visited:
            print(f"[DEBUG] 文件夹 {folder_id} 已访问，跳过")
            return
        if depth > max_depth:
            print(f"[WARN] 达到最大深度 {max_depth}，停止递归")
            return
        
        visited.add(folder_id)
        folder_ids.append(folder_id)
        
        params = {'start': 0, 'limit': 50}
        url = f"{self.base_url}/wiki/rest/api/content/{folder_id}/child/folder"
        response = self.session.get(url, headers=self.headers, params=params, timeout=30)
        response.raise_for_status()
        sub_folders = response.json().get("results", [])
        
        for folder in sub_folders:
            sub_id = folder.get("id")
            if sub_id and sub_id not in visited:
                self._collect_folder_ids(sub_id, folder_ids, visited, depth + 1, max_depth)

    def _collect_page_ids(self, page_id: str, page_ids: List[str], visited: set, depth: int, max_depth: int) -> None:
        """
        递归收集页面ID及其子页面ID
        
        Args:
            page_id: 当前页面ID
            page_ids: 收集结果的列表
            visited: 已访问页面ID集合，防止循环引用
            depth: 当前递归深度
            max_depth: 最大递归深度
        """
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

if __name__ == "__main__":
    # 测试代码
    from dotenv import load_dotenv
    load_dotenv()
    
    loader = ConfluenceLoader(base_url="https://pacvue-enterprise.atlassian.net")
    page_ids =loader.get_folder_docs_ids(folder_id="2196631")
    print(page_ids, "page_ids")
    print(len(page_ids), "page_ids length")
