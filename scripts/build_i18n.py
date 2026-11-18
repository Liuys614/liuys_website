#!/usr/bin/env python3
"""
YS Liu Studio — Comprehensive Multi-Language (i18n) Architecture & Static Generator
Generates full static localized experiences across 7 target languages:
  1. zh-tw (繁體中文 - 台灣/香港, #1 Non-English Market)
  2. de    (Deutsch - 德國/奧地利/瑞士, #1 Levain & Agricola EU Market)
  3. fr    (Français - 法國/加拿大, #1 Inkstone Market)
  4. ja    (日本語 - 日本, 高 ARPU 市場)
  5. ko    (한국어 - 韓國, 付費市場)
  6. es    (Español - 西班牙/智利/拉美)
  7. it    (Italiano - 義大利, Quit Vaping 核心市場)
+ en (Default English / x-default)

Strict SEO compliance:
  • 8-way bidirectional hreflang tags + x-default
  • Localized JSON-LD Schema (SoftwareApplication, Organization)
  • Localized OpenGraph and meta descriptions
  • Responsive UI Language Switcher on all pages
  • Clean root-relative asset URLs (zero image duplication)
  • Localized App Store attribution campaign tokens (?ct=lp_<locale>_hero, see scripts/site_campaign.py)
  • Standard XML sitemap with xhtml:link alternates
"""
import os
import re
import json
from datetime import datetime

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from apps_i18n_data import APPS_I18N

LOCALES = [
    {"code": "en", "dir": "", "name": "English", "html_lang": "en", "og_locale": "en_US"},
    {"code": "zh-tw", "dir": "zh-tw", "name": "繁體中文", "html_lang": "zh-TW", "og_locale": "zh_TW"},
    {"code": "de", "dir": "de", "name": "Deutsch", "html_lang": "de", "og_locale": "de_DE"},
    {"code": "fr", "dir": "fr", "name": "Français", "html_lang": "fr", "og_locale": "fr_FR"},
    {"code": "ja", "dir": "ja", "name": "日本語", "html_lang": "ja", "og_locale": "ja_JP"},
    {"code": "ko", "dir": "ko", "name": "한국어", "html_lang": "ko", "og_locale": "ko_KR"},
    {"code": "es", "dir": "es", "name": "Español", "html_lang": "es", "og_locale": "es_ES"},
    {"code": "it", "dir": "it", "name": "Italiano", "html_lang": "it", "og_locale": "it_IT"},
]

HREFLANG_MAP = {
    "en": "en",
    "zh-tw": "zh-TW",
    "de": "de",
    "fr": "fr",
    "ja": "ja",
    "ko": "ko",
    "es": "es",
    "it": "it",
}

APPS = [
    "agricola-scorer",
    "levain",
    "inkstone",
    "grocery-price",
    "alcohol-free-tracker",
    "quit-vaping",
    "quit-weed",
    "pill-reminder",
]

