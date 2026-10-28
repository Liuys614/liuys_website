#!/usr/bin/env python3
"""
Unified Master Programmatic SEO Pipeline for YS Liu Studio.
Orchestrates and manages publishing across all 8 apps:
  1. alcohol-free-tracker
  2. quit-weed
  3. quit-vaping
  4. pill-reminder
  5. grocery-price
  6. levain
  7. inkstone
  8. agricola-scorer

Features:
  --check      : Fast, unified GSC Strike Zone & queue inspection across all 8 apps (reuses 1 ADC token).
  --build      : Rebuilds HTML guides, hubs, and sitemaps across all 8 apps.
  --indexnow   : Submits all sitemap URLs to IndexNow (Bing/Yandex).
  --status     : Shows local counts of published and pending articles.
"""
import argparse
import glob
import json
import os
import subprocess
import sys
import urllib.request
import urllib.parse
import urllib.error
from datetime import datetime, timedelta

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Primary 7 Core Apps for Daily Programmatic SEO Publishing
APPS = [
    ("alcohol-free-tracker", "Alcohol Free Tracker"),
    ("quit-weed", "Quit Weed: Unfog"),
    ("quit-vaping", "Quit Vaping"),
    ("pill-reminder", "Supplement & Pill Reminder"),
    ("grocery-price", "Grocery Price Scanner"),
    ("levain", "Sourdough Bake Timer: Levain"),
    ("inkstone", "Inkstone: Sign PDF & Docs"),
]
PARKED_APPS = [
    ("agricola-scorer", "Agricola Score Sheet"),
]


def load_json(path, default=None):
    if not os.path.exists(path):
        return default if default is not None else {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_gcloud_token() -> str:
    try:
        proc = subprocess.run(
            ["gcloud", "auth", "application-default", "print-access-token"],
            capture_output=True, text=True, timeout=10
        )
        if proc.returncode == 0 and proc.stdout.strip():
            return proc.stdout.strip().splitlines()[-1]
    except Exception:
        pass
    return ""


def check_app_gsc_and_queue(app_dir: str, app_title: str, token: str) -> dict:
    app_path = os.path.join(ROOT_DIR, app_dir)
    cfg_path = os.path.join(app_path, "guides", "seo_config.json")
    manifest_path = os.path.join(app_path, "guides", "published_manifest.json")
    queue_path = os.path.join(app_path, "guides", "topic_queue.json")

    cfg = load_json(cfg_path, {})
    manifest = load_json(manifest_path, [])
    queue = load_json(queue_path, [])

    published_slugs = {m["slug"] for m in manifest}
    published_keywords = {m.get("target_keyword", "").lower() for m in manifest}
    pending = [q for q in queue if q.get("status") != "published" and q["slug"] not in published_slugs]

    site_prop = cfg.get("gsc_property", "sc-domain:ysliustudio.com")
    page_prefix = cfg.get("site_url", f"https://ysliustudio.com/{app_dir}")

    # GSC Query
    gsc_candidate = None
    gsc_error = None
    if token and site_prop:
        end_date = (datetime.now() - timedelta(days=2)).strftime("%Y-%m-%d")
        start_date = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
        encoded_site = urllib.parse.quote(site_prop, safe="")
        url = f"https://searchconsole.googleapis.com/webmasters/v3/sites/{encoded_site}/searchAnalytics/query"
        body = {
            "startDate": start_date,
            "endDate": end_date,
            "dimensions": ["query"],
            "rowLimit": 100
        }
        if site_prop.startswith("sc-domain:") and page_prefix:
            body["dimensionFilterGroups"] = [{
                "filters": [{
                    "dimension": "page",
                    "operator": "includingRegex",
                    "expression": page_prefix
                }]
            }]
        req = urllib.request.Request(url, data=json.dumps(body).encode("utf-8"), headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "X-Goog-User-Project": "kahoot-lite-2608"
        })
        try:
            with urllib.request.urlopen(req, timeout=12) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                rows = data.get("rows", [])
                candidates = []
                emerging = []
                for r in rows:
                    q = r.get("keys", [""])[0].strip().lower()
                    pos = float(r.get("position", 0))
                    impr = int(r.get("impressions", 0))
                    clicks = int(r.get("clicks", 0))
                    if q in published_keywords:
                        continue
                    if 15.0 <= pos <= 55.0 and impr >= 10:
                        candidates.append((impr, pos, clicks, q))
                    elif 10.0 <= pos <= 60.0 and impr >= 2:
                        emerging.append((impr, pos, clicks, q))
                if candidates or emerging:
                    pool = candidates if candidates else emerging
                    pool.sort(key=lambda x: x[0], reverse=True)
                    best = pool[0]
                    src = "gsc_strike_zone" if candidates else "gsc_emerging_strike_zone"
                    gsc_candidate = {
                        "source": src,
                        "keyword": best[3],
                        "impressions": best[0],
                        "position": round(best[1], 1),
                        "clicks": best[2]
                    }
        except Exception as e:
            gsc_error = str(e)

    return {
        "app_dir": app_dir,
        "app_title": app_title,
        "published_count": len(manifest),
        "pending_count": len(pending),
        "gsc_candidate": gsc_candidate,
        "gsc_error": gsc_error,
        "next_queue_topic": pending[0] if pending else None
    }


