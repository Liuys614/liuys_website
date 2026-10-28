#!/usr/bin/env python3
"""
Static Programmatic SEO Guide Builder for Inkstone: Sign PDF & Docs Website.
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


def render_guide_html(post: dict, cfg: dict, all_posts: list) -> str:
    site_url = cfg["site_url"].rstrip("/")
    app_id = cfg["app_id"]
    pt = DEFAULT_PROVIDER_TOKEN
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

    pitch_screen = post.get("pitch_screen", "inkstone.png")

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
                "image": f"{site_url}/assets/{pitch_screen}",
                "author": {
                    "@type": "Organization",
                    "name": "Inkstone Productivity Research"
                },
                "publisher": {
                    "@type": "Organization",
                    "name": "Inkstone: Sign PDF & Docs",
                    "logo": {
                        "@type": "ImageObject",
                        "url": f"{site_url}/assets/inkstone.png"
                    }
                }
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Inkstone Home", "item": f"{site_url}/"},
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
          <details open style="background:#f8fafc;border-radius:12px;padding:16px 20px;margin-bottom:12px;border:1px solid #e2e8f0;">
            <summary style="font-weight:700;color:#0f172a;cursor:pointer;">{q}</summary>
            <p style="margin:10px 0 0;font-size:0.95rem;color:#475569;line-height:1.6;">{a}</p>
          </details>""")

    faq_section_html = ""
    if faq_html_items:
        faq_section_html = f"""
        <section style="margin-top:40px;padding-top:28px;border-top:1px solid #e2e8f0;">
          <h2 style="font-size:1.4rem;font-weight:800;color:#0f172a;margin-bottom:18px;">Frequently Asked Questions</h2>
          {''.join(faq_html_items)}
        </section>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{html.escape(post['title'])} | Inkstone PDF Sign</title>
  <meta name="description" content="{html.escape(post['meta_description'])}" />
  <link rel="canonical" href="{canonical_url}" />
  <meta name="apple-itunes-app" content="app-id={app_id}" />
  <meta property="og:type" content="article" />
  <meta property="og:title" content="{html.escape(post['title'])}" />
  <meta property="og:description" content="{html.escape(post['meta_description'])}" />
  <meta property="og:url" content="{canonical_url}" />
  <link rel="icon" type="image/png" href="../assets/inkstone.png" />
  <style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #ffffff; color: #1e293b; margin: 0; line-height: 1.65; }}
    .site-nav {{ background: #fff; border-bottom: 1px solid #e2e8f0; padding: 14px 24px; display: flex; justify-content: space-between; align-items: center; max-width: 1040px; margin: 0 auto; }}
    .site-nav a {{ text-decoration: none; color: #0f172a; font-weight: 700; display: inline-flex; align-items: center; gap: 8px; }}
    .site-nav .btn {{ background: #6366f1; color: #fff; padding: 8px 16px; border-radius: 99px; font-size: 0.88rem; }}
    .guide-wrap {{ max-width: 820px; margin: 40px auto 72px; background: #fff; border-radius: 20px; padding: 40px; border: 1px solid #e2e8f0; box-shadow: 0 4px 24px rgba(15,23,42,0.04); }}
    .guide-wrap h1 {{ font-size: clamp(1.8rem, 3.5vw, 2.4rem); color: #0f172a; line-height: 1.2; margin: 12px 0 16px; font-weight: 800; }}
    .guide-meta {{ font-size: 0.86rem; color: #64748b; font-weight: 600; margin-bottom: 24px; padding-bottom: 16px; border-bottom: 1px solid #f1f5f9; }}
    .guide-content h2 {{ font-size: 1.35rem; color: #0f172a; margin: 32px 0 12px; font-weight: 800; }}
    .guide-content p, .guide-content li {{ font-size: 1.02rem; line-height: 1.72; color: #334155; margin-bottom: 14px; }}
    .guide-content ul, .guide-content ol {{ padding-left: 22px; margin-bottom: 18px; }}
    .guide-table {{ width: 100%; border-collapse: collapse; margin: 24px 0 32px; font-size: 0.94rem; }}
    .guide-table th {{ background: #f8fafc; padding: 12px 14px; text-align: left; border: 1px solid #e2e8f0; font-weight: 700; color: #0f172a; }}
    .guide-table td {{ padding: 12px 14px; border: 1px solid #e2e8f0; }}
    .guide-callout {{ background: #f5f3ff; border-left: 4px solid #6366f1; padding: 16px 20px; border-radius: 0 12px 12px 0; margin: 24px 0; font-size: 0.96rem; }}
    .guide-callout strong {{ display: block; margin-bottom: 4px; color: #4338ca; }}
    .app-card {{ background: linear-gradient(135deg, #f5f3ff 0%, #fff 100%); border: 1.5px solid #ddd6fe; border-radius: 18px; padding: 26px 30px; margin: 36px 0; display: flex; align-items: center; justify-content: space-between; gap: 24px; }}
    .app-card h3 {{ font-size: 1.22rem; font-weight: 800; color: #4338ca; margin: 0 0 6px; }}
    .app-card p {{ font-size: 0.92rem; color: #334155; margin: 0 0 14px; }}
    .app-card a {{ display: inline-block; background: #6366f1; color: #fff; padding: 9px 18px; border-radius: 99px; text-decoration: none; font-weight: 700; font-size: 0.88rem; }}
    .eyebrow {{ display: inline-block; background: #ede9fe; color: #4338ca; font-size: 0.74rem; font-weight: 700; text-transform: uppercase; padding: 4px 10px; border-radius: 99px; letter-spacing: 0.04em; }}
  </style>
  <script type="application/ld+json">
{json.dumps(schema_graph, indent=2)}
  </script>
</head>
<body>
  <div class="site-nav">
    <a href="../index.html">
      <span>Inkstone: Sign PDF &amp; Docs</span>
    </a>
    <a href="{html.escape(url_nav)}" class="btn" target="_blank" rel="noopener">Get Inkstone Free</a>
  </div>

  <main style="padding: 0 16px;">
    <article class="guide-wrap">
      <span class="eyebrow">{html.escape(post.get('category', 'Productivity Guide'))}</span>
      <h1>{html.escape(post['title'])}</h1>
      <div class="guide-meta">
        Published {html.escape(post['published_date'])} · {html.escape(post.get('reading_time', '5 min read'))} · Inkstone Mobile eSign Series
      </div>
      <div class="guide-content">
        {post['body_html']}
      </div>
      <div class="app-card">
        <div>
          <h3>{html.escape(post.get('pitch_headline', 'Sign documents & send browser links'))}</h3>
          <p>{html.escape(post.get('pitch_body', 'Zero account required for signers. Sign and share contracts in seconds.'))}</p>
          <a href="{html.escape(url_footer)}" target="_blank" rel="noopener">Download Inkstone on App Store &rarr;</a>
        </div>
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
    pt = DEFAULT_PROVIDER_TOKEN
    beacon = CF_BEACON
    canonical_url = f"{site_url}/guides/index.html"
    app_slug = site_url.rstrip("/").rsplit("/", 1)[-1]
    index_ct = guides_index_ct(app_slug)
    banner = smart_banner_tag(app_id) if app_is_released(app_id) else ""
    url_nav = make_asc_url(app_id, pt, index_ct)

    cards_html = []
    for p in posts:
        cards_html.append(f"""
        <article style="background:#fff;border:1px solid #e2e8f0;border-radius:16px;padding:24px;display:flex;flex-direction:column;align-items:flex-start;">
          <span style="display:inline-block;background:#ede9fe;color:#4338ca;font-size:0.74rem;font-weight:700;text-transform:uppercase;padding:3px 9px;border-radius:99px;margin-bottom:10px;">{html.escape(p.get('category', 'Guide'))}</span>
          <h2 style="font-size:1.22rem;font-weight:800;margin:4px 0 10px;"><a href="{p['slug']}.html" style="color:#0f172a;text-decoration:none;">{html.escape(p['title'])}</a></h2>
          <p style="font-size:0.92rem;color:#64748b;margin-bottom:16px;line-height:1.5;">{html.escape(p.get('summary_excerpt', p['meta_description']))}</p>
          <a href="{p['slug']}.html" style="font-weight:700;color:#6366f1;text-decoration:none;font-size:0.9rem;margin-top:auto;">Read Guide ({html.escape(p.get('reading_time', '5 min'))}) &rarr;</a>
        </article>""")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>PDF Signing, Digital Contracts & Document Guides | Inkstone</title>
  <meta name="description" content="Step-by-step guides on signing PDF documents on iPhone, preparing contracts for client signature without subscriptions, and filling PDF forms securely." />
  <link rel="canonical" href="{canonical_url}" />
  {banner}
  <style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #f8fafc; color: #1e293b; margin: 0; line-height: 1.65; }}
    .site-nav {{ background: #fff; border-bottom: 1px solid #e2e8f0; padding: 14px 24px; display: flex; justify-content: space-between; align-items: center; max-width: 1040px; margin: 0 auto; }}
    .site-nav a {{ text-decoration: none; color: #0f172a; font-weight: 700; }}
    .site-nav .btn {{ background: #6366f1; color: #fff; padding: 8px 16px; border-radius: 99px; font-size: 0.88rem; }}
  </style>
</head>
<body>
  <div class="site-nav">
    <a href="../index.html">Inkstone: Sign PDF &amp; Docs</a>
    <a href="{html.escape(url_nav)}" class="btn" target="_blank" rel="noopener">Get Inkstone App</a>
  </div>
  <main style="max-width:1040px;margin:48px auto 80px;padding:0 20px;">
    <div style="text-align:center;max-width:640px;margin:0 auto 48px;">
      <h1 style="font-size:clamp(2rem,3.8vw,2.7rem);font-weight:800;color:#0f172a;margin:12px 0;">PDF Signing &amp; Document Guides</h1>
      <p style="font-size:1.05rem;color:#64748b;">Simple, subscription-free ways to sign contracts, fill forms, and share encrypted signature requests on mobile.</p>
    </div>
    <div style="display:grid;grid-template-columns:repeat(auto-fill, minmax(320px, 1fr));gap:24px;">
      {''.join(cards_html)}
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
