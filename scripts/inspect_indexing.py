#!/usr/bin/env python3
"""
Inspect Google Search Console Indexing Status & Generate One-Click Request Deep Links.
Uses GSC URL Inspection API (v1) via gcloud ADC token to check indexing coverage.
"""
import sys
import json
import os
import subprocess
import urllib.parse
import urllib.request
import urllib.error

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GSC_RESOURCE = "sc-domain:ysliustudio.com"


def get_token() -> str:
    try:
        proc = subprocess.run(
            ["gcloud", "auth", "application-default", "print-access-token"],
            capture_output=True, text=True, timeout=10
        )
        if proc.returncode == 0 and proc.stdout.strip():
            return proc.stdout.strip().splitlines()[-1]
    except Exception:
        pass
    return None


def generate_deep_link(url: str, resource_id: str = GSC_RESOURCE) -> str:
    encoded_res = urllib.parse.quote(resource_id, safe="")
    encoded_url = urllib.parse.quote(url, safe="")
    return f"https://search.google.com/search-console/inspect?resource_id={encoded_res}&url={encoded_url}"


def inspect_url(url: str, token: str, resource_id: str = GSC_RESOURCE) -> dict:
    api_url = "https://searchconsole.googleapis.com/v1/urlInspection/index:inspect"
    payload = {
        "inspectionUrl": url,
        "siteUrl": resource_id
    }
    req = urllib.request.Request(
        api_url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "X-Goog-User-Project": "kahoot-lite-2608"
        }
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            idx_res = data.get("inspectionResult", {}).get("indexStatusResult", {})
            return {
                "url": url,
                "verdict": idx_res.get("verdict", "UNKNOWN"),
                "coverage": idx_res.get("coverageState", "Unknown"),
                "last_crawl": idx_res.get("lastCrawlTime", "Never"),
                "deep_link": generate_deep_link(url, resource_id)
            }
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode("utf-8", errors="replace")
        return {
            "url": url,
            "verdict": "ERROR",
            "coverage": f"HTTP {e.code}",
            "last_crawl": "N/A",
            "deep_link": generate_deep_link(url, resource_id),
            "error_detail": err_msg
        }
    except Exception as e:
        return {
            "url": url,
            "verdict": "ERROR",
            "coverage": str(e),
            "last_crawl": "N/A",
            "deep_link": generate_deep_link(url, resource_id)
        }


def main():
    urls = sys.argv[1:]
    if not urls:
        print("Usage: python3 scripts/inspect_indexing.py <url1> [url2] ...")
        sys.exit(1)

    token = get_token()
    if not token:
        print("Error: Could not retrieve gcloud ADC token.")
        sys.exit(1)

    print(f"\n🔍 Inspecting {len(urls)} URL(s) on Google Search Console ({GSC_RESOURCE})...\n")
    for u in urls:
        res = inspect_url(u, token)
        status_icon = "✅" if res["verdict"] == "PASS" else ("⏳" if "unknown" in res["coverage"].lower() else "⚠️")
        print(f"{status_icon} [{res['coverage']}] {u}")
        if res["verdict"] != "PASS":
            print(f"   👉 One-Click Request Deep Link: {res['deep_link']}")
        print()


if __name__ == "__main__":
    main()