# Translation dictionaries for Studio Homepage
STUDIO_I18N = {
    "en": {
        "title": "YS Liu Studio — Independent Mobile App Studio",
        "desc": "YS Liu Studio builds fast, privacy-first iOS apps for daily habits, health tracking, document signing, and everyday utility.",
        "og_desc": "Fast, privacy-first native iOS apps for everyday utility.",
        "nav_apps": "Apps",
        "nav_philosophy": "Philosophy",
        "nav_developer": "Developer",
        "nav_support": "Support",
        "nav_btn": "Meet the Developer",
        "pill_est": "Independent App Studio · Est. 2024",
        "hero_title": "Native iOS Apps for Daily Habits, Health, and Utility",
        "hero_desc": "<strong>YS Liu Studio</strong> builds native, offline-ready iOS apps for habit tracking, document signing, and daily utilities, with local storage and no ads or tracking.",
        "hero_btn_explore": "Explore Our Apps",
        "hero_btn_about": "About Louis Liu (Founder)",
        "dock_label": "6 apps live on the App Store",
        "marquee_native": "Native iOS performance",
        "marquee_privacy": "Privacy-first storage",
        "marquee_ux": "Simple, focused UX",
        "marquee_ai": "On-device processing",
        "marquee_accessible": "Accessible by design",
        "marquee_global": "40+ App Store storefronts",
        "marquee_offline": "Offline-first reliability",
        "pillar1_num": "01",
        "pillar1_title": "Fewer steps per task",
        "pillar1_desc": "Clear visual hierarchy, haptics, and VoiceOver support cut out unnecessary modals so everyday tasks take fewer taps.",
        "pillar2_num": "02",
        "pillar2_title": "Privacy and on-device storage",
        "pillar2_desc": "Your health logs, contracts, and habit records stay yours. Apps use on-device OCR, local storage, and encrypted signing links without ad trackers.",
        "pillar3_num": "03",
        "pillar3_title": "Native Swift architecture",
        "pillar3_desc": "Built with modern Swift concurrency, local persistence, and native iOS platform conventions for dependable everyday use.",
        "apps_pill": "Product suite",
        "apps_headline": "Apps by YS Liu Studio",
        "apps_sub": "Explore our lineup of native applications. Click any screenshot to inspect the interface in full resolution.",
        "btn_appstore": "View on App Store",
        "guides_pill": "Reference guides",
        "guides_headline": "Health, Habit &amp; Utility Guides",
        "guides_sub": "Reference guides and general timelines grounded in published research, alongside practical how-tos for our utility apps.",
        "guide1_desc": "Guides on cutting back or stopping alcohol, general recovery timelines, sleep disruption research, and urge-surfing strategies.",
        "guide1_l1": "30-Day Dry Challenge Guide",
        "guide1_l2": "Alcohol Recovery Timeline Overview",
        "guide1_l3": "Coping With Evening Alcohol Cravings: Urge Surfing",
        "guide1_l4": "Alcohol and Sleep Disruption: What Research Shows",
        "guide1_more": "View all Alcohol-Free Guides &rarr;",
        "guide2_desc": "Cannabis withdrawal overview, CB1 receptor recovery over about 4 weeks, early abstinence sleep changes, and paced breathing.",
        "guide2_l1": "Cannabis Withdrawal and CB1 Receptor Recovery",
        "guide2_l2": "Sleep Disturbance After Stopping Cannabis",
        "guide2_l3": "4-7-8 Paced Breathing for Cannabis Cravings",
        "guide2_more": "View all Quit Weed Guides &rarr;",
        "guide3_desc": "Nicotine withdrawal timeline (peaking in week 1 and easing over 2–4 weeks), urge-surfing basics, and pod spending math.",
        "guide3_l1": "Nicotine Withdrawal Timeline: What to Expect",
        "guide3_l2": "Urge Surfing for Acute Nicotine Cravings",
        "guide3_more": "View all Quit Vaping Guides &rarr;",
        "guide4_desc": "Supplement timing basics, meal absorption notes, medication interaction checks, and missed-dose reference guides.",
        "guide4_l1": "When to Take Magnesium Glycinate",
        "guide4_l2": "Vitamin &amp; Supplement Timing Guide",
        "guide4_more": "View all Pill Reminder Guides &rarr;",
        "guide5_desc": "Unit price formulas, package shrinkflation detection, and smart supermarket inflation shopping guides.",
        "guide5_l1": "How to Calculate Price per Ounce &amp; Gram",
        "guide5_l2": "Unit Cost &amp; Supermarket Math Guides",
        "guide5_more": "View all Smart Grocery Guides &rarr;",
        "guide6_desc": "Baker's percentage formulas, sourdough hydration scaling, and temperature-adjusted fermentation timing.",
        "guide6_l1": "Sourdough Hydration Calculator &amp; Percentages",
        "guide6_l2": "Bulk Fermentation &amp; Starter Feeding Charts",
        "guide6_more": "View all Sourdough Guides &rarr;",
        "guide7_desc": "Mobile contract signing, subscription-free eSign workflows, and browser link signature sharing.",
        "guide7_l1": "Sign PDF on iPhone Without Subscription",
        "guide7_l2": "Mobile eSign &amp; Contract Workflows",
        "guide7_more": "View all PDF Signing Guides &rarr;",
        "guide8_desc": "End-game victory point rules, harvest food engines, room upgrades, and begging card penalty math.",
        "guide8_l1": "Agricola Scoring Rules &amp; Point Calculations",
        "guide8_l2": "Harvest Food Engine &amp; Strategy Guides",
        "guide8_more": "View all Agricola Guides &rarr;",
        "guides_source_note": "Sources: Health and habit guides reference NIAAA, CDC, Smokefree.gov, NIH Office of Dietary Supplements, Hirvonen et al. (2012), Hughes (2007), Ebrahim et al. (2013), and Bowen &amp; Marlatt (2009). Educational information only, not medical advice.",
        "founder_eyebrow": "Behind the studio",
        "founder_title": "Engineered by Louis Liu",
        "founder_bio": "Senior Mobile Software Engineer with a background in streaming media at scale, compiler acceleration, and embedded systems.",
        "founder_btn": "View Engineer Profile & Resume",
        "contact_heading": "App Support &<br />Studio Inquiries",
        "contact_lead": "Have feedback on one of our apps, need customer support, or want to collaborate? Reach out directly anytime.",
        "btn_email": "Email Support",
        "btn_copy": "Copy Email",
        "footer_rights": "Copyright © 2026 YS Liu Studio. All Rights Reserved.",
        "footer_alcohol_free": "Alcohol-Free",
        "footer_quit_weed": "Quit Weed",
        "footer_quit_vaping": "Quit Vaping",
        "footer_sourdough": "Sourdough",
        "footer_back_top": "Back to Top",
        "lightbox_hint": "Use <kbd>←</kbd> <kbd>→</kbd> arrow keys to navigate, <kbd>Esc</kbd> to exit.",
        "toast_copied": "Email copied to clipboard",
    },
    "zh-tw": {
        "title": "YS Liu Studio — 獨立行動應用工作室",
        "desc": "YS Liu Studio 開發快速、重視隱私的 iOS 應用程式，涵蓋日常習慣、健康追蹤、文件簽署與生活實用工具。",
        "og_desc": "快速、重視隱私的原生 iOS 日常實用工具。",
        "nav_apps": "應用程式",
        "nav_philosophy": "設計理念",
        "nav_developer": "開發者",
        "nav_support": "支援",
        "nav_btn": "認識開發者",
        "pill_est": "獨立 App 工作室 · 創立於 2024",
        "hero_title": "專為日常習慣、健康與實用需求打造的原生 iOS 應用",
        "hero_desc": "<strong>YS Liu Studio</strong> 開發原生且可離線使用的 iOS 應用程式，涵蓋習慣追蹤、文件簽署與日常工具，資料儲存於本機，無廣告也無追蹤程式。",
        "hero_btn_explore": "瀏覽應用程式",
        "hero_btn_about": "關於創辦人 Louis Liu",
        "dock_label": "6 款 App 已於 App Store 上架",
        "marquee_native": "原生 iOS 效能",
        "marquee_privacy": "隱私優先的資料儲存",
        "marquee_ux": "簡潔專注的使用體驗",
        "marquee_ai": "裝置端本機運算",
        "marquee_accessible": "無障礙設計",
        "marquee_global": "支援 40+ 個 App Store 地區",
        "marquee_offline": "離線優先的穩定運作",
        "pillar1_num": "01",
        "pillar1_title": "減少每項任務的操作步驟",
        "pillar1_desc": "清晰的視覺層級、觸覺回饋與旁白支援，省去多餘彈窗，讓日常操作只需更少點擊即可完成。",
        "pillar2_num": "02",
        "pillar2_title": "隱私保護與裝置端儲存",
        "pillar2_desc": "您的健康紀錄、合約文件與習慣資料皆歸您所有。應用程式採用裝置端 OCR、本機儲存與加密簽署連結，不含廣告追蹤器。",
        "pillar3_num": "03",
        "pillar3_title": "原生 Swift 軟體架構",
        "pillar3_desc": "採用現代 Swift 並行處理、本機資料持久化與原生 iOS 平台規範打造，提供穩定可靠的日常使用體驗。",
        "apps_pill": "產品系列",
        "apps_headline": "YS Liu Studio 應用程式",
        "apps_sub": "瀏覽原生應用程式系列，點擊任一螢幕截圖即可檢視完整解析度介面。",
        "btn_appstore": "前往 App Store",
        "guides_pill": "參考指南",
        "guides_headline": "健康、習慣與實用工具指南",
        "guides_sub": "彙整基於公開研究的一般參考指南與時間軸，以及旗下實用工具的實作說明。",
        "guide1_desc": "減量或停酒的參考指南、一般生理恢復時間軸、睡眠干擾研究摘要，以及衝動衝浪應對方法。",
        "guide1_l1": "30 天無酒精挑戰指南",
        "guide1_l2": "停酒後的生理恢復時間軸概覽",
        "guide1_l3": "應對傍晚飲酒渴望：衝動衝浪練習",
        "guide1_l4": "酒精與睡眠干擾：研究觀察整理",
        "guide1_more": "查看所有無酒精指南 &rarr;",
        "guide2_desc": "大麻戒斷反應概覽、約 4 週的 CB1 受體恢復過程、停用初期睡眠變化，以及節律呼吸法。",
        "guide2_l1": "大麻戒斷與 CB1 受體恢復",
        "guide2_l2": "停用大麻後的睡眠變化",
        "guide2_l3": "4-7-8 節律呼吸法應對大麻渴望",
        "guide2_more": "查看所有戒大麻指南 &rarr;",
        "guide3_desc": "尼古丁戒斷時間軸（第 1 週達高峰，2 至 4 週內逐步緩和）、衝動衝浪基礎，以及煙彈花費試算。",
        "guide3_l1": "尼古丁戒斷時間軸：常見過程說明",
        "guide3_l2": "以衝動衝浪應對急性尼古丁渴望",
        "guide3_more": "查看所有戒電子煙指南 &rarr;",
        "guide4_desc": "保健品補充時段基礎、隨餐吸收注意事項、藥物交互作用查核，以及漏服時的參考指引。",
        "guide4_l1": "甘胺酸鎂適合什麼時候補充",
        "guide4_l2": "維他命與保健品補充時間指南",
        "guide4_more": "查看所有用藥提醒指南 &rarr;",
        "guide5_desc": "單位價格計算公式、包裝縮水辨識方法，以及超市比價防通膨採購指南。",
        "guide5_l1": "如何計算每盎司與每公克單價",
        "guide5_l2": "單位成本與超市比價計算指南",
        "guide5_more": "查看所有超市比價指南 &rarr;",
        "guide6_desc": "烘焙百分比公式、酸種含水率換算，以及依室溫調整的發酵時間計算。",
        "guide6_l1": "酸種含水率計算器與百分比說明",
        "guide6_l2": "基礎發酵與酵種餵養對照表",
        "guide6_more": "查看所有酸種烘焙指南 &rarr;",
        "guide7_desc": "手機合約簽署、免訂閱電子簽名流程，以及透過瀏覽器連結分享簽署。",
        "guide7_l1": "免訂閱在 iPhone 上簽署 PDF",
        "guide7_l2": "行動電子簽名與合約處理流程",
        "guide7_more": "查看所有 PDF 簽署指南 &rarr;",
        "guide8_desc": "終局計分規則、收成供食機制、房屋升級與乞討卡扣分計算。",
        "guide8_l1": "農家樂計分規則與分數計算",
        "guide8_l2": "收成供食與對局策略指南",
        "guide8_more": "查看所有農家樂指南 &rarr;",
        "guides_source_note": "資料來源：健康與習慣指南參考 NIAAA、CDC、Smokefree.gov、NIH Office of Dietary Supplements、Hirvonen et al. (2012)、Hughes (2007)、Ebrahim et al. (2013) 與 Bowen &amp; Marlatt (2009)。僅供一般參考資訊，不構成醫療建議。",
        "founder_eyebrow": "關於工作室",
        "founder_title": "由 Louis Liu 開發",
        "founder_bio": "資深行動軟體工程師，具備大規模影音串流、編譯器加速與嵌入式系統開發經驗。",
        "founder_btn": "檢視工程師檔案與履歷",
        "contact_heading": "應用程式支援與<br />工作室洽詢",
        "contact_lead": "對應用程式有任何回饋、需要協助或討論合作，歡迎隨時直接聯繫。",
        "btn_email": "寄信聯繫支援",
        "btn_copy": "複製 Email",
        "footer_rights": "版權所有 © 2026 YS Liu Studio。保留一切權利。",
        "footer_alcohol_free": "無酒精",
        "footer_quit_weed": "戒大麻",
        "footer_quit_vaping": "戒電子煙",
        "footer_sourdough": "酸種麵包",
        "footer_back_top": "回到頂部",
        "lightbox_hint": "使用 <kbd>←</kbd> <kbd>→</kbd> 方向鍵切換，按 <kbd>Esc</kbd> 關閉。",
        "toast_copied": "已複製電子郵件地址",
    },
    "de": {
        "title": "YS Liu Studio — Unabhängiges Mobile-App-Studio",
        "desc": "YS Liu Studio entwickelt schnelle, datenschutzorientierte iOS-Apps für tägliche Gewohnheiten, Gesundheits-Tracking, Dokumentensignatur und den Alltag.",
        "og_desc": "Schnelle, datenschutzorientierte native iOS-Apps für den Alltag.",
        "nav_apps": "Apps",
        "nav_philosophy": "Philosophie",
        "nav_developer": "Entwickler",
        "nav_support": "Support",
        "nav_btn": "Entwickler kennenlernen",
        "pill_est": "Unabhängiges App-Studio · Gegründet 2024",
        "hero_title": "Native iOS-Apps für tägliche Gewohnheiten, Gesundheit und Alltag",
        "hero_desc": "<strong>YS Liu Studio</strong> entwickelt native, offlinefähige iOS-Apps für Gewohnheitstracking, Dokumentensignatur und Alltagshelfer – mit lokaler Speicherung, ohne Werbung oder Tracking.",
        "hero_btn_explore": "Apps entdecken",
        "hero_btn_about": "Über Louis Liu (Gründer)",
        "dock_label": "6 Apps live im App Store",
        "marquee_native": "Native iOS-Leistung",
        "marquee_privacy": "Datenschutzfreundliche Speicherung",
        "marquee_ux": "Schlichte, fokussierte UX",
        "marquee_ai": "Verarbeitung auf dem Gerät",
        "marquee_accessible": "Barrierefrei gestaltet",
        "marquee_global": "40+ App Store-Länder",
        "marquee_offline": "Offline-first-Zuverlässigkeit",
        "pillar1_num": "01",
        "pillar1_title": "Weniger Schritte pro Aufgabe",
        "pillar1_desc": "Klare visuelle Hierarchie, Haptik und VoiceOver-Unterstützung vermeiden unnötige Dialoge, sodass Alltagsaufgaben weniger Tipps erfordern.",
        "pillar2_num": "02",
        "pillar2_title": "Datenschutz und lokale Speicherung",
        "pillar2_desc": "Ihre Gesundheitsprotokolle, Verträge und Gewohnheitsdaten bleiben bei Ihnen. Die Apps nutzen On-Device-OCR, lokale Speicherung und verschlüsselte Signaturlinks ohne Werbetracker.",
        "pillar3_num": "03",
        "pillar3_title": "Native Swift-Architektur",
        "pillar3_desc": "Entwickelt mit moderner Swift-Concurrency, lokaler Persistenz und nativen iOS-Konventionen für den zuverlässigen täglichen Einsatz.",
        "apps_pill": "Produktübersicht",
        "apps_headline": "Apps von YS Liu Studio",
        "apps_sub": "Entdecken Sie unsere nativen Apps. Klicken Sie auf Screenshots, um das Interface hochauflösend zu betrachten.",
        "btn_appstore": "Im App Store ansehen",
        "guides_pill": "Ratgeber & Leitfäden",
        "guides_headline": "Gesundheits-, Gewohnheits- &amp; Alltagsleitfäden",
        "guides_sub": "Nachschlagewerke und allgemeine Zeitpläne auf Basis veröffentlichter Forschung sowie praktische Anleitungen für unsere Utility-Apps.",
        "guide1_desc": "Leitfäden zum Reduzieren oder Beenden von Alkohol, allgemeine Erholungszeitpläne, Forschung zu Schlafstörungen und Urge-Surfing-Strategien.",
        "guide1_l1": "30-Tage-Verzichts-Leitfaden",
        "guide1_l2": "Überblick über den Erholungszeitplan",
        "guide1_l3": "Abendliches Alkoholverlangen bewältigen: Urge Surfing",
        "guide1_l4": "Alkohol und Schlafstörungen: Was die Forschung zeigt",
        "guide1_more": "Alle Leitfäden zum Alkoholverzicht &rarr;",
        "guide2_desc": "Überblick über Cannabisentzug, CB1-Rezeptor-Erholung über etwa 4 Wochen, Schlafveränderungen zu Beginn und ruhige Atemtechnik.",
        "guide2_l1": "Cannabisentzug und CB1-Rezeptor-Erholung",
        "guide2_l2": "Schlafstörungen nach dem Absetzen von Cannabis",
        "guide2_l3": "4-7-8-Atemtechnik bei Cannabisverlangen",
        "guide2_more": "Alle Leitfäden zum Cannabis-Ausstieg &rarr;",
        "guide3_desc": "Nikotinentzugs-Zeitplan (Höhepunkt in Woche 1, Abklingen über 2–4 Wochen), Urge-Surfing-Grundlagen und Pod-Kostenrechnung.",
        "guide3_l1": "Nikotinentzugs-Zeitplan: Was zu erwarten ist",
        "guide3_l2": "Urge Surfing bei akutem Nikotinverlangen",
        "guide3_more": "Alle Leitfäden zum Vape-Ausstieg &rarr;",
        "guide4_desc": "Grundlagen zum Einnahmezeitpunkt, Hinweise zur Aufnahme mit Mahlzeiten, Wechselwirkungs-Checks und Ratgeber bei vergessener Dosis.",
        "guide4_l1": "Wann Magnesiumglycinat einnehmen",
        "guide4_l2": "Ratgeber für Vitamin- &amp; Supplement-Zeiten",
        "guide4_more": "Alle Pill-Reminder-Leitfäden &rarr;",
        "guide5_desc": "Grundpreisformeln, Erkennung von Shrinkflation und Einkaufsratgeber gegen Supermarkt-Inflation.",
        "guide5_l1": "Preis pro Unze &amp; Gramm berechnen",
        "guide5_l2": "Leitfäden zu Stückkosten &amp; Supermarkt-Rechnen",
        "guide5_more": "Alle Einkaufsleitfäden ansehen &rarr;",
        "guide6_desc": "Bäckerprozent-Formeln, Sauerteig-Hydratationsskalierung und temperaturangepasste Gärzeiten.",
        "guide6_l1": "Sauerteig-Hydratationsrechner &amp; Prozente",
        "guide6_l2": "Stockgare- &amp; Anstellgut-Fütterungstabellen",
        "guide6_more": "Alle Sauerteig-Leitfäden ansehen &rarr;",
        "guide7_desc": "Mobiles Vertragssignieren, abo-freie eSign-Abläufe und Teilen von Browser-Signaturlinks.",
        "guide7_l1": "PDF auf dem iPhone ohne Abo signieren",
        "guide7_l2": "Mobile eSign- &amp; Vertrags-Workflows",
        "guide7_more": "Alle Leitfäden zum PDF-Signieren &rarr;",
        "guide8_desc": "Endspiel-Siegpunkteregeln, Ernte-Nahrungsversorgung, Hausausbauten und Betteleikarten-Abzüge.",
        "guide8_l1": "Agricola-Wertungsregeln &amp; Punkteberechnung",
        "guide8_l2": "Ernte-Versorgungs- &amp; Strategieleitfäden",
        "guide8_more": "Alle Agricola-Leitfäden ansehen &rarr;",
        "guides_source_note": "Quellen: Gesundheits- und Gewohnheitsleitfäden stützen sich auf NIAAA, CDC, Smokefree.gov, NIH Office of Dietary Supplements, Hirvonen et al. (2012), Hughes (2007), Ebrahim et al. (2013) und Bowen &amp; Marlatt (2009). Nur zu Informationszwecken, keine medizinische Beratung.",
        "founder_eyebrow": "Hinter dem Studio",
        "founder_title": "Entwickelt von Louis Liu",
        "founder_bio": "Senior Mobile Software Engineer mit Hintergrund in Streaming-Architekturen, Compiler-Optimierung und Embedded Systems.",
        "founder_btn": "Profil & Lebenslauf ansehen",
        "contact_heading": "Support &<br />Studio-Anfragen",
        "contact_lead": "Haben Sie Feedback, benötigen Support oder möchten zusammenarbeiten? Schreiben Sie uns jederzeit direkt.",
        "btn_email": "Support per E-Mail",
        "btn_copy": "E-Mail kopieren",
        "footer_rights": "Copyright © 2026 YS Liu Studio. Alle Rechte vorbehalten.",
        "footer_alcohol_free": "Alkoholfrei",
        "footer_quit_weed": "Cannabis-Ausstieg",
        "footer_quit_vaping": "Vape-Ausstieg",
        "footer_sourdough": "Sauerteig",
        "footer_back_top": "Nach oben",
        "lightbox_hint": "Mit <kbd>←</kbd> <kbd>→</kbd> navigieren, mit <kbd>Esc</kbd> schließen.",
        "toast_copied": "E-Mail-Adresse in die Zwischenablage kopiert",
    },
    "fr": {
        "title": "YS Liu Studio — Studio Indépendant d'Applications Mobiles",
        "desc": "YS Liu Studio développe des applications iOS rapides et respectueuses de la vie privée pour les habitudes quotidiennes, le suivi de santé, la signature de documents et les utilitaires du quotidien.",
        "og_desc": "Des applications iOS natives, rapides et respectueuses de la vie privée pour le quotidien.",
        "nav_apps": "Applications",
        "nav_philosophy": "Philosophie",
        "nav_developer": "Développeur",
        "nav_support": "Assistance",
        "nav_btn": "Rencontrer le développeur",
        "pill_est": "Studio d'Apps Indépendant · Fondé en 2024",
        "hero_title": "Applications iOS natives pour les habitudes, la santé et le quotidien",
        "hero_desc": "<strong>YS Liu Studio</strong> conçoit des applications iOS natives utilisables hors ligne pour le suivi d'habitudes, la signature de documents et les outils du quotidien, avec stockage local, sans publicité ni suivi.",
        "hero_btn_explore": "Découvrir nos applications",
        "hero_btn_about": "À propos de Louis Liu",
        "dock_label": "6 applications disponibles sur l'App Store",
        "marquee_native": "Performance iOS native",
        "marquee_privacy": "Stockage respectueux de la vie privée",
        "marquee_ux": "UX simple et ciblée",
        "marquee_ai": "Traitement sur l'appareil",
        "marquee_accessible": "Conçu pour l'accessibilité",
        "marquee_global": "40+ pays sur l'App Store",
        "marquee_offline": "Fiabilité hors ligne prioritaire",
        "pillar1_num": "01",
        "pillar1_title": "Moins d'étapes par tâche",
        "pillar1_desc": "Une hiérarchie visuelle claire, le retour haptique et la prise en charge de VoiceOver suppriment les fenêtres inutiles pour accomplir vos tâches en moins de gestes.",
        "pillar2_num": "02",
        "pillar2_title": "Vie privée et stockage sur l'appareil",
        "pillar2_desc": "Vos journaux de santé, contrats et suivis d'habitudes restent les vôtres. Les apps utilisent l'OCR sur l'appareil, le stockage local et des liens de signature chiffrés, sans traceurs publicitaires.",
        "pillar3_num": "03",
        "pillar3_title": "Architecture Swift native",
        "pillar3_desc": "Conçu avec la concurrence Swift moderne, la persistance locale et les conventions natives d'iOS pour une utilisation quotidienne fiable.",
        "apps_pill": "Suite d'applications",
        "apps_headline": "Applications par YS Liu Studio",
        "apps_sub": "Explorez nos applications natives. Cliquez sur une capture pour voir l'interface en haute résolution.",
        "btn_appstore": "Voir sur l'App Store",
        "guides_pill": "Guides de référence",
        "guides_headline": "Guides Santé, Habitudes et Utilitaires",
        "guides_sub": "Guides de référence et repères chronologiques généraux appuyés sur des études publiées, ainsi que des modes d'emploi pratiques pour nos applications utilitaires.",
        "guide1_desc": "Guides pour réduire ou arrêter l'alcool, repères généraux de récupération, études sur le sommeil et techniques de gestion des envies (urge surfing).",
        "guide1_l1": "Guide du défi 30 jours sans alcool",
        "guide1_l2": "Aperçu du calendrier de récupération",
        "guide1_l3": "Gérer les envies du soir : la méthode urge surfing",
        "guide1_l4": "Alcool et perturbations du sommeil : ce que montrent les études",
        "guide1_more": "Voir tous les guides sans alcool &rarr;",
        "guide2_desc": "Aperçu du sevrage cannabique, récupération des récepteurs CB1 sur environ 4 semaines, changements du sommeil au début et respiration rythmée.",
        "guide2_l1": "Sevrage cannabique et récupération des récepteurs CB1",
        "guide2_l2": "Troubles du sommeil après l'arrêt du cannabis",
        "guide2_l3": "Respiration rythmée 4-7-8 contre les envies de cannabis",
        "guide2_more": "Voir tous les guides d'arrêt du cannabis &rarr;",
        "guide3_desc": "Chronologie du sevrage nicotinique (pic la semaine 1, diminution sur 2–4 semaines), bases de l'urge surfing et calcul du coût des pods.",
        "guide3_l1": "Chronologie du sevrage nicotinique : à quoi s'attendre",
        "guide3_l2": "Urge surfing pour les envies aiguës de nicotine",
        "guide3_more": "Voir tous les guides d'arrêt de la vape &rarr;",
        "guide4_desc": "Bases du moment de prise des compléments, absorption avec les repas, vérification des interactions et repères en cas d'oubli.",
        "guide4_l1": "Quand prendre le glycinate de magnésium",
        "guide4_l2": "Guide des horaires de vitamines et compléments",
        "guide4_more": "Voir tous les guides Pill Reminder &rarr;",
        "guide5_desc": "Formules de prix unitaire, détection de la réduflation et guides d'achat face à l'inflation en supermarché.",
        "guide5_l1": "Comment calculer le prix par once et par gramme",
        "guide5_l2": "Guides de coût unitaire et calculs en supermarché",
        "guide5_more": "Voir tous les guides courses &rarr;",
        "guide6_desc": "Formules de pourcentage boulanger, calcul d'hydratation du levain et temps de fermentation ajustés à la température.",
        "guide6_l1": "Calculateur d'hydratation du levain et pourcentages",
        "guide6_l2": "Tableaux de fermentation en masse et rafraîchi du levain",
        "guide6_more": "Voir tous les guides pain au levain &rarr;",
        "guide7_desc": "Signature de contrats sur mobile, flux de signature électronique sans abonnement et partage de liens de signature par navigateur.",
        "guide7_l1": "Signer un PDF sur iPhone sans abonnement",
        "guide7_l2": "Flux de signature électronique mobile et contrats",
        "guide7_more": "Voir tous les guides de signature PDF &rarr;",
        "guide8_desc": "Règles de points de victoire en fin de partie, moteurs de nourriture aux récoltes, améliorations de pièces et pénalités de mendicité.",
        "guide8_l1": "Règles de score et calcul des points à Agricola",
        "guide8_l2": "Guides de gestion de nourriture aux récoltes et stratégie",
        "guide8_more": "Voir tous les guides Agricola &rarr;",
        "guides_source_note": "Sources : les guides santé et habitudes s'appuient sur NIAAA, CDC, Smokefree.gov, NIH Office of Dietary Supplements, Hirvonen et al. (2012), Hughes (2007), Ebrahim et al. (2013) et Bowen &amp; Marlatt (2009). Information à titre éducatif uniquement, ne constitue pas un avis médical.",
        "founder_eyebrow": "Le Fondateur",
        "founder_title": "Développé par Louis Liu",
        "founder_bio": "Ingénieur logiciel mobile senior, spécialiste du streaming à grande échelle, des compilateurs et des systèmes natifs.",
        "founder_btn": "Voir le profil et CV",
        "contact_heading": "Assistance &<br />Contact Studio",
        "contact_lead": "Une question, un retour ou une proposition de collaboration ? Écrivez-nous à tout moment.",
        "btn_email": "Contacter le support",
        "btn_copy": "Copier l'e-mail",
        "footer_rights": "Copyright © 2026 YS Liu Studio. Tous droits réservés.",
        "footer_alcohol_free": "Sans alcool",
        "footer_quit_weed": "Arrêt cannabis",
        "footer_quit_vaping": "Arrêt vape",
        "footer_sourdough": "Levain",
        "footer_back_top": "Haut de page",
        "lightbox_hint": "Utilisez les flèches <kbd>←</kbd> <kbd>→</kbd> pour naviguer, <kbd>Esc</kbd> pour quitter.",
        "toast_copied": "Adresse e-mail copiée dans le presse-papiers",
    },
    "ja": {
        "title": "YS Liu Studio — 独立系モバイルアプリスタジオ",
        "desc": "YS Liu Studio は、日々の習慣管理、健康記録、書類署名、日常ユーティリティ向けの高速でプライバシー重視の iOS アプリを開発しています。",
        "og_desc": "日常使いに最適な、高速でプライバシー重視のネイティブ iOS アプリ。",
        "nav_apps": "アプリ",
        "nav_philosophy": "設計思想",
        "nav_developer": "開発者",
        "nav_support": "サポート",
        "nav_btn": "開発者について",
        "pill_est": "インディーアプリスタジオ · 2024年設立",
        "hero_title": "日々の習慣、健康管理、実用ツールのためのネイティブ iOS アプリ",
        "hero_desc": "<strong>YS Liu Studio</strong> は、習慣記録、書類署名、日常ツール向けのオフライン対応ネイティブ iOS アプリを開発しています。データは端末内に保存され、広告やトラッキングはありません。",
        "hero_btn_explore": "アプリを見る",
        "hero_btn_about": "創業者 Louis Liu について",
        "dock_label": "App Store で配信中の 6 つのアプリ",
        "marquee_native": "ネイティブ iOS の動作性能",
        "marquee_privacy": "プライバシー優先のデータ保存",
        "marquee_ux": "シンプルで集中できる UX",
        "marquee_ai": "オンデバイス処理",
        "marquee_accessible": "アクセシビリティ配慮設計",
        "marquee_global": "40 以上の App Store 地域に対応",
        "marquee_offline": "オフライン優先の安定性",
        "pillar1_num": "01",
        "pillar1_title": "作業ごとのステップ数を削減",
        "pillar1_desc": "明確な視覚階層、触覚フィードバック、VoiceOver 対応により不要なモーダルを省き、日々の操作を少ないタップで完了できます。",
        "pillar2_num": "02",
        "pillar2_title": "プライバシーと端末内保存",
        "pillar2_desc": "健康記録や契約書、習慣ログはご自身のものとして守られます。端末内 OCR、ローカル保存、暗号化署名リンクを使用し、広告トラッカーは含みません。",
        "pillar3_num": "03",
        "pillar3_title": "ネイティブ Swift アーキテクチャ",
        "pillar3_desc": "最新の Swift Concurrency、ローカル永続化、iOS ネイティブの設計規範に基づいて構築され、毎日の安定した利用を支えます。",
        "apps_pill": "プロダクト一覧",
        "apps_headline": "YS Liu Studio のアプリ",
        "apps_sub": "ネイティブアプリのラインナップをご覧ください。スクリーンショットをクリックすると高解像度で表示できます。",
        "btn_appstore": "App Store で見る",
        "guides_pill": "リファレンスガイド",
        "guides_headline": "健康・習慣・実用ツールガイド",
        "guides_sub": "公開研究に基づく一般的な参考ガイドと回復の目安に加え、各ユーティリティアプリの実用的な使い方をまとめています。",
        "guide1_desc": "飲酒量の見直しや断酒に関するガイド、一般的な回復の目安、睡眠への影響に関する研究、衝動をやり過ごす（アージサーフィン）方法。",
        "guide1_l1": "30 日間禁酒チャレンジガイド",
        "guide1_l2": "断酒後の回復タイムライン概要",
        "guide1_l3": "夕方の飲酒欲求への対処：アージサーフィン",
        "guide1_l4": "アルコールと睡眠の乱れ：研究が示すこと",
        "guide1_more": "すべての禁酒ガイドを見る &rarr;",
        "guide2_desc": "大麻離脱症状の概要、約 4 週間での CB1 受容体の回復、断絶初期の睡眠変化、ペース呼吸法。",
        "guide2_l1": "大麻離脱と CB1 受容体の回復",
        "guide2_l2": "大麻中止後の睡眠の乱れ",
        "guide2_l3": "大麻への渇望に対処する 4-7-8 ペース呼吸法",
        "guide2_more": "すべての大麻離脱ガイドを見る &rarr;",
        "guide3_desc": "ニコチン離脱の経過（1 週目にピークを迎え、2〜4 週間で軽減）、アージサーフィンの基本、ポッド費用の計算。",
        "guide3_l1": "ニコチン離脱の経過：想定される変化",
        "guide3_l2": "急なニコチン渇望へのアージサーフィン",
        "guide3_more": "すべての脱ベイプガイドを見る &rarr;",
        "guide4_desc": "サプリメント摂取タイミングの基本、食事との吸収メモ、薬の飲み合わせ確認、飲み忘れ時の参考ガイド。",
        "guide4_l1": "グリシン酸マグネシウムを摂るタイミング",
        "guide4_l2": "ビタミン・サプリメント摂取タイミングガイド",
        "guide4_more": "すべてのお薬リマインダーガイドを見る &rarr;",
        "guide5_desc": "単価計算の計算式、ステルス値上げ（容量減少）の見分け方、スーパーでの買い物ガイド。",
        "guide5_l1": "オンス・グラム単価の計算方法",
        "guide5_l2": "単位コストとスーパーでの価格計算ガイド",
        "guide5_more": "すべてのスーパー単価ガイドを見る &rarr;",
        "guide6_desc": "ベーカーズパーセントの計算式、サワードウの加水率調整、温度に応じた発酵時間の目安。",
        "guide6_l1": "サワードウ加水率計算機＆パーセント解説",
        "guide6_l2": "一次発酵とスターター種継ぎチャート",
        "guide6_more": "すべてのサワードウガイドを見る &rarr;",
        "guide7_desc": "モバイルでの契約書署名、サブスク不要の電子署名フロー、ブラウザ署名リンク共有。",
        "guide7_l1": "サブスクなしで iPhone 上で PDF に署名する方法",
        "guide7_l2": "モバイル電子署名と契約書ワークフロー",
        "guide7_more": "すべての PDF 署名ガイドを見る &rarr;",
        "guide8_desc": "ゲーム終了時の得点ルール、収穫の食料供給、家の改築、物乞いカードの減点計算。",
        "guide8_l1": "アグリコラ得点ルール＆ポイント計算",
        "guide8_l2": "収穫の食料確保＆戦略ガイド",
        "guide8_more": "すべてのアグリコラガイドを見る &rarr;",
        "guides_source_note": "出典：健康・習慣ガイドは NIAAA、CDC、Smokefree.gov、NIH Office of Dietary Supplements、Hirvonen et al. (2012)、Hughes (2007)、Ebrahim et al. (2013)、Bowen &amp; Marlatt (2009) を参照しています。教育目的の情報であり、医療上の助言ではありません。",
        "founder_eyebrow": "スタジオについて",
        "founder_title": "Louis Liu による開発",
        "founder_bio": "大規模動画配信、コンパイラ高速化、組込みシステムの経験を持つシニアモバイルソフトウェアエンジニア。",
        "founder_btn": "プロフィールと経歴を見る",
        "contact_heading": "サポート＆<br />お問い合わせ",
        "contact_lead": "アプリへのフィードバックや技術サポート、協業のご相談など、いつでもお気軽にご連絡ください。",
        "btn_email": "サポートへメール",
        "btn_copy": "メールをコピー",
        "footer_rights": "© 2026 YS Liu Studio. 無断転載を禁じます。",
        "footer_alcohol_free": "禁酒",
        "footer_quit_weed": "大麻離脱",
        "footer_quit_vaping": "脱ベイプ",
        "footer_sourdough": "サワードウ",
        "footer_back_top": "トップへ戻る",
        "lightbox_hint": "<kbd>←</kbd> <kbd>→</kbd> キーで移動、<kbd>Esc</kbd> で閉じます。",
        "toast_copied": "メールアドレスをコピーしました",
    },
    "ko": {
        "title": "YS Liu Studio — 독립 모바일 앱 스튜디오",
        "desc": "YS Liu Studio는 일상 습관, 건강 기록, 문서 서명 및 생활 유틸리티를 위한 빠르고 프라이버시 중심의 iOS 앱을 개발합니다.",
        "og_desc": "일상적인 활용을 위한 빠르고 프라이버시 중심의 네이티브 iOS 앱.",
        "nav_apps": "앱",
        "nav_philosophy": "철학",
        "nav_developer": "개발자",
        "nav_support": "지원",
        "nav_btn": "개발자 소개",
        "pill_est": "인디 앱 스튜디오 · 2024년 설립",
        "hero_title": "일상 습관, 건강 관리, 유틸리티를 위한 네이티브 iOS 앱",
        "hero_desc": "<strong>YS Liu Studio</strong>는 습관 기록, 문서 서명, 일상 유틸리티를 위한 오프라인 지원 네이티브 iOS 앱을 개발합니다. 로컬 저장 방식을 사용하며 광고나 추적이 없습니다.",
        "hero_btn_explore": "전체 앱 둘러보기",
        "hero_btn_about": "설립자 Louis Liu 소개",
        "dock_label": "App Store에 출시된 6개의 앱",
        "marquee_native": "네이티브 iOS 성능",
        "marquee_privacy": "프라이버시 우선 저장",
        "marquee_ux": "단순하고 집중된 UX",
        "marquee_ai": "온디바이스 처리",
        "marquee_accessible": "접근성 중심 설계",
        "marquee_global": "40개 이상의 App Store 국가 지원",
        "marquee_offline": "오프라인 우선 안정성",
        "pillar1_num": "01",
        "pillar1_title": "작업당 더 적은 단계",
        "pillar1_desc": "명확한 시각적 계층, 햅틱 피드백, VoiceOver 지원으로 불필요한 팝업을 줄여 일상 작업을 더 적은 탭으로 마칠 수 있습니다.",
        "pillar2_num": "02",
        "pillar2_title": "프라이버시 및 기기 내 저장",
        "pillar2_desc": "건강 기록, 계약서, 습관 데이터는 오직 사용자의 것입니다. 앱은 광고 추적기 없이 온디바이스 OCR, 로컬 저장소, 암호화된 서명 링크를 사용합니다.",
        "pillar3_num": "03",
        "pillar3_title": "네이티브 Swift 아키텍처",
        "pillar3_desc": "최신 Swift 동시성, 로컬 데이터 저장, iOS 네이티브 플랫폼 규칙으로 구축되어 매일 안정적으로 사용할 수 있습니다.",
        "apps_pill": "제품 목록",
        "apps_headline": "YS Liu Studio의 앱",
        "apps_sub": "네이티브 앱을 확인해 보세요. 스크린샷을 클릭하면 고화질로 인터페이스를 확인할 수 있습니다.",
        "btn_appstore": "App Store에서 보기",
        "guides_pill": "참고 가이드",
        "guides_headline": "건강, 습관 및 유틸리티 가이드",
        "guides_sub": "공개된 연구에 기반한 일반 참고 가이드와 회복 일정, 그리고 유틸리티 앱의 실용적인 사용법을 제공합니다.",
        "guide1_desc": "절주 및 금주 가이드, 일반적인 신체 회복 일정, 수면 방해 연구 요약, 충동 서핑 대처 전략.",
        "guide1_l1": "30일 금주 챌린지 가이드",
        "guide1_l2": "금주 후 신체 회복 일정 개요",
        "guide1_l3": "저녁 음주 갈망 대처하기: 충동 서핑",
        "guide1_l4": "알코올과 수면 장애: 연구 결과 요약",
        "guide1_more": "모든 금주 가이드 보기 &rarr;",
        "guide2_desc": "대마 금단 현상 개요, 약 4주간의 CB1 수용체 회복, 중단 초기 수면 변화 및 호흡 조절법.",
        "guide2_l1": "대마 금단과 CB1 수용체 회복",
        "guide2_l2": "대마 중단 후 수면 장애",
        "guide2_l3": "대마 갈망을 위한 4-7-8 호흡법",
        "guide2_more": "모든 대마 중단 가이드 보기 &rarr;",
        "guide3_desc": "니코틴 금단 일정(1주차에 정점, 2~4주에 걸쳐 완화), 충동 서핑 기초 및 팟 지출 계산.",
        "guide3_l1": "니코틴 금단 일정: 예상되는 변화",
        "guide3_l2": "급성 니코틴 갈망을 위한 충동 서핑",
        "guide3_more": "모든 전자담배 금연 가이드 보기 &rarr;",
        "guide4_desc": "영양제 복용 시간 기초, 식사 중 흡수 참고 사항, 약물 상호작용 확인 및 복용 누락 시 참고 가이드.",
        "guide4_l1": "마그네슘 글리시네이트 복용 시기",
        "guide4_l2": "비타민 및 영양제 복용 시간 가이드",
        "guide4_more": "모든 복약 알림 가이드 보기 &rarr;",
        "guide5_desc": "단위 가격 계산 공식, 슈링크플레이션 확인법 및 마트 장보기 가이드.",
        "guide5_l1": "온스 및 그램당 가격 계산 방법",
        "guide5_l2": "단위 비용 및 마트 계산 가이드",
        "guide5_more": "모든 마트 장보기 가이드 보기 &rarr;",
        "guide6_desc": "베이커스 퍼센트 공식, 사워도우 수분율 계산 및 온도별 발효 시간 조절.",
        "guide6_l1": "사워도우 수분율 계산기 및 비율",
        "guide6_l2": "벌크 발효 및 스타터 먹이 주기 차트",
        "guide6_more": "모든 사워도우 가이드 보기 &rarr;",
        "guide7_desc": "모바일 계약 서명, 구독 없는 전자서명 워크플로 및 브라우저 서명 링크 공유.",
        "guide7_l1": "구독 없이 iPhone에서 PDF 서명하기",
        "guide7_l2": "모바일 전자서명 및 계약 워크플로",
        "guide7_more": "모든 PDF 서명 가이드 보기 &rarr;",
        "guide8_desc": "게임 종료 승점 규칙, 수확 식량 공급, 방 업그레이드 및 구걸 카드 감점 계산.",
        "guide8_l1": "아그리콜라 점수 규칙 및 승점 계산",
        "guide8_l2": "수확 식량 공급 및 전략 가이드",
        "guide8_more": "모든 아그리콜라 가이드 보기 &rarr;",
        "guides_source_note": "출처: 건강 및 습관 가이드는 NIAAA, CDC, Smokefree.gov, NIH Office of Dietary Supplements, Hirvonen et al. (2012), Hughes (2007), Ebrahim et al. (2013), Bowen &amp; Marlatt (2009)를 참고했습니다. 교육 목적의 일반 정보이며 의학적 조언이 아닙니다.",
        "founder_eyebrow": "스튜디오 소개",
        "founder_title": "개발자 Louis Liu 제작",
        "founder_bio": "대규모 스트리밍 플랫폼, 컴파일러 가속 및 임베디드 소프트웨어 경험을 보유한 시니어 모바일 엔지니어.",
        "founder_btn": "개발자 프로필 및 이력 보기",
        "contact_heading": "고객 지원 및<br />스튜디오 문의",
        "contact_lead": "앱에 대한 의견이나 기술 지원, 협업 제안이 있으신가요? 언제든 편하게 연락해 주세요.",
        "btn_email": "지원 이메일 보내기",
        "btn_copy": "이메일 복사",
        "footer_rights": "© 2026 YS Liu Studio. 모든 권리 보유.",
        "footer_alcohol_free": "금주",
        "footer_quit_weed": "대마 중단",
        "footer_quit_vaping": "전자담배 금연",
        "footer_sourdough": "사워도우",
        "footer_back_top": "맨 위로",
        "lightbox_hint": "<kbd>←</kbd> <kbd>→</kbd> 방향키로 이동하고 <kbd>Esc</kbd> 키로 닫습니다.",
        "toast_copied": "이메일 주소가 복사되었습니다",
    },
    "es": {
        "title": "YS Liu Studio — Estudio Independiente de Aplicaciones Móviles",
        "desc": "YS Liu Studio desarrolla aplicaciones iOS rápidas y centradas en la privacidad para hábitos diarios, seguimiento de salud, firma de documentos y utilidades cotidianas.",
        "og_desc": "Aplicaciones iOS nativas, rápidas y centradas en la privacidad para el día a día.",
        "nav_apps": "Aplicaciones",
        "nav_philosophy": "Filosofía",
        "nav_developer": "Desarrollador",
        "nav_support": "Soporte",
        "nav_btn": "Conoce al desarrollador",
        "pill_est": "Estudio de Apps Independiente · Fundado en 2024",
        "hero_title": "Aplicaciones iOS nativas para hábitos diarios, salud y utilidades",
        "hero_desc": "<strong>YS Liu Studio</strong> desarrolla aplicaciones iOS nativas listas para usar sin conexión para seguimiento de hábitos, firma de documentos y utilidades diarias, con almacenamiento local y sin anuncios ni rastreo.",
        "hero_btn_explore": "Explorar aplicaciones",
        "hero_btn_about": "Sobre Louis Liu (Fundador)",
        "dock_label": "6 aplicaciones disponibles en el App Store",
        "marquee_native": "Rendimiento nativo iOS",
        "marquee_privacy": "Almacenamiento privado",
        "marquee_ux": "UX sencilla y enfocada",
        "marquee_ai": "Procesamiento en el dispositivo",
        "marquee_accessible": "Diseño accesible",
        "marquee_global": "Más de 40 tiendas App Store",
        "marquee_offline": "Fiabilidad sin conexión",
        "pillar1_num": "01",
        "pillar1_title": "Menos pasos por tarea",
        "pillar1_desc": "Una jerarquía visual clara, háptica y compatibilidad con VoiceOver eliminan ventanas innecesarias para completar tareas cotidianas con menos toques.",
        "pillar2_num": "02",
        "pillar2_title": "Privacidad y almacenamiento local",
        "pillar2_desc": "Tus registros de salud, contratos y hábitos siguen siendo tuyos. Las apps usan OCR en el dispositivo, almacenamiento local y enlaces de firma cifrados sin rastreadores de anuncios.",
        "pillar3_num": "03",
        "pillar3_title": "Arquitectura Swift nativa",
        "pillar3_desc": "Desarrollado con concurrencia moderna en Swift, persistencia local y convenciones nativas de iOS para un uso diario fiable.",
        "apps_pill": "Catálogo de apps",
        "apps_headline": "Apps de YS Liu Studio",
        "apps_sub": "Descubre nuestras aplicaciones nativas. Haz clic en las capturas para ver la interfaz en alta resolución.",
        "btn_appstore": "Ver en App Store",
        "guides_pill": "Guías de referencia",
        "guides_headline": "Guías de salud, hábitos y utilidades",
        "guides_sub": "Guías de referencia y plazos generales basados en estudios publicados, junto con tutoriales prácticos para nuestras aplicaciones de utilidad.",
        "guide1_desc": "Guías para reducir o dejar el alcohol, plazos generales de recuperación, estudios sobre alteración del sueño y estrategias de urge surfing.",
        "guide1_l1": "Guía del reto de 30 días sin alcohol",
        "guide1_l2": "Resumen del calendario de recuperación",
        "guide1_l3": "Cómo manejar el antojo nocturno de alcohol: urge surfing",
        "guide1_l4": "Alcohol y alteración del sueño: qué muestran los estudios",
        "guide1_more": "Ver todas las guías sin alcohol &rarr;",
        "guide2_desc": "Resumen de la abstinencia de cannabis, recuperación de receptores CB1 en unas 4 semanas, cambios iniciales del sueño y respiración pausada.",
        "guide2_l1": "Abstinencia de cannabis y recuperación de receptores CB1",
        "guide2_l2": "Alteraciones del sueño tras dejar el cannabis",
        "guide2_l3": "Respiración pausada 4-7-8 para los antojos de cannabis",
        "guide2_more": "Ver todas las guías para dejar el cannabis &rarr;",
        "guide3_desc": "Plazos de abstinencia de nicotina (pico en la semana 1 y alivio en 2–4 semanas), fundamentos de urge surfing y cálculo de gasto en pods.",
        "guide3_l1": "Cronología de abstinencia de nicotina: qué esperar",
        "guide3_l2": "Urge surfing para antojos agudos de nicotina",
        "guide3_more": "Ver todas las guías para dejar el vapeo &rarr;",
        "guide4_desc": "Conceptos básicos sobre horarios de suplementos, absorción con comidas, revisión de interacciones y guías ante olvidos de dosis.",
        "guide4_l1": "Cuándo tomar glicinato de magnesio",
        "guide4_l2": "Guía de horarios para vitaminas y suplementos",
        "guide4_more": "Ver todas las guías de Pill Reminder &rarr;",
        "guide5_desc": "Fórmulas de precio unitario, detección de reduflación y guías de compra frente a la inflación en el supermercado.",
        "guide5_l1": "Cómo calcular el precio por onza y gramo",
        "guide5_l2": "Guías de coste unitario y cálculo en el supermercado",
        "guide5_more": "Ver todas las guías de compras &rarr;",
        "guide6_desc": "Fórmulas de porcentaje panadero, cálculo de hidratación de masa madre y tiempos de fermentación según temperatura.",
        "guide6_l1": "Calculadora de hidratación de masa madre y porcentajes",
        "guide6_l2": "Tablas de fermentación en bloque y refresco de masa madre",
        "guide6_more": "Ver todas las guías de masa madre &rarr;",
        "guide7_desc": "Firma móvil de contratos, flujos de firma electrónica sin suscripción y envío de enlaces de firma en navegador.",
        "guide7_l1": "Firmar PDF en iPhone sin suscripción",
        "guide7_l2": "Flujos móviles de firma electrónica y contratos",
        "guide7_more": "Ver todas las guías de firma PDF &rarr;",
        "guide8_desc": "Reglas de puntos de victoria finales, motores de comida en cosecha, mejoras de habitaciones y penalización de cartas de mendicidad.",
        "guide8_l1": "Reglas de puntuación y cálculo de puntos de Agricola",
        "guide8_l2": "Guías de motor de comida y estrategia de cosecha",
        "guide8_more": "Ver todas las guías de Agricola &rarr;",
        "guides_source_note": "Fuentes: las guías de salud y hábitos toman como referencia NIAAA, CDC, Smokefree.gov, NIH Office of Dietary Supplements, Hirvonen et al. (2012), Hughes (2007), Ebrahim et al. (2013) y Bowen &amp; Marlatt (2009). Solo información educativa, no es consejo médico.",
        "founder_eyebrow": "Detrás del Estudio",
        "founder_title": "Desarrollado por Louis Liu",
        "founder_bio": "Ingeniero de software móvil sénior con experiencia en streaming a escala, compiladores y sistemas embebidos.",
        "founder_btn": "Ver perfil y currículum",
        "contact_heading": "Soporte y<br />Consultas del Estudio",
        "contact_lead": "¿Tienes comentarios, necesitas soporte o quieres colaborar? Escríbenos directamente cuando quieras.",
        "btn_email": "Enviar correo de soporte",
        "btn_copy": "Copiar correo",
        "footer_rights": "Copyright © 2026 YS Liu Studio. Todos los derechos reservados.",
        "footer_alcohol_free": "Sin alcohol",
        "footer_quit_weed": "Dejar cannabis",
        "footer_quit_vaping": "Dejar vapeo",
        "footer_sourdough": "Masa madre",
        "footer_back_top": "Volver arriba",
        "lightbox_hint": "Usa las flechas <kbd>←</kbd> <kbd>→</kbd> para navegar y <kbd>Esc</kbd> para salir.",
        "toast_copied": "Correo copiado al portapapeles",
    },
    "it": {
        "title": "YS Liu Studio — Studio Indipendente di App Mobili",
        "desc": "YS Liu Studio sviluppa app iOS veloci e incentrate sulla privacy per abitudini quotidiane, monitoraggio della salute, firma di documenti e utilità di ogni giorno.",
        "og_desc": "App iOS native, veloci e incentrate sulla privacy per l'uso quotidiano.",
        "nav_apps": "Applicazioni",
        "nav_philosophy": "Filosofia",
        "nav_developer": "Sviluppatore",
        "nav_support": "Supporto",
        "nav_btn": "Incontra lo sviluppatore",
        "pill_est": "Studio di App Indipendente · Fondato nel 2024",
        "hero_title": "App iOS native per abitudini quotidiane, salute e utilità",
        "hero_desc": "<strong>YS Liu Studio</strong> sviluppa app iOS native utilizzabili offline per monitorare abitudini, firmare documenti e gestire attività quotidiane, con archiviazione locale e senza pubblicità o tracciamento.",
        "hero_btn_explore": "Scopri le nostre app",
        "hero_btn_about": "Chi è Louis Liu (Fondatore)",
        "dock_label": "6 app disponibili su App Store",
        "marquee_native": "Prestazioni iOS native",
        "marquee_privacy": "Archiviazione orientata alla privacy",
        "marquee_ux": "UX semplice ed essenziale",
        "marquee_ai": "Elaborazione sul dispositivo",
        "marquee_accessible": "Progettato per l'accessibilità",
        "marquee_global": "Oltre 40 store App Store",
        "marquee_offline": "Affidabilità offline-first",
        "pillar1_num": "01",
        "pillar1_title": "Meno passaggi per ogni attività",
        "pillar1_desc": "Gerarchia visiva chiara, feedback aptico e supporto VoiceOver eliminano finestre superflue, completando le attività quotidiane con meno tocchi.",
        "pillar2_num": "02",
        "pillar2_title": "Privacy e archiviazione locale",
        "pillar2_desc": "I tuoi registri sanitari, contratti e abitudini restano tuoi. Le app usano OCR sul dispositivo, archiviazione locale e link di firma cifrati, senza tracker pubblicitari.",
        "pillar3_num": "03",
        "pillar3_title": "Architettura Swift nativa",
        "pillar3_desc": "Sviluppate con concorrenza Swift moderna, persistenza locale e convenzioni native iOS per un uso quotidiano affidabile.",
        "apps_pill": "Suite di app",
        "apps_headline": "App di YS Liu Studio",
        "apps_sub": "Esplora le nostre app native. Tocca una schermata per vederla ad alta risoluzione.",
        "btn_appstore": "Vedi su App Store",
        "guides_pill": "Guide di riferimento",
        "guides_headline": "Guide su salute, abitudini e utilità",
        "guides_sub": "Guide di riferimento e tempi indicativi basati su ricerche pubblicate, insieme a istruzioni pratiche per le nostre app di utilità.",
        "guide1_desc": "Guide per ridurre o smettere con l'alcol, tempi generali di recupero, studi sui disturbi del sonno e strategie di urge surfing.",
        "guide1_l1": "Guida alla sfida 30 giorni senza alcol",
        "guide1_l2": "Panoramica dei tempi di recupero",
        "guide1_l3": "Gestire il desiderio serale di alcol: urge surfing",
        "guide1_l4": "Alcol e disturbi del sonno: cosa mostrano gli studi",
        "guide1_more": "Vedi tutte le guide senza alcol &rarr;",
        "guide2_desc": "Panoramica sull'astinenza da cannabis, recupero dei recettori CB1 in circa 4 settimane, variazioni iniziali del sonno e respirazione ritmata.",
        "guide2_l1": "Astinenza da cannabis e recupero dei recettori CB1",
        "guide2_l2": "Disturbi del sonno dopo la sospensione della cannabis",
        "guide2_l3": "Respirazione 4-7-8 per il desiderio di cannabis",
        "guide2_more": "Vedi tutte le guide per smettere con la cannabis &rarr;",
        "guide3_desc": "Tempi di astinenza da nicotina (picco nella prima settimana e riduzione in 2–4 settimane), basi di urge surfing e calcolo della spesa per pod.",
        "guide3_l1": "Tempi dell'astinenza da nicotina: cosa aspettarsi",
        "guide3_l2": "Urge surfing per il desiderio acuto di nicotina",
        "guide3_more": "Vedi tutte le guide per smettere di svapare &rarr;",
        "guide4_desc": "Basi sugli orari degli integratori, note sull'assorbimento ai pasti, verifica delle interazioni e guide in caso di dose dimenticata.",
        "guide4_l1": "Quando assumere il magnesio glicinato",
        "guide4_l2": "Guida agli orari di vitamine e integratori",
        "guide4_more": "Vedi tutte le guide di Pill Reminder &rarr;",
        "guide5_desc": "Formule per il prezzo unitario, rilevamento della sgrammatura e guide alla spesa contro l'inflazione al supermercato.",
        "guide5_l1": "Come calcolare il prezzo per oncia e grammo",
        "guide5_l2": "Guide al costo unitario e calcoli al supermercato",
        "guide5_more": "Vedi tutte le guide per la spesa &rarr;",
        "guide6_desc": "Formule della percentuale del panettiere, calcolo dell'idratazione del lievito madre e tempi di fermentazione in base alla temperatura.",
        "guide6_l1": "Calcolatore di idratazione e percentuali per lievito madre",
        "guide6_l2": "Tabelle di prima lievitazione e rinfresco del lievito",
        "guide6_more": "Vedi tutte le guide sul lievito madre &rarr;",
        "guide7_desc": "Firma di contratti su mobile, flussi eSign senza abbonamento e condivisione di link di firma via browser.",
        "guide7_l1": "Firmare PDF su iPhone senza abbonamento",
        "guide7_l2": "Flussi mobile per firma elettronica e contratti",
        "guide7_more": "Vedi tutte le guide per firmare PDF &rarr;",
        "guide8_desc": "Regole sui punti vittoria finali, gestione del cibo al raccolto, ristrutturazioni e calcolo penalità carte accattonaggio.",
        "guide8_l1": "Regole di punteggio e calcolo punti di Agricola",
        "guide8_l2": "Guide alla gestione del cibo e strategia di raccolta",
        "guide8_more": "Vedi tutte le guide su Agricola &rarr;",
        "guides_source_note": "Fonti: le guide su salute e abitudini fanno riferimento a NIAAA, CDC, Smokefree.gov, NIH Office of Dietary Supplements, Hirvonen et al. (2012), Hughes (2007), Ebrahim et al. (2013) e Bowen &amp; Marlatt (2009). Solo a scopo informativo, non costituisce parere medico.",
        "founder_eyebrow": "Dietro lo Studio",
        "founder_title": "Sviluppato da Louis Liu",
        "founder_bio": "Senior Mobile Software Engineer con esperienza in streaming su larga scala, ottimizzazione compilatori e sistemi nativi.",
        "founder_btn": "Visualizza profilo e CV",
        "contact_heading": "Supporto App &<br />Richieste di Contatto",
        "contact_lead": "Hai domande, suggerimenti o proposte di collaborazione? Scrivici direttamente in qualsiasi momento.",
        "btn_email": "Invia email al supporto",
        "btn_copy": "Copia email",
        "footer_rights": "Copyright © 2026 YS Liu Studio. Tutti i diritti riservati.",
        "footer_alcohol_free": "Senza alcol",
        "footer_quit_weed": "Smettere cannabis",
        "footer_quit_vaping": "Smettere svapo",
        "footer_sourdough": "Lievito madre",
        "footer_back_top": "Torna su",
        "lightbox_hint": "Usa i tasti freccia <kbd>←</kbd> <kbd>→</kbd> per navigare, <kbd>Esc</kbd> per uscire.",
        "toast_copied": "Email copiata negli appunti",
    },
}


