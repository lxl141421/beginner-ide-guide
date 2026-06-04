#!/usr/bin/env python3
"""
编程入门IDE指南 - 自动更新检查脚本（轻量版）
只检查 repo 的 pushed_at，不逐个查 release，大幅减少 API 调用。
"""

import json
import os
import re
import sys
import urllib.request
import urllib.error
from datetime import datetime, timedelta, timezone
from pathlib import Path

# 项目名 → GitHub owner/repo
REPO_MAP = {
    "Thonny":           "thonny/thonny",
    "Processing":       "processing/processing4",
    "Arduino IDE":      "arduino/arduino-ide",
    "Mu Editor":        "codewith/mu",
    "BlueJ":            None,  # 不确定 repo
    "Greenfoot":        "greenfoot/greenfoot",
    "Racket":           "racket/racket",
    "Code::Blocks":     None,
    "IntelliJ IDEA CE": "JetBrains/intellij-community",
    "PyCharm CE":       "JetBrains/pycharm-community",
    "VS Community":     None,
    "Eclipse":          "eclipse-platform/eclipse.platform",
    "NetBeans":         "apache/netbeans",
    "Android Studio":   None,
    "CLion":            None,
    "WebStorm":         None,
    "Spyder":           "spyder-ide/spyder",
    "VS Code":          "microsoft/vscode",
    "Neovim":           "neovim/neovim",
    "Sublime Text":     None,
    "Helix":            "helix-editor/helix",
    "Zed":              "zed-industries/zed",
    "Lapce":            "lapce/lapce",
    "Kate":             "KDE/kate",
}

STALE_DAYS = 365
API_BASE = "https://api.github.com"


def gh_get(path: str, timeout: int = 10) -> dict | None:
    url = f"{API_BASE}{path}"
    headers = {"Accept": "application/vnd.github.v3+json", "User-Agent": "beginner-ide-guide"}
    token = os.environ.get("GITHUB_TOKEN", "")
    if token:
        headers["Authorization"] = f"token {token}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode())
    except Exception as e:
        print(f"  ⚠ {path}: {e}")
        return None


def check_repo(name: str, repo: str | None) -> dict:
    result = {"name": name, "repo": repo, "status": "unknown", "last_active": "", "version": "", "note": ""}

    if not repo:
        result["status"] = "skip"
        result["note"] = "非开源/不在GitHub"
        return result

    print(f"  检查 {name} ({repo})...")
    data = gh_get(f"/repos/{repo}")
    if not data:
        result["status"] = "unknown"
        result["note"] = "API 请求失败"
        return result

    if data.get("archived"):
        result["status"] = "archived"
        result["last_active"] = data.get("pushed_at", "")
        return result

    pushed = data.get("pushed_at", "")
    result["last_active"] = pushed

    if pushed:
        try:
            last_dt = datetime.fromisoformat(pushed.replace("Z", "+00:00"))
            days = (datetime.now(timezone.utc) - last_dt).days
            result["status"] = "stale" if days > STALE_DAYS else "active"
        except (ValueError, TypeError):
            result["status"] = "unknown"

    return result


def format_date(iso_str: str) -> str:
    if not iso_str:
        return "-"
    try:
        return datetime.fromisoformat(iso_str.replace("Z", "+00:00")).strftime("%Y-%m-%d")
    except Exception:
        return iso_str[:10]


def status_emoji(s: str) -> str:
    return {"active": "✅", "stale": "⚠️ 可能停更", "archived": "📦 已归档", "skip": "⏭️", "unknown": "❓"}.get(s, "❓")


def update_readme(results: list[dict], readme_path: str):
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    lines = ["| 项目 | 最后活跃 | 状态 |", "|------|---------|------|"]
    for r in results:
        if r["status"] == "skip":
            continue
        lines.append(f"| {r['name']} | {format_date(r['last_active'])} | {status_emoji(r['status'])} |")

    new_table = "\n".join(lines)
    # 替换旧表格
    pattern = r"(\| 项目 \| 最后活跃 \| 状态 \|\n\|-+.*?)(?=\n\n|\n## )"
    content_new = re.sub(pattern, new_table, content, flags=re.DOTALL)

    now_str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    update_note = f"> 🤖 最后自动检查: {now_str}"
    content_new = re.sub(r"> 🤖 最后自动检查:.*", update_note, content_new)
    if "🤖 最后自动检查" not in content_new:
        content_new = content_new.replace("## 更新状态", f"## 更新状态\n\n{update_note}")

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content_new)
    print(f"\n✅ README 已更新: {readme_path}")


def main():
    readme_path = Path(__file__).parent.parent / "README.md"
    if not readme_path.exists():
        print(f"❌ 找不到 {readme_path}")
        sys.exit(1)

    print(f"{'='*50}")
    print(f"  编程入门IDE指南 - 更新检查")
    print(f"  {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    print(f"{'='*50}")

    results = []
    counts = {"active": 0, "stale": 0, "archived": 0}
    for name, repo in REPO_MAP.items():
        r = check_repo(name, repo)
        results.append(r)
        if r["status"] in counts:
            counts[r["status"]] += 1

    print(f"\n{'='*50}")
    print(f"  ✅ 活跃: {counts['active']}  ⚠️ 可能停更: {counts['stale']}  📦 归档: {counts['archived']}")
    print(f"{'='*50}")

    update_readme(results, str(readme_path))

    alerts = [r for r in results if r["status"] in ("stale", "archived")]
    if alerts:
        print("\n⚠️  以下项目可能需要移除：")
        for r in alerts:
            print(f"  - {r['name']}: {status_emoji(r['status'])} (最后活跃: {format_date(r['last_active'])})")


if __name__ == "__main__":
    main()
