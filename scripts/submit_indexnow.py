#!/usr/bin/env python3
"""
Submit all sitemap URLs to IndexNow API (Bing, Yandex, Seznam, Naver).
Allows instant search engine crawling of new and updated pages.
"""
import json
import os
import re
import urllib.request
import urllib.error

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITEMAP_PATH = os.path.join(ROOT_DIR, "sitemap.xml")
KEY = "4a8f9c2d1b7e6a5d3f2c1e8b7a6d5c4e"
HOST = "ysliustudio.com"
KEY_LOCATION = f"https://{HOST}/{KEY}.txt"


def get_urls_from_sitemap(sitemap_path: str) -> list:
    if not os.path.exists(sitemap_path):
        return []
    with open(sitemap_path, "r", encoding="utf-8") as f:
        content = f.read()
    urls = re.findall(r"<loc>(https://ysliustudio\.com/[^<]+)</loc>", content)
    # Deduplicate while preserving order
    seen = set()
    out = []
    for u in urls:
        if u not in seen:
            seen.add(u)
            out.append(u)
    return out


def submit_to_indexnow(urls: list):
    if not urls:
        print("No URLs found to submit.")
        return

    payload = {
        "host": HOST,
        "key": KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls
    }

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://api.indexnow.org/indexnow",
        data=data,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST"
    )

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            print(f"IndexNow submitted {len(urls)} URLs successfully (HTTP {resp.status}).")
    except urllib.error.HTTPError as e:
        print(f"IndexNow submission failed: HTTP {e.code} - {e.read().decode('utf-8', errors='replace')}")
    except Exception as e:
        print(f"IndexNow submission error: {e}")


def main():
    urls = get_urls_from_sitemap(SITEMAP_PATH)
    print(f"Found {len(urls)} URLs in {SITEMAP_PATH}")
    submit_to_indexnow(urls)


if __name__ == "__main__":
    main()