def get_localized_url(base_slug: str, locale_code: str) -> str:
    slug = base_slug.strip("/")
    path = f"/{slug}/" if slug else "/"
    if locale_code == "en":
        return f"https://ysliustudio.com{path}"
    return f"https://ysliustudio.com/{locale_code}{path}"


def get_relative_url(base_slug: str, locale_code: str) -> str:
    slug = base_slug.strip("/")
    path = f"/{slug}/" if slug else "/"
    if locale_code == "en":
        return path
    return f"/{locale_code}{path}"


def generate_hreflang_tags(base_slug: str) -> str:
    lines = []
    lines.append(f'  <link rel="alternate" hreflang="x-default" href="{get_localized_url(base_slug, "en")}" />')
    for loc in LOCALES:
        code = loc["code"]
        hl = HREFLANG_MAP[code]
        lines.append(f'  <link rel="alternate" hreflang="{hl}" href="{get_localized_url(base_slug, code)}" />')
    return "\n".join(lines)


def generate_language_switcher_html(base_slug: str, current_locale: str) -> str:
    curr_info = next((l for l in LOCALES if l["code"] == current_locale), LOCALES[0])
    options_html = []
    for loc in LOCALES:
        active = " active" if loc["code"] == current_locale else ""
        href = get_relative_url(base_slug, loc["code"])
        options_html.append(f'      <a href="{href}" class="lang-opt{active}" data-lang="{loc["code"]}">{loc["name"]}</a>')

    options_block = "\n".join(options_html)
    return f"""<div class="lang-switcher">
    <button class="lang-btn" type="button" aria-label="Select Language" aria-expanded="false">
      <svg class="lang-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <circle cx="12" cy="12" r="10"></circle>
        <line x1="2" y1="12" x2="22" y2="12"></line>
        <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
      </svg>
      <span class="lang-current">{curr_info["name"]}</span>
      <svg class="lang-chevron" viewBox="0 0 20 20" fill="currentColor">
        <path fill-rule="evenodd" d="M5.23 7.21a.75.75 0 011.06.02L10 11.168l3.71-3.938a.75.75 0 111.08 1.04l-4.25 4.5a.75.75 0 01-1.08 0l-4.25-4.5a.75.75 0 01.02-1.06z" clip-rule="evenodd" />
      </svg>
    </button>
    <div class="lang-dropdown">
{options_block}
    </div>
  </div>"""


