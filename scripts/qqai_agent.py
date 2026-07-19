"""QuangQuy AI safe coding agent for Google Colab.

The agent creates a structured plan with Gemini, validates file operations,
backs up changed files, and applies only create/update actions inside a repo.
Deletion and arbitrary shell execution are intentionally excluded.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

from google import genai


IGNORED_PARTS = {
    ".git", "node_modules", ".next", "dist", "build", ".venv", "venv",
    "__pycache__", ".ipynb_checkpoints", ".cache", "backups", "workspace",
}
SENSITIVE_NAMES = {
    ".env", ".env.local", ".env.production", "credentials.json",
    "service-account.json", "id_rsa", "id_ed25519",
}
TEXT_SUFFIXES = {
    ".md", ".txt", ".json", ".yaml", ".yml", ".toml", ".ini", ".cfg",
    ".py", ".js", ".jsx", ".ts", ".tsx", ".html", ".css", ".scss",
    ".vue", ".svelte", ".sh", ".sql", ".xml", ".csv",
}


@dataclass
class Change:
    path: str
    action: str
    content: str
    reason: str = ""


@dataclass
class AgentPlan:
    summary: str
    risk: str
    changes: list[Change]
    commands: list[str]
    notes: list[str]


class SafetyError(RuntimeError):
    pass


def _strip_json_fence(text: str) -> str:
    text = text.strip()
    match = re.search(r"```(?:json)?\s*(\{.*\})\s*```", text, re.S)
    return match.group(1) if match else text


def _is_sensitive(path: Path) -> bool:
    name = path.name.lower()
    return name in SENSITIVE_NAMES or "token" in name or "secret" in name


def _safe_path(root: Path, relative: str) -> Path:
    if not relative or relative.startswith(("/", "~")):
        raise SafetyError(f"Đường dẫn không hợp lệ: {relative!r}")
    target = (root / relative).resolve()
    root_resolved = root.resolve()
    if target != root_resolved and root_resolved not in target.parents:
        raise SafetyError(f"Đường dẫn vượt ngoài repository: {relative}")
    if _is_sensitive(target):
        raise SafetyError(f"Không được thao tác file nhạy cảm: {relative}")
    return target


def iter_project_files(root: Path, selected: Iterable[str] | None = None) -> list[Path]:
    if selected:
        files = [_safe_path(root, item) for item in selected]
        return [p for p in files if p.is_file() and not _is_sensitive(p)]

    result: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file() or any(part in IGNORED_PARTS for part in path.parts):
            continue
        if _is_sensitive(path) or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        result.append(path)
    return sorted(result)


def build_context(root: Path, selected: Iterable[str] | None = None,
                  max_total_chars: int = 90_000,
                  max_file_chars: int = 15_000) -> str:
    chunks: list[str] = []
    total = 0
    for path in iter_project_files(root, selected):
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        rel = path.relative_to(root)
        block = f"\n--- FILE: {rel} ---\n{text[:max_file_chars]}\n"
        if total + len(block) > max_total_chars:
            break
        chunks.append(block)
        total += len(block)
    return "".join(chunks)


def generate_plan(root: str | Path, task: str,
                  selected_files: Iterable[str] | None = None,
                  model: str = "gemini-3.5-flash",
                  api_key: str | None = None) -> AgentPlan:
    root_path = Path(root).resolve()
    if not root_path.is_dir():
        raise FileNotFoundError(f"Không tìm thấy repository: {root_path}")
    key = api_key or os.environ.get("GEMINI_API_KEY")
    if not key:
        raise RuntimeError("Thiếu GEMINI_API_KEY trong Colab Secrets hoặc biến môi trường.")

    context = build_context(root_path, selected_files)
    prompt = f"""
Bạn là Builder của dự án QuangQuy AI. Hãy lập kế hoạch sửa repository theo yêu cầu.

YÊU CẦU:
{task}

QUY TẮC BẮT BUỘC:
- Chỉ được action=create hoặc action=update. Không xóa, đổi tên hay di chuyển file.
- Chỉ thay đổi file nằm trong repository.
- Không tạo hoặc sửa .env, token, secret, credentials hoặc private key.
- Giữ thay đổi tối thiểu, dễ review và có thể build/test.
- Trả về JSON hợp lệ, không có markdown ngoài JSON.

SCHEMA:
{{
  "summary": "mô tả ngắn",
  "risk": "low|medium|high",
  "changes": [
    {{"path": "đường/dẫn/file", "action": "create|update", "content": "toàn bộ nội dung file sau thay đổi", "reason": "lý do"}}
  ],
  "commands": ["chỉ lệnh test/build an toàn nếu cần"],
  "notes": ["điều cần người dùng biết"]
}}

