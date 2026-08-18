#!/usr/bin/env python3
"""Publish /optimize to dennisyu.com via WordPress REST.

Reads credentials from environment only. Never prints secret values.
Expected env:
  DENNISYU_WP_USER
  DENNISYU_WP_APP_PASSWORD
"""
from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

SITE = "https://dennisyu.com"
SLUG = "optimize"
TITLE = "Optimize Live: Use AI Aggressively on Your Own Grok"
EXCERPT = (
    "Scan. Paste. Done. Cursor + Grok 4.6 is the workshop. Grok Bot is the "
    "named staff. The 10-skill agent system for Damon Burton's Optimize Live "
    "mastermind in Layton — personal brand, Knowledge Panel, AI Overviews, "
    "and a Content Factory your agency can run for clients."
)
HTML_PATH = Path(__file__).resolve().parents[1] / "pages" / "dennisyu-com-optimize.html"
UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
)


def env_creds() -> tuple[str, str]:
    user = os.environ.get("DENNISYU_WP_USER") or os.environ.get("WP_USER")
    password = os.environ.get("DENNISYU_WP_APP_PASSWORD") or os.environ.get("WP_APP_PASSWORD")
    if not user or not password:
        print("MISSING_CREDS: set DENNISYU_WP_USER and DENNISYU_WP_APP_PASSWORD")
        sys.exit(2)
    return user, password


def request(method: str, url: str, user: str, password: str, payload: dict | None = None) -> tuple[int, dict | str]:
    data = None
    headers = {
        "User-Agent": UA,
        "Accept": "application/json",
    }
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    token = f"{user}:{password}".encode("utf-8")
    import base64

    req.add_header("Authorization", "Basic " + base64.b64encode(token).decode("ascii"))
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            body = resp.read().decode("utf-8")
            try:
                return resp.status, json.loads(body)
            except json.JSONDecodeError:
                return resp.status, body
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        try:
            parsed = json.loads(body)
        except json.JSONDecodeError:
            parsed = body
        return e.code, parsed


def main() -> None:
    user, password = env_creds()
    html = HTML_PATH.read_text(encoding="utf-8")
    content = "<!-- wp:html -->\n" + html + "\n<!-- /wp:html -->"

    status, existing = request(
        "GET",
        f"{SITE}/wp-json/wp/v2/pages?slug={SLUG}&context=edit",
        user,
        password,
    )
    page_id = None
    if status == 200 and isinstance(existing, list) and existing:
        page_id = existing[0].get("id")

    payload = {
        "title": TITLE,
        "slug": SLUG,
        "status": "publish",
        "excerpt": EXCERPT,
        "content": content,
        "author": 30,
        "comment_status": "closed",
        "ping_status": "closed",
    }

    if page_id:
        method, url = "POST", f"{SITE}/wp-json/wp/v2/pages/{page_id}"
    else:
        method, url = "POST", f"{SITE}/wp-json/wp/v2/pages"

    status, result = request(method, url, user, password, payload)
    if status in (200, 201) and isinstance(result, dict):
        print("OK", status, "id", result.get("id"), "link", result.get("link"))
        return
    print("FAIL", status)
    if isinstance(result, dict):
        print("code", result.get("code"), "message", result.get("message"))
    else:
        print(str(result)[:400])
    sys.exit(1)


if __name__ == "__main__":
    main()
