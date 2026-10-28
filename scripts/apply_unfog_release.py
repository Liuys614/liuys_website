#!/usr/bin/env python3
"""Apply the Unfog / Quit Weed release flag to static pages.

The single switch is UNFOG_RELEASED in scripts/site_campaign.py.
False: download buttons become a non-link "Coming soon to the App Store"
and the Smart App Banner is omitted.
True: those buttons become App Store links again (ct=site-quit-weed-landing,
pt=DEFAULT_PROVIDER_TOKEN).

/quit-weed-tracker/ is a symlink to /quit-weed/, so editing quit-weed covers both.
Guide HTML is rendered by quit-weed/scripts/build_guide.py, which reads the same flag.
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from site_campaign import (  # noqa: E402
    DEFAULT_PROVIDER_TOKEN,
    UNFOG_APP_ID,
    UNFOG_RELEASED,
    coming_soon_markup,
    landing_ct,
    make_asc_url,
    smart_banner_tag,
)

APP_ID_IN_URL = re.compile(rf"id{UNFOG_APP_ID}")
ANCHOR_RE = re.compile(
    rf'<a\b[^>]*href="[^"]*id{UNFOG_APP_ID}[^"]*"[^>]*>.*?</a>',
    re.DOTALL,
)
BLOCK_RE = re.compile(r"<!-- UNFOG_CTA ([\w-]+) -->.*?<!-- /UNFOG_CTA -->", re.DOTALL)
BANNER_RE = re.compile(
    rf"\n?[ \t]*<!-- Smart App Banner -->\n[ \t]*<meta name=\"apple-itunes-app\" content=\"app-id={UNFOG_APP_ID}\"\s*/>\n?"
    rf"|\n?[ \t]*<meta name=\"apple-itunes-app\" content=\"app-id={UNFOG_APP_ID}\"\s*/>\n?"
)
DOWNLOAD_RE = re.compile(
    rf'\n[ \t]*"downloadUrl": "https://apps\.apple\.com/[^"]*id{UNFOG_APP_ID}[^"]*",?'
)
JS_BLOCK_RE = re.compile(
    r"// UNFOG_CTA homepage\n.*?// /UNFOG_CTA",
    re.DOTALL,
)

LANDING_CT = landing_ct("quit-weed")

# class, inner HTML used when the app is live again
LIVE_CTA = {
    "nav": ("btn-pill btn-forest", "Get App"),
    "hero": (
        "btn-store-primary",
        '<div class="store-btn-text"><span class="store-small">Download on the</span><span class="store-big">App Store</span></div>',
    ),
    "footer": (
        "btn-store-primary btn-store-gold",
        '<div class="store-btn-text"><span class="store-small">Download on the</span><span class="store-big">App Store</span></div>',
    ),
    "footlink": ("", "App Store"),
    "legal": ("btn-pill btn-forest", "Download App"),
}

FILE_SLOTS = {
    "index.html": ["nav", "hero", "footer", "footlink"],
    "privacy.html": ["legal"],
    "support.html": ["legal"],
    "terms.html": ["legal"],
}


def _class_of(tag: str) -> str:
    match = re.search(r'class="([^"]*)"', tag)
    return match.group(1) if match else ""


def _live_anchor(class_name: str, inner: str) -> str:
    url = make_asc_url(UNFOG_APP_ID, DEFAULT_PROVIDER_TOKEN, LANDING_CT)
    if class_name:
        return (
            f'<a href="{url}" class="{class_name}" target="_blank" rel="noopener">{inner}</a>'
        )
    return f'<a href="{url}" target="_blank" rel="noopener">{inner}</a>'


def _render_slot(name: str, fallback_class: str = "") -> str:
    class_name, inner = LIVE_CTA[name]
    if fallback_class and not class_name:
        class_name = fallback_class
    if UNFOG_RELEASED:
        if name == "footlink":
            return _live_anchor("", "App Store")
        return _live_anchor(class_name, inner)
    use_class = class_name or fallback_class
    return coming_soon_markup(use_class)


def _wrap(name: str, inner: str) -> str:
    return f"<!-- UNFOG_CTA {name} -->{inner}<!-- /UNFOG_CTA -->"


def _migrate_anchors(text: str, names: list) -> str:
    slots = iter(names)

    def sub(match: re.Match) -> str:
        name = next(slots)
        return _wrap(name, _render_slot(name, _class_of(match.group(0))))

    updated, count = ANCHOR_RE.subn(sub, text)
    if count != len(names):
        raise SystemExit(
            f"Expected {len(names)} Unfog App Store anchors, found {count}."
        )
    return updated


def _refresh_blocks(text: str) -> str:
    def sub(match: re.Match) -> str:
        name = match.group(1)
        if name not in LIVE_CTA:
            raise SystemExit(f"Unknown Unfog CTA slot {name}")
        return _wrap(name, _render_slot(name))

    return BLOCK_RE.sub(sub, text)


def _sync_schema_and_banner(text: str) -> str:
    text = BANNER_RE.sub("\n", text)
    text = DOWNLOAD_RE.sub("", text)
    if not UNFOG_RELEASED:
        return text

    banner = "  " + smart_banner_tag(UNFOG_APP_ID)
    if "apple-itunes-app" not in text:
        canon = '<link rel="canonical" href="https://ysliustudio.com/quit-weed/" />'
        if canon in text:
            text = text.replace(canon, canon + "\n\n  <!-- Smart App Banner -->\n" + banner, 1)
    url_line = '"url": "https://ysliustudio.com/quit-weed/",'
    download = (
        '"downloadUrl": "'
        + make_asc_url(UNFOG_APP_ID, DEFAULT_PROVIDER_TOKEN, LANDING_CT)
        + '",'
    )
    if url_line in text and "downloadUrl" not in text:
        text = text.replace(url_line, url_line + "\n        " + download, 1)
    return text


def sync_quit_weed_html(path: str) -> None:
    filename = os.path.basename(path)
    names = FILE_SLOTS[filename]
    with open(path, "r", encoding="utf-8") as handle:
        text = handle.read()
    if "UNFOG_CTA" not in text:
        text = _migrate_anchors(text, names)
    text = _refresh_blocks(text)
    if filename == "index.html":
        text = _sync_schema_and_banner(text)
    if not UNFOG_RELEASED and APP_ID_IN_URL.search(text):
        raise SystemExit(f"Unfog App Store URL still present in {path}")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)


def _homepage_link_block() -> str:
    if UNFOG_RELEASED:
        url = make_asc_url(UNFOG_APP_ID, DEFAULT_PROVIDER_TOKEN, "site-home")
        body = (
            "{\n"
            '        "label": "App Store",\n'
            f'        "url": "{url}",\n'
            '        "type": "appstore"\n'
            "      }"
        )
    else:
        body = (
            "{\n"
            '        "label": "Coming soon to the App Store",\n'
            '        "type": "coming-soon"\n'
            "      }"
        )
    return f"// UNFOG_CTA homepage\n      {body},\n      // /UNFOG_CTA"


def sync_homepage_card(path: str) -> None:
    with open(path, "r", encoding="utf-8") as handle:
        text = handle.read()
    block = _homepage_link_block()
    if "// UNFOG_CTA homepage" in text:
        updated, count = JS_BLOCK_RE.subn(block, text, count=1)
        if count != 1:
            raise SystemExit("Could not refresh the Unfog homepage CTA in apps-data.js")
        text = updated
    else:
        pattern = re.compile(
            r'\{\s*"label": "App Store",\s*"url": "https://apps\.apple\.com/[^"]*id'
            + UNFOG_APP_ID
            + r'[^"]*",\s*"type": "appstore"\s*\}',
            re.DOTALL,
        )
        if not pattern.search(text):
            raise SystemExit("Could not find the Unfog homepage App Store link in apps-data.js")
        text = pattern.sub(block, text, count=1)
    if not UNFOG_RELEASED and APP_ID_IN_URL.search(text):
        raise SystemExit("Unfog App Store URL still present in apps-data.js")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)


def apply_unfog_release() -> None:
    quit_weed = os.path.join(ROOT, "quit-weed")
    for name in FILE_SLOTS:
        sync_quit_weed_html(os.path.join(quit_weed, name))
    sync_homepage_card(os.path.join(ROOT, "apps-data.js"))
    state = "live App Store links" if UNFOG_RELEASED else "coming soon"
    print(f"Unfog release flag is {UNFOG_RELEASED}: static CTAs set to {state}.")


if __name__ == "__main__":
    apply_unfog_release()
