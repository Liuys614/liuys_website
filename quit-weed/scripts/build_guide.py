#!/usr/bin/env python3
"""
Static Programmatic SEO Guide Builder for T-Break & Quit Weed: Unfog.
Compiles JSON guide definitions in guides/posts/*.json into:
  1. guides/<slug>.html (with JSON-LD Article + FAQPage + ASC Campaign Links)
  2. guides/index.html (Science Guides Hub page)
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
GUIDES_DIR = os.path.join(ROOT_DIR, "guides")
POSTS_DIR = os.path.join(GUIDES_DIR, "posts")
CONFIG_PATH = os.path.join(GUIDES_DIR, "seo_config.json")


def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def make_asc_url(app_id: str, pt: str, ct: str) -> str:
    clean_ct = re.sub(r"[^a-zA-Z0-9_-]", "_", ct)[:40]
    return f"https://apps.apple.com/app/apple-store/id{app_id}?pt={pt}&ct={clean_ct}&mt=8"


def render_guide_html(post: dict, cfg: dict, all_posts: list) -> str:
    site_url = cfg["site_url"].rstrip("/")
    app_id = cfg["app_id"]
    pt = cfg["provider_token"]
    slug = post["slug"]
    canonical_url = f"{site_url}/guides/{slug}.html"
    prefix = post.get("campaign_prefix", f"seo_{slug[:24]}")

    url_nav = make_asc_url(app_id, pt, f"{prefix}_nav")
    url_footer = make_asc_url(app_id, pt, f"{prefix}_foot")

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

    pitch_screen = post.get("pitch_screen", "02-body-recovery.webp")

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
                    "name": "Unfog Neuroscience Editorial"
                },
                "publisher": {
                    "@type": "Organization",
                    "name": "T-Break & Quit Weed: Unfog",
                    "logo": {
                        "@type": "ImageObject",
                        "url": f"{site_url}/assets/app-icon.png"
                    }
                }
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Unfog Home", "item": f"{site_url}/"},
                    {"@type": "ListItem", "position": 2, "name": "Science Guides", "item": f"{site_url}/guides/index.html"},
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
  <title>{html.escape(post['title'])} | Unfog Science Guides</title>
  <meta name="description" content="{html.escape(post['meta_description'])}" />
  <link rel="canonical" href="{canonical_url}" />
  <meta name="apple-itunes-app" content="app-id={app_id}" />
  <meta property="og:type" content="article" />
  <meta property="og:title" content="{html.escape(post['title'])}" />
  <meta property="og:description" content="{html.escape(post['meta_description'])}" />
  <meta property="og:url" content="{canonical_url}" />
  <meta property="og:image" content="{site_url}/assets/appstore/{pitch_screen}" />
  <link rel="icon" type="image/png" href="../assets/app-icon.png" />
  <link rel="stylesheet" href="../styles.css" />
  <style>
    .guide-shell {{ max-width: 820px; margin: 48px auto 72px; background: #fff; border-radius: 28px; padding: 44px; border: 1px solid rgba(30,63,53,0.11); box-shadow: 0 18px 42px -12px rgba(21,46,38,0.08); }}
    .guide-shell h1 {{ font-size: clamp(1.9rem, 3.5vw, 2.6rem); color: #152E26; line-height: 1.15; margin: 12px 0 14px; font-weight: 800; }}
    .guide-meta-bar {{ font-size: 0.86rem; color: #52665E; font-weight: 600; margin-bottom: 28px; padding-bottom: 20px; border-bottom: 1px solid rgba(30,63,53,0.1); }}
    .guide-content h2 {{ font-size: 1.38rem; color: #1E3F35; margin: 30px 0 12px; font-weight: 800; }}
    .guide-content p, .guide-content li {{ font-size: 1.02rem; line-height: 1.72; color: #233B32; margin-bottom: 14px; }}
    .guide-content ul {{ padding-left: 22px; margin-bottom: 18px; }}
    .guide-faq-box {{ margin-top: 38px; padding-top: 28px; border-top: 1px solid rgba(30,63,53,0.12); }}
    .guide-faq-item {{ background: #F6F4EE; border-radius: 16px; padding: 16px 20px; margin-bottom: 12px; }}
    .guide-faq-item summary {{ font-weight: 800; color: #152E26; cursor: pointer; }}
    .guide-faq-item p {{ margin: 10px 0 0; font-size: 0.95rem; color: #385249; }}
  </style>
  <script type="application/ld+json">
{json.dumps(schema_graph, indent=2)}
  </script>
</head>
<body>
  <header class="site-header">
    <div class="container nav-inner">
      <div class="brand-cluster">
        <a href="../index.html" class="brand-logo">
          <img src="../assets/app-icon.png" alt="Unfog Icon" class="brand-icon" width="34" height="34" />
          <span class="brand-title">Unfog</span>
        </a>
        <span class="crumb-sep">/</span>
        <a href="index.html" class="studio-crumb">Science Guides</a>
      </div>
      <a href="{html.escape(url_nav)}" class="btn-pill btn-forest" target="_blank" rel="noopener">Get Unfog App</a>
    </div>
  </header>

  <main class="container">
    <article class="guide-shell">
      <span class="eyebrow-pill">{html.escape(post.get('category', 'Science Guide'))}</span>
      <h1>{html.escape(post['title'])}</h1>
      <div class="guide-meta-bar">
        Published {html.escape(post['published_date'])} · {html.escape(post.get('reading_time', '5 min read'))} · Evidence-Based THC &amp; CB1 Recovery Series
      </div>
      <div class="guide-content">
        {post['body_html']}
      </div>
      {faq_section_html}
    </article>

    <section class="final-cta-section" style="padding-top: 0;">
      <div class="final-cta-card">
        <img src="../assets/app-icon.png" alt="Unfog App Icon" class="final-cta-icon" width="72" height="72" />
        <h2 class="final-cta-title">Track Your CB1 Reset Privately on iPhone.</h2>
        <p class="final-cta-sub">30-Day T-Break or Quit for Good · 4-7-8 Vagus Nerve Lotus · 100% On-Device</p>
        <a href="{html.escape(url_footer)}" class="btn-store-primary btn-store-gold" target="_blank" rel="noopener">
          <div class="store-btn-text">
            <span class="store-small">Download on the</span>
            <span class="store-big">App Store</span>
          </div>
        </a>
      </div>
    </section>
  </main>
</body>
</html>
"""