NỘI DUNG REPOSITORY:
{context}
"""
    client = genai.Client(api_key=key)
    response = client.models.generate_content(model=model, contents=prompt)
    raw = _strip_json_fence(response.text or "")
    data = json.loads(raw)
    changes = [Change(**item) for item in data.get("changes", [])]
    plan = AgentPlan(
        summary=str(data.get("summary", "")),
        risk=str(data.get("risk", "high")).lower(),
        changes=changes,
        commands=[str(x) for x in data.get("commands", [])],
        notes=[str(x) for x in data.get("notes", [])],
    )
    validate_plan(root_path, plan)
    return plan


def validate_plan(root: Path, plan: AgentPlan) -> None:
    if plan.risk not in {"low", "medium", "high"}:
        raise SafetyError(f"Mức rủi ro không hợp lệ: {plan.risk}")
    if len(plan.changes) > 30:
        raise SafetyError("Quá nhiều file trong một lần thay đổi; hãy chia tác vụ nhỏ hơn.")
    for change in plan.changes:
        if change.action not in {"create", "update"}:
            raise SafetyError(f"Action bị chặn: {change.action}")
        target = _safe_path(root, change.path)
        if change.action == "create" and target.exists():
            raise SafetyError(f"File đã tồn tại nhưng plan yêu cầu create: {change.path}")
        if change.action == "update" and not target.exists():
            raise SafetyError(f"File chưa tồn tại nhưng plan yêu cầu update: {change.path}")
        if len(change.content) > 500_000:
            raise SafetyError(f"Nội dung file quá lớn: {change.path}")


def print_plan(plan: AgentPlan) -> None:
    print(f"TÓM TẮT: {plan.summary}")
    print(f"RỦI RO: {plan.risk.upper()}")
    print("\nFILE THAY ĐỔI:")
    for idx, change in enumerate(plan.changes, 1):
        print(f" {idx}. [{change.action}] {change.path} — {change.reason}")
    if plan.commands:
        print("\nLỆNH KIỂM TRA:")
        for command in plan.commands:
            print(f" - {command}")
    if plan.notes:
        print("\nGHI CHÚ:")
        for note in plan.notes:
            print(f" - {note}")


def backup_changes(root: Path, plan: AgentPlan, backup_root: str | Path) -> Path:
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    destination = Path(backup_root).expanduser().resolve() / timestamp
    destination.mkdir(parents=True, exist_ok=True)
    for change in plan.changes:
        source = _safe_path(root, change.path)
        if source.exists():
            target = destination / change.path
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
    return destination


def apply_plan(root: str | Path, plan: AgentPlan, *, approved: bool,
               backup_root: str | Path | None = None) -> list[str]:
    root_path = Path(root).resolve()
    validate_plan(root_path, plan)
    if not approved:
        raise SafetyError("Chưa được duyệt. Đặt approved=True sau khi xem kế hoạch.")
    if plan.risk == "high":
        raise SafetyError("Plan rủi ro cao bị chặn; hãy chia nhỏ hoặc review thủ công.")

    if backup_root:
        backup_changes(root_path, plan, backup_root)

    changed: list[str] = []
    for change in plan.changes:
        target = _safe_path(root_path, change.path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(change.content, encoding="utf-8")
        changed.append(change.path)
    return changed


def run_allowed_commands(root: str | Path, commands: Iterable[str],
                         allowlist: Iterable[str]) -> list[dict[str, Any]]:
    root_path = Path(root).resolve()
    allowed = set(allowlist)
    results: list[dict[str, Any]] = []
    for command in commands:
        if command not in allowed:
            results.append({"command": command, "skipped": True, "reason": "not allowlisted"})
            continue
        completed = subprocess.run(
            command.split(), cwd=root_path, capture_output=True, text=True, timeout=600
        )
        results.append({
            "command": command,
            "returncode": completed.returncode,
            "stdout": completed.stdout[-4000:],
            "stderr": completed.stderr[-4000:],
        })
    return results


def git_commit(root: str | Path, branch: str, message: str) -> None:
    root_path = Path(root).resolve()
    subprocess.run(["git", "checkout", "-B", branch], cwd=root_path, check=True)
    subprocess.run(["git", "add", "-A"], cwd=root_path, check=True)
    status = subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=root_path)
    if status.returncode == 0:
        print("Không có thay đổi để commit.")
        return
    subprocess.run(["git", "commit", "-m", message], cwd=root_path, check=True)
