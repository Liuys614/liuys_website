#!/usr/bin/env python3
"""
Static Programmatic SEO Guide Builder for Supplement & Pill Reminder Website.
Compiles JSON guide definitions in guides/posts/*.json into:
  1. guides/<slug>.html (with JSON-LD Article + FAQPage + ASC Campaign Links)
  2. guides/index.html (Guides Hub page)
  3. sitemap.xml (local + master /Users/louisliu/Documents/repo/liuys_website/sitemap.xml)
  4. guides/published_manifest.json
"""
import json
import glob
import os
import re
from datetime import datetime
import html

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MONOREPO_ROOT = os.path.dirname(ROOT_DIR)
import sys
sys.path.insert(0, os.path.join(MONOREPO_ROOT, "scripts"))
from site_campaign import (  # noqa: E402
    CF_BEACON,
    PROVIDER_TOKEN,
    app_is_released,
    coming_soon_markup,
    guide_ct,
    guides_index_ct,
    make_asc_url,
    smart_banner_tag,
)

GUIDES_DIR = os.path.join(ROOT_DIR, "guides")
POSTS_DIR = os.path.join(GUIDES_DIR, "posts")
CONFIG_PATH = os.path.join(GUIDES_DIR, "seo_config.json")


def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def render_guide_html(post: dict, cfg: dict, all_posts: list) -> str:
    site_url = cfg["site_url"].rstrip("/")
    app_id = cfg["app_id"]
    pt = PROVIDER_TOKEN
    beacon = CF_BEACON
    slug = post["slug"]
    canonical_url = f"{site_url}/guides/{slug}.html"
    page_ct = guide_ct(slug)

    url_nav = make_asc_url(app_id, pt, page_ct)
    url_footer = make_asc_url(app_id, pt, page_ct)

    faqs = post.get("faqs", [])
    faq_schema_entities = [
        {
            "@type": "Question",
            "name": item["question"],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": item["answer"]
            }
        }
        for item in faqs
    ]

    pitch_screen = post.get("pitch_screen", "01-never-miss-a-dose.webp")

    schema_graph = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Article",
                "headline": post["title"],
                "description": post["meta_description"],
                "datePublished": post["published_date"],
                "dateModified": post["published_date"],
                "mainEntityOfPage": canonical_url,
                "image": f"{site_url}/assets/appstore/{pitch_screen}",
                "author": {
                    "@type": "Organization",
                    "name": "Pill Reminder Medical Editorial"
                },
                "publisher": {
                    "@type": "Organization",
                    "name": "Supplement & Pill Reminder",
                    "logo": {
                        "@type": "ImageObject",
                        "url": f"{site_url}/assets/app-icon-180.png"
                    }
                }
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Pill Reminder Home", "item": f"{site_url}/"},
                    {"@type": "ListItem", "position": 2, "name": "Guides Hub", "item": f"{site_url}/guides/index.html"},
                    {"@type": "ListItem", "position": 3, "name": post["title"], "item": canonical_url}
                ]
            }
        ]
    }
    if faq_schema_entities:
        schema_graph["@graph"].append({
            "@type": "FAQPage",
            "mainEntity": faq_schema_entities
        })

    faq_html_items = []
    for item in faqs:
        q = html.escape(item["question"])
        a = html.escape(item["answer"])
        faq_html_items.append(f"""
          <details open class="guide-faq-item">
            <summary>{q}</summary>
            <p>{a}</p>
          </details>""")

    faq_section_html = ""
    if faq_html_items:
        faq_section_html = f"""
        <section class="guide-faq-box">
          <span class="eyebrow-pill">FAQ</span>
          <h2>Frequently Asked Questions</h2>
          {''.join(faq_html_items)}
        </section>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{html.escape(post['title'])} | Supplement & Pill Reminder</title>
  <meta name="description" content="{html.escape(post['meta_description'])}" />
  <link rel="canonical" href="{canonical_url}" />
  <meta name="apple-itunes-app" content="app-id={app_id}" />
  <meta property="og:type" content="article" />
  <meta property="og:title" content="{html.escape(post['title'])}" />
  <meta property="og:description" content="{html.escape(post['meta_description'])}" />
  <meta property="og:url" content="{canonical_url}" />
  <meta property="og:image" content="{site_url}/assets/appstore/{pitch_screen}" />
  <link rel="icon" type="image/png" href="../assets/favicon-32.png" />
  <link rel="stylesheet" href="../styles.css" />
  <style>
    .guide-shell {{ max-width: 820px; margin: 48px auto 72px; background: #fff; border-radius: 24px; padding: 44px; border: 1px solid var(--hairline-strong); box-shadow: var(--shadow-soft); }}
    .guide-shell h1 {{ font-size: clamp(1.9rem, 3.5vw, 2.5rem); color: var(--ink); line-height: 1.18; margin: 12px 0 14px; font-weight: 800; }}
    .guide-meta-bar {{ font-size: 0.86rem; color: var(--muted); font-weight: 600; margin-bottom: 28px; padding-bottom: 20px; border-bottom: 1px solid var(--hairline); }}
    .guide-content h2 {{ font-size: 1.38rem; color: var(--brand-dark); margin: 32px 0 12px; font-weight: 800; }}
    .guide-content p, .guide-content li {{ font-size: 1.02rem; line-height: 1.72; color: var(--ink-soft); margin-bottom: 14px; }}
    .guide-content ul, .guide-content ol {{ padding-left: 22px; margin-bottom: 18px; }}
    .guide-table-wrap {{ overflow-x: auto; margin: 24px 0 32px; }}
    .guide-table {{ width: 100%; border-collapse: collapse; font-size: 0.95rem; text-align: left; }}
    .guide-table th {{ background: var(--paper-deep); color: var(--ink); font-weight: 700; padding: 12px 16px; border: 1px solid var(--hairline-strong); }}
    .guide-table td {{ padding: 12px 16px; border: 1px solid var(--hairline-strong); color: var(--ink-soft); }}
    .guide-callout {{ background: var(--due-soft); border-left: 4px solid var(--due); padding: 16px 20px; border-radius: 0 12px 12px 0; margin: 24px 0; font-size: 0.96rem; line-height: 1.6; color: var(--ink); }}
    .guide-callout strong {{ display: block; margin-bottom: 4px; color: var(--brand-dark); }}
    .app-pitch-card {{ background: linear-gradient(135deg, var(--paper-deep) 0%, #fff 100%); border: 1.5px solid var(--hairline-strong); border-radius: 20px; padding: 28px 32px; display: flex; align-items: center; justify-content: space-between; gap: 24px; margin: 36px 0; }}
    .app-pitch-card .eyebrow {{ font-size: 0.78rem; font-weight: 700; text-transform: uppercase; color: var(--taken); letter-spacing: 0.05em; margin-bottom: 6px; }}
    .app-pitch-card h3 {{ font-size: 1.25rem; font-weight: 800; color: var(--ink); margin: 0 0 8px; }}
    .app-pitch-card p {{ font-size: 0.94rem; color: var(--ink-soft); margin-bottom: 16px; }}
    .guide-faq-box {{ margin-top: 38px; padding-top: 28px; border-top: 1px solid var(--hairline); }}
    .guide-faq-item {{ background: var(--paper); border-radius: 14px; padding: 16px 20px; margin-bottom: 12px; }}
    .guide-faq-item summary {{ font-weight: 800; color: var(--ink); cursor: pointer; }}
    .guide-faq-item p {{ margin: 10px 0 0; font-size: 0.95rem; color: var(--ink-soft); }}
    .eyebrow-pill {{ display: inline-block; background: var(--brand-soft); color: var(--brand); font-size: 0.76rem; font-weight: 700; text-transform: uppercase; padding: 4px 10px; border-radius: 99px; letter-spacing: 0.04em; }}
  </style>
  <script type="application/ld+json">
{json.dumps(schema_graph, indent=2)}
  </script>
</head>
<body>
  <header class="header">
    <div class="content header-inner">
      <a href="../index.html" class="brand">
        <span class="brand-title">Supplement &amp; Pill Reminder</span>
      </a>
      <a href="{html.escape(url_nav)}" class="nav-download" target="_blank" rel="noopener">Get Pill Reminder</a>
    </div>
  </header>

  <main class="content">
    <article class="guide-shell">
      <span class="eyebrow-pill">{html.escape(post.get('category', 'Supplement Guide'))}</span>
      <h1>{html.escape(post['title'])}</h1>
      <div class="guide-meta-bar">
        Published {html.escape(post['published_date'])} · {html.escape(post.get('reading_time', '5 min read'))} · Evidence-Based Supplement &amp; Medication Series
      </div>
      <div class="guide-content">
        {post['body_html']}
      </div>
      {faq_section_html}
    </article>
  </main>
{beacon}
</body>
</html>
"""


