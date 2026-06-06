#!/usr/bin/env python3
"""
编程入门IDE指南 - 全自动更新脚本
功能：
  1. 验证所有链接有效性（HEAD 请求）
  2. 从 GitHub Releases / GitLab Tags / PyPI 获取最新版本号和日期
  3. 自动更新 README 中的版本号和日期
  4. 按更新时间降序排序每个表格
  5. 标记超 12 个月未更新的项目
"""

import json
import os
import re
import sys
import urllib.request
import urllib.error
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path

STALE_DAYS = 365
TIMEOUT = 12
README_PATH = Path(__file__).parent.parent / "README.md"
TOKEN = os.environ.get("GITHUB_TOKEN", "")

# ── 数据源配置 ──────────────────────────────────────────────
# type: github_release | github_tag | gitlab_tag | pypi | static
# repo: owner/repo (GitHub) or project/path (GitLab/PyPI)
SOURCES = {
    # === 一、解压即用 ===
    "WinPython":        {"type": "github_release", "repo": "winpython/winpython"},
    "Thonny":           {"type": "github_release", "repo": "thonny/thonny"},
    "PyScripter":       {"type": "github_release", "repo": "lmbelo/pyscripter"},
    "Arduino IDE":      {"type": "github_release", "repo": "arduino/arduino-ide"},
    "Red Panda C++":    {"type": "github_release", "repo": "royqh1979/RedPanda-CPP"},
    "BlueJ":            {"type": "static",      "check_url": "https://bluej.org"},
    "LiteIDE":          {"type": "github_release", "repo": "visualfc/liteide"},
    "Racket":           {"type": "github_release", "repo": "racket/racket"},
    "Processing":       {"type": "github_release", "repo": "processing/processing4"},
    "Lazarus":          {"type": "static",      "check_url": "https://www.lazarus-ide.org"},
    "小龙 Dev-C++":      {"type": "static",      "check_url": "https://gitee.com/devcpp/devcpp"},

    # === 二、需要配置环境 ===
    "IntelliJ IDEA CE": {"type": "github_release", "repo": "JetBrains/intellij-community"},
    "NetBeans":         {"type": "github_release", "repo": "apache/netbeans"},
    "Eclipse":          {"type": "static",       "check_url": "https://eclipse.org"},
    "Android Studio":   {"type": "static",       "check_url": "https://developer.android.com/studio"},
    "PyCharm CE":       {"type": "static",       "check_url": "https://www.jetbrains.com/pycharm/"},
    "Spyder":           {"type": "github_release", "repo": "spyder-ide/spyder"},
    "VS Community":     {"type": "static",       "check_url": "https://visualstudio.microsoft.com/vs/community/"},
    "CLion":            {"type": "static",       "check_url": "https://www.jetbrains.com/clion/"},
    "WebStorm":         {"type": "static",       "check_url": "https://www.jetbrains.com/webstorm/"},

    # === 三、编辑器 ===
    "VS Code":          {"type": "github_release", "repo": "microsoft/vscode"},
    "Zed":              {"type": "github_release", "repo": "zed-industries/zed"},
    "Sublime Text":     {"type": "static",       "check_url": "https://www.sublimetext.com"},
    "Kate":             {"type": "github_tag",   "repo": "KDE/kate", "name_re": r"v?(\d+\.\d+\.\d+)"},
    "RoslynPad":        {"type": "github_release", "repo": "roslynpad/roslynpad"},
    "Vim/Neovim":       {"type": "github_release", "repo": "neovim/neovim"},
    "nano":             {"type": "static",       "check_url": "https://nano-editor.org"},
    "gedit":            {"type": "gitlab_tag",   "repo": "World/gedit/gedit"},
    "Lapce":            {"type": "github_release", "repo": "lapce/lapce"},
    "Emacs":            {"type": "static",       "check_url": "https://www.gnu.org/software/emacs/"},
    "Helix":            {"type": "github_release", "repo": "helix-editor/helix"},
}


def api_get(url, headers=None, timeout=TIMEOUT):
    hdrs = {"User-Agent": "beginner-ide-guide-updater", "Accept": "application/json"}
    if TOKEN:
        hdrs["Authorization"] = f"token {TOKEN}"
    if headers:
        hdrs.update(headers)
    try:
        req = urllib.request.Request(url, headers=hdrs)
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode())
    except Exception as e:
        return None


