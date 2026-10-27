#!/usr/bin/env python3
"""
Hybrid Keyword Discovery Selector for Inkstone: Sign PDF & Docs Programmatic SEO.
"""
import json
import os
import subprocess
from datetime import datetime, timedelta

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GUIDES_DIR = os.path.join(ROOT_DIR, "guides")
QUEUE_PATH = os.path.join(GUIDES_DIR, "topic_queue.json")
MANIFEST_PATH = os.path.join(GUIDES_DIR, "published_manifest.json")
CONFIG_PATH = os.path.join(GUIDES_DIR, "seo_config.json")


def load_json(path, default):
    if not os.path.exists(path):
        return default
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def query_gsc_property(site_prop: str, page_prefix: str, start_date: str, end_date: str, token: str, published_keywords: set):
    import urllib.request
    import urllib.parse
    import urllib.error
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
    payload = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(url, data=payload, headers={
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "X-Goog-User-Project": "kahoot-lite-2608"
    })
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            rows = data.get("rows", [])
            candidates = []
            emerging_candidates = []
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
                    emerging_candidates.append((impr, pos, clicks, q))
            if candidates or emerging_candidates:
                pool = candidates if candidates else emerging_candidates
                pool.sort(key=lambda x: x[0], reverse=True)
                best = pool[0]
                slug = best[3].replace(" ", "-")[:55]
                src = "gsc_strike_zone" if candidates else "gsc_emerging_strike_zone"
                return {
                    "source": src,
                    "gsc_property_used": site_prop,
                    "slug": slug,
                    "target_keyword": best[3],
                    "gsc_impressions": best[0],
                    "gsc_position": round(best[1], 1),
                    "gsc_clicks": best[2],
                    "category": "Search Console · Guide",
                    "campaign_prefix": f"seo_{slug[:24].replace('-', '_')}",
                    "pitch_screen": "inkstone.png",
                    "pitch_headline": "Sign PDF documents & share encrypted links on iPhone",
                    "pitch_body": "Sign contracts, fill forms, and share web signing links without monthly fees."
                }, None
            return None, f"GSC ({site_prop}) returned {len(rows)} queries, 0 matched Strike Zone (pos 15..55, impr >= 10) or Emerging (pos 10..60, impr >= 2)."
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="replace")
        try:
            err_json = json.loads(err_body)
            msg = err_json.get("error", {}).get("message", err_body)
        except Exception:
            msg = err_body
        return None, f"GSC ({site_prop}) HTTP {e.code}: {msg}"


def try_gsc_strike_zone(cfg: dict, published_keywords: set):
    end_date = (datetime.now() - timedelta(days=2)).strftime("%Y-%m-%d")
    start_date = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
    primary_prop = cfg.get("gsc_property", "sc-domain:ysliustudio.com")
    page_prefix = cfg.get("site_url", "https://ysliustudio.com/inkstone")
    properties_to_try = [primary_prop, "sc-domain:ysliustudio.com"]

    reasons = []
    try:
        token_proc = subprocess.run(
            ["gcloud", "auth", "application-default", "print-access-token"],
            capture_output=True, text=True, timeout=10
        )
        if token_proc.returncode == 0 and token_proc.stdout.strip():
            token = token_proc.stdout.strip().splitlines()[-1]
            for prop in set(properties_to_try):
                topic, reason = query_gsc_property(prop, page_prefix, start_date, end_date, token, published_keywords)
                if topic:
                    return topic, None
                if reason:
                    reasons.append(reason)
        else:
            reasons.append("gcloud ADC token unavailable")
    except Exception as e:
        reasons.append(f"GSC query exception: {str(e)}")

    return None, " | ".join(reasons) if reasons else "GSC not queried"


def main():
    cfg = load_json(CONFIG_PATH, {})
    manifest = load_json(MANIFEST_PATH, [])
    queue = load_json(QUEUE_PATH, [])

    published_slugs = {m["slug"] for m in manifest}
    published_keywords = {m.get("target_keyword", "").lower() for m in manifest}

    gsc_topic, gsc_reason = try_gsc_strike_zone(cfg, published_keywords)
    if gsc_topic and gsc_topic["slug"] not in published_slugs:
        print(json.dumps(gsc_topic, indent=2))
        return

    for item in queue:
        if item["slug"] not in published_slugs and item.get("status") != "published":
            out = dict(item)
            out["source"] = "seed_topic_queue"
            out["fallback_reason"] = gsc_reason
            print(json.dumps(out, indent=2))
            return

    print(json.dumps({"source": "exhausted", "message": "All queued seed topics published."}, indent=2))


if __name__ == "__main__":
    main()
