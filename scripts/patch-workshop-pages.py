#!/usr/bin/env python3
"""Patch dennisyu.com workshop landing pages: unjam mobile header, dual-runtime, family index.

Canonical runnable copy is the cloud-agent workspace file
`/agent/scripts/patch-workshop-pages.py` (this GitHub copy is the same job: inject
`workshop-chrome.css`, expand https://dennisyu.com/workshops/ cards).

Live pages were already patched 19 Aug 2026 via WordPress REST. Re-run from a
machine that has DENNISYU_WP_USER + DENNISYU_WP_APP_PASSWORD (never commit those).
"""
from __future__ import annotations

import sys
from pathlib import Path

# Import the chrome file next to this script when both are present.
CHROME_PATH = Path(__file__).resolve().parent / "workshop-chrome.css"

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


def main() -> None:
    if not CHROME_PATH.is_file():
        raise SystemExit(f"missing {CHROME_PATH}")
    print("chrome bytes", CHROME_PATH.stat().st_size)
    print("slugs", ", ".join(SLUGS))
    print("Live index: https://dennisyu.com/workshops/")
    print("This notes copy does not write WordPress. Use the agent workspace script.")
    sys.exit(0)


if __name__ == "__main__":
    main()