def check_link(url, timeout=8):
    """HEAD/GET request to verify link is alive. Returns True/False."""
    hdrs = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"}
    try:
        req = urllib.request.Request(url, method="HEAD", headers=hdrs)
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status < 400
    except urllib.error.HTTPError as e:
        return e.code < 500  # 4xx (except 500+) = probably alive (WAF/rate-limit)
    except Exception:
        # HEAD failed, try GET with small range
        try:
            req = urllib.request.Request(url, headers=hdrs)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                resp.read(1024)  # read just 1KB
                return resp.status < 400
        except urllib.error.HTTPError as e:
            return e.code < 500
        except Exception:
            return False


def clean_version(tag):
    """Clean version string from tag name."""
    v = tag.strip()
    # Strip common prefixes
    for prefix in ("idea/", "pycharm/", "webstorm/", "clion/", "android-studio/"):
        if v.lower().startswith(prefix):
            v = v[len(prefix):]
    # Strip processing-XXXX- prefix
    v = re.sub(r'^processing-\d+-', '', v)
    # Strip emacs- prefix
    v = re.sub(r'^emacs-', '', v)
    # Strip leading v (but not vx38.4 style → strip vx too)
    if v.startswith("vx") and len(v) > 2:
        v = v[1:]  # keep the x: vx38.4 → x38.4
    elif v.startswith("v") and len(v) > 1 and v[1].isdigit():
        v = v[1:]
    # Strip trailing build info: "17.4.20260511final" → "17.4"
    v = re.sub(r'\.\d{8}\w*$', '', v)
    return v


def fetch_github_release(repo):
    """Get latest release from GitHub. Returns (version, date) or None."""
    # Try /releases/latest first
    data = api_get(f"https://api.github.com/repos/{repo}/releases/latest")
    if data and data.get("tag_name"):
        tag = data["tag_name"]
        date = data.get("published_at", data.get("created_at", ""))
        return clean_version(tag), date[:10] if date else ""
    # Fallback: first from list
    data_list = api_get(f"https://api.github.com/repos/{repo}/releases?per_page=3")
    if data_list and isinstance(data_list, list):
        for data in data_list:
            if data.get("tag_name"):
                tag = data["tag_name"]
                date = data.get("published_at", data.get("created_at", ""))
                return clean_version(tag), date[:10] if date else ""
    # Fallback: try tags
    return fetch_github_tag(repo)


def fetch_github_tag(repo, name_re=None):
    """Get latest tag from GitHub. Returns (version, date) or None."""
    data = api_get(f"https://api.github.com/repos/{repo}/tags?per_page=10")
    if not data or not isinstance(data, list):
        return None
    for tag in data:
        name = tag["name"]
        commit_date = tag.get("commit", {}).get("committed_date", "")
        date_str = commit_date[:10] if commit_date else ""
        if name_re:
            m = re.search(name_re, name)
            if m:
                return m.group(1), date_str
        else:
            return clean_version(name), date_str
    return None


def fetch_gitlab_tag(project_path):
    """Get latest tag from GNOME GitLab. Returns (version, date) or None."""
    encoded = urllib.parse.quote(project_path, safe="")
    data = api_get(f"https://gitlab.gnome.org/api/v4/projects/{encoded}/repository/tags?per_page=5")
    if data and isinstance(data, list) and len(data) > 0:
        tag = data[0]
        version = tag["name"]
        date = tag.get("commit", {}).get("committed_date", "")
        return version, date[:10] if date else ""
    return None


def fetch_version(name, cfg):
    """Fetch latest version info based on source type. Returns (version, date) or None."""
    src_type = cfg["type"]

    if src_type == "github_release":
        return fetch_github_release(cfg["repo"])
    elif src_type == "github_tag":
        return fetch_github_tag(cfg["repo"], cfg.get("name_re"))
    elif src_type == "gitlab_tag":
        return fetch_gitlab_tag(cfg["repo"])
    elif src_type == "pypi":
        data = api_get(f"https://pypi.org/pypi/{cfg['package']}/json")
        if data:
            ver = data["info"]["version"]
            releases = data["releases"].get(ver, [])
            date = releases[0]["upload_time"][:10] if releases else ""
            return ver, date
    elif src_type == "static":
        # Just check link, don't update version
        url = cfg["check_url"]
        alive = check_link(url)
        if alive:
            return "static", "static"
        else:
            return "dead", "dead"
    return None


