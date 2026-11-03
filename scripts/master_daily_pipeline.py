#!/usr/bin/env python3
"""
Unified Master Programmatic SEO Pipeline for YS Liu Studio (All 8 Apps).
Designed under strict Anti-Scaled-Content-Abuse (Anti-Content-Farm) principles:
  1. Refresh Before Spawn (Zero Cannibalization):
     Prioritizes enriching existing guides that already earn GSC impressions with newly
     discovered long-tail queries rather than spawning thin duplicate articles.
  2. Natural Editorial Velocity (Max 1 New Guide / Day across 8 Apps):
     Rotates across all 8 apps based on GSC crawl momentum, days since last publication,
     and guide count so no subfolder exhibits robotic mass-publishing spikes.
  3. High Information Gain & Utility Density:
     Enforces concise 750-1,150 word guides with quantitative tables, calculators, or
     decision matrices and accurate sitemap `lastmod` timestamps.

Apps Managed (All 8):
  1. alcohol-free-tracker ("Alcohol Free Tracker")
  2. quit-weed            ("Quit Weed: Unfog")
  3. quit-vaping          ("Quit Vaping")
  4. pill-reminder        ("Supplement & Pill Reminder")
  5. grocery-price        ("Grocery Price Scanner")
  6. levain               ("Sourdough Bake Timer: Levain")
  7. inkstone             ("Inkstone: Sign PDF & Docs")
  8. agricola-scorer      ("Agricola Score Sheet")
"""
import argparse
import csv
import glob
import json
import math
import os
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from datetime import datetime, timedelta

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GSC_SITE = "sc-domain:ysliustudio.com"
FINANCIAL_RECORDS_DIR = "/Users/louisliu/Documents/App_Financial_Records"

APPS = [
    ("alcohol-free-tracker", "Alcohol Free Tracker", "/Users/louisliu/Documents/repo/liuys_website/SEO-Strategy-Playbook.md"),
    ("quit-weed", "Quit Weed: Unfog", "/Users/louisliu/Documents/repo/liuys_website/SEO-Strategy-Playbook.md"),
    ("quit-vaping", "Quit Vaping", "/Users/louisliu/Documents/repo/liuys_website/SEO-Strategy-Playbook.md"),
    ("pill-reminder", "Supplement & Pill Reminder", "/Users/louisliu/Documents/repo/liuys_website/SEO-Strategy-Playbook.md"),
    ("grocery-price", "Grocery Price Scanner", "/Users/louisliu/Documents/repo/liuys_website/SEO-Strategy-Playbook.md"),
    ("levain", "Sourdough Bake Timer: Levain", "/Users/louisliu/Documents/repo/liuys_website/SEO-Strategy-Playbook.md"),
    ("inkstone", "Inkstone: Sign PDF & Docs", "/Users/louisliu/Documents/repo/liuys_website/SEO-Strategy-Playbook.md"),
    ("agricola-scorer", "Agricola Score Sheet", "/Users/louisliu/Documents/repo/liuys_website/SEO-Strategy-Playbook.md"),
]

STOPWORDS = {
    "the", "and", "for", "with", "how", "what", "when", "why", "does", "can",
    "you", "your", "from", "that", "this", "are", "was", "after", "while",
    "into", "without", "best", "guide", "complete", "chart", "timeline"
}


