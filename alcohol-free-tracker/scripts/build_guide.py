#!/usr/bin/env python3
"""
Static Programmatic SEO Guide Builder for Alcohol Free Tracker Website.
Compiles JSON guide definitions in guides/posts/*.json into:
  1. guides/<slug>.html (with JSON-LD Article + FAQPage + ASC Campaign Links)
  2. guides/index.html (Guides Hub page)
  3. index.html (#home-guides-list preview cards)
  4. sitemap.xml (local + master /Users/louisliu/Documents/repo/liuys_website/sitemap.xml)
  5. guides/published_manifest.json
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
    DEFAULT_PROVIDER_TOKEN,
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


def get_full_title(post: dict) -> str:
    sub = post.get("subtitle", "").strip()
    if sub:
        if post["title"].endswith("?") or post["title"].endswith("!"):
            return f"{post['title']} {sub}"
        return f"{post['title']}: {sub}"
    return post["title"]


def get_category_icon(category: str) -> str:
    c = category.lower()
    if any(k in c for k in ["craving", "urge"]):
        return "🌊"
    if any(k in c for k in ["financ", "saving", "money"]):
        return "💰"
    if any(k in c for k in ["mental", "anxiety", "neuro", "hangover"]):
        return "🧠"
    if any(k in c for k in ["recovery", "timeline", "body"]):
        return "⏳"
    return "✦"


def render_guide_card(p: dict, link_prefix: str = "") -> str:
    slug = p["slug"]
    cat = p.get("category", "Guide")
    cat_icon = get_category_icon(cat)
    title = html.escape(p["title"])
    subtitle = html.escape(p.get("subtitle", ""))
    excerpt = html.escape(p.get("summary_excerpt", p.get("meta_description", "")))
    reading_time = html.escape(p.get("reading_time", "5 min read"))
    link = f"{link_prefix}{slug}.html"

    subtitle_html = f'\n              <p class="guide-card-subtitle">{subtitle}</p>' if subtitle else ""

    return f"""            <article class="guide-card">
              <div class="guide-card-meta">
                <span class="guide-tag">{cat_icon} {html.escape(cat)}</span>
                <span class="guide-reading-time">{reading_time}</span>
              </div>
              <h3 class="guide-card-title"><a href="{link}">{title}</a></h3>{subtitle_html}
              <p class="guide-card-excerpt">{excerpt}</p>
              <div class="guide-card-footer">
                <a class="guide-read-link" href="{link}">Read guide &rarr;</a>
              </div>
            </article>"""


def render_guide_html(post: dict, cfg: dict, all_posts: list) -> str:
    site_url = cfg["site_url"].rstrip("/")
    app_id = cfg["app_id"]
    pt = DEFAULT_PROVIDER_TOKEN
    beacon = CF_BEACON
    slug = post["slug"]
    canonical_url = f"{site_url}/guides/{slug}.html"
    page_ct = guide_ct(slug)
    full_title = get_full_title(post)
    cat_icon = get_category_icon(post.get("category", "Guide"))

    url_nav = make_asc_url(app_id, pt, page_ct)
    url_sidebar = make_asc_url(app_id, pt, page_ct)
    url_footer = make_asc_url(app_id, pt, page_ct)
    url_sticky = make_asc_url(app_id, pt, page_ct)

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

    schema_graph = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Article",
                "headline": full_title,
                "description": post["meta_description"],
                "datePublished": post["published_date"],
                "dateModified": post["published_date"],
                "mainEntityOfPage": canonical_url,
                "image": f"{site_url}/assets/appstore/{post.get('pitch_screen', '02-body-recovery.webp')}",
                "author": {
                    "@type": "Organization",
                    "name": "Alcohol Free Tracker Editorial"
                },
                "publisher": {
                    "@type": "Organization",
                    "name": "Alcohol Free Tracker",
                    "logo": {
                        "@type": "ImageObject",
                        "url": f"{site_url}/assets/app-icon.png"
                    }
                }
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{site_url}/"},
                    {"@type": "ListItem", "position": 2, "name": "Guides", "item": f"{site_url}/guides/index.html"},
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
              <details open>
                <summary>{q}</summary>
                <p>{a}</p>
              </details>""")
    faq_section_html = ""
    if faq_html_items:
        faq_section_html = f"""
            <div class="support-card faq" style="margin-top: 42px;">
              <p class="eyebrow">Frequently Asked Questions</p>
              <h2>Common questions about {html.escape(post.get('target_keyword', 'recovery'))}</h2>
              {''.join(faq_html_items)}
            </div>"""

    # Related guides
    related = [p for p in all_posts if p["slug"] != slug][:3]
    related_links_html = ""
    if related:
        items = "".join(
            f'<li><a href="{p["slug"]}.html">{html.escape(p["title"])}</a></li>'
            for p in related
        )
        related_links_html = f"""
            <div class="sidebar-card">
              <p class="eyebrow">Related Guides</p>
              <h3>Keep reading</h3>
              <ul style="padding-left: 18px; margin: 0; font-size: 0.9rem;">{items}</ul>
            </div>"""

    # Generate Table of Contents from h2 tags and inject anchor IDs
    headings = []

    def inject_h2(match):
        raw_text = match.group(1)
        plain_text = re.sub(r"<[^>]+>", "", raw_text).strip()
        slug_id = re.sub(r"[^a-z0-9]+", "-", plain_text.lower()).strip("-")
        headings.append((slug_id, plain_text))
        return f'<h2 id="{slug_id}">{raw_text}</h2>'

    rendered_body = re.sub(r"<h2>(.*?)</h2>", inject_h2, post["body_html"])

    toc_html = ""
    if headings:
        toc_items = "".join(
            f'<li><a href="#{hid}">{html.escape(htext)}</a></li>'
            for hid, htext in headings
        )
        toc_html = f"""
            <div class="sidebar-card toc-card">
              <p class="eyebrow">On This Page</p>
              <h3>Table of Contents</h3>
              <ul class="toc-list">
                {toc_items}
              </ul>
            </div>"""

    pitch_screen = post.get("pitch_screen", "02-body-recovery.webp")

    return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="referrer" content="origin-when-cross-origin">
    <meta name="apple-itunes-app" content="app-id={app_id}, affiliate-data=pt={pt}&ct=web_smart_banner, app-argument={canonical_url}">
    <meta name="description" content="{html.escape(post['meta_description'])}">
    <meta name="theme-color" content="#F7F4EE">
    <link rel="canonical" href="{canonical_url}">
    <meta property="og:type" content="article">
    <meta property="og:url" content="{canonical_url}">
    <meta property="og:title" content="{html.escape(full_title)} — Alcohol Free Tracker">
    <meta property="og:description" content="{html.escape(post['meta_description'])}">
    <meta property="og:image" content="{site_url}/assets/appstore/{pitch_screen}">
    <title>{html.escape(full_title)} | Alcohol Free Tracker Guides</title>
    <link rel="icon" href="../assets/app-icon.png">
    <link rel="apple-touch-icon" href="../assets/app-icon.png">
    <link rel="stylesheet" href="../styles.css">
    <script type="application/ld+json">
{json.dumps(schema_graph, indent=2)}
    </script>
  </head>
  <body class="guide-page">
    <header class="site-header">
      <nav class="nav container" aria-label="Primary navigation">
        <a class="brand" href="../index.html" aria-label="Alcohol Free Tracker home">
          <img src="../assets/app-icon.png" alt="">
          <span>Alcohol Free Tracker</span>
        </a>
        <div class="nav-links">
          <a href="../index.html#features">Features</a>
          <a href="../index.html#gallery">Screens</a>
          <a href="index.html">Guides</a>
          <a href="../index.html#support">Support</a>
          <a class="nav-download" data-campaign="{page_ct}" href="{html.escape(url_nav)}" target="_blank" rel="noopener">Download</a>
        </div>
      </nav>
    </header>

    <main>
      <section class="guide-hero">
        <div class="container">
          <div class="guide-breadcrumb">
            <a href="../index.html">Home</a> &rsaquo; <a href="index.html">Guides</a> &rsaquo; <span>{html.escape(post.get('category', 'Guide'))}</span>
          </div>
          <span class="guide-tag">{cat_icon} {html.escape(post.get('category', 'Evidence-Based Guide'))}</span>
          <h1 class="guide-hero-title">{html.escape(post['title'])}</h1>
          {f'<p class="guide-hero-subtitle">{html.escape(post["subtitle"])}</p>' if post.get('subtitle') else ''}
          <div class="guide-meta">
            <span>Published {html.escape(post['published_date'])}</span>
            <span>&middot;</span>
            <span>{html.escape(post.get('reading_time', '5 min read'))}</span>
            <span>&middot;</span>
            <span>100% Private Sobriety &amp; Recovery Series</span>
          </div>
        </div>
      </section>

      <div class="container guide-layout">
        <div>
          <article class="guide-article">
            {rendered_body}
          </article>
          {faq_section_html}
        </div>

        <aside class="guide-sidebar" aria-label="Table of contents and related guides">
          {toc_html}
          {related_links_html}
        </aside>
      </div>

      <section class="cta-section">
        <div class="container">
          <div class="cta-card">
            <div>
              <p class="eyebrow">100% Private on iPhone &amp; iPad</p>
              <h2>Track your alcohol-free days without judgment.</h2>
              <p>Follow your physiological body recovery, calm cravings in 3 minutes, and watch your savings grow.</p>
            </div>
            <a class="button button-light app-store-button" data-campaign="{page_ct}" href="{html.escape(url_footer)}" target="_blank" rel="noopener" aria-label="Download Alcohol Free Tracker on the App Store">
              <span class="store-kicker">Download on the</span>
              <span class="store-name">App Store</span>
            </a>
          </div>
        </div>
      </section>
    </main>

    <footer class="site-footer">
      <div class="container">
        <div class="footer-grid">
          <div>
            <a class="brand" href="../index.html"><img src="../assets/app-icon.png" alt=""><span>Alcohol Free Tracker</span></a>
            <p class="footer-copy">A private, local-first tracker for alcohol-free days, body recovery, mindful drinking, and quiet reflection.</p>
          </div>
          <div class="footer-links">
            <a href="index.html">Guides</a>
            <a href="../index.html#support">Support</a>
            <a href="../privacy.html">Privacy</a>
            <a href="../terms.html">Terms</a>
          </div>
        </div>
        <p class="copyright">&copy; <span data-year>2026</span> Alcohol Free Tracker. Educational content only; not medical advice or a substitute for professional care.</p>
      </div>
    </footer>

    <script src="../script.js"></script>
  {beacon}