def render_guides_index_html(posts: list, cfg: dict) -> str:
    site_url = cfg["site_url"].rstrip("/")
    app_id = cfg["app_id"]
    pt = PROVIDER_TOKEN
    beacon = CF_BEACON
    canonical_url = f"{site_url}/guides/index.html"
    app_slug = site_url.rstrip("/").rsplit("/", 1)[-1]
    index_ct = guides_index_ct(app_slug)
    banner = smart_banner_tag(app_id) if app_is_released(app_id) else ""
    url_nav = make_asc_url(app_id, pt, index_ct)

    cards_html = []
    for p in posts:
        cards_html.append(f"""
        <article class="feature-card" style="display: flex; flex-direction: column; align-items: flex-start; text-align: left; padding: 28px;">
          <span class="eyebrow-pill" style="margin-bottom: 10px;">{html.escape(p.get('category', 'Guide'))}</span>
          <h2 style="font-size: 1.25rem; font-weight: 800; margin: 4px 0 10px;"><a href="{p['slug']}.html" style="color: inherit; text-decoration: none;">{html.escape(p['title'])}</a></h2>
          <p style="font-size: 0.94rem; color: var(--muted); margin-bottom: 16px; line-height: 1.5;">{html.escape(p.get('summary_excerpt', p['meta_description']))}</p>
          <a href="{p['slug']}.html" style="font-weight: 700; color: var(--taken); text-decoration: none; font-size: 0.92rem; margin-top: auto;">Read Guide ({html.escape(p.get('reading_time', '5 min'))}) &rarr;</a>
        </article>""")

    empty_placeholder = ""
    if not cards_html:
        empty_placeholder = "<p style='color: var(--muted); grid-column: 1/-1;'>Publishing daily evidence-based guides soon.</p>"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Supplement Timing, Bioavailability & Medication Guides | Pill Reminder</title>
  <meta name="description" content="Evidence-based guides on supplement timing, vitamin bioavailability, missed medication protocols, and safe daily dosing schedules." />
  <link rel="canonical" href="{canonical_url}" />
  {banner}
  <link rel="icon" type="image/png" href="../assets/favicon-32.png" />
  <link rel="stylesheet" href="../styles.css" />
