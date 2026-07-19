from pathlib import Path
import os
import subprocess

REPO_URL = "https://github.com/qquy28888-ops/quangquy-ai.git"
WORKDIR = Path("/content/quangquy-ai")


def run(command: str, cwd: Path | None = None) -> None:
    print(f"$ {command}")
    subprocess.run(command, shell=True, check=True, cwd=cwd)


if not WORKDIR.exists():
    run(f"git clone {REPO_URL} {WORKDIR}")
else:
    run("git pull", WORKDIR)

os.chdir(WORKDIR)
print("\nQuangQuy AI đã sẵn sàng tại:", WORKDIR)
print("Các file trong thư mục gốc:")
for item in sorted(WORKDIR.iterdir()):
    print("-", item.name)

print("\nLưu ý: Không nhập token trực tiếp vào notebook hoặc commit file .env lên GitHub.")
