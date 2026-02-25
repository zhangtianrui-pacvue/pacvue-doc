"""
兼容层：对外保留 doc_loader.py 导入路径。
核心实现迁移到 runtime.doc_service。
"""

from runtime.doc_service import (  # noqa: F401
    DocLoader,
    get_doc_loader,
    init_with_confluence,
    get_last_confluence_update,
    set_last_confluence_update,
)

