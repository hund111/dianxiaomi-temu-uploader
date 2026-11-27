#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把仓库最近的提交写回 README.md 的「项目动态」区块。

由 .github/workflows/update-activity.yml 在每次 push / 每日定时 / 手动触发时调用。
只在两个标记之间改写，其余内容一个字不动。
"""

import datetime
import json
import os
import re
import urllib.request

START = "<!-- ACTIVITY:START -->"
END = "<!-- ACTIVITY:END -->"
RECENT = 5

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README = os.path.join(ROOT, "README.md")
REPO = os.environ.get("REPO", "")
TOKEN = os.environ.get("GITHUB_TOKEN", "")


def api(path):
    url = "https://api.github.com/repos/%s%s" % (REPO, path)
    req = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json",
        "Authorization": "Bearer %s" % TOKEN,
        "User-Agent": "activity-refresh",
    })
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8")), resp.headers


def total_commits():
    try:
        _, headers = api("/commits?per_page=1")
        link = headers.get("Link", "") or ""
        m = re.search(r'[?&]page=(\d+)>;\s*rel="last"', link)
        return int(m.group(1)) if m else None
    except Exception:
        return None


def clean(text, limit=46):
    text = (text or "").splitlines()[0] if text else ""
    text = text.replace("|", "\\|").replace("`", "'").strip()
    return text[:limit] + ("…" if len(text) > limit else "")


def build_block():
    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8)))
    stamp = now.strftime("%Y-%m-%d %H:%M")
    try:
        commits, _ = api("/commits?per_page=%d" % RECENT)
    except Exception as e:
        return "%s\n> 读取提交失败：%s\n%s" % (START, e, END)

    total = total_commits()
    lines = [START, ""]
    lines.append("> 最近刷新：**%s**（北京时间）%s" % (
        stamp, "· 累计提交 **%d** 次" % total if total else ""))
    lines.append("")
    lines.append("| 日期 | 提交信息 | 作者 | 提交 |")
    lines.append("|---|---|---|---|")
    for c in commits:
        info = c.get("commit", {})
        date = (info.get("committer") or {}).get("date", "")[:10]
        msg = clean(info.get("message", ""))
        author = (info.get("author") or {}).get("name", "") or "-"
        sha = c.get("sha", "")[:7]
        link = "https://github.com/%s/commit/%s" % (REPO, c.get("sha", ""))
        lines.append("| %s | %s | %s | [`%s`](%s) |" % (date, msg, author, sha, link))
    lines.append("")
    lines.append("<sub>这个模块由 `.github/workflows/update-activity.yml` 自动维护，无需手动改。</sub>")
    lines.append(END)
    return "\n".join(lines)


def main():
    if not REPO:
        raise SystemExit("缺少环境变量 REPO（形如 owner/name）")
    with open(README, "r", encoding="utf-8") as f:
        text = f.read()
    if START not in text or END not in text:
        raise SystemExit("README 里没找到项目动态标记，跳过")
    head, rest = text.split(START, 1)
    _, tail = rest.split(END, 1)
    new_text = head + build_block() + tail
    if new_text == text:
        print("内容无变化")
        return
    with open(README, "w", encoding="utf-8", newline="\n") as f:
        f.write(new_text)
    print("项目动态已更新")


if __name__ == "__main__":
    main()