</body>
</html>
"""


def render_guides_index_html(posts: list, cfg: dict) -> str:
    site_url = cfg["site_url"].rstrip("/")
    app_id = cfg["app_id"]
    pt = DEFAULT_PROVIDER_TOKEN
    beacon = CF_BEACON
    canonical_url = f"{site_url}/guides/index.html"
    app_slug = site_url.rstrip("/").rsplit("/", 1)[-1]
    index_ct = guides_index_ct(app_slug)
    banner = smart_banner_tag(app_id) if app_is_released(app_id) else ""
    url_nav = make_asc_url(app_id, pt, index_ct)

    cards_html = [render_guide_card(p, "") for p in posts]

    return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="referrer" content="origin-when-cross-origin">
    <meta name="apple-itunes-app" content="app-id={app_id}, affiliate-data=pt={pt}&ct=web_smart_banner, app-argument={canonical_url}">
    <meta name="description" content="Evidence-based guides on alcohol body recovery timelines, 3-minute urge surfing for evening cravings, hangover anxiety relief, and mindful drinking.">
    <meta name="theme-color" content="#F7F4EE">
    <link rel="canonical" href="{canonical_url}">
    <title>Sobriety, Body Recovery &amp; Mindful Drinking Guides | Alcohol Free Tracker</title>
    <link rel="icon" href="../assets/app-icon.png">
    <link rel="apple-touch-icon" href="../assets/app-icon.png">
    <link rel="stylesheet" href="../styles.css">
  </head>
  <body class="guides-index-page">
    <header class="site-header">
      <nav class="nav container" aria-label="Primary navigation">
        <a class="brand" href="../index.html" aria-label="Alcohol Free Tracker home">
          <img src="../assets/app-icon.png" alt="">
          <span>Alcohol Free Tracker</span>
        </a>
        <div class="nav-links">
          <a href="../index.html#features">Features</a>
          <a href="../index.html#gallery">Screens</a>
          <a href="index.html" aria-current="page">Guides</a>
          <a href="../index.html#support">Support</a>
          <a class="nav-download" data-campaign="{index_ct}" href="{html.escape(url_nav)}" target="_blank" rel="noopener">Download</a>
        </div>
      </nav>
    </header>

    <main>
      <section class="guide-hero">
        <div class="container">
          <p class="eyebrow">Evidence-Based Resource Library</p>
          <h1>Guides for alcohol-free recovery &amp; mindful drinking.</h1>
          <p class="hero-lede">Practical physiological timelines, neuroscience-backed craving protocols, and judgment-free strategies for cutting back or staying sober.</p>
        </div>
      </section>

      <section class="section" style="padding-top: 56px;">
        <div class="container">
          <div class="guides-preview-grid">
            {''.join(cards_html)}
          </div>
        </div>
      </section>
    </main>

    <footer class="site-footer">
      <div class="container">
        <div class="footer-grid">
          <div>
            <a class="brand" href="../index.html"><img src="../assets/app-icon.png" alt=""><span>Alcohol Free Tracker</span></a>
            <p class="footer-copy">A private, local-first tracker for alcohol-free days, body recovery, mindful drinking, and quiet reflection.</p>
          </div>
          <div class="footer-links">
            <a href="../index.html">Home</a>
            <a href="../index.html#support">Support</a>
            <a href="../privacy.html">Privacy</a>
            <a href="../terms.html">Terms</a>
          </div>
        </div>
        <p class="copyright">&copy; <span data-year>2026</span> Alcohol Free Tracker. Not medical advice or a substitute for professional care.</p>
      </div>
    </footer>

    <script src="../script.js"></script>
  {beacon}
</body>
</html>
"""