</head>
<body>
  <header class="header">
    <div class="content header-inner">
      <a href="../index.html" class="brand">
        <span class="brand-title">Supplement &amp; Pill Reminder</span>
      </a>
      <a href="{html.escape(url_nav)}" class="nav-download" target="_blank" rel="noopener">Get Pill Reminder</a>
    </div>
  </header>

  <main class="content" style="padding: 56px 20px 80px;">
    <div style="text-align: center; max-width: 680px; margin: 0 auto 48px;">
      <span class="eyebrow-pill" style="margin-bottom: 12px;">💊 Evidence-Based Health Library</span>
      <h1 style="font-size: clamp(2rem, 4vw, 2.8rem); font-weight: 800; color: var(--ink); margin: 12px 0;">Supplement &amp; Medication Guides</h1>
      <p style="font-size: 1.05rem; color: var(--muted); line-height: 1.6;">Optimal timing, nutrient synergy, missed dose protocols, and science-backed supplement schedules.</p>
    </div>

    <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 24px;">
      {''.join(cards_html)}{empty_placeholder}
    </div>
  </main>
{beacon}
</body>
</html>
"""


def update_sitemaps(posts: list, cfg: dict):
    site_url = cfg["site_url"].rstrip("/")
    today = datetime.now().strftime("%Y-%m-%d")
    urls = [
        (f"{site_url}/", today),
        (f"{site_url}/guides/index.html", today),
        (f"{site_url}/privacy.html", today),
        (f"{site_url}/terms.html", today),
    ]
    for p in posts:
        urls.append((f"{site_url}/guides/{p['slug']}.html", p.get("published_date", today)))

    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    ]
    for loc, lastmod in urls:
        xml_lines.append(f"  <url><loc>{loc}</loc><lastmod>{lastmod}</lastmod></url>")
    xml_lines.append("</urlset>\n")

    with open(os.path.join(ROOT_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write("\n".join(xml_lines))

    master_sitemap = os.path.join(MONOREPO_ROOT, "sitemap.xml")
    if os.path.exists(master_sitemap):
        with open(master_sitemap, "r", encoding="utf-8") as f:
            master_content = f.read()
        for loc, lastmod in urls:
            if loc not in master_content:
                entry = f"  <url><loc>{loc}</loc><lastmod>{lastmod}</lastmod></url>\n"
                master_content = master_content.replace("</urlset>", entry + "</urlset>")
        with open(master_sitemap, "w", encoding="utf-8") as f:
            f.write(master_content)


def main():
    cfg = load_config()
    post_files = sorted(glob.glob(os.path.join(POSTS_DIR, "*.json")))
    posts = []
    for pf in post_files:
        with open(pf, "r", encoding="utf-8") as f:
            posts.append(json.load(f))

    posts.sort(key=lambda x: x.get("published_date", ""), reverse=True)

    for post in posts:
        out_path = os.path.join(GUIDES_DIR, f"{post['slug']}.html")
        html_str = render_guide_html(post, cfg, posts)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html_str)
        print(f"Built guide: guides/{post['slug']}.html")

    index_html = render_guides_index_html(posts, cfg)
    with open(os.path.join(GUIDES_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html)
    print("Built guides/index.html")

    update_sitemaps(posts, cfg)

    manifest = [
        {
            "slug": p["slug"],
            "title": p["title"],
            "target_keyword": p.get("target_keyword", ""),
            "published_date": p.get("published_date", ""),
            "category": p.get("category", "")
        }
        for p in posts
    ]
    with open(os.path.join(GUIDES_DIR, "published_manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)
    print(f"Updated local + master sitemap.xml & published_manifest.json ({len(manifest)} published guides)")


if __name__ == "__main__":
    main()
