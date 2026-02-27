import subprocess
from pathlib import Path
from typing import Dict, Optional


class RepoSyncError(RuntimeError):
    pass


class RepoSyncManager:
    def __init__(self, repo_url: str, local_path: str):
        self.repo_url = repo_url.strip()
        self.local_path = Path(local_path)

    def sync(self) -> Dict[str, Optional[str]]:
        if not self.repo_url:
            raise RepoSyncError("repo_url 不能为空")

        self.local_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.local_path.exists():
            self._clone_repo()
            new_commit = self._get_head_commit()
            return {
                "action": "cloned",
                "old_commit": None,
                "new_commit": new_commit,
                "changed": "true",
            }

        if not (self.local_path / ".git").exists():
            raise RepoSyncError(
                f"本地目录存在但不是 Git 仓库: {self.local_path}"
            )

        self._validate_remote_url()
        old_commit = self._get_head_commit()
        self._git(["fetch", "--all", "--prune"])
        self._git(["pull", "--ff-only"])
        new_commit = self._get_head_commit()
        return {
            "action": "pulled",
            "old_commit": old_commit,
            "new_commit": new_commit,
            "changed": "true" if old_commit != new_commit else "false",
        }

    def _clone_repo(self) -> None:
        parent_dir = str(self.local_path.parent)
        self._run(
            [
                "git",
                "clone",
                self.repo_url
            ],
            cwd=parent_dir,
        )

    def _validate_remote_url(self) -> None:
        current = self._git(["remote", "get-url", "origin"])
        if current.strip().lower() != self.repo_url.lower():
            raise RepoSyncError(
                "本地仓库 origin 与配置不一致："
                f" current={current.strip()} expected={self.repo_url}"
            )

    def _get_head_commit(self) -> str:
        return self._git(["rev-parse", "HEAD"]).strip()

    def _git(self, args: list[str]) -> str:
        return self._run(["git", *args], cwd=str(self.local_path))

    @staticmethod
    def _run(cmd: list[str], cwd: str) -> str:
        result = subprocess.run(
            cmd,
            cwd=cwd,
            text=True,
            capture_output=True,
            check=False,
            shell=False,
        )
        if result.returncode != 0:
            stderr = result.stderr.strip() or "(无错误输出)"
            raise RepoSyncError(f"命令执行失败: {' '.join(cmd)}\n{stderr}")
        return result.stdout.strip()

if __name__ == "__main__":
    repo_sync = RepoSyncManager(repo_url="https://github.com/Pacvue/elementPlus-vue3.git", local_path="./repo_cache/elementPlus-vue3")
    result = repo_sync.sync()
    print(result)