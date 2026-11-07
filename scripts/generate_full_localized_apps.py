#!/usr/bin/env python3
"""
Generate 100% UI-Parity Deeply-Localized Landing Pages for all 8 apps across 7 target locales:
zh-tw, ja, ko, de, fr, es, it.

Fixes applied:
1. Pure borderless RAW screenshots for Hero Phones to eliminate double-border artifacts across all 7 locales.
2. 100% deep translations of every section (Hero, Floating Badges, Science, Urge Surfing, Recovery Stages, Compare Tables, Features, Bento Grids, Gallery, FAQs in HTML & JSON-LD, Footer).
3. Root-relative asset and hyperlink paths:
   - CSS/JS/images root-relative
   - href="privacy.html" -> href="/{app}/privacy.html"
   - href="terms.html" -> href="/{app}/terms.html"
   - href="support.html" -> href="/{app}/support.html"
   - href="guides/..." -> href="/{app}/guides/..."
   - href="tools/..." -> href="/{app}/tools/..."
   - Brand logo links -> href="/{locale}/"
4. Accurate 8-way alternate hreflang and canonical links.
"""

import os
import re
import copy
from translations_data import LOCALES_META, APP_TRANSLATIONS
from comprehensive_translations import COMMON_DICT, DEEP_APP_CONTENT
from total_translations_data import TOTAL_TRANSLATIONS
from translations_pack_other_apps import OTHER_APPS_TRANSLATIONS
from translations_pack_top_apps import TOP_APPS_TRANSLATIONS
from translations_pack_aft_all import AFT_EXTRA_TRANSLATIONS
from translations_pack_round3_polish import ROUND3_TRANSLATIONS
from complete_final_translations import COMPLETE_FINAL_TRANSLATIONS
from compile_master_translations import COMMON_STRINGS

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

# Build Unified Master Dictionary
MASTER_APP_CONTENT = {}
for source in [DEEP_APP_CONTENT, TOTAL_TRANSLATIONS, OTHER_APPS_TRANSLATIONS, TOP_APPS_TRANSLATIONS, ROUND3_TRANSLATIONS, COMPLETE_FINAL_TRANSLATIONS]:
    for app_slug, locales in source.items():
        if app_slug not in MASTER_APP_CONTENT:
            MASTER_APP_CONTENT[app_slug] = {}
        for loc, dict_items in locales.items():
            if loc not in MASTER_APP_CONTENT[app_slug]:
                MASTER_APP_CONTENT[app_slug][loc] = {}
            MASTER_APP_CONTENT[app_slug][loc].update(dict_items)

# Add AFT Extra translations for ko, de, fr, es, it
for loc, dict_items in AFT_EXTRA_TRANSLATIONS.items():
    if 'alcohol-free-tracker' in MASTER_APP_CONTENT:
        if loc not in MASTER_APP_CONTENT['alcohol-free-tracker']:
            MASTER_APP_CONTENT['alcohol-free-tracker'][loc] = {}
        MASTER_APP_CONTENT['alcohol-free-tracker'][loc].update(dict_items)

# Merge Common Dictionaries
MERGED_COMMON = copy.deepcopy(COMMON_DICT)
for loc, items in COMMON_STRINGS.items():
    if loc not in MERGED_COMMON:
        MERGED_COMMON[loc] = {}
    MERGED_COMMON[loc].update(items)

