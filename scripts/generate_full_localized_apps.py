#!/usr/bin/env python3
"""
Generate 100% UI-Parity Deeply-Localized Landing Pages for all 8 apps across 7 target locales:
zh-tw, ja, ko, de, fr, es, it.

Fixes:
1. Pure borderless RAW screenshots for Hero Phones to eliminate double-border artifacts.
2. 100% deep translations of every section (Hero, Science, Urge Surfing, Recovery, Compare, Features, Gallery, FAQ, Footer).
3. Root-relative asset paths for 100% CSS/JS/font fidelity.
4. Accurate 8-way alternate hreflang and canonical links.
"""

import os
import re
from translations_data import LOCALES_META, APP_TRANSLATIONS
from comprehensive_translations import COMMON_DICT, DEEP_APP_CONTENT

BASE_DIR = '/Users/louisliu/Documents/repo/liuys_website'
SITE_ORIGIN = 'https://ysliustudio.com'

APPS = [
    'quit-vaping',
    'alcohol-free-tracker',
    'pill-reminder',
    'quit-weed',
    'levain',
    'grocery-price',
    'inkstone',
    'agricola-scorer',
]

def render_lang_switcher(current_locale, app_slug):
    current_name = LOCALES_META.get(current_locale, {}).get("name", "English") if current_locale != "en" else "English"
    
    options = [
        ('en', 'English', f'/{app_slug}/'),
        ('zh-tw', '繁體中文', f'/zh-tw/{app_slug}/'),
        ('de', 'Deutsch', f'/de/{app_slug}/'),
        ('fr', 'Français', f'/fr/{app_slug}/'),
        ('ja', '日本語', f'/ja/{app_slug}/'),
        ('ko', '한국어', f'/ko/{app_slug}/'),
        ('es', 'Español', f'/es/{app_slug}/'),
        ('it', 'Italiano', f'/it/{app_slug}/'),
    ]
    
    opts_html = []
    for loc, name, url in options:
        active = ' active' if loc == current_locale else ''
        opts_html.append(f'      <a href="{url}" class="lang-opt{active}" data-lang="{loc}">{name}</a>')
    opts_str = "\n".join(opts_html)
    
    return f"""<div class="lang-switcher">
    <button class="lang-btn" type="button" aria-label="Select Language" aria-expanded="false">
      <svg class="lang-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <circle cx="12" cy="12" r="10"></circle>
        <line x1="2" y1="12" x2="22" y2="12"></line>
        <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
      </svg>
      <span class="lang-current">{current_name}</span>
      <svg class="lang-chevron" viewBox="0 0 20 20" fill="currentColor">
        <path fill-rule="evenodd" d="M5.23 7.21a.75.75 0 011.06.02L10 11.168l3.71-3.938a.75.75 0 111.08 1.04l-4.25 4.5a.75.75 0 01-1.08 0l-4.25-4.5a.75.75 0 01.02-1.06z" clip-rule="evenodd" />
      </svg>
    </button>
    <div class="lang-dropdown">
{opts_str}
    </div>
  </div>"""

def normalize_assets_and_scripts(html, app):
    html = re.sub(r'href=[\"\']styles\.css[\"\']', f'href="/{app}/styles.css"', html)
    html = re.sub(r'href=[\"\']style\.css[\"\']', f'href="/{app}/style.css"', html)
    html = re.sub(r'src=[\"\']script\.js[\"\']', f'src="/{app}/script.js"', html)
    html = re.sub(r'src=[\"\']scripts/', f'src="/{app}/scripts/', html)
    html = re.sub(r'href=[\"\']assets/', f'href="/{app}/assets/', html)
    html = re.sub(r'src=[\"\']assets/', f'src="/{app}/assets/', html)
    html = re.sub(r'srcset=[\"\']assets/', f'srcset="/{app}/assets/', html)
    
    if '/lang-switcher.css' not in html:
        html = html.replace('</head>', '  <link rel="stylesheet" href="/lang-switcher.css">\n</head>')
    if '/lang-switcher.js' not in html:
        html = html.replace('</body>', '  <script src="/lang-switcher.js"></script>\n</body>')
        
    return html