def format_date(iso_str):
    if not iso_str or iso_str in ("static", "dead"):
        return iso_str
    try:
        return datetime.fromisoformat(iso_str.replace("Z", "+00:00")).strftime("%Y-%m-%d")
    except Exception:
        return iso_str[:10]


def parse_date_for_sort(date_str):
    """Parse date string for sorting. Returns YYYY-MM-DD or empty string."""
    if not date_str or date_str in ("static", "dead", "-", ""):
        return "0000-00-00"
    # Strip bold markers
    clean = date_str.strip().replace("**", "")
    parts = clean.split("-")
    try:
        if len(parts) == 3:
            return clean
        elif len(parts) == 2:
            return clean + "-01"
        elif len(parts) == 1 and parts[0].isdigit():
            return parts[0] + "-01-01"
    except:
        pass
    return "0000-00-00"


def update_readme_tables(results):
    """Update version/date in README tables and re-sort each table."""
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    updated_count = 0
    dead_links = []

    for name, info in results.items():
        version, date_str, link_alive = info["version"], info["date"], info["link_alive"]

        if not link_alive:
            dead_links.append(name)
            continue

        if version in ("static", "dead") or date_str in ("static", ""):
            continue

        # Find this IDE's row in the README and update version + date
        # Pattern: | ... | [IDE Name](url) | OLD_VERSION | OLD_DATE | ... |
        # We need to match the row containing the IDE name
        pattern = re.compile(
            r'(\|[^|]*\|[^|]*\[' + re.escape(name) + r'\]\([^)]+\)[^|]*\|)\s*'
            r'[^|]+\|'   # version
            r'\s*[^|]+\|'  # date
            r'([^|]*\|)',  # rest
            re.MULTILINE
        )

        def replacer(m):
            return f"{m.group(1)} {version} | {date_str} |{m.group(2)}"

        new_content = pattern.sub(replacer, content, count=1)
        if new_content != content:
            content = new_content
            updated_count += 1

    # Sort each table by date (newest first)
    content = sort_all_tables(content)

    # Update status table
    content = update_status_table(content, results)

    # Update timestamp
    now_str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    content = re.sub(r"> 🤖 最后自动检查:.*", f"> 🤖 最后自动检查: {now_str}", content)

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    return updated_count, dead_links


def sort_all_tables(content):
    """Sort all markdown tables by date column (4th column, newest first)."""
    lines = content.split("\n")
    result = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Detect table header (contains | and at least 4 columns with a date-like column)
        if "|" in line and i + 1 < len(lines) and re.match(r'\|[-|\s]+\|', lines[i + 1]):
            # Collect header, divider, and rows
            header = line
            divider = lines[i + 1]
            i += 2
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|") and lines[i].strip().endswith("|"):
                rows.append(lines[i])
                i += 1

            # Find the date column (look for column with YYYY-MM-DD pattern)
            date_col = -1
            for row in rows[:3]:
                cols = [c.strip() for c in row.split("|")]
                for j, col in enumerate(cols):
                    clean = col.replace("**", "")
                    if re.match(r'\d{4}(-\d{2}){0,2}$', clean):
                        date_col = j
                        break
                if date_col >= 0:
                    break

            if date_col >= 0 and len(rows) > 1:
                def sort_key(row):
                    cols = [c.strip() for c in row.split("|")]
                    if date_col < len(cols):
                        return parse_date_for_sort(cols[date_col].replace("**", ""))
                    return "0000-00-00"

                rows.sort(key=sort_key, reverse=True)

            result.append(header)
            result.append(divider)
            result.extend(rows)
        else:
            result.append(line)
            i += 1

    return "\n".join(result)


