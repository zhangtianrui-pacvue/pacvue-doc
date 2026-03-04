import os
import shutil
import subprocess
import time
from pathlib import Path
from typing import Dict, Optional


class RepoSyncError(RuntimeError):
    pass


class RepoSyncManager:
    def __init__(self, repo_url: str, local_path: str):
        self.repo_url = repo_url.strip()
        self.local_path = Path(local_path)
        self._lock_path = self.local_path.parent / ".repo_sync.lock"

    def sync(self) -> Dict[str, Optional[str]]:
        if not self.repo_url:
            raise RepoSyncError("repo_url 不能为空")

        self.local_path.parent.mkdir(parents=True, exist_ok=True)
        self._acquire_lock()
        try:
            return self._do_sync()
        finally:
            self._release_lock()

    def _do_sync(self) -> Dict[str, Optional[str]]:
        git_dir = self.local_path / ".git"
        dir_exists = self.local_path.exists()

        # 目录存在、.git 存在 → 正常 pull
        if dir_exists and git_dir.exists():
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

        # 目录存在、.git 存在但 checkout 可能不完整 → 尝试恢复
        if dir_exists and git_dir.exists():
            self._try_restore_checkout()
            new_commit = self._get_head_commit()
            return {
                "action": "restored",
                "old_commit": None,
                "new_commit": new_commit,
                "changed": "true",
            }

        # 目录存在但不是 git 仓库（partial clone 残留） → 清理后重新 clone
        if dir_exists and not git_dir.exists():
            print(f"[信息] 检测到残留目录（非 git 仓库），正在清理: {self.local_path}")
            shutil.rmtree(self.local_path, ignore_errors=True)

        # clone
        self._clone_repo()

        # clone 后如果 checkout 不完整，尝试修复
        if (self.local_path / ".git").exists():
            try:
                self._try_restore_checkout()
            except RepoSyncError:
                pass  # restore 失败不阻断后续流程

        new_commit = self._get_head_commit()
        return {
            "action": "cloned",
            "old_commit": None,
            "new_commit": new_commit,
            "changed": "true",
        }

    def _clone_repo(self) -> None:
        parent_dir = str(self.local_path.parent)
        target_name = self.local_path.name
        # -c core.longpaths=true 解决 Windows 260 字符路径限制
        result = subprocess.run(
            ["git", "-c", "core.longpaths=true", "clone", self.repo_url, target_name],
            cwd=parent_dir,
            text=True,
            capture_output=True,
            check=False,
            shell=False,
        )
        # git clone 在 checkout 失败时返回非零，但对象库已经完整
        # "Clone succeeded, but checkout failed" 可通过 restore 修复，不直接报错
        if result.returncode != 0:
            checkout_failed = (
                "checkout failed" in (result.stderr or "").lower()
                or "checkout failed" in (result.stdout or "").lower()
            )
            if not checkout_failed:
                stderr = result.stderr.strip() or "(无错误输出)"
                raise RepoSyncError(
                    f"git clone 失败: {self.repo_url}\n{stderr}"
                )
            # checkout 失败但对象库完整，继续交给 _try_restore_checkout 处理

    def _try_restore_checkout(self) -> None:
        """在 partial checkout 场景下用 git restore 补全工作区文件。"""
        self._git(["-c", "core.longpaths=true", "restore", "--source=HEAD", ":/"])

    def _validate_remote_url(self) -> None:
        current = self._git(["remote", "get-url", "origin"])
        if current.strip().lower() != self.repo_url.lower():
            raise RepoSyncError(
                "本地仓库 origin 与配置不一致："
                f" current={current.strip()} expected={self.repo_url}"
            )

    def _get_head_commit(self) -> str:
        return self._git(["rev-parse", "HEAD"]).strip()

    def _git(self, args: list) -> str:
        return self._run(["git", *args], cwd=str(self.local_path))

    @staticmethod
    def _run(cmd: list, cwd: str) -> str:
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

    # ── 跨进程锁（防止并发 clone） ──────────────────────────────────────────

    def _acquire_lock(self, timeout_seconds: int = 30) -> None:
        """
        尝试获取文件锁。锁超过 10 分钟未更新视为 stale，自动清理后重试。
        """
        start = time.time()
        while True:
            if self._try_create_lock():
                return
            if self._is_stale_lock():
                print(f"[信息] 检测到僵尸锁文件，自动清理后重试...")
                self._release_lock()
                time.sleep(0.2)
                continue
            if time.time() - start >= timeout_seconds:
                raise RepoSyncError("仓库同步锁等待超时，请手动删除 repo_cache/.repo_sync.lock 后重试")
            time.sleep(0.5)

    def _try_create_lock(self) -> bool:
        try:
            fd = os.open(str(self._lock_path), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            with os.fdopen(fd, "w", encoding="utf-8") as f:
                f.write(str(os.getpid()))
            return True
        except FileExistsError:
            return False

    def _is_stale_lock(self) -> bool:
        try:
            mtime = self._lock_path.stat().st_mtime
        except FileNotFoundError:
            return True
        # 锁文件超过 10 分钟未更新，视为僵尸锁
        return (time.time() - mtime) > 600

    def _release_lock(self) -> None:
        try:
            if self._lock_path.exists():
                self._lock_path.unlink()
        except Exception:
            pass


if __name__ == "__main__":
    repo_sync = RepoSyncManager(
        repo_url="https://github.com/Pacvue/elementPlus-vue3.git",
        local_path="./repo_cache/elementPlus-vue3",
    )
    print(repo_sync.sync())
