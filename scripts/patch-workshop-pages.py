#!/usr/bin/env python3
"""Patch dennisyu.com workshop landing pages: unjam mobile header, dual-runtime, family index."""
from __future__ import annotations

import base64
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

SITE = "https://dennisyu.com"
UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
)
ROOT = Path(__file__).resolve().parents[1]
CHROME_PATH = Path(__file__).resolve().parent / "workshop-chrome.css"

# Replica / workshop leave-behinds that share the jammed XPro header.
SLUGS = (
    "dealcon",
    "wichita",
    "digimarcon",
    "jva",
    "workshops",
    "affiliateworld",
    "dunk-playbook",
    "dunkademics",
    "activate",
    "workshop",
)
RUNTIME_SLUGS = {"dealcon", "wichita", "digimarcon", "jva"}

RUNTIME_BADGE = """
<div class=\"badge\" id=\"dy-runtime\">⚡ <span><b>Same factory, any runtime.</b> This page still installs on Claude. Cursor + Grok 4.6 is the workshop; Grok Bot is the named staff. Grok-skinned leave-behind: <a href=\"https://dennisyu.com/optimize/\" style=\"color:var(--accent2);font-weight:700\">dennisyu.com/optimize</a>. Every room we have replicated: <a href=\"https://dennisyu.com/workshops/\" style=\"color:var(--accent2);font-weight:700\">dennisyu.com/workshops</a>.</span></div>
"""

NEW_ROOM_CARDS = """
    <div class=\"ex\" id=\"ex-optimize\" style=\"display:grid;grid-template-columns:118px 1fr;gap:26px;align-items:start\">
      <div class=\"badge\" style=\"background:var(--gold)\">OPTIMIZE<br>LIVE<br>2026</div>
      <div>
        <h3><a href=\"https://dennisyu.com/optimize\">dennisyu.com/optimize →</a></h3>
        <p class=\"muted\">Damon Burton’s Optimize Live in Layton. Same 10-skill pack, skinned Grok-first (Cursor + Grok 4.6 / Grok Bot). Stories, credibility audit, Topic Wheel, then Dollar a Day on every channel — this room’s leave-behind is a YouTube $1/day demo, not a Facebook-only trick.</p>
      </div>
    </div>
"""

def env_creds() -> tuple[str, str]:
    user = os.environ.get("DENNISYU_WP_USER") or os.environ.get("WP_USER")
    password = os.environ.get("DENNISYU_WP_APP_PASSWORD") or os.environ.get("WP_APP_PASSWORD")
    envf = Path("/tmp/wp.env")
    if (not user or not password) and envf.is_file():
        for line in envf.read_text(encoding="utf-8").splitlines():
            if line.startswith("DENNISYU_WP_USER=") and not user:
                user = line.split("=", 1)[1]
            elif line.startswith("DENNISYU_WP_APP_PASSWORD=") and not password:
                password = line.split("=", 1)[1]
    if not user or not password:
        print("MISSING_CREDS")
        sys.exit(2)
    return user, password