def run_check():
    print("=" * 72)
    print("   YS Liu Studio — Daily Pipeline Check Across All 8 Apps")
    print("=" * 72)
    token = get_gcloud_token()
    if token:
        print("✓ Google Search Console OAuth token active.")
    else:
        print("⚠ GSC token unavailable; falling back to queue inspection only.")
    print()

    for app_dir, title in APPS:
        res = check_app_gsc_and_queue(app_dir, title, token)
        gsc = res["gsc_candidate"]
        q_next = res["next_queue_topic"]
        
        status_badge = "🟢 GSC STRIKE ZONE" if gsc and gsc["source"] == "gsc_strike_zone" else (
            "🟡 GSC EMERGING" if gsc else "⚪ QUEUE FALLBACK"
        )
        print(f"[{status_badge}] {res['app_title']} ({app_dir})")
        print(f"  • Published: {res['published_count']} guides | Queue: {res['pending_count']} pending")

        if gsc:
            print(f"  • TARGET (GSC): \"{gsc['keyword']}\" (Impr: {gsc['impressions']}, Pos: {gsc['position']}, Clicks: {gsc['clicks']})")
        elif q_next:
            print(f"  • NEXT IN QUEUE: \"{q_next['slug']}\"")
            print(f"    Keyword: \"{q_next['target_keyword']}\"")
        else:
            print(f"  • STATUS: Queue exhausted! Needs new keywords.")
        print()
    print("=" * 72)


def run_build():
    print("Rebuilding guides & sitemaps for all 8 apps...")
    for app_dir, title in APPS:
        builder = os.path.join(ROOT_DIR, app_dir, "scripts", "build_guide.py")
        if os.path.exists(builder):
            proc = subprocess.run(["python3", builder], cwd=os.path.join(ROOT_DIR, app_dir), capture_output=True, text=True)
            print(f"✓ {title}: {proc.stdout.strip().splitlines()[-1] if proc.stdout else 'done'}")
    print("All builds complete.")


def run_indexnow():
    script = os.path.join(ROOT_DIR, "scripts", "submit_indexnow.py")
    if os.path.exists(script):
        subprocess.run(["python3", script])


def run_status():
    script = os.path.join(ROOT_DIR, "scripts", "status_all_seo.py")
    if os.path.exists(script):
        subprocess.run(["python3", script])


def main():
    parser = argparse.ArgumentParser(description="Master Daily Publishing Pipeline for YS Liu Studio")
    parser.add_argument("--check", action="store_true", help="Inspect GSC Strike Zone & Topic Queue for all 8 apps")
    parser.add_argument("--build", action="store_true", help="Rebuild all guides and sitemaps across 8 apps")
    parser.add_argument("--indexnow", action="store_true", help="Submit all sitemap URLs to IndexNow")
    parser.add_argument("--status", action="store_true", help="Show published and queue counts")

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    args = parser.parse_args()

    if args.check:
        run_check()
    if args.build:
        run_build()
    if args.indexnow:
        run_indexnow()
    if args.status:
        run_status()


if __name__ == "__main__":
    main()