def load_json(path, default=None):
    if not os.path.exists(path):
        return default if default is not None else {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def tokenize(text: str) -> set:
    words = re.findall(r"[a-z0-9]+", text.lower())
    return {w for w in words if len(w) > 2 and w not in STOPWORDS}


def token_overlap_ratio(query: str, target: str) -> float:
    q_tokens = tokenize(query)
    t_tokens = tokenize(target)
    if not q_tokens or not t_tokens:
        return 0.0
    inter = q_tokens.intersection(t_tokens)
    return len(inter) / min(len(q_tokens), len(t_tokens))


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


def gsc_query(token: str, dimensions: list, start_date: str, end_date: str, row_limit: int = 250) -> list:
    if not token:
        return []
    encoded_site = urllib.parse.quote(GSC_SITE, safe="")
    url = f"https://searchconsole.googleapis.com/webmasters/v3/sites/{encoded_site}/searchAnalytics/query"
    body = {
        "startDate": start_date,
        "endDate": end_date,
        "dimensions": dimensions,
        "rowLimit": row_limit
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(body).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "X-Goog-User-Project": "kahoot-lite-2608"
        }
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data.get("rows", [])
    except Exception:
        return []


def get_recent_revenue_by_app() -> dict:
    """
    Parses exact ASC sales reports from ~/Documents/App_Financial_Records to determine
    the latest monthly / 30-day proceeds per app.
    Used to grant organic rotation weighting bonuses to apps generating actual revenue.
    """
    app_mapping = {
        "pill-reminder": ["pill reminder", "supplement", "pillreminder"],
        "alcohol-free-tracker": ["alcohol", "alcoholfreetracker"],
        "agricola-scorer": ["agricola"],
        "grocery-price": ["grocery", "groceryprice"],
        "quit-vaping": ["vaping", "vape"],
        "quit-weed": ["unfog", "weed"],
        "levain": ["levain", "sourdough"],
        "inkstone": ["inkstone", "sign pdf"]
    }
    rev_by_app = {k: 0.0 for k in app_mapping}
    if not os.path.exists(FINANCIAL_RECORDS_DIR):
        return rev_by_app

    # Priority 1: Check most recent consolidated monthly report (.tsv)
    monthly_files = sorted(glob.glob(os.path.join(FINANCIAL_RECORDS_DIR, "2026", "*", "Revenue", "ASC_Monthly_SalesReport_*.tsv")))
    target_files = []
    if monthly_files:
        target_files = [monthly_files[-1]]
    else:
        # Fallback to recent daily files
        daily_files = sorted(glob.glob(os.path.join(FINANCIAL_RECORDS_DIR, "2026", "*", "Revenue", "daily", "*.tsv")))
        target_files = daily_files[-30:]

    for fpath in target_files:
        try:
            with open(fpath, "r", encoding="utf-8", errors="replace") as f:
                reader = csv.DictReader(f, delimiter="\t")
                for r in reader:
                    sku = (r.get("SKU", "") or "").lower()
                    title = (r.get("Title", "") or "").lower()
                    proceeds = float(r.get("Developer Proceeds", 0) or 0)
                    for app_key, patterns in app_mapping.items():
                        if any(p in sku or p in title for p in patterns):
                            rev_by_app[app_key] += proceeds
                            break
        except Exception:
            pass

    return rev_by_app


def collect_portfolio_data(token: str) -> dict:
    end_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    start_date = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
    today_str = datetime.now().strftime("%Y-%m-%d")
    today_dt = datetime.strptime(today_str, "%Y-%m-%d")

    rev_map = get_recent_revenue_by_app()
    query_page_rows = gsc_query(token, ["query", "page"], start_date, end_date)
    page_rows = gsc_query(token, ["page"], start_date, end_date)

    app_data = {}
    for app_dir, app_title, log_path in APPS:
        app_path = os.path.join(ROOT_DIR, app_dir)
        posts_dir = os.path.join(app_path, "guides", "posts")
        queue_path = os.path.join(app_path, "guides", "topic_queue.json")
        cfg_path = os.path.join(app_path, "guides", "seo_config.json")

        cfg = load_json(cfg_path, {})
        queue = load_json(queue_path, [])

        posts = {}
        for pf in sorted(glob.glob(os.path.join(posts_dir, "*.json"))):
            p = load_json(pf, {})
            if p.get("slug"):
                posts[p["slug"]] = p

        published_slugs = set(posts.keys())
        pending_queue = [
            q for q in queue
            if q.get("status") != "published" and q.get("slug") not in published_slugs
        ]

        pub_dates = [p.get("published_date", "2026-10-20") for p in posts.values()]
        latest_pub_str = max(pub_dates, default="2026-10-20")
        try:
            days_since_pub = (today_dt - datetime.strptime(latest_pub_str, "%Y-%m-%d")).days
        except Exception:
            days_since_pub = 14

        revenue = rev_map.get(app_dir, 0.0)
        app_data[app_dir] = {
            "app_dir": app_dir,
            "app_title": app_title,
            "log_path": log_path,
            "site_url": cfg.get("site_url", f"https://ysliustudio.com/{app_dir}"),
            "posts": posts,
            "published_count": len(posts),
            "latest_published_date": latest_pub_str,
            "days_since_last_publish": days_since_pub,
            "recent_revenue_usd": round(revenue, 2),
            "pending_queue": pending_queue,
            "gsc_pages": {},
            "gsc_queries": [],
            "total_page_impressions": 0,
            "total_page_clicks": 0,
        }

    # Map page-level GSC metrics
    for r in page_rows:
        page_url = r.get("keys", [""])[0]
        impr = int(r.get("impressions", 0))
        clicks = int(r.get("clicks", 0))
        pos = round(float(r.get("position", 0)), 1)
        for app_dir in app_data:
            if f"/{app_dir}/" in page_url:
                app_data[app_dir]["gsc_pages"][page_url] = {
                    "impressions": impr,
                    "clicks": clicks,
                    "position": pos,
                    "queries": []
                }
                app_data[app_dir]["total_page_impressions"] += impr
                app_data[app_dir]["total_page_clicks"] += clicks

    # Map query+page GSC metrics
    for r in query_page_rows:
        keys = r.get("keys", ["", ""])
        q = keys[0].strip().lower()
        page_url = keys[1]
        impr = int(r.get("impressions", 0))
        clicks = int(r.get("clicks", 0))
        pos = round(float(r.get("position", 0)), 1)
        for app_dir in app_data:
            if f"/{app_dir}/" in page_url:
                q_obj = {
                    "query": q,
                    "page": page_url,
                    "impressions": impr,
                    "clicks": clicks,
                    "position": pos
                }
                app_data[app_dir]["gsc_queries"].append(q_obj)
                if page_url in app_data[app_dir]["gsc_pages"]:
                    app_data[app_dir]["gsc_pages"][page_url]["queries"].append(q_obj)

    return app_data


def build_recommendations(app_data: dict) -> dict:
    """
    Produces a Google-safe Daily Action Plan:
      1. `refresh_target`: An existing published guide with real GSC queries not yet explicitly
         covered in its `secondary_keywords` or `faqs` (prevents keyword cannibalization).
      2. `publish_target`: Strictly 1 app & topic to publish today (either a genuinely distinct
         GSC query or the top-priority app from the 8-app fair rotation).
    """
    refresh_candidates = []
    distinct_gsc_new_topics = []

    for app_dir, info in app_data.items():
        posts = info["posts"]
        # Check each query in GSC for this app
        slug_to_uncovered_queries = {}
        for q_obj in info["gsc_queries"]:
            q = q_obj["query"]
            page_url = q_obj["page"]
            m = re.search(r"/guides/([^/]+)\.html$", page_url)
            if m and m.group(1) in posts:
                slug = m.group(1)
                post = posts[slug]
                sec_and_faq = " ".join([
                    post.get("target_keyword", ""),
                    " ".join(post.get("secondary_keywords", [])),
                    " ".join(f.get("question", "") for f in post.get("faqs", []))
                ]).lower()
                if q not in sec_and_faq:
                    slug_to_uncovered_queries.setdefault(slug, []).append(q_obj)
            else:
                # Query landed on index/homepage; check if any existing post covers it
                covered = False
                for slug, post in posts.items():
                    if token_overlap_ratio(q, post.get("target_keyword", "") + " " + post.get("title", "")) >= 0.5:
                        covered = True
                        slug_to_uncovered_queries.setdefault(slug, []).append(q_obj)
                        break
                if not covered and q_obj["impressions"] >= 2 and 10.0 <= q_obj["position"] <= 90.0:
                    distinct_gsc_new_topics.append((app_dir, q_obj))

        for slug, q_list in slug_to_uncovered_queries.items():
            post = posts[slug]
            upd_str = post.get("updated_date", post.get("published_date", "2026-10-20"))
            try:
                days_since_upd = (datetime.now() - datetime.strptime(upd_str, "%Y-%m-%d")).days
            except Exception:
                days_since_upd = 14
            if days_since_upd < 3:
                continue
            page_url = f"{info['site_url'].rstrip('/')}/guides/{slug}.html"
            page_stats = info["gsc_pages"].get(page_url, {"impressions": sum(x["impressions"] for x in q_list), "position": q_list[0]["position"]})
            refresh_candidates.append({
                "action": "REFRESH_EXISTING_GUIDE",
                "app_dir": app_dir,
                "app_title": info["app_title"],
                "slug": slug,
                "post_json_path": f"{app_dir}/guides/posts/{slug}.json",
                "url": page_url,
                "page_impressions": page_stats.get("impressions", 0),
                "page_position": page_stats.get("position", 0),
                "uncovered_gsc_queries": sorted(q_list, key=lambda x: (-x["impressions"], x["position"])),
                "rationale": (
                    f"Existing guide already ranks at avg pos {page_stats.get('position', 0)} with "
                    f"{page_stats.get('impressions', 0)} GSC impressions, and surfaced {len(q_list)} "
                    f"real user search queries not yet explicitly targeted in secondary_keywords/FAQs. "
                    f"Enriching this canonical URL avoids keyword cannibalization and boosts CTR/rankings."
                )
            })

    refresh_candidates.sort(key=lambda x: (-x["page_impressions"], x["page_position"]))
    best_refresh = refresh_candidates[0] if refresh_candidates else None

    # Select 1 app for PUBLISH_NEW
    publish_target = None
    if distinct_gsc_new_topics:
        distinct_gsc_new_topics.sort(key=lambda x: (-x[1]["impressions"], x[1]["position"]))
        win_app, win_q = distinct_gsc_new_topics[0]
        slug = re.sub(r"[^a-z0-9]+", "-", win_q["query"].lower()).strip("-")[:55]
        publish_target = {
            "action": "PUBLISH_NEW_GUIDE",
            "selection_mode": "gsc_strike_zone_discovery",
            "app_dir": win_app,
            "app_title": app_data[win_app]["app_title"],
            "log_path": app_data[win_app]["log_path"],
            "topic": {
                "slug": slug,
                "target_keyword": win_q["query"],
                "gsc_impressions": win_q["impressions"],
                "gsc_position": win_q["position"],
                "category": "Search Console · Guide",
                "campaign_prefix": f"seo_{slug[:24].replace('-', '_')}"
            },
            "rationale": f"Discovered distinct GSC query '{win_q['query']}' (Impr: {win_q['impressions']}, Pos: {win_q['position']}) with zero cannibalization."
        }
    else:
        # 8-App Fair Anti-Spike Rotation
        rotation_pool = []
        for app_dir, info in app_data.items():
            if not info["pending_queue"]:
                continue
            # Score: higher days_since_last_publish + lower published_count + active GSC impressions bonus + revenue weight
            days_score = min(info["days_since_last_publish"], 30) * 3.0
            scarcity_score = max(0, 15 - info["published_count"]) * 4.0
            crawl_bonus = min(info["total_page_impressions"], 20) * 1.5
            # Revenue Weight Bonus: grant logarithmic priority to apps generating proven ASC proceeds
            # e.g., $150 -> +26.3 pts, $95 -> +23.8 pts, $47 -> +20.2 pts, $25 -> +17.1 pts, $0 -> 0 pts
            rev_usd = info.get("recent_revenue_usd", 0.0)
            revenue_bonus = round(math.log10(rev_usd + 1.0) * 12.0, 1)

            # Penalize apps published within last 24 hours to prevent consecutive-day spam
            recent_penalty = -50.0 if info["days_since_last_publish"] <= 1 else 0.0
            # Diversify across subfolders: if this app already has today's refresh_target, let another app get the new guide
            same_app_refresh_penalty = -15.0 if (best_refresh and best_refresh["app_dir"] == app_dir) else 0.0
            total_score = round(days_score + scarcity_score + crawl_bonus + revenue_bonus + recent_penalty + same_app_refresh_penalty, 1)
            rotation_pool.append((total_score, revenue_bonus, app_dir, info))

        rotation_pool.sort(key=lambda x: (-x[0], x[3]["published_count"]))
        if rotation_pool:
            top_score, rev_bonus, win_app, win_info = rotation_pool[0]
            next_topic = win_info["pending_queue"][0]
            publish_target = {
                "action": "PUBLISH_NEW_GUIDE",
                "selection_mode": "eight_app_fair_rotation",
                "rotation_score": top_score,
                "revenue_bonus": rev_bonus,
                "recent_revenue_usd": win_info.get("recent_revenue_usd", 0.0),
                "app_dir": win_app,
                "app_title": win_info["app_title"],
                "log_path": win_info["log_path"],
                "published_count": win_info["published_count"],
                "days_since_last_publish": win_info["days_since_last_publish"],
                "subfolder_gsc_impressions": win_info["total_page_impressions"],
                "topic": next_topic,
                "rationale": (
                    f"Selected via 8-App Revenue-Weighted Anti-Spike Rotation (score {top_score}): "
                    f"{win_info['app_title']} has {win_info['published_count']} guides "
                    f"({win_info['days_since_last_publish']}d since last publish), "
                    f"USD ${win_info.get('recent_revenue_usd', 0.0):.2f} recent ASC revenue (+{rev_bonus} pts), "
                    f"and {win_info['total_page_impressions']} GSC page impressions."
                )
            }

    return {
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "anti_spam_policy": {
            "max_new_guides_per_day": 1,
            "max_refreshes_per_day": 2,
            "word_count_cap": "750-1,150 words (concise, zero AI fluff)",
            "mandatory_elements": [
                "50-word quantitative TL;DR answer box at the top of body_html",
                "At least 1 structured HTML comparison table, dosage/timing chart, or interactive calculator link",
                "Contextual native iOS app pitch card with ASC campaign token (ct=seo_*)",
                "3-4 high-intent FAQs matching conversational long-tail queries"
            ]
        },
        "refresh_target": best_refresh,
        "additional_refresh_candidates": refresh_candidates[1:3],
        "publish_target": publish_target
    }


def run_check():
    print("=" * 76)
    print("   YS Liu Studio — 8-App Anti-Content-Farm SEO Pipeline Check")
    print("=" * 76)
    token = get_gcloud_token()
    if token:
        print("✓ Google Search Console OAuth token active (`sc-domain:ysliustudio.com`).")
    else:
        print("⚠ GSC token unavailable; falling back to local manifest & queue state.")
    print()

    app_data = collect_portfolio_data(token)
    for app_dir, title, _ in APPS:
        info = app_data[app_dir]
        q_next = info["pending_queue"][0] if info["pending_queue"] else None
        impr = info["total_page_impressions"]
        q_cnt = len(info["gsc_queries"])

        badge = "🟢 GSC ACTIVE" if impr >= 5 else ("🟡 GSC WARMING" if impr >= 1 else "⚪ COLD START")
        rev_val = info.get("recent_revenue_usd", 0.0)
        rev_str = f" | Recent Revenue: USD ${rev_val:.2f}" if rev_val > 0 else ""
        print(f"[{badge}] {info['app_title']} ({app_dir}){rev_str}")
        print(f"  • Guides: {info['published_count']} published (last: {info['latest_published_date']}, {info['days_since_last_publish']}d ago) | Queue: {len(info['pending_queue'])} pending")
        print(f"  • GSC (30d): {impr} page impressions across {len(info['gsc_pages'])} URLs | {q_cnt} visible query rows")
        if info["gsc_queries"]:
            top_q = sorted(info["gsc_queries"], key=lambda x: (-x["impressions"], x["position"]))[:2]
            q_str = "; ".join(f"\"{x['query']}\" (impr:{x['impressions']}, pos:{x['position']})" for x in top_q)
            print(f"  • Top GSC Queries: {q_str}")
        if q_next:
            print(f"  • Next Queue Topic: \"{q_next['slug']}\"")
        print()

    rec = build_recommendations(app_data)
    print("-" * 76)
    print("🎯 TODAY'S RECOMMENDED ANTI-SPAM ACTION PLAN:")
    if rec["refresh_target"]:
        rt = rec["refresh_target"]
        qs = ", ".join(f"\"{q['query']}\" (pos {q['position']})" for q in rt["uncovered_gsc_queries"][:3])
        print(f"  1. [REFRESH EXISTING] {rt['app_title']} -> `{rt['post_json_path']}`")
        print(f"     • Uncovered GSC Queries to weave in: {qs}")
    if rec["publish_target"]:
        pt = rec["publish_target"]
        print(f"  2. [PUBLISH 1 NEW GUIDE] {pt['app_title']} ({pt['app_dir']})")
        print(f"     • Slug: `{pt['topic']['slug']}`")
        print(f"     • Keyword: \"{pt['topic']['target_keyword']}\"")
        print(f"     • Why: {pt['rationale']}")
    print("=" * 76)


def run_recommend():
    token = get_gcloud_token()
    app_data = collect_portfolio_data(token)
    rec = build_recommendations(app_data)
    print(json.dumps(rec, indent=2))


def run_build(only_apps: list = None):
    target_apps = [a for a in APPS if not only_apps or a[0] in only_apps]
    print(f"Rebuilding guides & sitemaps for {len(target_apps)} app(s)...")
    for app_dir, title, _ in target_apps:
        builder = os.path.join(ROOT_DIR, app_dir, "scripts", "build_guide.py")
        if os.path.exists(builder):
            proc = subprocess.run(
                ["python3", builder],
                cwd=os.path.join(ROOT_DIR, app_dir),
                capture_output=True, text=True
            )
            last_line = proc.stdout.strip().splitlines()[-1] if proc.stdout else "done"
            print(f"✓ {title}: {last_line}")
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
    parser = argparse.ArgumentParser(description="Master 8-App Programmatic SEO Pipeline for YS Liu Studio")
    parser.add_argument("--check", action="store_true", help="Human-readable GSC & Queue inspection across all 8 apps")
    parser.add_argument("--recommend", action="store_true", help="Output JSON Daily Action Plan (1 Refresh + 1 New Guide across 8 apps)")
    parser.add_argument("--build", action="store_true", help="Rebuild HTML guides and sitemaps across all 8 apps")
    parser.add_argument("--app", type=str, default="", help="Optional single app_dir filter for --build")
    parser.add_argument("--indexnow", action="store_true", help="Submit all sitemap URLs to IndexNow")
    parser.add_argument("--status", action="store_true", help="Show published and queue counts across all 8 apps")

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    args = parser.parse_args()

    if args.check:
        run_check()
    if args.recommend:
        run_recommend()
    if args.build:
        only = [args.app] if args.app else None
        run_build(only)
    if args.indexnow:
        run_indexnow()
    if args.status:
        run_status()


if __name__ == "__main__":
    main()
