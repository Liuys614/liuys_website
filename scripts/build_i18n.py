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
  • Localized App Store attribution campaign tokens (?ct=site-...)
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
        "desc": "YS Liu Studio crafts fast, intuitive, and privacy-first iOS & Android applications for productivity, health, finance, and everyday utility.",
        "nav_apps": "Apps",
        "nav_philosophy": "Philosophy",
        "nav_developer": "Developer",
        "nav_support": "Support",
        "nav_btn": "Meet the Developer",
        "pill_est": "Independent App Studio · Est. 2024",
        "hero_title": "Thoughtful Mobile Apps Crafted for Everyday Clarity.",
        "hero_desc": "<strong>YS Liu Studio</strong> builds native, privacy-first applications designed to solve real everyday problems without the bloat. Every app is engineered with obsessive attention to tactile UX details, zero-friction workflows, and instant offline reliability.",
        "hero_btn_explore": "Explore Our Apps",
        "hero_btn_about": "About Louis Liu (Founder)",
        "dock_label": "8 Production Apps Live on the App Store",
        "marquee_native": "100% Native Performance",
        "marquee_privacy": "Privacy-First Architecture",
        "marquee_ux": "Zero-Friction UX",
        "marquee_ai": "On-Device Intelligence",
        "marquee_accessible": "Accessible by Design",
        "marquee_global": "40+ Global Storefronts",
        "marquee_offline": "Offline-First Reliability",
        "pillar1_num": "01",
        "pillar1_title": "Minimum Steps, Maximum Flow",
        "pillar1_desc": "Every tap counts. We obsess over visual hierarchy, haptics, and accessibility cues to eliminate unnecessary modals and help you finish tasks in seconds.",
        "pillar2_num": "02",
        "pillar2_title": "Privacy & On-Device First",
        "pillar2_desc": "Your health logs, contracts, and personal habits belong to you. We leverage on-device OCR, local databases, and end-to-end encryption without ad trackers.",
        "pillar3_num": "03",
        "pillar3_title": "Enterprise-Grade Craftsmanship",
        "pillar3_desc": "Built with the same architectural rigor used in apps serving millions—combining modern Swift concurrency, rock-solid stability, and native platform polish.",
        "apps_pill": "Product Suite",
        "apps_headline": "Apps by YS Liu Studio",
        "apps_sub": "Explore our lineup of native applications. Click any screenshot to inspect the interface in full resolution.",
        "btn_appstore": "View on App Store",
        "guides_pill": "Evidence-Based Research",
        "guides_headline": "Health & Habit Recovery Guides",
        "guides_sub": "Deep-dive medical, neuroscience, and timeline blueprints crafted to support mindful habit change and long-term sobriety.",
        "founder_eyebrow": "Behind the Studio",
        "founder_title": "Engineered by Louis Liu",
        "founder_bio": "Senior Mobile Software Engineer with a background in streaming media at scale, compiler acceleration, and embedded systems.",
        "founder_btn": "View Engineer Profile & Resume",
        "contact_heading": "App Support &<br />Studio Inquiries",
        "contact_lead": "Have feedback on one of our apps, need customer support, or want to collaborate? Reach out directly anytime.",
        "btn_email": "Send Direct Email",
        "btn_copy": "Copy Email Address",
        "footer_rights": "YS Liu Studio · All rights reserved · Built with pride for iOS & Android.",
    },
    "zh-tw": {
        "title": "YS Liu Studio — 專注極致體驗的獨立行動應用工作室",
        "desc": "YS Liu Studio 打造極速、直覺且重視隱私的 iOS 原生應用，涵蓋生活工具、健康管理、飲食烘焙與財務比價。",
        "nav_apps": "精選應用",
        "nav_philosophy": "設計哲學",
        "nav_developer": "開發者介紹",
        "nav_support": "支援與諮詢",
        "nav_btn": "認識開發者",
        "pill_est": "獨立 App 工作室 · 創立於 2024",
        "hero_title": "為日常生活減負，打造純粹高效的行動體驗。",
        "hero_desc": "<strong>YS Liu Studio</strong> 專注於開發原生、隱私優先且無冗餘干擾的行動應用。我們以對觸覺回饋、零摩擦流程與完全離線運行的極致追求，解決生活中的真實問題。",
        "hero_btn_explore": "探索全部應用",
        "hero_btn_about": "關於創辦人 Louis Liu",
        "dock_label": "8 款正式上架 App Store 的精選作品",
        "marquee_native": "100% 原生極致流暢",
        "marquee_privacy": "本機隱私優先架構",
        "marquee_ux": "零摩擦極簡互動",
        "marquee_ai": "裝置端智慧運算",
        "marquee_accessible": "無障礙友善設計",
        "marquee_global": "全球 40+ 國家在地化",
        "marquee_offline": "完全離線可用保證",
        "pillar1_num": "01",
        "pillar1_title": "極簡步驟，自然流暢",
        "pillar1_desc": "每次點擊都至關重要。我們推敲視覺層級、觸覺回饋與無障礙提示，消除多餘彈窗，讓您在數秒內優雅完成任務。",
        "pillar2_num": "02",
        "pillar2_title": "100% 隱私與裝置端運算",
        "pillar2_desc": "您的健康日誌、簽名合約與個人習慣僅屬於您。我們採用裝置端 OCR、本地資料庫與端對端技術，絕無廣告追蹤碼。",
        "pillar3_num": "03",
        "pillar3_title": "百萬級企業架構標準",
        "pillar3_desc": "以支撐百萬用戶的嚴謹架構打造每一款獨立 App——結合現代 Swift 並行技術、極致穩定性與蘋果原生設計細節。",
        "apps_pill": "完整產品矩陣",
        "apps_headline": "YS Liu Studio 出品應用",
        "apps_sub": "瀏覽我們精心打造的原生應用系列。點擊任一螢幕截圖即可全螢幕檢視介面細節。",
        "btn_appstore": "前往 App Store 開發者頁",
        "guides_pill": "實證科學研究",
        "guides_headline": "健康與戒除習慣科學指南",
        "guides_sub": "基於神經科學、醫學文獻與生理修復時間軸的深度指南，陪伴您完成持續的習慣轉變。",
        "founder_eyebrow": "工作室核心",
        "founder_title": "由 Louis Liu 獨立工程打造",
        "founder_bio": "資深行動軟體工程師，具備大規模影音串流架構、編譯器加速與嵌入式底層開發經驗。",
        "founder_btn": "檢視工程師檔案與履歷",
        "contact_heading": "應用技術支援與<br />商務合作洽詢",
        "contact_lead": "對我們的 App 有任何回饋、需要客戶支援或探討合作機會？歡迎隨時與我們聯繫。",
        "btn_email": "發送電子郵件",
        "btn_copy": "複製 Email 地址",
        "footer_rights": "YS Liu Studio · 版權所有 · 專注為 iOS 打造精緻原生應用。",
    },
    "de": {
        "title": "YS Liu Studio — Unabhängiges Mobile-App-Studio",
        "desc": "YS Liu Studio entwickelt schnelle, intuitive und datenschutzorientierte iOS-Apps für Alltag, Gesundheit, Finanzen und Produktivität.",
        "nav_apps": "Apps",
        "nav_philosophy": "Philosophie",
        "nav_developer": "Entwickler",
        "nav_support": "Support",
        "nav_btn": "Entwickler kennenlernen",
        "pill_est": "Unabhängiges App-Studio · Gegründet 2024",
        "hero_title": "Durchdachte Apps für alltägliche Klarheit.",
        "hero_desc": "<strong>YS Liu Studio</strong> baut native, datenschutzfreundliche Apps ohne Ballast. Jede App zeichnet sich durch haptische Details, reibungslose Abläufe und zuverlässige Offline-Nutzung aus.",
        "hero_btn_explore": "Apps entdecken",
        "hero_btn_about": "Über Louis Liu (Gründer)",
        "dock_label": "8 Apps live im App Store verfügbar",
        "marquee_native": "100% Native Performance",
        "marquee_privacy": "Datenschutz an erster Stelle",
        "marquee_ux": "Reibungslose Bedienung",
        "marquee_ai": "On-Device Intelligenz",
        "marquee_accessible": "Barrierefrei nach Design",
        "marquee_global": "40+ Länder weltweit",
        "marquee_offline": "100% Offline-Zuverlässigkeit",
        "pillar1_num": "01",
        "pillar1_title": "Minimale Schritte, maximaler Fluss",
        "pillar1_desc": "Jede Berührung zählt. Wir optimieren visuelle Hierarchie und Haptik, um unnötige Dialoge zu vermeiden und Aufgaben in Sekunden zu lösen.",
        "pillar2_num": "02",
        "pillar2_title": "Datenschutz & Lokale Speicherung",
        "pillar2_desc": "Ihre Gesundheitsdaten, Dokumente und Gewohnheiten gehören Ihnen. Wir nutzen lokale Datenbanken und OCR ohne Werbetracker.",
        "pillar3_num": "03",
        "pillar3_title": "Handwerkskunst auf Unternehmensniveau",
        "pillar3_desc": "Entwickelt nach Standards, die Millionen von Nutzern tragen—moderne Swift-Parallelität und felsenfeste Stabilität.",
        "apps_pill": "Produktpalette",
        "apps_headline": "Apps von YS Liu Studio",
        "apps_sub": "Entdecken Sie unsere nativen Apps. Klicken Sie auf Screenshots, um das Interface hochauflösend zu betrachten.",
        "btn_appstore": "Im App Store ansehen",
        "guides_pill": "Wissenschaftliche Ratgeber",
        "guides_headline": "Gesundheits- & Erholungs-Leitfäden",
        "guides_sub": "Fundierte neurologische Leitfäden und Zeitpläne für bewusste Lebensgewohnheiten und Regeneration.",
        "founder_eyebrow": "Hinter dem Studio",
        "founder_title": "Entwickelt von Louis Liu",
        "founder_bio": "Senior Mobile Software Engineer mit Hintergrund in Streaming-Architekturen, Compiler-Optimierung und Embedded Systems.",
        "founder_btn": "Profil & Lebenslauf ansehen",
        "contact_heading": "Support &<br />Studio-Anfragen",
        "contact_lead": "Haben Sie Feedback, benötigen Support oder möchten zusammenarbeiten? Schreiben Sie uns jederzeit direkt.",
        "btn_email": "Direkte E-Mail senden",
        "btn_copy": "E-Mail kopieren",
        "footer_rights": "YS Liu Studio · Alle Rechte vorbehalten · Entwickelt mit Leidenschaft für iOS.",
    },
    "fr": {
        "title": "YS Liu Studio — Studio Indépendant d'Applications Mobiles",
        "desc": "YS Liu Studio conçoit des applications iOS rapides, intuitives et respectueuses de la vie privée pour la productivité, la santé et le quotidien.",
        "nav_apps": "Applications",
        "nav_philosophy": "Philosophie",
        "nav_developer": "Développeur",
        "nav_support": "Assistance",
        "nav_btn": "Rencontrer le développeur",
        "pill_est": "Studio d'Apps Indépendant · Fondé en 2024",
        "hero_title": "Des applications mobiles pensées pour la clarté du quotidien.",
        "hero_desc": "<strong>YS Liu Studio</strong> crée des applications natives et respectueuses de la vie privée, conçues pour résoudre vos besoins quotidiens sans superflu ni publicité, avec une fiabilité hors-ligne totale.",
        "hero_btn_explore": "Découvrir nos applications",
        "hero_btn_about": "À propos de Louis Liu",
        "dock_label": "8 applications disponibles sur l'App Store",
        "marquee_native": "Performance 100% Native",
        "marquee_privacy": "Confidentialité Absolue",
        "marquee_ux": "Expérience Fluide Sans Friction",
        "marquee_ai": "Intelligence sur l'Appareil",
        "marquee_accessible": "Accessibilité Intuitive",
        "marquee_global": "40+ Pays Supportés",
        "marquee_offline": "Fiabilité 100% Hors Ligne",
        "pillar1_num": "01",
        "pillar1_title": "Moins d'étapes, plus d'efficacité",
        "pillar1_desc": "Chaque geste compte. Nous éliminons les étapes inutiles pour vous permettre d'accomplir vos tâches en quelques secondes.",
        "pillar2_num": "02",
        "pillar2_title": "Vie privée & Données locales",
        "pillar2_desc": "Vos documents, contrats et données de santé restent sur votre appareil. Zéro publicité, zéro tracker.",
        "pillar3_num": "03",
        "pillar3_title": "Rigueur et qualité logicielle",
        "pillar3_desc": "Conçu avec les exigences des systèmes traitant des millions d'utilisateurs: Swift moderne et stabilité absolue.",
        "apps_pill": "Suite logicielle",
        "apps_headline": "Applications par YS Liu Studio",
        "apps_sub": "Explorez nos applications natives. Cliquez sur une capture pour voir l'interface en haute résolution.",
        "btn_appstore": "Voir sur l'App Store",
        "guides_pill": "Recherche et preuves",
        "guides_headline": "Guides de Santé et d'Habitudes",
        "guides_sub": "Guides médicaux et chronologies physiologiques pour accompagner vos objectifs de bien-être durable.",
        "founder_eyebrow": "Le Fondateur",
        "founder_title": "Développé par Louis Liu",
        "founder_bio": "Ingénieur logiciel mobile senior, spécialiste du streaming à grande échelle, des compilateurs et des systèmes natifs.",
        "founder_btn": "Voir le profil et CV",
        "contact_heading": "Assistance &<br />Contact Studio",
        "contact_lead": "Une question, un retour ou une proposition de collaboration ? Écrivez-nous à tout moment.",
        "btn_email": "Envoyer un e-mail",
        "btn_copy": "Copier l'e-mail",
        "footer_rights": "YS Liu Studio · Tous droits réservés · Conçu avec fierté pour iOS.",
    },
    "ja": {
        "title": "YS Liu Studio — 洗練されたモバイルアプリを届ける個人スタジオ",
        "desc": "YS Liu Studio は、プライバシー最優先で高速・直感的な iOS ネイティブアプリを開発しています。健康管理、日常のツール、パン作り、価格比較をサポート。",
        "nav_apps": "アプリ",
        "nav_philosophy": "設計思想",
        "nav_developer": "開発者",
        "nav_support": "サポート",
        "nav_btn": "開発者について",
        "pill_est": "インディーアプリスタジオ · 2024年設立",
        "hero_title": "毎日の生活に明快さを。細部までこだわったモバイルアプリ。",
        "hero_desc": "<strong>YS Liu Studio</strong> は、無駄を削ぎ落とし、日常の課題を解決するプライバシー重視のネイティブアプリを制作しています。触覚フィードバック、摩擦ゼロの操作感、完全オフライン対応を追求。",
        "hero_btn_explore": "アプリを見る",
        "hero_btn_about": "創業者 Louis Liu について",
        "dock_label": "App Store で配信中の 8 つのアプリ",
        "marquee_native": "100% ネイティブの快適動作",
        "marquee_privacy": "完全ローカル・プライバシー重視",
        "marquee_ux": "迷わないゼロフリクションUI",
        "marquee_ai": "端末内オンデバイス処理",
        "marquee_accessible": "アクセシビリティ対応",
        "marquee_global": "世界40カ国以上で展開",
        "marquee_offline": "オフライン完全動作保証",
        "pillar1_num": "01",
        "pillar1_title": "最小限のタップ、最高の心地よさ",
        "pillar1_desc": "不要なポップアップやモーダルを排除し、視覚階層と触覚振動にこだわることで、数秒で目的を達成できます。",
        "pillar2_num": "02",
        "pillar2_title": "端末内完結のプライバシー保護",
        "pillar2_desc": "健康記録や契約書、生活ログはあなただけのもの。外部サーバーへの送信や広告トラッカーは一切ありません。",
        "pillar3_num": "03",
        "pillar3_title": "数百万規模を支える堅牢な品質",
        "pillar3_desc": "大規模ストリーミングで培った知見をもとに、最新の Swift Concurrency と安定した設計で構築しています。",
        "apps_pill": "プロダクト一覧",
        "apps_headline": "YS Liu Studio のアプリ",
        "apps_sub": "こだわりのネイティブアプリをご覧ください。スクリーンショットをタップして高画質で確認できます。",
        "btn_appstore": "App Store で見る",
        "guides_pill": "科学的エビデンス",
        "guides_headline": "健康・習慣改善ガイド",
        "guides_sub": "神経科学や生理学に基づいた回復タイムラインと、習慣改善を支える実践ガイド。",
        "founder_eyebrow": "スタジオについて",
        "founder_title": "Louis Liu による個人開発",
        "founder_bio": "大規模動画配信、コンパイラ高速化、組込みシステムの経験を持つシニアモバイルソフトウェアエンジニア。",
        "founder_btn": "プロフィールと経歴を見る",
        "contact_heading": "サポート＆<br />お問い合わせ",
        "contact_lead": "アプリへのフィードバックや技術サポート、協業のご相談など、いつでもお気軽にご連絡ください。",
        "btn_email": "メールを送る",
        "btn_copy": "メールアドレスをコピー",
        "footer_rights": "YS Liu Studio · 無断転載を禁じます · iOS 向けに誠心誠意開発。",
    },
    "ko": {
        "title": "YS Liu Studio — 독립 모바일 앱 스튜디오",
        "desc": "YS Liu Studio는 생산성, 건강 관리, 베이킹, 가격 비교를 위한 빠르고 직관적이며 프라이버시를 최우선으로 하는 네이티브 iOS 앱을 만듭니다.",
        "nav_apps": "앱",
        "nav_philosophy": "철학",
        "nav_developer": "개발자",
        "nav_support": "지원",
        "nav_btn": "개발자 소개",
        "pill_est": "인디 앱 스튜디오 · 2024년 설립",
        "hero_title": "일상의 명확함을 위한 섬세한 모바일 앱.",
        "hero_desc": "<strong>YS Liu Studio</strong>는 군더더기 없이 일상의 문제를 해결하는 프라이버시 우선 네이티브 앱을 개발합니다. 손끝에 전해지는 햅틱 피드백, 직관적인 워크플로우, 완벽한 오프라인 안정성을 고집합니다.",
        "hero_btn_explore": "전체 앱 둘러보기",
        "hero_btn_about": "설립자 Louis Liu 소개",
        "dock_label": "App Store에서 서비스 중인 8개의 앱",
        "marquee_native": "100% 네이티브 퍼포먼스",
        "marquee_privacy": "철저한 프라이버시 보호",
        "marquee_ux": "군더더기 없는 직관적 UI",
        "marquee_ai": "온디바이스 인텔리전스",
        "marquee_accessible": "접근성 중심 디자인",
        "marquee_global": "전 세계 40+ 국가 지원",
        "marquee_offline": "오프라인 신뢰성 보장",
        "pillar1_num": "01",
        "pillar1_title": "최소한의 단계, 극대화된 몰입",
        "pillar1_desc": "불필요한 팝업을 줄이고 시각적 계층 구조에 집중하여 몇 초 만에 작업을 완료할 수 있도록 설계합니다.",
        "pillar2_num": "02",
        "pillar2_title": "기기 내 저장 및 프라이버시 우선",
        "pillar2_desc": "건강 기록과 서명 문서는 기기 내에만 안전하게 보관됩니다. 광고 트래커나 무단 서버 업로드가 없습니다.",
        "pillar3_num": "03",
        "pillar3_title": "엔터프라이즈급 소프트웨어 완성도",
        "pillar3_desc": "수백만 사용자를 지원하는 대규모 시스템 수준의 엄격한 Swift 아키텍처와 견고한 안정성을 바탕으로 제작됩니다.",
        "apps_pill": "제품 라인업",
        "apps_headline": "YS Liu Studio의 앱",
        "apps_sub": "정성껏 만든 네이티브 앱을 확인해 보세요. 스크린샷을 클릭하면 고화질로 인터페이스를 확인할 수 있습니다.",
        "btn_appstore": "App Store에서 보기",
        "guides_pill": "과학적 리서치",
        "guides_headline": "건강 및 습관 회복 가이드",
        "guides_sub": "신경과학과 생리학적 회복 타임라인을 바탕으로 건강한 습관 변화를 돕는 심층 가이드.",
        "founder_eyebrow": "스튜디오 소개",
        "founder_title": "개발자 Louis Liu 제작",
        "founder_bio": "대규모 스트리밍 플랫폼, 컴파일러 가속 및 임베디드 소프트웨어 경험을 보유한 시니어 모바일 엔지니어.",
        "founder_btn": "개발자 프로필 및 이력 보기",
        "contact_heading": "고객 지원 및<br />스튜디오 문의",
        "contact_lead": "앱에 대한 의견이나 기술 지원, 협업 제안이 있으신가요? 언제든 편하게 연락해 주세요.",
        "btn_email": "이메일 보내기",
        "btn_copy": "이메일 주소 복사",
        "footer_rights": "YS Liu Studio · All rights reserved · iOS를 위해 정성껏 만들었습니다.",
    },
    "es": {
        "title": "YS Liu Studio — Estudio Independiente de Aplicaciones Móviles",
        "desc": "YS Liu Studio crea aplicaciones iOS rápidas, intuitivas y enfocadas en la privacidad para productividad, salud, finanzas y utilidad cotidiana.",
        "nav_apps": "Aplicaciones",
        "nav_philosophy": "Filosofía",
        "nav_developer": "Desarrollador",
        "nav_support": "Soporte",
        "nav_btn": "Conoce al desarrollador",
        "pill_est": "Estudio de Apps Independiente · Fundado en 2024",
        "hero_title": "Aplicaciones móviles diseñadas para aportar claridad al día a día.",
        "hero_desc": "<strong>YS Liu Studio</strong> construye aplicaciones nativas y privadas diseñadas para resolver problemas reales sin publicidad ni sobrecarga. Cada app cuenta con un cuidado diseño táctil y fiabilidad sin conexión.",
        "hero_btn_explore": "Explorar aplicaciones",
        "hero_btn_about": "Sobre Louis Liu (Fundador)",
        "dock_label": "8 aplicaciones disponibles en el App Store",
        "marquee_native": "Rendimiento 100% Nativo",
        "marquee_privacy": "Privacidad Ante Todo",
        "marquee_ux": "Experiencia Sin Fricción",
        "marquee_ai": "Inteligencia en el Dispositivo",
        "marquee_accessible": "Diseño Accesible",
        "marquee_global": "Más de 40 países",
        "marquee_offline": "Fiabilidad 100% Fuera de Línea",
        "pillar1_num": "01",
        "pillar1_title": "Menos pasos, más agilidad",
        "pillar1_desc": "Cada toque cuenta. Optimizamos la jerarquía visual y la respuesta háptica para completar tareas en segundos.",
        "pillar2_num": "02",
        "pillar2_title": "Privacidad y datos en el dispositivo",
        "pillar2_desc": "Tus datos de salud, contratos y hábitos te pertenecen. Sin rastreadores de anuncios ni subidas a servidores.",
        "pillar3_num": "03",
        "pillar3_title": "Calidad de nivel empresarial",
        "pillar3_desc": "Construido con la misma solidez que sistemas para millones de usuarios: Swift moderno y máxima estabilidad.",
        "apps_pill": "Suite de Productos",
        "apps_headline": "Apps de YS Liu Studio",
        "apps_sub": "Descubre nuestras aplicaciones nativas. Haz clic en las capturas para ver la interfaz en alta resolución.",
        "btn_appstore": "Ver en App Store",
        "guides_pill": "Investigación y Evidencia",
        "guides_headline": "Guías de Salud y Hábitos",
        "guides_sub": "Guías científicas y cronogramas de recuperación fisiológica para apoyar cambios duraderos.",
        "founder_eyebrow": "Detrás del Estudio",
        "founder_title": "Desarrollado por Louis Liu",
        "founder_bio": "Ingeniero de software móvil sénior con experiencia en streaming a escala, compiladores y sistemas embebidos.",
        "founder_btn": "Ver perfil y currículum",
        "contact_heading": "Soporte y<br />Consultas del Estudio",
        "contact_lead": "¿Tienes comentarios, necesitas soporte o quieres colaborar? Escríbenos directamente cuando quieras.",
        "btn_email": "Enviar correo directo",
        "btn_copy": "Copiar correo",
        "footer_rights": "YS Liu Studio · Todos los derechos reservados · Hecho con orgullo para iOS.",
    },
    "it": {
        "title": "YS Liu Studio — Studio Indipendente di App Mobili",
        "desc": "YS Liu Studio crea app iOS native, veloci e incentrate sulla privacy per produttività, salute, finanza e uso quotidiano.",
        "nav_apps": "Applicazioni",
        "nav_philosophy": "Filosofia",
        "nav_developer": "Sviluppatore",
        "nav_support": "Supporto",
        "nav_btn": "Incontra lo sviluppatore",
        "pill_est": "Studio di App Indipendente · Fondato nel 2024",
        "hero_title": "App mobili pensate per portare chiarezza nella vita di tutti i giorni.",
        "hero_desc": "<strong>YS Liu Studio</strong> progetta applicazioni native incentrate sulla privacy per risolvere problemi reali senza complessità inutili. Massima attenzione ai dettagli tattili e funzionamento 100% offline.",
        "hero_btn_explore": "Scopri le nostre app",
        "hero_btn_about": "Chi è Louis Liu (Fondatore)",
        "dock_label": "8 app disponibili su App Store",
        "marquee_native": "Prestazioni 100% Native",
        "marquee_privacy": "Architettura Privacy-First",
        "marquee_ux": "Interfaccia Senza Attrito",
        "marquee_ai": "Elaborazione Locale sul Dispositivo",
        "marquee_accessible": "Accessibilità Nativa",
        "marquee_global": "40+ Paesi nel Mondo",
        "marquee_offline": "Funzionamento Offline Garantito",
        "pillar1_num": "01",
        "pillar1_title": "Minimi passaggi, massimo flusso",
        "pillar1_desc": "Ogni tocco conta. Riduciamo all'essenziale i passaggi per consentirti di completare le attività in pochi istanti.",
        "pillar2_num": "02",
        "pillar2_title": "Privacy e dati solo sul dispositivo",
        "pillar2_desc": "I tuoi dati sanitari, i contratti e le abitudini appartengono solo a te. Nessun tracker pubblicitario.",
        "pillar3_num": "03",
        "pillar3_title": "Rigore ingegneristico di alto livello",
        "pillar3_desc": "Sviluppato con gli standard utilizzati per app con milioni di utenti: Swift moderno e stabilità assoluta.",
        "apps_pill": "Suite di Prodotti",
        "apps_headline": "App di YS Liu Studio",
        "apps_sub": "Esplora le nostre app native. Tocca una schermata per vederla ad alta risoluzione.",
        "btn_appstore": "Vedi su App Store",
        "guides_pill": "Evidenze Scientifiche",
        "guides_headline": "Guide su Salute e Recupero Abitudini",
        "guides_sub": "Guide mediche e cronologie fisiologiche per supportare cambiamenti consapevoli e duraturi.",
        "founder_eyebrow": "Dietro lo Studio",
        "founder_title": "Sviluppato da Louis Liu",
        "founder_bio": "Senior Mobile Software Engineer con esperienza in streaming su larga scala, ottimizzazione compilatori e sistemi nativi.",
        "founder_btn": "Visualizza profilo e CV",
        "contact_heading": "Supporto App &<br />Richieste di Contatto",
        "contact_lead": "Hai domande, suggerimenti o proposte di collaborazione? Scrivici direttamente in qualsiasi momento.",
        "btn_email": "Invia un'e-mail",
        "btn_copy": "Copia indirizzo e-mail",
        "footer_rights": "YS Liu Studio · Tutti i diritti riservati · Progettato con cura per iOS.",
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
    html = re.sub(r'<meta property="og:description" content="[^"]*" />', f'<meta property="og:description" content="{t["desc"]}" />', html, count=1)

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
    html = html.replace('8 Production Apps Live on the App Store', t["dock_label"])
    html = html.replace('6 Production Apps Live on the App Store', t["dock_label"])

    # Replace Marquee
    html = html.replace('100% Native Performance', t["marquee_native"])
    html = html.replace('Privacy-First Architecture', t["marquee_privacy"])
    html = html.replace('Zero-Friction UX', t["marquee_ux"])
    html = html.replace('On-Device Intelligence', t["marquee_ai"])
    html = html.replace('Accessible by Design', t["marquee_accessible"])
    html = html.replace('40+ Global Storefronts', t["marquee_global"])
    html = html.replace('Offline-First Reliability', t["marquee_offline"])

    # Replace Pillars
    html = html.replace('Minimum Steps, Maximum Flow', t["pillar1_title"])
    html = re.sub(r'Every tap counts\. We obsess over visual hierarchy[\s\S]*?finish tasks in seconds\.', t["pillar1_desc"], html)
    html = html.replace('Privacy & On-Device First', t["pillar2_title"])
    html = re.sub(r'Your health logs, contracts, and personal habits belong to you[\s\S]*?without ad trackers\.', t["pillar2_desc"], html)
    html = html.replace('Enterprise-Grade Craftsmanship', t["pillar3_title"])
    html = re.sub(r'Built with the same architectural rigor used in apps serving millions[\s\S]*?native platform polish\.', t["pillar3_desc"], html)

    # Replace Apps Section Headers
    html = html.replace('<span class="pill-text">Product Suite</span>', f'<span class="pill-text">{t["apps_pill"]}</span>')
    html = html.replace('<h2 class="projects-headline">Apps by YS Liu Studio</h2>', f'<h2 class="projects-headline">{t["apps_headline"]}</h2>')
    html = re.sub(r'Explore our lineup of native applications\. Click any screenshot to inspect the interface in full resolution\.', t["apps_sub"], html)
    html = html.replace('<span>View on App Store</span>', f'<span>{t["btn_appstore"]}</span>')

    # Replace Guides Section Headers
    html = html.replace('<span class="pill-text">Evidence-Based Research</span>', f'<span class="pill-text">{t["guides_pill"]}</span>')
    html = html.replace('<h2 class="projects-headline">Health & Habit Recovery Guides</h2>', f'<h2 class="projects-headline">{t["guides_headline"]}</h2>')
    html = re.sub(r'Deep-dive medical, neuroscience, and timeline blueprints crafted to support mindful habit change and long-term sobriety\.', t["guides_sub"], html)

    # Replace Founder Banner
    html = html.replace('Behind the Studio', t["founder_eyebrow"])
    html = html.replace('Engineered by Louis Liu', t["founder_title"])
    html = re.sub(r'Senior Mobile Software Engineer with a background in streaming media at scale[\s\S]*?embedded systems\.', t["founder_bio"], html)
    html = html.replace('<span>View Engineer Profile & Resume</span>', f'<span>{t["founder_btn"]}</span>')

    # Replace Contact & Support
    html = re.sub(r'App Support &<br />\s*Studio Inquiries', t["contact_heading"], html)
    html = re.sub(r'Have feedback on one of our apps, need customer support, or want to collaborate\? Reach out directly anytime\.', t["contact_lead"], html)
    html = html.replace('<span>Send Direct Email</span>', f'<span>{t["btn_email"]}</span>')
    html = html.replace('<span>Copy Email Address</span>', f'<span>{t["btn_copy"]}</span>')

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
    appstore_url = f"https://apps.apple.com/app/apple-store/id{app_data['track_id']}?pt=127596623&ct=site-{app_slug}-{locale_code}&mt=8"

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
  <meta name="apple-itunes-app" content="app-id={app_data['track_id']}, affiliate-data=pt=127596623&ct=site-{app_slug}-{locale_code}, app-argument={canonical_url}">
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