PATCH_EXTRA = {
    # HTML Entity and apostrophe variations for Alcohol Free Tracker guides
    "An evidence-based timeline detailing how dehydration, vasopressin suppression, and cortisol drive &#x27;alcohol face&#x27;—and the exact days when facial swelling clears.": {
        "zh-tw": "依據實證醫學詳解脫水、抗利尿激素抑制與皮質醇如何引發「酒精臉」浮腫——以及臉部水腫完全消退的確切天數時間軸。",
        "ja": "脱水、バソプレシン抑制、コルチゾールが引き起こす「むくみ顔」のメカニズムと、顔の腫れが引く具体的な日数を示す医学的タイムライン。",
        "ko": "탈수, 바소프레신 억제, 코르티솔이 유발하는 '알코올 부종' 메커니즘과 얼굴 붓기가 완전히 빠지는 구체적인 일차별 회복 타임라인.",
        "de": "Eine evidenzbasierte Zeitleiste, die erklärt, wie Dehydrierung, Vasopressin-Hemmung und Cortisol das 'Alkoholgesicht' verursachen – und wann die Schwellungen abklingen.",
        "fr": "Une chronologie scientifique expliquant comment la déshydratation, l'inhibition de la vasopressine et le cortisol provoquent le 'visage d'alcool' — et quand les gonflements disparaissent.",
        "es": "Una cronología basada en evidencia que detalla cómo la deshidratación, la inhibición de la vasopresina y el cortisol causan la 'cara de alcohol' y en qué días desaparece la hinchazón.",
        "it": "Una cronologia scientifica che spiega come disidratazione, inibizione della vasopressina e cortisolo causano il 'viso da alcol' — e i giorni esatti in cui il gonfiore svanisce."
    },
    "Why your sobriety journey shouldn&#x27;t live on a public server. An in-depth guide to private, offline sobriety tracking without mandatory sign-ups, social guilt, or expensive subscriptions.": {
        "zh-tw": "為什麼你的清醒歷程不該儲存在公開伺服器上。深入解析如何使用無強制註冊、無社交愧疚感、無高昂訂閱費的本機離線隱私戒酒追蹤工具。",
        "ja": "断酒の記録を公開サーバーに置くべきではない理由。強制登録や同調圧力、高額な課金に頼らない、完全ローカル＆プライベートな断酒記録の徹底解説。",
        "ko": "금주 여정이 공개 서버에 저장되어서는 안 되는 이유. 강제 회원가입, 사회적 죄책감, 비싼 구독료 없이 100% 로컬 오프라인으로 기록하는 프라이빗 금주 가이드.",
        "de": "Warum deine Abstinenz nicht auf einem öffentlichen Server liegen sollte: Ein Leitfaden für privates, offlinegeführtes Tracking ohne Kontozwang oder teure Abos.",
        "fr": "Pourquoi votre parcours de sobriété ne devrait pas vivre sur un serveur public : un guide approfondi du suivi privé hors ligne sans compte obligatoire ni abonnement coûteux.",
        "es": "Por qué tu camino hacia la sobriedad no debería estar en un servidor público: una guía completa sobre el seguimiento privado sin conexión, sin registros ni suscripciones caras.",
        "it": "Perché il tuo percorso di sobrietà non dovrebbe risiedere su un server pubblico: una guida approfondita al tracciamento privato offline senza account obbligatorio né abbonamenti costosi."
    },
    "Read guide &rarr;": {
        "zh-tw": "閱讀指南 →",
        "ja": "ガイドを読む →",
        "ko": "가이드 읽기 →",
        "de": "Leitfaden lesen →",
        "fr": "Lire le guide →",
        "es": "Leer la guía →",
        "it": "Leggi la guida →"
    },
    "Read full guide &rarr;": {
        "zh-tw": "閱讀完整指南 →",
        "ja": "ガイド全文を読む →",
        "ko": "가이드 전체 읽기 →",
        "de": "Vollständigen Leitfaden lesen →",
        "fr": "Lire le guide complet →",
        "es": "Leer la guía completa →",
        "it": "Leggi la guida completa →"
    },
    "How to Cure Vaper&#x27;s Tongue Fast: Causes, Reset Protocol &amp; Recovery Timeline": {
        "zh-tw": "如何快速改善電子煙味覺喪失（Vaper's Tongue）：成因、重置指南與恢復時程",
        "ja": "ベイパーズ・タング（味覚障害）を素早く治す方法：原因、リセット手順と回復タイムライン",
        "ko": "베이퍼스 텅(맛 감각 저하) 빠른 회복법: 원인, 리셋 프로토콜 및 타임라인",
        "de": "Vaper's Tongue schnell heilen: Ursachen, Reset-Protokoll & Erholungs-Zeitleiste",
        "fr": "Soigner la langue du vapoteur rapidement : causes, protocole de réinitialisation et chronologie",
        "es": "Cómo curar la lengua de vapeador rápido: causas, protocolo de reinicio y recuperación",
        "it": "Come curare la lingua dello svapatore: cause, protocollo di ripristino e tempi di recupero"
    },
    "A clinical breakdown of why high-potency e-liquids numb your taste buds and olfactory nerves, plus a 5-step rapid reset protocol and 72-hour recovery timeline.": {
        "zh-tw": "臨床剖析高濃度煙油為何麻痺味蕾與嗅覺神經，並提供 5 步驟快速重置方案與 72 小時恢復時間軸。",
        "ja": "高濃度リキッドが味蕾と嗅覚神経を麻痺させる原因を臨床解説。5ステップの早期回復手順と72時間タイムラインを公開。",
        "ko": "고농도 액상이 미각과 후각 신경을 마비시키는 원인에 대한 임상 분석과 5단계 급속 리셋 프로토콜 및 72시간 회복 일정.",
        "de": "Klinische Analyse, warum hochdosierte E-Liquids Geschmacksknospen und Geruchsnerven betäuben, plus 5-Schritte-Reset-Protokoll und 72-Stunden-Zeitleiste.",
        "fr": "Analyse clinique expliquant l'engourdissement des papilles et de l'odorat par les e-liquides, avec protocole de réinitialisation en 5 étapes et chronologie sur 72h.",
        "es": "Análisis clínico de cómo los e-líquidos paralizan papilas gustativas y olfato, más protocolo de reinicio en 5 pasos y cronología de 72 horas.",
        "it": "Analisi clinica del perché i liquidi intorpidiscono papille e nervi olfattivi, più protocollo di reset in 5 fasi e sequenza di 72 ore."
    },
    "Sensory Health · Flavor Fatigue": {
        "zh-tw": "感官健康 · 味覺疲勞",
        "ja": "感覚の健康・フレーバー疲労",
        "ko": "감각 건강 · 미각 피로",
        "de": "Sensorische Gesundheit · Geschmacksermüdung",
        "fr": "Santé sensorielle · Fatigue gustative",
        "es": "Salud sensorial · Fatiga del sabor",
        "it": "Salute sensoriale · Affaticamento gustativo"
    },
    "Unfog THC & T-Break": {
        "zh-tw": "告別腦霧 THC 與耐受度重置",
        "ja": "頭のモヤモヤ解消 THC＆T-Break",
        "ko": "브레인 포그 해소 THC 및 T-Break",
        "de": "Klarheit im Kopf & T-Break",
        "fr": "Clarté mentale & T-Break",
        "es": "Claridad mental y T-Break",
        "it": "Chiarezza mentale e T-Break"
    }
}