def replace_screenshots_for_locale(html, app, locale):
    loc_shot_dir = os.path.join(BASE_DIR, app, 'assets/screenshots_localized', locale)
    if not os.path.isdir(loc_shot_dir):
        return html
    
    available_files = os.listdir(loc_shot_dir)
    
    if app == 'quit-vaping':
        # Replace hero phone with borderless RAW screenshot
        if 'hero-today-recovery-raw.webp' in available_files:
            html = re.sub(
                rf'/{app}/assets/screens/hero-today-recovery\.webp',
                f'/{app}/assets/screenshots_localized/{locale}/hero-today-recovery-raw.webp',
                html
            )
        # Replace appstore carousel
        for f in available_files:
            if re.match(r'^\d\d-', f):
                html = re.sub(
                    rf'/{app}/assets/appstore/{re.escape(f)}',
                    f'/{app}/assets/screenshots_localized/{locale}/{f}',
                    html
                )

    elif app == 'alcohol-free-tracker':
        # Replace hero phone with borderless RAW screenshot
        if 'hero-today-raw.webp' in available_files:
            html = re.sub(
                rf'/{app}/assets/screens/06-today-light\.webp',
                f'/{app}/assets/screenshots_localized/{locale}/hero-today-raw.webp',
                html
            )
        # Replace appstore carousel
        for f in available_files:
            if re.match(r'^\d\d-', f):
                html = re.sub(
                    rf'/{app}/assets/appstore/{re.escape(f)}',
                    f'/{app}/assets/screenshots_localized/{locale}/{f}',
                    html
                )

    elif app == 'pill-reminder':
        # Replace hero phone with borderless RAW screenshot
        if 'hero-home-raw.webp' in available_files:
            html = re.sub(
                rf'/{app}/assets/screens/hero-home\.webp',
                f'/{app}/assets/screenshots_localized/{locale}/hero-home-raw.webp',
                html
            )
        for f in available_files:
            if re.match(r'^\d\d-', f):
                html = re.sub(
                    rf'/{app}/assets/appstore/{re.escape(f)}',
                    f'/{app}/assets/screenshots_localized/{locale}/{f}',
                    html
                )

    elif app == 'levain':
        for f in available_files:
            m = re.match(r'shot-(\d+)\.webp', f)
            if m:
                num = m.group(1)
                html = re.sub(
                    rf'/{app}/assets/shots/shot-{num}\.png',
                    f'/{app}/assets/screenshots_localized/{locale}/{f}',
                    html
                )

    elif app == 'quit-weed':
        if 'hero-today-recovery-raw.webp' in available_files:
            html = re.sub(
                rf'/{app}/assets/screens/hero-today-recovery\.webp',
                f'/{app}/assets/screenshots_localized/{locale}/hero-today-recovery-raw.webp',
                html
            )

    elif app == 'inkstone':
        for f in available_files:
            m = re.match(r'(\d+)\.webp', f)
            if m:
                num = m.group(1)
                html = re.sub(
                    rf'/{app}/assets/screenshots/{num}\.png',
                    f'/{app}/assets/screenshots_localized/{locale}/{f}',
                    html
                )
                html = re.sub(
                    rf'/{app}/assets/{num}\.png',
                    f'/{app}/assets/screenshots_localized/{locale}/{f}',
                    html
                )

    return html

def update_seo_metadata(html, app, locale):
    meta_info = LOCALES_META.get(locale, {"name": locale, "html_lang": locale})
    app_trans = APP_TRANSLATIONS.get(app, {}).get(locale, {})
    
    html = re.sub(r'<html\s+lang=[\"\'][^\"\']*[\"\']>', f'<html lang="{meta_info["html_lang"]}">', html)
    new_canon = f"{SITE_ORIGIN}/{locale}/{app}/"
    html = re.sub(r'<link\s+rel=[\"\']canonical[\"\'][^>]*>', f'<link rel="canonical" href="{new_canon}">', html)
    
    if "title" in app_trans:
        title_str = app_trans["title"]
        html = re.sub(r'<title>.*?</title>', f'<title>{title_str}</title>', html, flags=re.DOTALL)
        html = re.sub(r'<meta\s+property=[\"\']og:title[\"\']\s+content=[\"\'][^\"\']*[\"\']>', f'<meta property="og:title" content="{title_str}">', html)

    if "meta_desc" in app_trans:
        desc_str = app_trans["meta_desc"]
        html = re.sub(r'<meta\s+name=[\"\']description[\"\']\s+content=[\"\'][^\"\']*[\"\']>', f'<meta name="description" content="{desc_str}">', html)
        html = re.sub(r'<meta\s+property=[\"\']og:description[\"\']\s+content=[\"\'][^\"\']*[\"\']>', f'<meta property="og:description" content="{desc_str}">', html)

    html = re.sub(r'<meta\s+property=[\"\']og:url[\"\']\s+content=[\"\'][^\"\']*[\"\']>', f'<meta property="og:url" content="{new_canon}">', html)

    hreflangs = [
        f'  <link rel="alternate" hreflang="x-default" href="{SITE_ORIGIN}/{app}/" />',
        f'  <link rel="alternate" hreflang="en" href="{SITE_ORIGIN}/{app}/" />',
        f'  <link rel="alternate" hreflang="zh-TW" href="{SITE_ORIGIN}/zh-tw/{app}/" />',
        f'  <link rel="alternate" hreflang="de" href="{SITE_ORIGIN}/de/{app}/" />',
        f'  <link rel="alternate" hreflang="fr" href="{SITE_ORIGIN}/fr/{app}/" />',
        f'  <link rel="alternate" hreflang="ja" href="{SITE_ORIGIN}/ja/{app}/" />',
        f'  <link rel="alternate" hreflang="ko" href="{SITE_ORIGIN}/ko/{app}/" />',
        f'  <link rel="alternate" hreflang="es" href="{SITE_ORIGIN}/es/{app}/" />',
        f'  <link rel="alternate" hreflang="it" href="{SITE_ORIGIN}/it/{app}/" />',
    ]
    html = re.sub(r'(<link\s+rel=[\"\']alternate[\"\'][^>]*>\s*)+', "\n".join(hreflangs) + "\n", html)
    
    return html