def update_homepage_guides_preview(posts: list):
    index_path = os.path.join(ROOT_DIR, "index.html")
    if not os.path.exists(index_path):
        return
    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()

    cards = [render_guide_card(p, "guides/") for p in posts[:3]]

    replacement = '<div class="guides-preview-grid" id="home-guides-list">\n' + "\n".join(cards) + "\n          </div>"
    pattern = r'<div class="guides-preview-grid" id="home-guides-list">.*?(?=\s*<div style="margin-top: 28px;">)'
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(new_content)


def update_sitemaps(posts: list, cfg: dict):
    site_url = cfg["site_url"].rstrip("/")
    today = datetime.now().strftime("%Y-%m-%d")
    urls = [
        (f"{site_url}/", today),
        (f"{site_url}/guides/index.html", today),
        (f"{site_url}/support.html", "2026-10-20"),
        (f"{site_url}/privacy.html", "2026-10-20"),
        (f"{site_url}/terms.html", "2026-10-20"),
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

    # Also update master monorepo sitemap.xml at /Users/louisliu/Documents/repo/liuys_website/sitemap.xml
    master_sitemap = os.path.join(MONOREPO_ROOT, "sitemap.xml")
    if os.path.exists(master_sitemap):
        with open(master_sitemap, "r", encoding="utf-8") as f:
            master_content = f.read()
        for p in posts:
            guide_loc = f"{site_url}/guides/{p['slug']}.html"
            pub_date = p.get("published_date", today)
            if guide_loc not in master_content:
                entry = f"  <url><loc>{guide_loc}</loc><lastmod>{pub_date}</lastmod></url>\n"
                marker = f"<url><loc>{site_url}/guides/index.html</loc>"
                if marker in master_content:
                    idx = master_content.find("\n", master_content.find(marker))
                    if idx != -1:
                        master_content = master_content[:idx+1] + entry + master_content[idx+1:]
                else:
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

    # Sort newest first
    posts.sort(key=lambda x: x.get("published_date", ""), reverse=True)

    for post in posts:
        out_path = os.path.join(GUIDES_DIR, f"{post['slug']}.html")
        html_str = render_guide_html(post, cfg, posts)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html_str)
        print(f"Built guide: guides/{post['slug']}.html")

    # Build guides/index.html
    index_html = render_guides_index_html(posts, cfg)
    with open(os.path.join(GUIDES_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html)
    print("Built guides/index.html")

    # Update homepage preview & sitemaps
    update_homepage_guides_preview(posts)
    update_sitemaps(posts, cfg)

    # Save manifest
    manifest = [
        {
            "slug": p["slug"],
            "title": p["title"],
            "subtitle": p.get("subtitle", ""),
            "target_keyword": p.get("target_keyword", ""),
            "published_date": p.get("published_date", ""),
            "campaign_prefix": p.get("campaign_prefix", "")
        }
        for p in posts
    ]
    with open(os.path.join(GUIDES_DIR, "published_manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)
    print(f"Updated local + master sitemap.xml & published_manifest.json ({len(posts)} total guides).")


if __name__ == "__main__":
    main()