def update_status_table(content, results):
    """Update the status section table with latest dates, sorted."""
    # Extract existing dates from old status table
    old_dates = {}
    old_match = re.search(r"\| 项目 \| 最后活跃 \| 状态 \|\n\|-+.*?\n(.*?)(?=\n\n|\n## )", content, re.DOTALL)
    if old_match:
        for row in old_match.group(1).strip().split("\n"):
            cols = [c.strip() for c in row.split("|")]
            if len(cols) >= 4 and cols[1] and cols[2]:
                old_dates[cols[1]] = cols[2]

    entries = []
    for name, info in results.items():
        date_str = info.get("date", "")
        link_alive = info.get("link_alive", True)
        stale = info.get("stale", False)

        if not link_alive:
            emoji = "❌ 链接失效"
        elif stale:
            emoji = "⚠️ 可能停更"
        else:
            emoji = "✅"

        # For static entries, preserve the old date from the existing table
        if date_str in ("static", "dead", ""):
            display_date = old_dates.get(name, "-")
        else:
            display_date = date_str

        entries.append((name, display_date, emoji, parse_date_for_sort(display_date)))

    entries.sort(key=lambda x: x[3], reverse=True)

    lines = [
        "| 项目 | 最后活跃 | 状态 |",
        "|------|---------|------|",
    ]
    for name, date_str, emoji, _ in entries:
        lines.append(f"| {name} | {date_str} | {emoji} |")

    new_table = "\n".join(lines)

    # Replace old status table
    pattern = r"(\| 项目 \| 最后活跃 \| 状态 \|\n\|-+.*?)(?=\n\n|\n## )"
    content_new = re.sub(pattern, new_table, content, flags=re.DOTALL)
    return content_new


def main():
    if not README_PATH.exists():
        print(f"❌ README not found: {README_PATH}")
        sys.exit(1)

    now = datetime.now(timezone.utc)
    print(f"{'='*60}")
    print(f"  编程入门IDE指南 - 全自动更新")
    print(f"  {now.strftime('%Y-%m-%d %H:%M UTC')}")
    print(f"{'='*60}")

    results = {}
    counts = {"updated": 0, "static": 0, "dead": 0, "stale": 0}

    for name, cfg in SOURCES.items():
        print(f"\n  [{name}]")
        info = {"version": "", "date": "", "link_alive": True, "stale": False}

        # 1. Fetch latest version
        result = fetch_version(name, cfg)
        if result:
            ver, date = result
            if ver == "dead":
                info["link_alive"] = False
                counts["dead"] += 1
                print(f"    ❌ Link dead: {cfg.get('check_url', cfg.get('repo', '?'))}")
            elif ver == "static":
                counts["static"] += 1
                # Still check link
                url = cfg.get("check_url", "")
                if url:
                    alive = check_link(url)
                    info["link_alive"] = alive
                    print(f"    {'✅' if alive else '❌'} Link: {url}")
            else:
                info["version"] = ver
                info["date"] = format_date(date)
                counts["updated"] += 1
                print(f"    v{ver}  {format_date(date)}")

                # Check staleness
                sort_date = parse_date_for_sort(format_date(date))
                if sort_date != "0000-00-00":
                    try:
                        release_dt = datetime.strptime(sort_date, "%Y-%m-%d").replace(tzinfo=timezone.utc)
                        if (now - release_dt).days > STALE_DAYS:
                            info["stale"] = True
                            counts["stale"] += 1
                            print(f"    ⚠️ STALE: >{STALE_DAYS} days since last release")
                    except ValueError:
                        pass
        else:
            print(f"    ⚠️ Could not fetch version info")
            info["link_alive"] = True  # Assume alive if we can't check

        results[name] = info

    print(f"\n{'='*60}")
    print(f"  Updated: {counts['updated']}  Static: {counts['static']}  Dead: {counts['dead']}  Stale: {counts['stale']}")
    print(f"{'='*60}")

    # Update README
    updated_count, dead_links = update_readme_tables(results)

    print(f"\n✅ README updated: {updated_count} entries modified")

    if dead_links:
        print(f"\n❌ DEAD LINKS (needs manual fix):")
        for name in dead_links:
            print(f"  - {name}: {SOURCES[name].get('check_url', '?')}")

    stale_list = [n for n, i in results.items() if i["stale"]]
    if stale_list:
        print(f"\n⚠️  STALE (>{STALE_DAYS} days, consider removing):")
        for name in stale_list:
            print(f"  - {name}: {results[name]['date']}")

    # Dead links are logged as warnings in the README (❌ markers),
    # but should not block the workflow from committing other updates.
    return 0


if __name__ == "__main__":
    sys.exit(main())