def update_switcher_and_nav(html, app, locale):
    new_switcher = render_lang_switcher(locale, app)
    if 'class="lang-switcher"' in html:
        html = re.sub(r'<div class="lang-switcher">.*?</div>\s*</div>', new_switcher + "\n", html, flags=re.DOTALL)
    else:
        html = html.replace('<div class="nav-links">', f'<div class="nav-links">\n{new_switcher}')
        
    html = re.sub(r'<a\s+class=[\"\']brand[\"\']\s+href=[\"\'][^\"\']*[\"\']', f'<a class="brand" href="/{locale}/"', html)
    return html

def apply_deep_translations(html, app, locale):
    # 1. Apply app-specific hero & meta
    app_trans = APP_TRANSLATIONS.get(app, {}).get(locale, {})
    if "eyebrow" in app_trans:
        html = re.sub(r'(<p\s+class=[\"\']eyebrow[\"\'][^>]*>).*?(</p>)', rf'\g<1>{app_trans["eyebrow"]}\g<2>', html, flags=re.DOTALL)
    if "h1" in app_trans:
        html = re.sub(r'(<h1[^>]*>).*?(</h1>)', rf'\g<1>{app_trans["h1"]}\g<2>', html, flags=re.DOTALL)
    if "lede" in app_trans:
        html = re.sub(r'(<p\s+class=[\"\']hero-lede[\"\'][^>]*>).*?(</p>)', rf'\g<1>{app_trans["lede"]}\g<2>', html, flags=re.DOTALL)
    if "store_note" in app_trans:
        html = re.sub(r'(<p\s+class=[\"\']store-note[\"\'][^>]*>).*?(</p>)', rf'\g<1>{app_trans["store_note"]}\g<2>', html, flags=re.DOTALL)
    if "explore_science" in app_trans:
        html = re.sub(r'(<a\s+class=[\"\']button\s+button-secondary[\"\']\s+href=[\"\']#science[\"\'][^>]*>).*?(</a>)', rf'\g<1>{app_trans["explore_science"]}\g<2>', html, flags=re.DOTALL)

    # 2. Apply global common dict
    common = COMMON_DICT.get(locale, {})
    # Sort strings longest first to prevent prefix collisions
    for en_str, loc_str in sorted(common.items(), key=lambda x: -len(x[0])):
        # Replace between tags or exact tag content
        html = re.sub(rf'>\s*{re.escape(en_str)}\s*<', f'>{loc_str}<', html)

    # 3. Apply app deep dictionary (covers Science, Compare, Features, FAQ, etc.)
    deep_dict = DEEP_APP_CONTENT.get(app, {}).get(locale, {})
    for en_str, loc_str in sorted(deep_dict.items(), key=lambda x: -len(x[0])):
        # Match inside HTML elements
        pattern = re.compile(rf'(>|\"|&nbsp;)\s*{re.escape(en_str)}\s*(<|\"|&nbsp;)', re.IGNORECASE)
        html = pattern.sub(rf'\g<1>{loc_str}\g<2>', html)
        # Also direct replace in case of loose inline text
        html = html.replace(f">{en_str}<", f">{loc_str}<")
        html = html.replace(f"<strong>{en_str}</strong>", f"<strong>{loc_str}</strong>")
        html = html.replace(f"<small>{en_str}</small>", f"<small>{loc_str}</small>")

    return html

def build_app_page(app, locale):
    en_index_path = os.path.join(BASE_DIR, app, 'index.html')
    if not os.path.isfile(en_index_path):
        return
        
    with open(en_index_path, 'r', encoding='utf-8') as f:
        html = f.read()

    html = normalize_assets_and_scripts(html, app)
    html = replace_screenshots_for_locale(html, app, locale)
    html = update_seo_metadata(html, app, locale)
    html = update_switcher_and_nav(html, app, locale)
    html = apply_deep_translations(html, app, locale)

    out_dir = os.path.join(BASE_DIR, locale, app)
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, 'index.html')
    
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(html)
        
    print(f"  [DEEP GENERATED] {locale}/{app}/index.html ({len(html)} bytes)")

def main():
    print("=== Generating 100% Deep UI-Parity Localized App Landing Pages ===")
    target_locales = list(LOCALES_META.keys())
    
    for app in APPS:
        print(f"\nProcessing App: {app}")
        for loc in target_locales:
            build_app_page(app, loc)
            
    print("\n=== Generation Finished ===")

if __name__ == '__main__':
    main()
