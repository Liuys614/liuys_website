#!/usr/bin/env python3
"""Pre-publish prose check for guide posts (report only, changes nothing).

Usage:
    python3 scripts/unslop_check.py <app>/guides/posts/<slug>.json [more.json ...]

Runs the unslop-writing skill's deterministic scanners (phrase + structure) on the
post's title, meta description, body and FAQs, plus site-specific health-claim checks:

  Health checks (alcohol-free-tracker, quit-weed, quit-vaping, pill-reminder only):
  * vague attribution ("studies show", "research demonstrates") with no named source
  * pseudo-clinical inflation ("clinical", "peer-reviewed", "evidence-based") used as a label
  * absolute health promises ("always", "harmless", "is broken", "guarantees")
  * em dashes (target: at most 2 per guide)

Exit code 1 when a hard problem is found, so the daily task can stop before publishing.
"""
from __future__ import annotations

import html
import json
import os
import re
import subprocess
import sys

SKILL = os.path.expanduser("~/.claude/skills/unslop-writing/scripts")

VAGUE = re.compile(
    r"\b((?:recent |clinical |circadian |sleep |neuroimaging |some )?(?:studies|research|neuroscience(?: research)?|science|experts?|scientists)"
    r" (?:show|shows|showed|suggest|suggests|indicate|indicates|demonstrate|demonstrates|prove|proves|say|says|agree|found|have shown))\b",
    re.I,
)
CLINICAL = re.compile(r"\b(clinical(?:ly)?(?! trial| guideline| practice)|peer[- ]reviewed|evidence[- ]based|science[- ]backed|scientifically proven)\b", re.I)
ABSOLUTE = re.compile(r"\b(always take|never take|is harmless|completely harmless|(?:addiction|dependence|habit) is (?:broken|gone|over)|guarantee[sd]? (?:that|to|you|recovery|results)|cures? (?:anxiety|insomnia|withdrawal|addiction|cravings)|100% safe|zero risk)\b", re.I)
SOURCE_HINT = re.compile(r"(\(\d{4}\)|et al\.|doi\.org|pubmed|ncbi\.nlm|nih\.gov|journal of|\bJ\.? ?[A-Z][a-z]+)", re.I)


def post_text(path: str) -> tuple[str, str]:
    p = json.load(open(path, encoding="utf-8"))
    body = p.get("body_html", "")
    body = re.sub(r"<(script|style)[\s\S]*?</\1>", " ", body)
    body = re.sub(r"</(p|li|h[1-6]|tr|div|blockquote)>", "\n\n", body)
    body = html.unescape(re.sub(r"<[^>]+>", " ", body))
    faqs = "\n\n".join(f"{f.get('question','')}\n\n{f.get('answer','')}" for f in p.get("faqs", []))
    parts = [p.get("title", ""), p.get("meta_description", ""), body, faqs]
    text = "\n\n".join(re.sub(r"[ \t]+", " ", x).strip() for x in parts if x)
    return re.sub(r"\n{3,}", "\n\n", text), p.get("body_html", "")


def run_scanner(name: str, text: str) -> dict:
    script = os.path.join(SKILL, name)
    if not os.path.exists(script):
        return {"skipped": f"{script} not found"}
    proc = subprocess.run([sys.executable, script], input=text, capture_output=True, text=True)
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError:
        return {"error": (proc.stderr or proc.stdout)[-300:]}


def snippet(text: str, m: re.Match, pad: int = 70) -> str:
    return text[max(0, m.start() - pad): m.end() + pad].replace("\n", " ").strip()


HEALTH_APPS = ("alcohol-free-tracker", "quit-weed", "quit-vaping", "pill-reminder")


def check(path: str) -> int:
    text, raw = post_text(path)
    hard = 0
    health = any(path.replace("\\", "/").startswith(a + "/") or f"/{a}/" in path for a in HEALTH_APPS)
    print(f"\n=== {path}")

    phrases = run_scanner("banned_phrase_scan.py", text)
    for v in phrases.get("violations", [])[:12]:
        if v.get("severity") == "hard":
            hard += 1
        print(f"  [{v.get('severity')}] phrase '{v.get('phrase')}' ({v.get('category')})")

    structure = run_scanner("structure_scan.py", text)
    for v in (structure.get("violations") or structure.get("patterns") or [])[:8]:
        name = v.get("pattern") or v.get("name") or v.get("category")
        sev = v.get("severity", "soft")
        if sev == "hard":
            hard += 1
        print(f"  [{sev}] structure '{name}': {str(v.get('context') or v.get('text') or '')[:90]}")

    for m in (VAGUE.finditer(text) if health else []):
        near = text[m.start(): m.end() + 260]
        if SOURCE_HINT.search(near) or "<a href" in raw[max(0, raw.find(m.group(0)) - 200): raw.find(m.group(0)) + 400]:
            continue
        hard += 1
        print(f"  [hard] vague attribution, no named source: \"{snippet(text, m)}\"")
    for m in (CLINICAL.finditer(text) if health else []):
        hard += 1
        print(f"  [hard] clinical label: \"{snippet(text, m)}\"")
    for m in (ABSOLUTE.finditer(text) if health else []):
        hard += 1
        print(f"  [hard] absolute health claim: \"{snippet(text, m)}\"")

    dashes = text.count("—")
    if dashes > 2:
        print(f"  [soft] {dashes} em dashes (target <= 2)")

    print(f"  -> {'FAIL' if hard else 'PASS'} ({hard} hard)")
    return hard


def main() -> None:
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    total = sum(check(p) for p in sys.argv[1:])
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