for en_str, locs in PATCH_EXTRA.items():
    for loc, trans_str in locs.items():
        if loc not in MERGED_COMMON:
            MERGED_COMMON[loc] = {}
        MERGED_COMMON[loc][en_str] = trans_str

# Hero Floating Badges per locale
HERO_BADGES = {
    "zh-tw": {
        "Deep REM Sleep": "深度 REM 睡眠",
        "Day 7 · restoring": "第 7 天 · 迅速修復中",
        "Brain Fog Clears": "大腦迷霧消散",
        "Day 14 · focus returns": "第 14 天 · 專注力完全回歸",
        "Craving SOS": "衝動急救 SOS",
        "Calm 4-6 PM": "平息傍晚誘因高峰",
        "No third-party tracking": "零第三方追蹤",
        "No account": "無需註冊帳號",
        "No ads": "無廣告干擾",
        "Works offline": "支援離線使用",
    },
    "ja": {
        "Deep REM Sleep": "深いレム睡眠",
        "Day 7 · restoring": "7日目 · 回復進行中",
        "Brain Fog Clears": "脳のモヤが晴れる",
        "Day 14 · focus returns": "14日目 · 集中力回復",
        "Craving SOS": "欲求レスキュー SOS",
        "Calm 4-6 PM": "夕方の波を鎮める",
        "No third-party tracking": "第三者追跡なし",
        "No account": "アカウント不要",
        "No ads": "広告一切なし",
        "Works offline": "オフライン対応",
    },
    "ko": {
        "Deep REM Sleep": "깊은 렘수면",
        "Day 7 · restoring": "7일차 · 회복 진행 중",
        "Brain Fog Clears": "브레인포그 해소",
        "Day 14 · focus returns": "14일차 · 집중력 회복",
        "Craving SOS": "갈망 완화 SOS",
        "Calm 4-6 PM": "퇴근길 유혹 진정",
        "No third-party tracking": "제3자 추적 없음",
        "No account": "계정 가입 불필요",
        "No ads": "광고 없음",
        "Works offline": "오프라인 지원",
    },
    "de": {
        "Deep REM Sleep": "Tiefer REM-Schlaf",
        "Day 7 · restoring": "Tag 7 · erholt sich",
        "Brain Fog Clears": "Gehirnnebel lichtet sich",
        "Day 14 · focus returns": "Tag 14 · Fokus kehrt zurück",
        "Craving SOS": "Verlangen-SOS",
        "Calm 4-6 PM": "Abendliches Verlangen beruhigen",
        "No third-party tracking": "Kein Drittanbieter-Tracking",
        "No account": "Kein Konto",
        "No ads": "Keine Werbung",
        "Works offline": "Offline nutzbar",
    },
    "fr": {
        "Deep REM Sleep": "Sommeil paradoxal profond",
        "Day 7 · restoring": "Jour 7 · en récupération",
        "Brain Fog Clears": "Brouillard mental dissipé",
        "Day 14 · focus returns": "Jour 14 · concentration retrouvée",
        "Craving SOS": "SOS Envie aiguë",
        "Calm 4-6 PM": "Calmer l'envie de fin d'après-midi",
        "No third-party tracking": "Zéro pistage tiers",
        "No account": "Sans compte",
        "No ads": "Sans pub",
        "Works offline": "Fonctionne hors ligne",
    },
    "es": {
        "Deep REM Sleep": "Sueño REM profundo",
        "Day 7 · restoring": "Día 7 · recuperándose",
        "Brain Fog Clears": "Niebla mental disipada",
        "Day 14 · focus returns": "Día 14 · concentración recuperada",
        "Craving SOS": "SOS Deseo intenso",
        "Calm 4-6 PM": "Calmar el pico de la tarde",
        "No third-party tracking": "Sin rastreo de terceros",
        "No account": "Sin cuenta",
        "No ads": "Sin anuncios",
        "Works offline": "Funciona sin conexión",
    },
    "it": {
        "Deep REM Sleep": "Sonno REM profondo",
        "Day 7 · restoring": "Giorno 7 · in ripresa",
        "Brain Fog Clears": "Nebbia mentale svanita",
        "Day 14 · focus returns": "Giorno 14 · concentrazione ritrovata",
        "Craving SOS": "SOS Impulso improvviso",
        "Calm 4-6 PM": "Calma il picco del tardo pomeriggio",
        "No third-party tracking": "Zero tracciamento terzi",
        "No account": "Nessun account",
        "No ads": "Senza pubblicità",
        "Works offline": "Funziona offline",
    }
}

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

