"""
兼容层：对外保持 confluence_get.py 导入路径不变。
"""

from connectors.confluence_client import (
    ConfluenceLoader,
    html_to_text,
)