def render_guides_index_html(posts: list, cfg: dict) -> str:
    site_url = cfg["site_url"].rstrip("/")
    app_id = cfg["app_id"]
    pt = cfg["provider_token"]
    canonical_url = f"{site_url}/guides/index.html"
    url_nav = make_asc_url(app_id, pt, "web_guides_nav")

    cards_html = []
    for p in posts:
        cards_html.append(f"""
        <article class="bento-card" style="flex-direction: column; align-items: flex-start;">
          <span class="bento-tag">{html.escape(p.get('category', 'Science Guide'))}</span>
          <h2 class="bento-title" style="font-size: 1.28rem;"><a href="{p['slug']}.html" style="color: inherit; text-decoration: none;">{html.escape(p['title'])}</a></h2>
          <p class="bento-desc" style="margin-bottom: 12px;">{html.escape(p.get('summary_excerpt', p['meta_description']))}</p>
          <a href="{p['slug']}.html" style="font-weight: 800; color: #2D6A4F; text-decoration: none; font-size: 0.9rem;">Read Guide ({html.escape(p.get('reading_time', '5 min'))}) →</a>
        </article>""")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>THC Withdrawal, CB1 Recovery & T-Break Science Guides | Unfog</title>
  <meta name="description" content="Evidence-based guides on cannabis tolerance breaks (T-Breaks), CB1 receptor upregulation timelines, REM sleep dream rebound, and 4-7-8 craving relief." />
  <link rel="canonical" href="{canonical_url}" />
  <link rel="icon" type="image/png" href="../assets/app-icon.png" />
  <link rel="stylesheet" href="../styles.css" />
</head>
<body>
  <header class="site-header">
    <div class="container nav-inner">
      <div class="brand-cluster">
        <a href="../index.html" class="brand-logo">
          <img src="../assets/app-icon.png" alt="Unfog Icon" class="brand-icon" width="34" height="34" />
          <span class="brand-title">Unfog</span>
        </a>
        <span class="crumb-sep">/</span>
        <span class="brand-tag">Science Guides</span>
      </div>
      <a href="{html.escape(url_nav)}" class="btn-pill btn-forest" target="_blank" rel="noopener">Get Unfog App</a>
    </div>
  </header>

  <main class="container" style="padding: 56px 24px 80px;">
    <div class="section-header-compact">
      <span class="eyebrow-pill">📚 Neuroscience &amp; T-Break Library</span>
      <h1 class="section-title">THC Detox &amp; CB1 Recovery Guides</h1>
      <p class="section-sub">Peer-reviewed physiological timelines and practical protocols for resetting cannabis tolerance and clearing brain fog.</p>
    </div>

    <div class="bento-grid" style="grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));">
      {''.join(cards_html)}
    </div>
  </main>
</body>
</html>
"""


def update_sitemaps(posts: list, cfg: dict):
    site_url = cfg["site_url"].rstrip("/")
    today = datetime.now().strftime("%Y-%m-%d")
    urls = [
        (f"{site_url}/", today),
        (f"{site_url}/guides/index.html", today),
        (f"{site_url}/support.html", today),
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

    # Update master monorepo sitemap.xml
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