def normalize_assets_and_scripts(html, app, locale):
    # CSS and JS assets to root-relative
    html = re.sub(r'href=[\"\']styles\.css[\"\']', f'href="/{app}/styles.css"', html)
    html = re.sub(r'href=[\"\']style\.css[\"\']', f'href="/{app}/style.css"', html)
    html = re.sub(r'src=[\"\']script\.js[\"\']', f'src="/{app}/script.js"', html)
    html = re.sub(r'src=[\"\']scripts/', f'src="/{app}/scripts/', html)
    html = re.sub(r'href=[\"\']assets/', f'href="/{app}/assets/', html)
    html = re.sub(r'src=[\"\']assets/', f'src="/{app}/assets/', html)
    html = re.sub(r'srcset=[\"\']assets/', f'srcset="/{app}/assets/', html)

    # Normalize relative page links to root-relative paths to eliminate 404s in subdirectories
    html = re.sub(r'href=[\"\']privacy\.html[\"\']', f'href="/{app}/privacy.html"', html)
    html = re.sub(r'href=[\"\']terms\.html[\"\']', f'href="/{app}/terms.html"', html)
    html = re.sub(r'href=[\"\']support\.html[\"\']', f'href="/{app}/support.html"', html)
    html = re.sub(r'href=[\"\']guides/index\.html[\"\']', f'href="/{app}/guides/index.html"', html)
    html = re.sub(r'href=[\"\']guides/([^\"]*)[\"\']', rf'href="/{app}/guides/\1"', html)
    html = re.sub(r'href=[\"\']tools/([^\"]*)[\"\']', rf'href="/{app}/tools/\1"', html)

    # Handle brand links in nav or footer
    html = re.sub(r'<a\s+([^>]*\s+)?class=[\"\']brand[\"\']\s+href=[\"\']index\.html[\"\']', f'<a \\1class="brand" href="/{locale}/"', html)
    html = re.sub(r'<a\s+href=[\"\']index\.html[\"\']\s+class=[\"\']brand[\"\']', f'<a href="/{locale}/" class="brand"', html)
    html = re.sub(r'<a\s+([^>]*\s+)?class=[\"\']logo[\"\']\s+href=[\"\']/[\"\']', f'<a \\1class="logo" href="/{locale}/"', html)

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
        if 'hero-today-recovery-raw.webp' in available_files:
            html = re.sub(
                rf'/{app}/assets/screens/hero-today-recovery\.webp',
                f'/{app}/assets/screenshots_localized/{locale}/hero-today-recovery-raw.webp',
                html
            )
        for f in available_files:
            if re.match(r'^\d\d-', f):
                html = re.sub(
                    rf'/{app}/assets/appstore/{re.escape(f)}',
                    f'/{app}/assets/screenshots_localized/{locale}/{f}',
                    html
                )

    elif app == 'alcohol-free-tracker':
        if 'hero-today-raw.webp' in available_files:
            html = re.sub(
                rf'/{app}/assets/screens/06-today-light\.webp',
                f'/{app}/assets/screenshots_localized/{locale}/hero-today-raw.webp',
                html
            )
        for f in available_files:
            if re.match(r'^\d\d-', f):
                html = re.sub(
                    rf'/{app}/assets/appstore/{re.escape(f)}',
                    f'/{app}/assets/screenshots_localized/{locale}/{f}',
                    html
                )

    elif app == 'pill-reminder':
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

    elif app == 'quit-weed':
        if 'hero-today-recovery-raw.webp' in available_files:
            html = re.sub(
                rf'/{app}/assets/screens/hero-today-recovery\.webp',
                f'/{app}/assets/screenshots_localized/{locale}/hero-today-recovery-raw.webp',
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
    # 1. Apply app-specific hero & metadata
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

    # 2. Translate Hero floating badges
    hero_badges = HERO_BADGES.get(locale, {})
    for en_badge, loc_badge in sorted(hero_badges.items(), key=lambda x: -len(x[0])):
        html = html.replace(f">{en_badge}<", f">{loc_badge}<")
        html = html.replace(f"<strong>{en_badge}</strong>", f"<strong>{loc_badge}</strong>")
        html = html.replace(f"<span>{en_badge}</span>", f"<span>{loc_badge}</span>")
        html = html.replace(f"<li>{en_badge}</li>", f"<li>{loc_badge}</li>")

    # 3. Apply global common dictionary
    common = MERGED_COMMON.get(locale, {})
    for en_str, loc_str in sorted(common.items(), key=lambda x: -len(x[0])):
        html = re.sub(rf'>\s*{re.escape(en_str)}\s*<', f'>{loc_str}<', html)

    # 4. Apply App-Specific Deep Master Content (Science, FAQ, Bento, Comparisons, etc.)
    app_dict = MASTER_APP_CONTENT.get(app, {}).get(locale, {})
    
    # Expand dictionary with HTML entity variants (& vs &amp;, quotes)
    expanded_dict = {}
    for en_str, loc_str in app_dict.items():
        expanded_dict[en_str] = loc_str
        if "&" in en_str and "&amp;" not in en_str:
            expanded_dict[en_str.replace("&", "&amp;")] = loc_str
        if "&amp;" in en_str:
            expanded_dict[en_str.replace("&amp;", "&")] = loc_str
        if '"' in en_str:
            expanded_dict[en_str.replace('"', '&quot;')] = loc_str

    # Sort strings longest first to prevent prefix collisions
    for en_str, loc_str in sorted(expanded_dict.items(), key=lambda x: -len(x[0])):
        # Replace inside JSON-LD script strings
        html = html.replace(f'"{en_str}"', f'"{loc_str}"')
        
        # Direct replacements for tags
        html = html.replace(f">{en_str}<", f">{loc_str}<")
        html = html.replace(f"<summary>{en_str}</summary>", f"<summary>{loc_str}</summary>")
        html = html.replace(f"<p>{en_str}</p>", f"<p>{loc_str}</p>")
        html = html.replace(f"<h2>{en_str}</h2>", f"<h2>{loc_str}</h2>")
        html = html.replace(f"<h3>{en_str}</h3>", f"<h3>{loc_str}</h3>")
        html = html.replace(f"<h4>{en_str}</h4>", f"<h4>{loc_str}</h4>")
        html = html.replace(f"<strong>{en_str}</strong>", f"<strong>{loc_str}</strong>")
        html = html.replace(f"<span>{en_str}</span>", f"<span>{loc_str}</span>")
        html = html.replace(f"<li>{en_str}</li>", f"<li>{loc_str}</li>")
        html = html.replace(f"<small>{en_str}</small>", f"<small>{loc_str}</small>")

        # Robust regex pattern for boundary-safe & whitespace-flexible replacements
        words = [re.escape(w) for w in re.split(r'\s+', en_str.strip())]
        if words:
            regex_str = r'\s+'.join(words)
            pattern = re.compile(rf'(>|\"|&nbsp;)\s*{regex_str}\s*(<|\"|&nbsp;)', re.IGNORECASE)
            html = pattern.sub(lambda m: f"{m.group(1)}{loc_str}{m.group(2)}", html)

    return html

def build_app_page(app, locale):
    en_index_path = os.path.join(BASE_DIR, app, 'index.html')
    if not os.path.isfile(en_index_path):
        return
        
    with open(en_index_path, 'r', encoding='utf-8') as f:
        html = f.read()

    html = normalize_assets_and_scripts(html, app, locale)
    html = replace_screenshots_for_locale(html, app, locale)
    html = update_seo_metadata(html, app, locale)
    html = update_switcher_and_nav(html, app, locale)
    html = apply_deep_translations(html, app, locale)

    out_dir = os.path.join(BASE_DIR, locale, app)
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, 'index.html')
    
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(html)
        
    print(f"  [100% DEEP GENERATED] {locale}/{app}/index.html ({len(html)} bytes)")

def main():
    print("=== Generating 100% UI-Parity Deep Localized Landing Pages ===")
    target_locales = list(LOCALES_META.keys())
    
    for app in APPS:
        print(f"\nProcessing App: {app}")
        for loc in target_locales:
            build_app_page(app, loc)
            
    print("\n=== Generation Finished Successfully ===")

if __name__ == '__main__':
    main()
