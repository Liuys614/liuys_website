#!/usr/bin/env python3
"""
Static Programmatic SEO Guide Builder for Agricola Score Sheet Website.
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
                "author": {
                    "@type": "Organization",
                    "name": "Agricola Board Game Rules Research"
                },
                "publisher": {
                    "@type": "Organization",
                    "name": "Agricola Score Sheet",
                    "logo": {
                        "@type": "ImageObject",
                        "url": f"{site_url}/app-icon.png"
                    }
                }
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Agricola Scorer Home", "item": f"{site_url}/"},
                    {"@type": "ListItem", "position": 2, "name": "Rules Guides", "item": f"{site_url}/guides/index.html"},
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
          <details open style="background:#fcfaf6;border-radius:12px;padding:16px 20px;margin-bottom:12px;border:1px solid #e7dac9;">
            <summary style="font-weight:700;color:#2c1810;cursor:pointer;">{q}</summary>
            <p style="margin:10px 0 0;font-size:0.95rem;color:#5c4738;line-height:1.6;">{a}</p>
          </details>""")

    faq_section_html = ""
    if faq_html_items:
        faq_section_html = f"""
        <section style="margin-top:40px;padding-top:28px;border-top:1px solid #e7dac9;">
          <h2 style="font-size:1.4rem;font-weight:800;color:#2c1810;margin-bottom:18px;">Frequently Asked Questions</h2>
          {''.join(faq_html_items)}
        </section>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{html.escape(post['title'])} | Agricola Score Sheet</title>
  <meta name="description" content="{html.escape(post['meta_description'])}" />
  <link rel="canonical" href="{canonical_url}" />
  <meta name="apple-itunes-app" content="app-id={app_id}" />
  <meta property="og:type" content="article" />
  <meta property="og:title" content="{html.escape(post['title'])}" />
  <meta property="og:description" content="{html.escape(post['meta_description'])}" />
  <meta property="og:url" content="{canonical_url}" />
  <style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #fbf9f5; color: #2c1810; margin: 0; line-height: 1.65; }}
    .site-nav {{ background: #fff; border-bottom: 1px solid #e7dac9; padding: 14px 24px; display: flex; justify-content: space-between; align-items: center; max-width: 1040px; margin: 0 auto; }}
    .site-nav a {{ text-decoration: none; color: #2c1810; font-weight: 700; }}
    .site-nav .btn {{ background: #8b5a2b; color: #fff; padding: 8px 16px; border-radius: 99px; font-size: 0.88rem; }}
    .guide-wrap {{ max-width: 820px; margin: 40px auto 72px; background: #fff; border-radius: 20px; padding: 40px; border: 1px solid #e7dac9; box-shadow: 0 4px 24px rgba(44,24,16,0.04); }}
    .guide-wrap h1 {{ font-size: clamp(1.8rem, 3.5vw, 2.4rem); color: #2c1810; line-height: 1.2; margin: 12px 0 16px; font-weight: 800; }}
    .guide-meta {{ font-size: 0.86rem; color: #7d6350; font-weight: 600; margin-bottom: 24px; padding-bottom: 16px; border-bottom: 1px solid #f2e9de; }}
    .guide-content h2 {{ font-size: 1.35rem; color: #2c1810; margin: 32px 0 12px; font-weight: 800; }}
    .guide-content p, .guide-content li {{ font-size: 1.02rem; line-height: 1.72; color: #423023; margin-bottom: 14px; }}
    .guide-content ul, .guide-content ol {{ padding-left: 22px; margin-bottom: 18px; }}
    .guide-table {{ width: 100%; border-collapse: collapse; margin: 24px 0 32px; font-size: 0.94rem; }}
    .guide-table th {{ background: #f7f1e8; padding: 12px 14px; text-align: left; border: 1px solid #e7dac9; font-weight: 700; color: #2c1810; }}
    .guide-table td {{ padding: 12px 14px; border: 1px solid #e7dac9; }}
    .guide-callout {{ background: #fdf6ec; border-left: 4px solid #b45309; padding: 16px 20px; border-radius: 0 12px 12px 0; margin: 24px 0; font-size: 0.96rem; }}
    .guide-callout strong {{ display: block; margin-bottom: 4px; color: #92400e; }}
    .app-card {{ background: linear-gradient(135deg, #fdf6ec 0%, #fff 100%); border: 1.5px solid #fed7aa; border-radius: 18px; padding: 26px 30px; margin: 36px 0; display: flex; align-items: center; justify-content: space-between; gap: 24px; }}
    .app-card h3 {{ font-size: 1.22rem; font-weight: 800; color: #92400e; margin: 0 0 6px; }}
    .app-card p {{ font-size: 0.92rem; color: #423023; margin: 0 0 14px; }}
    .app-card a {{ display: inline-block; background: #8b5a2b; color: #fff; padding: 9px 18px; border-radius: 99px; text-decoration: none; font-weight: 700; font-size: 0.88rem; }}
    .eyebrow {{ display: inline-block; background: #fef3c7; color: #92400e; font-size: 0.74rem; font-weight: 700; text-transform: uppercase; padding: 4px 10px; border-radius: 99px; letter-spacing: 0.04em; }}
  </style>
  <script type="application/ld+json">
{json.dumps(schema_graph, indent=2)}
  </script>
</head>
<body>
  <div class="site-nav">
    <a href="../index.html">Agricola Score Sheet</a>
    <a href="{html.escape(url_nav)}" class="btn" target="_blank" rel="noopener">Get Scorer on App Store</a>
  </div>

  <main style="padding: 0 16px;">
    <article class="guide-wrap">
      <span class="eyebrow">{html.escape(post.get('category', 'Board Game Rules'))}</span>
      <h1>{html.escape(post['title'])}</h1>
      <div class="guide-meta">
        Published {html.escape(post['published_date'])} · {html.escape(post.get('reading_time', '5 min read'))} · Agricola Companion Rules Series
      </div>
      <div class="guide-content">
        {post['body_html']}
      </div>
      <div class="app-card">
        <div>
          <h3>{html.escape(post.get('pitch_headline', 'Score your Agricola games in seconds'))}</h3>
          <p>{html.escape(post.get('pitch_body', 'Zero math errors, automatic penalty tracking, and saved match history on iPhone.'))}</p>
          <a href="{html.escape(url_footer)}" target="_blank" rel="noopener">Download Agricola Scorer &rarr;</a>
        </div>
      </div>
      {faq_section_html}
    </article>
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
        <article style="background:#fff;border:1px solid #e7dac9;border-radius:16px;padding:24px;display:flex;flex-direction:column;align-items:flex-start;">
          <span style="display:inline-block;background:#fef3c7;color:#92400e;font-size:0.74rem;font-weight:700;text-transform:uppercase;padding:3px 9px;border-radius:99px;margin-bottom:10px;">{html.escape(p.get('category', 'Rules Guide'))}</span>
          <h2 style="font-size:1.22rem;font-weight:800;margin:4px 0 10px;"><a href="{p['slug']}.html" style="color:#2c1810;text-decoration:none;">{html.escape(p['title'])}</a></h2>
          <p style="font-size:0.92rem;color:#7d6350;margin-bottom:16px;line-height:1.5;">{html.escape(p.get('summary_excerpt', p['meta_description']))}</p>
          <a href="{p['slug']}.html" style="font-weight:700;color:#8b5a2b;text-decoration:none;font-size:0.9rem;margin-top:auto;">Read Guide ({html.escape(p.get('reading_time', '5 min'))}) &rarr;</a>
        </article>""")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Agricola Board Game Rules &amp; Scoring Strategy Guides</title>
  <meta name="description" content="Master end-game Agricola point calculations, avoid begging card penalties, and optimize farmyard scoring with clear rules and strategy guides." />
  <link rel="canonical" href="{canonical_url}" />
  <style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #fbf9f5; color: #2c1810; margin: 0; line-height: 1.65; }}
    .site-nav {{ background: #fff; border-bottom: 1px solid #e7dac9; padding: 14px 24px; display: flex; justify-content: space-between; align-items: center; max-width: 1040px; margin: 0 auto; }}
    .site-nav a {{ text-decoration: none; color: #2c1810; font-weight: 700; }}
    .site-nav .btn {{ background: #8b5a2b; color: #fff; padding: 8px 16px; border-radius: 99px; font-size: 0.88rem; }}
  </style>
</head>
<body>
  <div class="site-nav">
    <a href="../index.html">Agricola Score Sheet</a>
    <a href="{html.escape(url_nav)}" class="btn" target="_blank" rel="noopener">Get Scorer App</a>
  </div>
  <main style="max-width:1040px;margin:48px auto 80px;padding:0 20px;">
    <div style="text-align:center;max-width:640px;margin:0 auto 48px;">
      <h1 style="font-size:clamp(2rem,3.8vw,2.7rem);font-weight:800;color:#2c1810;margin:12px 0;">Agricola Scoring &amp; Strategy Guides</h1>
      <p style="font-size:1.05rem;color:#7d6350;">Point category charts, harvest food engines, room upgrades, and card bonus calculations.</p>
    </div>
    <div style="display:grid;grid-template-columns:repeat(auto-fill, minmax(320px, 1fr));gap:24px;">
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