def update_root_index_html():
    """Injects hreflang and language switcher into default root index.html."""
    path = os.path.join(ROOT_DIR, "index.html")
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Update hreflang
    hreflangs = generate_hreflang_tags("")
    if '<link rel="alternate" hreflang="x-default"' not in html:
        canonical_pattern = r'(<link rel="canonical" href="https://ysliustudio\.com/" />)'
        replacement = r'\1\n' + hreflangs
        html = re.sub(canonical_pattern, replacement, html, count=1)

    # 2. Add language switcher to navbar
    switcher_html = generate_language_switcher_html("", "en")
    if 'class="lang-switcher"' not in html:
        nav_pattern = r'(<div class="nav-cta-wrap">)'
        replacement = r'\1\n        ' + switcher_html
        html = re.sub(nav_pattern, replacement, html, count=1)

    # 3. Add lang-switcher.js script before closing body
    if 'src="/lang-switcher.js"' not in html:
        html = html.replace('</body>', '  <script src="/lang-switcher.js" defer></script>\n</body>')

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("✔ Updated root index.html with hreflang & language switcher.")


def build_localized_studio_home(locale_code: str):
    """Builds /<locale>/index.html based on root index.html and STUDIO_I18N dictionary."""
    t = STUDIO_I18N[locale_code]
    loc_info = next(l for l in LOCALES if l["code"] == locale_code)
    target_dir = os.path.join(ROOT_DIR, locale_code)
    os.makedirs(target_dir, exist_ok=True)
    target_file = os.path.join(target_dir, "index.html")

    # Read base template from root index.html
    with open(os.path.join(ROOT_DIR, "index.html"), "r", encoding="utf-8") as f:
        html = f.read()

    # Replace html lang
    html = re.sub(r'<html lang="[a-zA-Z\-]+">', f'<html lang="{loc_info["html_lang"]}">', html, count=1)

    # Replace canonical and og:url
    curr_url = get_localized_url("", locale_code)
    html = re.sub(r'<link rel="canonical" href="[^"]+" />', f'<link rel="canonical" href="{curr_url}" />', html, count=1)
    html = re.sub(r'<meta property="og:url" content="[^"]+" />', f'<meta property="og:url" content="{curr_url}" />', html, count=1)

    # Replace Title and Description
    html = re.sub(r'<title>[^<]+</title>', f'<title>{t["title"]}</title>', html, count=1)
    html = re.sub(r'<meta name="description" content="[^"]*" />', f'<meta name="description" content="{t["desc"]}" />', html, count=1)
    html = re.sub(r'<meta property="og:title" content="[^"]*" />', f'<meta property="og:title" content="{t["title"]}" />', html, count=1)
    html = re.sub(r'<meta property="og:description" content="[^"]*" />', f'<meta property="og:description" content="{t["og_desc"]}" />', html, count=1)

    # Replace Navigation texts
    html = html.replace('<a href="#apps" class="nav-link active">Apps</a>', f'<a href="#apps" class="nav-link active">{t["nav_apps"]}</a>')
    html = html.replace('<a href="#philosophy" class="nav-link">Philosophy</a>', f'<a href="#philosophy" class="nav-link">{t["nav_philosophy"]}</a>')
    html = html.replace('<a href="/developer/" class="nav-link">Developer</a>', f'<a href="/developer/" class="nav-link">{t["nav_developer"]}</a>')
    html = html.replace('<a href="#contact" class="nav-link">Support</a>', f'<a href="#contact" class="nav-link">{t["nav_support"]}</a>')
    html = re.sub(r'<span>Meet the Developer</span>', f'<span>{t["nav_btn"]}</span>', html, count=1)

    # Replace Language Switcher with active locale
    curr_switcher = generate_language_switcher_html("", locale_code)
    html = re.sub(r'<div class="lang-switcher">[\s\S]*?</div>\s*</div>', curr_switcher, html, count=1)

    # Replace Hero & Dock
    html = html.replace('Independent App Studio · Est. 2024', t["pill_est"])
    html = re.sub(r'<h1 class="hero-title studio-display-title">[\s\S]*?</h1>', f'<h1 class="hero-title studio-display-title">\n            {t["hero_title"]}\n          </h1>', html, count=1)
    html = re.sub(r'<p class="hero-description studio-lead">[\s\S]*?</p>', f'<p class="hero-description studio-lead">\n            {t["hero_desc"]}\n          </p>', html, count=1)
    html = re.sub(r'<span>Explore Our Apps</span>', f'<span>{t["hero_btn_explore"]}</span>', html, count=1)
    html = re.sub(r'<span>About Louis Liu \(Founder\)</span>', f'<span>{t["hero_btn_about"]}</span>', html, count=1)
    html = html.replace('6 apps live on the App Store', t["dock_label"])

    # Replace Marquee
    html = html.replace('<span class="marquee-item">Native iOS performance</span>', f'<span class="marquee-item">{t["marquee_native"]}</span>')
    html = html.replace('<span class="marquee-item">Privacy-first storage</span>', f'<span class="marquee-item">{t["marquee_privacy"]}</span>')
    html = html.replace('<span class="marquee-item">Simple, focused UX</span>', f'<span class="marquee-item">{t["marquee_ux"]}</span>')
    html = html.replace('<span class="marquee-item">On-device processing</span>', f'<span class="marquee-item">{t["marquee_ai"]}</span>')
    html = html.replace('<span class="marquee-item">Accessible by design</span>', f'<span class="marquee-item">{t["marquee_accessible"]}</span>')
    html = html.replace('<span class="marquee-item">40+ App Store storefronts</span>', f'<span class="marquee-item">{t["marquee_global"]}</span>')
    html = html.replace('<span class="marquee-item">Offline-first reliability</span>', f'<span class="marquee-item">{t["marquee_offline"]}</span>')

    # Replace Pillars
    html = html.replace('Fewer steps per task', t["pillar1_title"])
    html = re.sub(r'Clear visual hierarchy, haptics, and VoiceOver support cut out unnecessary modals so everyday tasks take fewer taps\.', t["pillar1_desc"], html)
    html = html.replace('Privacy and on-device storage', t["pillar2_title"])
    html = re.sub(r'Your health logs, contracts, and habit records stay yours\. Apps use on-device OCR, local storage, and encrypted signing links without ad trackers\.', t["pillar2_desc"], html)
    html = html.replace('Native Swift architecture', t["pillar3_title"])
    html = re.sub(r'Built with modern Swift concurrency, local persistence, and native iOS platform conventions for dependable everyday use\.', t["pillar3_desc"], html)

    # Replace Apps Section Headers
    html = html.replace('<span class="pill-text">Product suite</span>', f'<span class="pill-text">{t["apps_pill"]}</span>')
    html = html.replace('<h2 class="projects-headline">Apps by YS Liu Studio</h2>', f'<h2 class="projects-headline">{t["apps_headline"]}</h2>')
    html = re.sub(r'Explore our lineup of native applications\. Click any screenshot to inspect the interface in full resolution\.', t["apps_sub"], html)
    html = html.replace('<span>View on App Store</span>', f'<span>{t["btn_appstore"]}</span>')

    # Replace Guides Section Headers
    html = html.replace('<span class="pill-text">Reference guides</span>', f'<span class="pill-text">{t["guides_pill"]}</span>')
    html = html.replace('<h2 class="projects-headline">Health, Habit &amp; Utility Guides</h2>', f'<h2 class="projects-headline">{t["guides_headline"]}</h2>')
    html = re.sub(r'Reference guides and general timelines grounded in published research, alongside practical how-tos for our utility apps\.', t["guides_sub"], html)

    # Replace Guides Hub Cards
    html = html.replace('Guides on cutting back or stopping alcohol, general recovery timelines, sleep disruption research, and urge-surfing strategies.', t["guide1_desc"])
    html = html.replace('>30-Day Dry Challenge Guide</a>', f'>{t["guide1_l1"]}</a>')
    html = html.replace('>Alcohol Recovery Timeline Overview</a>', f'>{t["guide1_l2"]}</a>')
    html = html.replace('>Coping With Evening Alcohol Cravings: Urge Surfing</a>', f'>{t["guide1_l3"]}</a>')
    html = html.replace('>Alcohol and Sleep Disruption: What Research Shows</a>', f'>{t["guide1_l4"]}</a>')
    html = html.replace('>View all Alcohol-Free Guides &rarr;</a>', f'>{t["guide1_more"]}</a>')

    html = html.replace('Cannabis withdrawal overview, CB1 receptor recovery over about 4 weeks, early abstinence sleep changes, and paced breathing.', t["guide2_desc"])
    html = html.replace('>Cannabis Withdrawal and CB1 Receptor Recovery</a>', f'>{t["guide2_l1"]}</a>')
    html = html.replace('>Sleep Disturbance After Stopping Cannabis</a>', f'>{t["guide2_l2"]}</a>')
    html = html.replace('>4-7-8 Paced Breathing for Cannabis Cravings</a>', f'>{t["guide2_l3"]}</a>')
    html = html.replace('>View all Quit Weed Guides &rarr;</a>', f'>{t["guide2_more"]}</a>')

    html = html.replace('Nicotine withdrawal timeline (peaking in week 1 and easing over 2–4 weeks), urge-surfing basics, and pod spending math.', t["guide3_desc"])
    html = html.replace('>Nicotine Withdrawal Timeline: What to Expect</a>', f'>{t["guide3_l1"]}</a>')
    html = html.replace('>Urge Surfing for Acute Nicotine Cravings</a>', f'>{t["guide3_l2"]}</a>')
    html = html.replace('>View all Quit Vaping Guides &rarr;</a>', f'>{t["guide3_more"]}</a>')

    html = html.replace('Supplement timing basics, meal absorption notes, medication interaction checks, and missed-dose reference guides.', t["guide4_desc"])
    html = html.replace('>When to Take Magnesium Glycinate</a>', f'>{t["guide4_l1"]}</a>')
    html = html.replace('>Vitamin &amp; Supplement Timing Guide</a>', f'>{t["guide4_l2"]}</a>')
    html = html.replace('>View all Pill Reminder Guides &rarr;</a>', f'>{t["guide4_more"]}</a>')

    html = html.replace('Unit price formulas, package shrinkflation detection, and smart supermarket inflation shopping guides.', t["guide5_desc"])
    html = html.replace('>How to Calculate Price per Ounce &amp; Gram</a>', f'>{t["guide5_l1"]}</a>')
    html = html.replace('>Unit Cost &amp; Supermarket Math Guides</a>', f'>{t["guide5_l2"]}</a>')
    html = html.replace('>View all Smart Grocery Guides &rarr;</a>', f'>{t["guide5_more"]}</a>')

    html = html.replace("Baker's percentage formulas, sourdough hydration scaling, and temperature-adjusted fermentation timing.", t["guide6_desc"])
    html = html.replace('>Sourdough Hydration Calculator &amp; Percentages</a>', f'>{t["guide6_l1"]}</a>')
    html = html.replace('>Bulk Fermentation &amp; Starter Feeding Charts</a>', f'>{t["guide6_l2"]}</a>')
    html = html.replace('>View all Sourdough Guides &rarr;</a>', f'>{t["guide6_more"]}</a>')

    html = html.replace('Mobile contract signing, subscription-free eSign workflows, and browser link signature sharing.', t["guide7_desc"])
    html = html.replace('>Sign PDF on iPhone Without Subscription</a>', f'>{t["guide7_l1"]}</a>')
    html = html.replace('>Mobile eSign &amp; Contract Workflows</a>', f'>{t["guide7_l2"]}</a>')
    html = html.replace('>View all PDF Signing Guides &rarr;</a>', f'>{t["guide7_more"]}</a>')

    html = html.replace('End-game victory point rules, harvest food engines, room upgrades, and begging card penalty math.', t["guide8_desc"])
    html = html.replace('>Agricola Scoring Rules &amp; Point Calculations</a>', f'>{t["guide8_l1"]}</a>')
    html = html.replace('>Harvest Food Engine &amp; Strategy Guides</a>', f'>{t["guide8_l2"]}</a>')
    html = html.replace('>View all Agricola Guides &rarr;</a>', f'>{t["guide8_more"]}</a>')

    html = html.replace('Sources: Health and habit guides reference NIAAA, CDC, Smokefree.gov, NIH Office of Dietary Supplements, Hirvonen et al. (2012), Hughes (2007), Ebrahim et al. (2013), and Bowen &amp; Marlatt (2009). Educational information only, not medical advice.', t["guides_source_note"])

    # Replace Founder Banner
    html = html.replace('Behind the studio', t["founder_eyebrow"])
    html = html.replace('Engineered by Louis Liu', t["founder_title"])
    html = re.sub(r'Senior Mobile Software Engineer with a background in streaming media at scale[\s\S]*?embedded systems\.', t["founder_bio"], html)
    html = html.replace('<span>View Engineer Profile & Resume</span>', f'<span>{t["founder_btn"]}</span>')

    # Replace Contact & Support
    html = re.sub(r'App Support &<br />\s*Studio Inquiries', t["contact_heading"], html)
    html = re.sub(r'Have feedback on one of our apps, need customer support, or want to collaborate\? Reach out directly anytime\.', t["contact_lead"], html)
    html = html.replace('<span>Email Support</span>', f'<span>{t["btn_email"]}</span>')
    html = html.replace('<span id="copyEmailLabel">Copy Email</span>', f'<span id="copyEmailLabel">{t["btn_copy"]}</span>')

    # Replace Footer
    html = html.replace('<span>Copyright © 2026 YS Liu Studio. All Rights Reserved.</span>', f'<span>{t["footer_rights"]}</span>')
    html = html.replace('<a href="/developer/" class="cta-back-top">Developer</a>', f'<a href="/developer/" class="cta-back-top">{t["nav_developer"]}</a>')
    html = html.replace('<a href="/alcohol-free-tracker/guides/" class="cta-back-top">Alcohol-Free</a>', f'<a href="/alcohol-free-tracker/guides/" class="cta-back-top">{t["footer_alcohol_free"]}</a>')
    html = html.replace('<a href="/quit-weed/guides/" class="cta-back-top">Quit Weed</a>', f'<a href="/quit-weed/guides/" class="cta-back-top">{t["footer_quit_weed"]}</a>')
    html = html.replace('<a href="/quit-vaping/guides/" class="cta-back-top">Quit Vaping</a>', f'<a href="/quit-vaping/guides/" class="cta-back-top">{t["footer_quit_vaping"]}</a>')
    html = html.replace('<a href="/levain/guides/" class="cta-back-top">Sourdough</a>', f'<a href="/levain/guides/" class="cta-back-top">{t["footer_sourdough"]}</a>')
    html = html.replace('<span>Back to Top</span>', f'<span>{t["footer_back_top"]}</span>')

    # Replace Lightbox Hint & Toast
    html = html.replace('Use <kbd>←</kbd> <kbd>→</kbd> arrow keys to navigate, <kbd>Esc</kbd> to exit.', t["lightbox_hint"])
    html = html.replace('<span id="toastMessage">Email copied to clipboard</span>', f'<span id="toastMessage">{t["toast_copied"]}</span>')

    with open(target_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✔ Generated studio home: /{locale_code}/index.html")


def update_english_app_page(app_slug: str):
    """Injects canonical, 8 hreflangs and Language Switcher into English app landing page."""
    app_index = os.path.join(ROOT_DIR, app_slug, "index.html")
    if not os.path.exists(app_index):
        return

    with open(app_index, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Injects / updates hreflangs
    hreflangs = generate_hreflang_tags(app_slug)
    if '<link rel="alternate" hreflang="x-default"' not in html:
        canonical_url = f"https://ysliustudio.com/{app_slug}/"
        if '<link rel="canonical"' in html:
            html = re.sub(r'(<link rel="canonical" [^>]+>)', r'\1\n' + hreflangs, html, count=1)
        else:
            html = re.sub(r'(<head[^>]*>)', r'\1\n  <link rel="canonical" href="' + canonical_url + '" />\n' + hreflangs, html, count=1)

    # 2. Add lang-switcher.css if missing
    if 'href="/lang-switcher.css"' not in html:
        html = re.sub(r'(</head>)', r'  <link rel="stylesheet" href="/lang-switcher.css" />\n\1', html, count=1)

    # 3. Add lang-switcher.js before </body>
    if 'src="/lang-switcher.js"' not in html:
        html = html.replace('</body>', '  <script src="/lang-switcher.js" defer></script>\n</body>')

    # 4. Inject switcher UI if not present
    if 'class="lang-switcher"' not in html:
        switcher = generate_language_switcher_html(app_slug, "en")
        if app_slug in ("alcohol-free-tracker", "quit-vaping", "quit-weed", "pill-reminder"):
            html = re.sub(r'(<div class="nav-links"[^>]*>)', r'\1\n          ' + switcher, html, count=1)
        elif app_slug == "grocery-price":
            html = re.sub(r'(<div class="site-nav"[^>]*>)', r'\1\n            ' + switcher, html, count=1)
        elif app_slug == "levain":
            topbar = f"""<div class="wrap" style="display: flex; justify-content: space-between; align-items: center; padding-top: 1.5rem; padding-bottom: 0.5rem;">
  <a href="/" style="font-weight: 700; text-decoration: none; color: inherit; display: inline-flex; align-items: center; gap: 0.5rem;">
    <svg viewBox="0 0 24 24" fill="none" style="width: 20px; height: 20px;"><rect width="24" height="24" rx="6" fill="#00dc82"/><path d="M8 6.8V17.2H16.2" stroke="#0a0b0e" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
    <span>YS Liu Studio</span>
  </a>
  {switcher}
</div>"""
            html = html.replace('<body>', '<body>\n' + topbar, 1)
        elif app_slug == "inkstone":
            topbar = f"""<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem;">
  <a href="/" style="font-weight: 700; text-decoration: none; color: inherit; font-size: 0.95rem;">← YS Liu Studio</a>
  {switcher}
</div>"""
            html = html.replace('<header>', topbar + '\n  <header>', 1)
        elif app_slug == "agricola-scorer":
            topbar = f"""<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
  <a href="/" style="font-weight: bold; text-decoration: none; color: #336633;">← YS Liu Studio</a>
  {switcher}
</div>"""
            html = html.replace('<body>', '<body>\n' + topbar, 1)

    with open(app_index, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✔ Updated English app page: /{app_slug}/index.html with hreflang & switcher.")


def build_localized_app_page(app_slug: str, locale_code: str):
    """Generates /{locale}/{app}/index.html with full localization."""
    app_data = APPS_I18N.get(app_slug, {})
    t = app_data.get(locale_code)
    if not t:
        return

    loc_info = next(l for l in LOCALES if l["code"] == locale_code)
    target_dir = os.path.join(ROOT_DIR, locale_code, app_slug)
    os.makedirs(target_dir, exist_ok=True)
    target_file = os.path.join(target_dir, "index.html")

    canonical_url = get_localized_url(app_slug, locale_code)
    hreflangs = generate_hreflang_tags(app_slug)
    switcher = generate_language_switcher_html(app_slug, locale_code)
    appstore_url = f"https://apps.apple.com/app/apple-store/id{app_data['track_id']}?pt=127596623&ct=lp_{locale_code.replace('-', '')}_hero&mt=8"

    # Feature list bullets
    features_html = ""
    if "features" in t:
        for f in t["features"]:
            features_html += f"""        <li class="app-feat-item">
          <svg class="feat-check" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>
          <span>{f}</span>
        </li>\n"""
    elif "feat1_title" in t:
        for i in range(1, 5):
            title_k = f"feat{i}_title"
            desc_k = f"feat{i}_desc"
            if title_k in t:
                features_html += f"""        <li class="app-feat-item">
          <svg class="feat-check" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>
          <div><strong>{t[title_k]}:</strong> {t[desc_k]}</div>
        </li>\n"""

    page_html = f"""<!DOCTYPE html>
<html lang="{loc_info['html_lang']}">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{t['title']}</title>
  <meta name="description" content="{t['desc']}" />
  <link rel="canonical" href="{canonical_url}" />
{hreflangs}
  <meta property="og:type" content="website" />
  <meta property="og:title" content="{t['title']}" />
  <meta property="og:description" content="{t['desc']}" />
  <meta property="og:url" content="{canonical_url}" />
  <meta property="og:locale" content="{loc_info['og_locale']}" />
  <meta name="apple-itunes-app" content="app-id={app_data['track_id']}, affiliate-data=pt=127596623&ct=sb_{locale_code.replace('-', '')}_lp, app-argument={canonical_url}">
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=Space+Grotesk:wght@600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="/styles.css" />
  <link rel="stylesheet" href="/lang-switcher.css" />
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "{t['hero_title']}",
    "operatingSystem": "iOS",
    "applicationCategory": "UtilitiesApplication",
    "url": "{canonical_url}",
    "downloadUrl": "{appstore_url}",
    "description": "{t['desc']}",
    "offers": {{
      "@type": "Offer",
      "price": "0",
      "priceCurrency": "USD"
    }}
  }}
  </script>
  <style>
    .app-landing-wrap {{ max-width: 980px; margin: 0 auto; padding: 3rem 1.5rem 6rem; }}
    .app-hero-header {{ display: flex; align-items: center; gap: 1.75rem; margin-bottom: 2rem; flex-wrap: wrap; }}
    .app-big-icon {{ width: 96px; height: 96px; border-radius: 22px; box-shadow: 0 10px 25px rgba(0,0,0,0.12); flex-shrink: 0; }}
    .app-hero-info {{ flex: 1; min-width: 280px; }}
    .app-badge {{ display: inline-flex; padding: 0.3rem 0.8rem; background: rgba(0,220,130,0.12); color: #047857; border-radius: 9999px; font-size: 0.82rem; font-weight: 700; margin-bottom: 0.6rem; }}
    .app-main-title {{ font-size: clamp(2rem, 4vw, 2.8rem); font-weight: 900; line-height: 1.15; color: #0a0b0e; margin: 0 0 0.5rem; letter-spacing: -0.025em; }}
    .app-hero-sub {{ font-size: 1.15rem; color: #475569; line-height: 1.6; margin: 0; }}
    .app-cta-row {{ display: flex; gap: 1rem; margin: 2rem 0 3rem; flex-wrap: wrap; align-items: center; }}
    .btn-app-dl {{ display: inline-flex; align-items: center; gap: 0.65rem; background: #0a0b0e; color: #ffffff; padding: 0.95rem 1.85rem; border-radius: 100px; font-size: 1rem; font-weight: 700; text-decoration: none; transition: transform 0.15s ease, background 0.15s ease; box-shadow: 0 8px 20px rgba(0,0,0,0.15); }}
    .btn-app-dl:hover {{ background: #27272a; transform: translateY(-2px); }}
    .btn-app-dl svg {{ width: 20px; height: 20px; }}
    .btn-app-back {{ display: inline-flex; align-items: center; gap: 0.4rem; padding: 0.95rem 1.5rem; border-radius: 100px; border: 1.5px solid #e2e8f0; color: #334155; font-size: 0.95rem; font-weight: 600; text-decoration: none; transition: all 0.15s ease; }}
    .btn-app-back:hover {{ background: #f8fafc; border-color: #cbd5e1; color: #0f172a; }}
    .app-features-card {{ background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 20px; padding: 2.25rem; box-shadow: 0 4px 16px rgba(15,23,42,0.04); margin-bottom: 3.5rem; }}
    .app-features-card h2 {{ font-size: 1.45rem; font-weight: 800; color: #0a0b0e; margin: 0 0 1.25rem; }}
    .app-feat-list {{ list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 1rem; }}
    .app-feat-item {{ display: flex; align-items: flex-start; gap: 0.75rem; font-size: 1rem; color: #334155; line-height: 1.6; }}
    .feat-check {{ width: 20px; height: 20px; color: #059669; flex-shrink: 0; margin-top: 2px; }}
    .app-footer-nav {{ display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #e2e8f0; padding-top: 2rem; flex-wrap: wrap; gap: 1rem; color: #64748b; font-size: 0.9rem; }}
    .app-footer-nav a {{ color: #0f172a; font-weight: 600; text-decoration: none; }}
    .app-footer-nav a:hover {{ text-decoration: underline; }}
  </style>
</head>
<body>

  <!-- Navigation -->
  <header class="navbar">
    <div class="nav-container">
      <a href="/{locale_code}/" class="nav-brand">
        <span class="brand-logo-icon">
          <svg viewBox="0 0 24 24" fill="none">
            <rect width="24" height="24" rx="6" fill="#00dc82" />
            <path d="M8 6.8V17.2H16.2" stroke="#0a0b0e" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </span>
        <span class="brand-name">YS Liu Studio</span>
      </a>

      <div class="nav-cta-wrap">
        {switcher}
        <a href="/{locale_code}/" class="btn btn-nav">
          <span>YS Liu Studio</span>
        </a>
      </div>
    </div>
  </header>

  <main class="app-landing-wrap">
    <!-- Header -->
    <div class="app-hero-header">
      <img src="{app_data['icon']}" alt="{t['hero_title']} Icon" class="app-big-icon" />
      <div class="app-hero-info">
        <span class="app-badge">iOS App · YS Liu Studio</span>
        <h1 class="app-main-title">{t['hero_title']}</h1>
        <p class="app-hero-sub">{t['hero_sub']}</p>
      </div>
    </div>

    <!-- CTA Row -->
    <div class="app-cta-row">
      <a href="{appstore_url}" target="_blank" rel="noopener noreferrer" class="btn-app-dl">
        <svg viewBox="0 0 170 170" fill="currentColor">
          <path d="M150.37 130.25c-2.45 5.66-5.35 10.87-8.71 15.66-4.58 6.53-8.33 11.05-11.22 13.56-4.48 4.12-9.28 6.23-14.42 6.35-3.69 0-8.14-1.05-13.32-3.18-5.19-2.12-9.97-3.17-14.34-3.17-4.58 0-9.49 1.05-14.75 3.17-5.26 2.13-9.5 3.24-12.74 3.35-4.35.13-9.16-1.9-14.42-6.08-3.7-3.04-7.6-7.77-11.71-14.19-5.78-9.02-10.3-19.34-13.57-30.95-3.26-11.61-4.9-22.75-4.9-33.42 0-14.65 3.7-26.65 11.09-36 7.4-9.35 16.63-14.11 27.69-14.28 5.34 0 11.2 1.34 17.58 4.02 6.38 2.68 10.4 4.07 12.06 4.17 2.05 0 6.39-1.48 13.01-4.44 6.63-2.96 12.19-4.27 16.7-3.92 12.38.83 22.35 5.48 29.9 13.97-10.88 6.59-16.2 15.69-15.96 27.32.25 9.17 3.77 16.96 10.58 23.36 6.8 6.4 14.88 10.02 24.23 10.85-2.22 6.64-4.8 12.96-7.75 18.96zM119.22 31.84c0-7.39 2.67-14.23 8.01-20.52 5.34-6.29 11.89-10.28 19.66-11.97.74 7.73-1.68 14.76-7.25 21.08-5.57 6.32-12.37 10.12-20.42 11.41z"/>
        </svg>
        <span>{t.get('download_btn', 'Download on App Store')}</span>
      </a>

      <a href="/{locale_code}/" class="btn-app-back">
        <span>← {t.get('back_studio', 'YS Liu Studio')}</span>
      </a>
    </div>

    <!-- Features Card -->
    <div class="app-features-card">
      <h2>{t.get('features_title', 'Key Features')}</h2>
      <ul class="app-feat-list">
{features_html}      </ul>
    </div>

    <!-- Footer -->
    <footer class="app-footer-nav">
      <div>© {datetime.now().year} YS Liu Studio. All rights reserved.</div>
      <div style="display: flex; gap: 1.5rem;">
        <a href="/{app_slug}/privacy.html">Privacy Policy</a>
        <a href="/{locale_code}/">YS Liu Studio Home</a>
      </div>
    </footer>
  </main>

  <script src="/lang-switcher.js" defer></script>
</body>
</html>"""

    with open(target_file, "w", encoding="utf-8") as f:
        f.write(page_html)
    print(f"✔ Generated app page: /{locale_code}/{app_slug}/index.html")


def build_sitemap_xml():
    """Generates a complete, multi-language sitemap.xml with xhtml:link alternates."""
    today = datetime.now().strftime("%Y-%m-%d")
    sitemap_path = os.path.join(ROOT_DIR, "sitemap.xml")

    # Read existing sitemap to preserve custom guides and tools
    existing_urls = []
    if os.path.exists(sitemap_path):
        with open(sitemap_path, "r", encoding="utf-8") as f:
            content = f.read()
            # Find all <loc>
            existing_urls = re.findall(r'<loc>(https://ysliustudio\.com/[^<]+)</loc>', content)

    # Core URLs to include
    urls_to_include = []

    # 1. Studio Homepages (en + 7 locales)
    for loc in LOCALES:
        code = loc["code"]
        loc_url = get_localized_url("", code)
        urls_to_include.append((loc_url, "1.0", ""))

    # 2. Developer Page
    urls_to_include.append(("https://ysliustudio.com/developer/", "0.9", None))

    # 3. Apps in all 8 locales
    for app in APPS:
        for loc in LOCALES:
            code = loc["code"]
            app_url = get_localized_url(app, code)
            urls_to_include.append((app_url, "0.9" if code == "en" else "0.85", app))

    # 4. Add existing guides and tools that aren't already included
    included_locs = {u[0] for u in urls_to_include}
    for u in existing_urls:
        if u not in included_locs:
            urls_to_include.append((u, "0.7", None))

    # Build XML
    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
        '        xmlns:xhtml="http://www.w3.org/1999/xhtml">',
    ]

    for url, prio, slug in urls_to_include:
        xml_lines.append('  <url>')
        xml_lines.append(f'    <loc>{url}</loc>')
        xml_lines.append(f'    <lastmod>{today}</lastmod>')
        xml_lines.append(f'    <priority>{prio}</priority>')

        # If slug is not None, inject xhtml:link alternates
        if slug is not None:
            xml_lines.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="{get_localized_url(slug, "en")}"/>')
            for loc in LOCALES:
                hl = HREFLANG_MAP[loc["code"]]
                xml_lines.append(f'    <xhtml:link rel="alternate" hreflang="{hl}" href="{get_localized_url(slug, loc["code"])}"/>')

        xml_lines.append('  </url>')

    xml_lines.append('</urlset>')

    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write("\n".join(xml_lines) + "\n")
    print(f"✔ Generated enhanced multi-lingual sitemap.xml ({len(urls_to_include)} URLs).")


def main():
    print("=" * 72)
    print("   YS Liu Studio — Building Multi-Language Architecture & Pages")
    print("=" * 72)

    # 1. Update Root English Homepage
    update_root_index_html()

    # 2. Build 7 Localized Studio Homepages
    for loc in LOCALES:
        if loc["code"] == "en":
            continue
        build_localized_studio_home(loc["code"])

    # 3. Update English App Pages and Build 56 Localized App Landing Pages
    for app in APPS:
        update_english_app_page(app)
        for loc in LOCALES:
            if loc["code"] == "en":
                continue
            build_localized_app_page(app, loc["code"])

    # 4. Generate Enhanced Multi-Lingual Sitemap
    build_sitemap_xml()

    print()
    print("🎉 All 8 languages successfully generated and linked!")


if __name__ == "__main__":
    main()
