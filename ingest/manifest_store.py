import json
from pathlib import Path
from typing import Dict, Any, List


class ManifestStore:
    def __init__(self, manifest_path: str):
        self.manifest_path = manifest_path

    def load_latest(self) -> Dict[str, Dict[str, Any]]:
        latest_by_doc_id: Dict[str, Dict[str, Any]] = {}
        file_path = Path(self.manifest_path)
        if not file_path.exists():
            return latest_by_doc_id

        try:
            with file_path.open("r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        row = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    doc_id = row.get("doc_id")
                    if not doc_id:
                        continue
                    latest_by_doc_id[doc_id] = row
        except Exception as e:
            print(f"[警告] 读取 manifest 失败: {e}")
        return latest_by_doc_id

    def append_records(self, records: List[Dict[str, Any]]) -> None:
        if not records:
            return
        Path(self.manifest_path).parent.mkdir(parents=True, exist_ok=True)
        try:
            with open(self.manifest_path, "a", encoding="utf-8") as f:
                for row in records:
                    f.write(json.dumps(row, ensure_ascii=False) + "\n")
        except Exception as e:
            print(f"[错误] 写入 manifest 失败: {e}")

