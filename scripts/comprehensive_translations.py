"""
Comprehensive Deep Translations for all 8 apps across 7 target languages
"""

COMMON_DICT = {   'de': {   '100% On-Device': '100% Lokal auf dem Gerät',
              'Anti-Shame': 'Ohne Beschämung',
              'App Store': 'App Store',
              'Back to Home': 'Zur Startseite',
              'CRAVING INTENSITY': 'INTENSITÄT',
              'Calm 4-6 breath': 'Ruhiger 4-6 Atemzug',
              'Calm 4-6 breathing': 'Ruhige 4-6 Atmung',
              'Compare': 'Vergleich',
              'Craving Crests': 'Verlangen erreicht Höhepunkt',
              'Craving SOS': 'Verlangen SOS',
              'DOWNLOAD NOW': 'JETZT HERUNTERLADEN',
              'Day 7 · restoring': 'Tag 7 · Regeneration',
              'Deep REM Sleep': 'Tiefer REM-Schlaf',
              'Download Free': 'Kostenlos herunterladen',
              'Download on the': 'Laden im',
              'Download on the App Store': 'Im App Store laden',
              'Explore the Science ↓': 'Erholung & Wissenschaft ansehen ↓',
              'FAQ': 'FAQ',
              'FREQUENTLY ASKED QUESTIONS': 'HÄUFIG GESTELLTE FRAGEN',
              'For iPhone & iPad · Free to start · 100% Private': 'Für iPhone & iPad · Kostenlos starten · 100% lokal '
                                                                  '& privat',
              'Guides': 'Leitfäden',
              'HOW WE COMPARE': 'UNSER VERGLEICH',
              'ON-DEVICE PRIVACY': '100% LOKALE PRIVATSPHÄRE',
              'PASS': 'ABKLINGEN',
              'PEAK': 'HÖHEPUNKT',
              'Privacy Policy': 'Datenschutz',
              'RISE': 'AUFSTIEG',
              'Ready for a calmer kind of progress?': 'Bereit für einen ruhigeren, nachhaltigen Fortschritt?',
              'Research-informed': 'Wissenschaftsbasiert',
              'SCREEN GALLERY': 'SCREENSHOTS',
              'Science': 'Wissenschaft',
              'Screens': 'Screenshots',
              'Support': 'Support',
              'THE SCIENCE': 'DIE WISSENSCHAFT',
              'TIME &rarr;': 'ZEITVERLAUF →',
              'TIME →': 'ZEITVERLAUF →',
              'Terms of Service': 'Nutzungsbedingungen',
              'The Science': 'Wissenschaftliche Basis',
              'The science': 'Wissenschaftliche Basis',
              'View All Guides →': 'Alle Leitfäden ansehen →',
              'Zero Accounts': 'Ohne Registrierung'},
    'es': {   '100% On-Device': '100% en tu dispositivo',
              'Anti-Shame': 'Sin culpa ni humillación',
              'App Store': 'App Store',
              'Back to Home': 'Volver al inicio',
              'CRAVING INTENSITY': 'INTENSIDAD',
              'Calm 4-6 breath': 'Respiración pausada 4-6s',
              'Calm 4-6 breathing': 'Respiración 4-6s',
              'Compare': 'Comparativa',
              'Craving Crests': 'Pico de ansia superado',
              'Craving SOS': 'SOS Ansias',
              'DOWNLOAD NOW': 'DESCARGAR AHORA',
              'Day 7 · restoring': 'Día 7 · en recuperación',
              'Deep REM Sleep': 'Sueño REM profundo',
              'Download Free': 'Descargar gratis',
              'Download on the': 'Descargar en',
              'Download on the App Store': 'Descargar en App Store',
              'Explore the Science ↓': 'Explora la ciencia médica ↓',
              'FAQ': 'Preguntas frecuentes',
              'FREQUENTLY ASKED QUESTIONS': 'PREGUNTAS FRECUENTES',
              'For iPhone & iPad · Free to start · 100% Private': 'Para iPhone y iPad · Empieza gratis · 100% privado '
                                                                  'en tu dispositivo',
              'Guides': 'Guías',
              'HOW WE COMPARE': 'CÓMO NOS COMPARAMOS',
              'ON-DEVICE PRIVACY': 'PRIVACIDAD 100% EN EL DISPOSITIVO',
              'PASS': 'BAJADA',
              'PEAK': 'PICO',
              'Privacy Policy': 'Privacidad',
              'RISE': 'SUBIDA',
              'Ready for a calmer kind of progress?': '¿Listo para un progreso más tranquilo y sin agobios?',
              'Research-informed': 'Basado en estudios',
              'SCREEN GALLERY': 'GALERÍA DE CAPTURAS',
              'Science': 'Ciencia',
              'Screens': 'Capturas',
              'Support': 'Soporte',
              'THE SCIENCE': 'LA CIENCIA',
              'TIME &rarr;': 'PASO DEL TIEMPO →',
              'TIME →': 'PASO DEL TIEMPO →',
              'Terms of Service': 'Términos de servicio',
              'The Science': 'Base científica',
              'The science': 'Base científica',
              'View All Guides →': 'Ver todas las guías →',
              'Zero Accounts': 'Sin cuentas ni registros'},
    'fr': {   '100% On-Device': "100% sur l'appareil",
              'Anti-Shame': 'Sans culpabilisation',
              'App Store': 'l’App Store',
              'Back to Home': 'Accueil',
              'CRAVING INTENSITY': 'INTENSITÉ',
              'Calm 4-6 breath': 'Respiration apaisante 4-6s',
              'Calm 4-6 breathing': 'Respiration 4-6s',
              'Compare': 'Comparatif',
              'Craving Crests': "Pic de l'envie",
              'Craving SOS': 'SOS Envie',
              'DOWNLOAD NOW': 'TÉLÉCHARGER MAINTENANT',
              'Day 7 · restoring': 'Jour 7 · régénération en cours',
              'Deep REM Sleep': 'Sommeil paradoxal profond',
              'Download Free': 'Télécharger gratuitement',
              'Download on the': 'Télécharger dans',
              'Download on the App Store': "Télécharger sur l'App Store",
              'Explore the Science ↓': 'Découvrir la science ↓',
              'FAQ': 'FAQ',
              'FREQUENTLY ASKED QUESTIONS': 'QUESTIONS FRÉQUENTES',
              'For iPhone & iPad · Free to start · 100% Private': "Pour iPhone & iPad · Gratuit · 100% sur l'appareil",
              'Guides': 'Guides',
              'HOW WE COMPARE': 'NOTRE COMPARATIF',
              'ON-DEVICE PRIVACY': 'CONFIDENTIALITÉ 100% LOCALE',
              'PASS': 'APAISSEMENT',
              'PEAK': 'PIC',
              'Privacy Policy': 'Confidentialité',
              'RISE': 'MONTÉE',
              'Ready for a calmer kind of progress?': 'Prêt pour une progression plus sereine et durable ?',
              'Research-informed': 'Fondé sur la recherche',
              'SCREEN GALLERY': "GALERIE D'ÉCRANS",
              'Science': 'Science',
              'Screens': 'Écrans',
              'Support': 'Support',
              'THE SCIENCE': 'LA SCIENCE',
              'TIME &rarr;': 'TEMPS ÉCOULÉ →',
              'TIME →': 'TEMPS ÉCOULÉ →',
              'Terms of Service': "Conditions d'utilisation",
              'The Science': 'Fondements scientifiques',
              'The science': 'Fondements scientifiques',
              'View All Guides →': 'Voir tous les guides →',
              'Zero Accounts': 'Sans compte requis'},
    'it': {   '100% On-Device': '100% sul tuo dispositivo',
              'Anti-Shame': 'Senza giudizi né sensi di colpa',
              'App Store': 'App Store',
              'Back to Home': 'Torna alla home',
              'CRAVING INTENSITY': 'INTENSITÀ',
              'Calm 4-6 breath': 'Respirazione calma 4-6s',
              'Calm 4-6 breathing': 'Respirazione 4-6s',
              'Compare': 'Confronta',
              'Craving Crests': 'Picco della voglia superato',
              'Craving SOS': 'SOS Voglia',
              'DOWNLOAD NOW': 'SCARICA ORA',
              'Day 7 · restoring': 'Giorno 7 · rigenerazione in corso',
              'Deep REM Sleep': 'Sonno REM profondo',
              'Download Free': 'Scarica gratis',
              'Download on the': 'Scarica su',
              'Download on the App Store': 'Scarica su App Store',
              'Explore the Science ↓': 'Esplora i benefici scientifici ↓',
              'FAQ': 'Domande frequenti',
              'FREQUENTLY ASKED QUESTIONS': 'DOMANDE FREQUENTI',
              'For iPhone & iPad · Free to start · 100% Private': 'Per iPhone e iPad · Inizia gratis · 100% offline e '
                                                                  'privato',
              'Guides': 'Guide',
              'HOW WE COMPARE': 'IL NOSTRO CONFRONTO',
              'ON-DEVICE PRIVACY': 'PRIVACY 100% SUL DISPOSITIVO',
              'PASS': 'CALO',
              'PEAK': 'PICCO',
              'Privacy Policy': 'Privacy',
              'RISE': 'SALITA',
              'Ready for a calmer kind of progress?': 'Pronto per un percorso sereno e privo di stress?',
              'Research-informed': 'Basato sulla scienza',
              'SCREEN GALLERY': 'GALLERIA SCHERMATE',
              'Science': 'Scienza',
              'Screens': 'Schermate',
              'Support': 'Supporto',
              'THE SCIENCE': 'LA SCIENZA',
              'TIME &rarr;': 'PASSARE DEL TEMPO →',
              'TIME →': 'PASSARE DEL TEMPO →',
              'Terms of Service': 'Termini di servizio',
              'The Science': 'Basi scientifiche',
              'The science': 'Basi scientifiche',
              'View All Guides →': 'Visualizza tutte le guide →',
              'Zero Accounts': 'Nessun account richiesto'},
    'ja': {   '100% On-Device': '100%端末内保存',
              'Anti-Shame': '罪悪感を与えない設計',
              'App Store': 'App Store',
              'Back to Home': 'ホームに戻る',
              'CRAVING INTENSITY': '渇望の強さ',
              'Calm 4-6 breath': '4-6秒の穏やかな呼吸',
              'Calm 4-6 breathing': '4-6秒の呼吸法',
              'Compare': '特徴比較',
              'Craving Crests': '欲求のピーク',
              'Craving SOS': '渇望緊急SOS',
              'DOWNLOAD NOW': '今すぐダウンロード',
              'Day 7 · restoring': '7日目 · 回復進行中',
              'Deep REM Sleep': '深いレム睡眠',
              'Download Free': '無料ダウンロード',
              'Download on the': '入手する',
              'Download on the App Store': 'App Storeからダウンロード',
              'Explore the Science ↓': '科学的根拠を見る ↓',
              'FAQ': 'よくある質問',
              'FREQUENTLY ASKED QUESTIONS': 'よくある質問',
              'For iPhone & iPad · Free to start · 100% Private': 'iPhone & iPad対応 · 無料で利用開始 · 100%完全オンデバイス',
              'Guides': 'ガイド',
              'HOW WE COMPARE': '他社アプリとの比較',
              'ON-DEVICE PRIVACY': '完全オンデバイスの安心',
              'PASS': '消退',
              'PEAK': '頂点',
              'Privacy Policy': 'プライバシーポリシー',
              'RISE': '上昇',
              'Ready for a calmer kind of progress?': 'もっと穏やかで前向きな一歩を踏み出しませんか？',
              'Research-informed': '医学研究に基づく設計',
              'SCREEN GALLERY': 'アプリ画面一覧',
              'Science': '科学的根拠',
              'Screens': 'スクリーンショット',
              'Support': 'サポート',
              'THE SCIENCE': '科学的根拠',
              'TIME &rarr;': '時間経過 →',
              'TIME →': '時間経過 →',
              'Terms of Service': '利用規約',
              'The Science': '科学的根拠',
              'The science': '科学的根拠',
              'View All Guides →': 'すべてのガイドを見る →',
              'Zero Accounts': 'アカウント登録不要'},
    'ko': {   '100% On-Device': '100% 온디바이스',
              'Anti-Shame': '자책 없는 긍정적 트래킹',
              'App Store': 'App Store',
              'Back to Home': '홈으로 돌아가기',
              'CRAVING INTENSITY': '갈망 강도',
              'Calm 4-6 breath': '4-6초 편안한 호흡',
              'Calm 4-6 breathing': '4-6초 편안한 호흡',
              'Compare': '비교하기',
              'Craving Crests': '갈망의 파도 정점',
              'Craving SOS': '갈망 긴급 SOS',
              'DOWNLOAD NOW': '지금 다운로드',
              'Day 7 · restoring': '7일차 · 회복 진행 중',
              'Deep REM Sleep': '깊은 렘수면',
              'Download Free': '무료 다운로드',
              'Download on the': '다운로드하기',
              'Download on the App Store': 'App Store에서 다운로드',
              'Explore the Science ↓': '신체 회복 과학 탐색하기 ↓',
              'FAQ': '자주 묻는 질문',
              'FREQUENTLY ASKED QUESTIONS': '자주 묻는 질문',
              'For iPhone & iPad · Free to start · 100% Private': 'iPhone 및 iPad 지원 · 무료 시작 · 100% 기기 내 개인정보 보호',
              'Guides': '가이드',
              'HOW WE COMPARE': '비교 및 장점',
              'ON-DEVICE PRIVACY': '100% 기기 내 개인정보 보호',
              'PASS': '소멸',
              'PEAK': '정점',
              'Privacy Policy': '개인정보 처리방침',
              'RISE': '상승',
              'Ready for a calmer kind of progress?': '더 편안하고 흔들림 없는 진전을 시작할 준비가 되셨나요?',
              'Research-informed': '임상 연구 기반',
              'SCREEN GALLERY': '화면 둘러보기',
              'Science': '과학적 근거',
              'Screens': '스크린샷',
              'Support': '지원',
              'THE SCIENCE': '과학적 근거',
              'TIME &rarr;': '시간 흐름 →',
              'TIME →': '시간 흐름 →',
              'Terms of Service': '이용약관',
              'The Science': '과학적 근거',
              'The science': '과학적 근거',
              'View All Guides →': '모든 가이드 보기 →',
              'Zero Accounts': '계정 가입 없음'},
    'zh-tw': {   '100% On-Device': '100% 本地存儲',
                 'Anti-Shame': '不評判零壓力',
                 'App Store': 'App Store',
                 'Back to Home': '返回首頁',
                 'CRAVING INTENSITY': '渴望強度',
                 'Calm 4-6 breath': '4-6 秒緩慢深呼吸',
                 'Calm 4-6 breathing': '4-6 秒緩慢深呼吸',
                 'Compare': '特色比較',
                 'Craving Crests': '渴望浪潮高峰',
                 'Craving SOS': '渴望緊急舒緩 (SOS)',
                 'DOWNLOAD NOW': '立即前往下載',
                 'Day 7 · restoring': '第 7 天 · 逐步修復中',
                 'Deep REM Sleep': '深度 REM 睡眠',
                 'Download Free': '免費下載',
                 'Download on the': '前往下載於',
                 'Download on the App Store': '在 App Store 上下載',
                 'Explore the Science ↓': '探索身體修復科學 ↓',
                 'FAQ': '常見問題',
                 'FREQUENTLY ASKED QUESTIONS': '常見問題解答',
                 'For iPhone & iPad · Free to start · 100% Private': '適用於 iPhone 與 iPad · 免費開始 · 100% 離線隱私保護',
                 'Guides': '實用指南',
                 'HOW WE COMPARE': '產品優勢對比',
                 'ON-DEVICE PRIVACY': '100% 離線隱私保護',
                 'PASS': '消退',
                 'PEAK': '頂峰',
                 'Privacy Policy': '隱私權政策',
                 'RISE': '升起',
                 'Ready for a calmer kind of progress?': '準備好展開更平靜、無負擔的進步了嗎？',
                 'Research-informed': '實證醫學研究',
                 'SCREEN GALLERY': '精美介面展示',
                 'Science': '科學依據',
                 'Screens': '畫面展示',
                 'Support': '支援中心',
                 'THE SCIENCE': '科學實證',
                 'TIME &rarr;': '時間軸 →',
                 'TIME →': '時間軸 →',
                 'Terms of Service': '服務條款',
                 'The Science': '科學實證原理',
                 'The science': '科學實證原理',
                 'View All Guides →': '瀏覽所有實用指南 →',
                 'Zero Accounts': '免註冊免帳號'}}

DEEP_APP_CONTENT = {   'alcohol-free-tracker': {   'de': {   '01 · URGE SURFING': '01 · URGE SURFING (VERLANGEN SURFEN)',
                                          '02 · BODY RECOVERY': '02 · KÖRPERLICHE REGENERATION',
                                          '1 Year': '1 Jahr',
                                          '14 Days': '14 Tage',
                                          '24 Hours': '24 Stunden',
                                          '30 Days': '30 Tage',
                                          '7 Days': '7 Tage',
                                          '72 Hours': '72 Stunden',
                                          '8 Hours': '8 Stunden',
                                          '90 Days': '90 Tage',
                                          'A cue — 5 PM, the fridge, a bad day.': 'Der Auslöser — 17 Uhr, der '
                                                                                  'Kühlschrank, ein schwerer Tag.',
                                          'Acute Detox': 'Akute Entgiftung',
                                          'Alcohol Free Tracker': 'Alcohol Free Tracker',
                                          'An urge rises, peaks, and passes — if you let it.': 'Ein Verlangen steigt '
                                                                                               'auf, erreicht seinen '
                                                                                               'Höhepunkt und vergeht '
                                                                                               '— wenn du es zulässt.',
                                          'Answers when you need them.': 'Antworten auf deine Fragen',
                                          'Blood alcohol reaches zero. Blood oxygen levels begin normalizing.': 'Blutalkohol '
                                                                                                                'erreicht '
                                                                                                                'Null. '
                                                                                                                'Der '
                                                                                                                'Sauerstoffgehalt '
                                                                                                                'im '
                                                                                                                'Blut '
                                                                                                                'normalisiert '
                                                                                                                'sich.',
                                          'Blood pressure stabilizes. Risk of acute cardiac events begins to drop.': 'Blutdruck '
                                                                                                                     'stabilisiert '
                                                                                                                     'sich. '
                                                                                                                     'Das '
                                                                                                                     'Risiko '
                                                                                                                     'akuter '
                                                                                                                     'Herz-Kreislauf-Probleme '
                                                                                                                     'sinkt.',
                                          'Breathe until it fades on its own.': 'Atme ruhig weiter, bis die Welle von '
                                                                                'selbst abebbt.',
                                          'CRAVING INTENSITY': 'INTENSITÄT DES VERLANGENS',
                                          'Cravings are waves.': 'Verlangen kommt in Wellen.',
                                          'Deep REM Sleep': 'Tiefer REM-Schlaf',
                                          'Dopamine Re-sensitizing': 'Dopamin-Resensibilisierung',
                                          'From evening craving relief to long-term milestones.': 'Von der Linderung '
                                                                                                  'abendlicher Gelüste '
                                                                                                  'bis hin zu '
                                                                                                  'Meilensteinen.',
                                          'Heart & Circulation': 'Herz & Kreislauf',
                                          'Immune & Neural Clarity': 'Immunsystem & geistige Klarheit',
                                          'Liver & Gut Repair': 'Leber- & Darm-Erholung',
                                          'Liver fat drops up to 15%. Gut lining begins rebuilding.': 'Leberfett sinkt '
                                                                                                      'um bis zu 15%. '
                                                                                                      'Die Darmwand '
                                                                                                      'beginnt sich zu '
                                                                                                      'regenerieren.',
                                          'Long-Term Cellular Health': 'Langfristige Zellgesundheit',
                                          'Metabolism & Skin': 'Stoffwechsel & Hautbild',
                                          'Natural pleasure responses start coming back. Anxiety begins receding.': 'Natürliche '
                                                                                                                    'Freude '
                                                                                                                    'kehrt '
                                                                                                                    'zurück. '
                                                                                                                    'Grundlose '
                                                                                                                    'Ängste '
                                                                                                                    'lassen '
                                                                                                                    'spürbar '
                                                                                                                    'nach.',
                                          "Notice it in your body. Don't argue with it.": 'Spüre es in deinem Körper. '
                                                                                          'Kämpfe nicht dagegen an.',
                                          'Pass': 'Abklingen',
                                          'Peak': 'Höhepunkt',
                                          'Repair begins hours after your last drink.': 'Die Regeneration beginnt '
                                                                                        'wenige Stunden nach dem '
                                                                                        'letzten Getränk.',
                                          'Rise': 'Aufstieg',
                                          'Significantly lower lifetime cancer, cardiovascular, and liver disease risk.': 'Deutlich '
                                                                                                                          'geringeres '
                                                                                                                          'Lebenszeitrisiko '
                                                                                                                          'für '
                                                                                                                          'Krebs, '
                                                                                                                          'Herz- '
                                                                                                                          'und '
                                                                                                                          'Lebererkrankungen.',
                                          'Sleep architecture begins to reset. Dreams return. Morning brain fog lifts.': 'Schlafstruktur '
                                                                                                                         'regeneriert '
                                                                                                                         'sich. '
                                                                                                                         'Träume '
                                                                                                                         'kehren '
                                                                                                                         'zurück. '
                                                                                                                         'Der '
                                                                                                                         'Morgennebel '
                                                                                                                         'weicht.',
                                          'TIME &rarr;': 'ZEITVERLAUF →',
                                          'TIME →': 'ZEITVERLAUF →',
                                          'The old way broke your spirit. The new way protects your momentum.': 'Alte '
                                                                                                                'Methoden '
                                                                                                                'demotivieren. '
                                                                                                                'Unser '
                                                                                                                'Ansatz '
                                                                                                                'schützt '
                                                                                                                'deine '
                                                                                                                'Motivation.',
                                          'Traditional Sobriety Apps': 'Herkömmliche Nüchternheits-Apps',
                                          'Visceral fat drops. Facial redness and systemic puffiness clear noticeably.': 'Viszeralfett '
                                                                                                                         'sinkt. '
                                                                                                                         'Gesichtsrötungen '
                                                                                                                         'und '
                                                                                                                         'Schwellungen '
                                                                                                                         'klingen '
                                                                                                                         'deutlich '
                                                                                                                         'ab.',
                                          'White blood cell counts normalize. Neurogenesis accelerates. Focus locks in.': 'Weiße '
                                                                                                                          'Blutkörperchen '
                                                                                                                          'normalisieren '
                                                                                                                          'sich. '
                                                                                                                          'Neurogenese '
                                                                                                                          'beschleunigt. '
                                                                                                                          'Fokus '
                                                                                                                          'schärft '
                                                                                                                          'sich.',
                                          'Your body is already healing.': 'Dein Körper heilt bereits.',
                                          'Your personal tracking does not need an audience.': 'Dein persönlicher '
                                                                                               'Fortschritt braucht '
                                                                                               'kein Publikum.'},
                                'es': {   '01 · URGE SURFING': '01 · TÉCNICA URGE SURFING',
                                          '02 · BODY RECOVERY': '02 · RECUPERACIÓN FÍSICA',
                                          '1 Year': '1 Año',
                                          '14 Days': '14 Días',
                                          '24 Hours': '24 Horas',
                                          '30 Days': '30 Días',
                                          '7 Days': '7 Días',
                                          '72 Hours': '72 Horas',
                                          '8 Hours': '8 Horas',
                                          '90 Days': '90 Días',
                                          'A cue — 5 PM, the fridge, a bad day.': 'El detonante — las 19h, la nevera, '
                                                                                  'un día difícil.',
                                          'Acute Detox': 'Desintoxicación aguda',
                                          'Alcohol Free Tracker': 'Alcohol Free Tracker',
                                          'An urge rises, peaks, and passes — if you let it.': 'Un ansia sube, llega '
                                                                                               'al pico y pasa — si la '
                                                                                               'dejas fluir.',
                                          'Answers when you need them.': 'Respuestas a todas tus preguntas',
                                          'Blood alcohol reaches zero. Blood oxygen levels begin normalizing.': 'El '
                                                                                                                'alcohol '
                                                                                                                'en '
                                                                                                                'sangre '
                                                                                                                'llega '
                                                                                                                'a '
                                                                                                                'cero. '
                                                                                                                'El '
                                                                                                                'oxígeno '
                                                                                                                'en '
                                                                                                                'sangre '
                                                                                                                'se '
                                                                                                                'normaliza.',
                                          'Blood pressure stabilizes. Risk of acute cardiac events begins to drop.': 'La '
                                                                                                                     'presión '
                                                                                                                     'arterial '
                                                                                                                     'se '
                                                                                                                     'estabiliza. '
                                                                                                                     'Baja '
                                                                                                                     'el '
                                                                                                                     'riesgo '
                                                                                                                     'cardiovascular '
                                                                                                                     'agudo.',
                                          'Breathe until it fades on its own.': 'Respira acompasadamente hasta que '
                                                                                'desaparezca por sí sola.',
                                          'CRAVING INTENSITY': 'INTENSIDAD DEL ANSIA',
                                          'Cravings are waves.': 'Las ansias vienen en oleadas.',
                                          'Deep REM Sleep': 'Sueño REM profundo',
                                          'Dopamine Re-sensitizing': 'Regeneración de dopamina',
                                          'From evening craving relief to long-term milestones.': 'Desde aliviar las '
                                                                                                  'ansias de la tarde '
                                                                                                  'hasta grandes '
                                                                                                  'logros.',
                                          'Heart & Circulation': 'Corazón y circulación',
                                          'Immune & Neural Clarity': 'Inmunidad y lucidez mental',
                                          'Liver & Gut Repair': 'Reparación hepática e intestinal',
                                          'Liver fat drops up to 15%. Gut lining begins rebuilding.': 'La grasa del '
                                                                                                      'hígado baja '
                                                                                                      'hasta un 15%. '
                                                                                                      'La pared '
                                                                                                      'intestinal se '
                                                                                                      'regenera.',
                                          'Long-Term Cellular Health': 'Salud celular a largo plazo',
                                          'Metabolism & Skin': 'Metabolismo y piel luminosa',
                                          'Natural pleasure responses start coming back. Anxiety begins receding.': 'Vuelve '
                                                                                                                    'el '
                                                                                                                    'disfrute '
                                                                                                                    'de '
                                                                                                                    'las '
                                                                                                                    'pequeñas '
                                                                                                                    'cosas. '
                                                                                                                    'La '
                                                                                                                    'ansiedad '
                                                                                                                    'disminuye.',
                                          "Notice it in your body. Don't argue with it.": 'Siente la sensación en tu '
                                                                                          'cuerpo sin juzgarla.',
                                          'Pass': 'Bajada',
                                          'Peak': 'Pico',
                                          'Repair begins hours after your last drink.': 'La reparación celular '
                                                                                        'comienza horas después de tu '
                                                                                        'última copa.',
                                          'Rise': 'Subida',
                                          'Significantly lower lifetime cancer, cardiovascular, and liver disease risk.': 'Menor '
                                                                                                                          'riesgo '
                                                                                                                          'a '
                                                                                                                          'lo '
                                                                                                                          'largo '
                                                                                                                          'de '
                                                                                                                          'la '
                                                                                                                          'vida '
                                                                                                                          'de '
                                                                                                                          'cáncer, '
                                                                                                                          'enfermedades '
                                                                                                                          'cardíacas '
                                                                                                                          'y '
                                                                                                                          'hepáticas.',
                                          'Sleep architecture begins to reset. Dreams return. Morning brain fog lifts.': 'El '
                                                                                                                         'ciclo '
                                                                                                                         'del '
                                                                                                                         'sueño '
                                                                                                                         'se '
                                                                                                                         'reajusta. '
                                                                                                                         'Vuelven '
                                                                                                                         'los '
                                                                                                                         'sueños. '
                                                                                                                         'Desaparece '
                                                                                                                         'la '
                                                                                                                         'niebla '
                                                                                                                         'mental.',
                                          'TIME &rarr;': 'PASO DEL TIEMPO →',
                                          'TIME →': 'PASO DEL TIEMPO →',
                                          'The old way broke your spirit. The new way protects your momentum.': 'El '
                                                                                                                'método '
                                                                                                                'tradicional '
                                                                                                                'te '
                                                                                                                'culpabilizaba. '
                                                                                                                'El '
                                                                                                                'nuestro '
                                                                                                                'protege '
                                                                                                                'tu '
                                                                                                                'constancia.',
                                          'Traditional Sobriety Apps': 'Apps tradicionales',
                                          'Visceral fat drops. Facial redness and systemic puffiness clear noticeably.': 'Se '
                                                                                                                         'reduce '
                                                                                                                         'la '
                                                                                                                         'grasa '
                                                                                                                         'visceral. '
                                                                                                                         'Desaparece '
                                                                                                                         'la '
                                                                                                                         'hinchazón '
                                                                                                                         'y '
                                                                                                                         'rojeces '
                                                                                                                         'del '
                                                                                                                         'rostro.',
                                          'White blood cell counts normalize. Neurogenesis accelerates. Focus locks in.': 'Los '
                                                                                                                          'glóbulos '
                                                                                                                          'blancos '
                                                                                                                          'se '
                                                                                                                          'normalizan. '
                                                                                                                          'Mejora '
                                                                                                                          'la '
                                                                                                                          'neurogénesis '
                                                                                                                          'y '
                                                                                                                          'el '
                                                                                                                          'enfoque '
                                                                                                                          'mental.',
                                          'Your body is already healing.': 'Tu cuerpo ya se está recuperando.',
                                          'Your personal tracking does not need an audience.': 'Tu proceso personal no '
                                                                                               'necesita '
                                                                                               'espectadores.'},
                                'fr': {   '01 · URGE SURFING': "01 · URGE SURFING (SURF SUR L'ENVIE)",
                                          '02 · BODY RECOVERY': '02 · RÉCUPÉRATION DU CORPS',
                                          '1 Year': '1 An',
                                          '14 Days': '14 Jours',
                                          '24 Hours': '24 Heures',
                                          '30 Days': '30 Jours',
                                          '7 Days': '7 Jours',
                                          '72 Hours': '72 Heures',
                                          '8 Hours': '8 Heures',
                                          '90 Days': '90 Jours',
                                          'A cue — 5 PM, the fridge, a bad day.': 'Le déclencheur — 18h, le '
                                                                                  'réfrigérateur, une dure journée.',
                                          'Acute Detox': 'Détox aiguë',
                                          'Alcohol Free Tracker': 'Alcohol Free Tracker',
                                          'An urge rises, peaks, and passes — if you let it.': 'Une envie monte, '
                                                                                               'culmine et disparaît — '
                                                                                               'si vous la laissez '
                                                                                               'faire.',
                                          'Answers when you need them.': 'Des réponses claires à vos questions',
                                          'Blood alcohol reaches zero. Blood oxygen levels begin normalizing.': "L'alcoolémie "
                                                                                                                'tombe '
                                                                                                                'à '
                                                                                                                'zéro. '
                                                                                                                "L'oxygène "
                                                                                                                'sanguin '
                                                                                                                'se '
                                                                                                                'normalise.',
                                          'Blood pressure stabilizes. Risk of acute cardiac events begins to drop.': 'La '
                                                                                                                     'tension '
                                                                                                                     'se '
                                                                                                                     'stabilise. '
                                                                                                                     'Le '
                                                                                                                     'risque '
                                                                                                                     "d'événement "
                                                                                                                     'cardiaque '
                                                                                                                     'diminue.',
                                          'Breathe until it fades on its own.': "Respirez calmement jusqu'à ce qu'elle "
                                                                                "s'estompe naturellement.",
                                          'CRAVING INTENSITY': "INTENSITÉ DE L'ENVIE",
                                          'Cravings are waves.': 'Les envies sont comme des vagues.',
                                          'Deep REM Sleep': 'Sommeil paradoxal profond',
                                          'Dopamine Re-sensitizing': 'Restauration de la dopamine',
                                          'From evening craving relief to long-term milestones.': "De l'apaisement des "
                                                                                                  'envies du soir aux '
                                                                                                  'grandes victoires.',
                                          'Heart & Circulation': 'Cœur et circulation',
                                          'Immune & Neural Clarity': "Système immunitaire et clarté d'esprit",
                                          'Liver & Gut Repair': 'Régénération hépatique et intestinale',
                                          'Liver fat drops up to 15%. Gut lining begins rebuilding.': 'La graisse '
                                                                                                      'hépatique chute '
                                                                                                      "jusqu'à 15%. La "
                                                                                                      'muqueuse '
                                                                                                      'intestinale se '
                                                                                                      'reconstruit.',
                                          'Long-Term Cellular Health': 'Santé cellulaire durable',
                                          'Metabolism & Skin': 'Métabolisme et éclat de la peau',
                                          'Natural pleasure responses start coming back. Anxiety begins receding.': 'Le '
                                                                                                                    'plaisir '
                                                                                                                    'des '
                                                                                                                    'choses '
                                                                                                                    'simples '
                                                                                                                    'revient. '
                                                                                                                    "L'anxiété "
                                                                                                                    "s'estompe "
                                                                                                                    'nettement.',
                                          "Notice it in your body. Don't argue with it.": 'Ressentez-la dans votre '
                                                                                          'corps. Ne luttez pas contre '
                                                                                          'elle.',
                                          'Pass': 'Apaisement',
                                          'Peak': 'Pic',
                                          'Repair begins hours after your last drink.': 'La régénération commence '
                                                                                        'quelques heures après votre '
                                                                                        'dernier verre.',
                                          'Rise': 'Montée',
                                          'Significantly lower lifetime cancer, cardiovascular, and liver disease risk.': 'Baisse '
                                                                                                                          'majeure '
                                                                                                                          'des '
                                                                                                                          'risques '
                                                                                                                          'de '
                                                                                                                          'cancers, '
                                                                                                                          'maladies '
                                                                                                                          'hépatiques '
                                                                                                                          'et '
                                                                                                                          'cardiovasculaires.',
                                          'Sleep architecture begins to reset. Dreams return. Morning brain fog lifts.': 'Le '
                                                                                                                         'cycle '
                                                                                                                         'du '
                                                                                                                         'sommeil '
                                                                                                                         'se '
                                                                                                                         'réinitialise. '
                                                                                                                         'Les '
                                                                                                                         'rêves '
                                                                                                                         'reviennent. '
                                                                                                                         'Le '
                                                                                                                         'brouillard '
                                                                                                                         'matinal '
                                                                                                                         'se '
                                                                                                                         'dissipe.',
                                          'TIME &rarr;': 'TEMPS ÉCOULÉ →',
                                          'TIME →': 'TEMPS ÉCOULÉ →',
                                          'The old way broke your spirit. The new way protects your momentum.': "L'ancienne "
                                                                                                                'approche '
                                                                                                                'culpabilisait. '
                                                                                                                'Notre '
                                                                                                                'méthode '
                                                                                                                'préserve '
                                                                                                                'votre '
                                                                                                                'élan.',
                                          'Traditional Sobriety Apps': 'Applications classiques',
                                          'Visceral fat drops. Facial redness and systemic puffiness clear noticeably.': 'La '
                                                                                                                         'graisse '
                                                                                                                         'viscérale '
                                                                                                                         'diminue. '
                                                                                                                         'Rougeurs '
                                                                                                                         'et '
                                                                                                                         'gonflements '
                                                                                                                         'du '
                                                                                                                         'visage '
                                                                                                                         'disparaissent.',
                                          'White blood cell counts normalize. Neurogenesis accelerates. Focus locks in.': 'Les '
                                                                                                                          'globules '
                                                                                                                          'blancs '
                                                                                                                          'se '
                                                                                                                          'normalisent. '
                                                                                                                          'La '
                                                                                                                          'neurogenèse '
                                                                                                                          "s'accélère. "
                                                                                                                          'La '
                                                                                                                          'concentration '
                                                                                                                          'revient.',
                                          'Your body is already healing.': 'Votre corps est déjà en train de guérir.',
                                          'Your personal tracking does not need an audience.': 'Votre parcours de '
                                                                                               "santé n'a pas besoin "
                                                                                               'de public.'},
                                'it': {   '01 · URGE SURFING': '01 · URGE SURFING (DOMARE LA VOGLIA)',
                                          '02 · BODY RECOVERY': '02 · RECUPERO DEL CORPO',
                                          '1 Year': '1 Anno',
                                          '14 Days': '14 Giorni',
                                          '24 Hours': '24 Ore',
                                          '30 Days': '30 Giorni',
                                          '7 Days': '7 Giorni',
                                          '72 Hours': '72 Ore',
                                          '8 Hours': '8 Ore',
                                          '90 Days': '90 Giorni',
                                          'A cue — 5 PM, the fridge, a bad day.': 'Il fattore scatenante — le 18, il '
                                                                                  'frigo, una giornata no.',
                                          'Acute Detox': 'Disintossicazione acuta',
                                          'Alcohol Free Tracker': 'Alcohol Free Tracker',
                                          'An urge rises, peaks, and passes — if you let it.': 'Un impulso cresce, '
                                                                                               'tocca il picco e '
                                                                                               'svanisce — se glielo '
                                                                                               'permetti.',
                                          'Answers when you need them.': 'Risposte a tutte le tue domande',
                                          'Blood alcohol reaches zero. Blood oxygen levels begin normalizing.': "L'alcol "
                                                                                                                'nel '
                                                                                                                'sangue '
                                                                                                                'va a '
                                                                                                                'zero. '
                                                                                                                "L'ossigenazione "
                                                                                                                'sanguigna '
                                                                                                                'si '
                                                                                                                'normalizza.',
                                          'Blood pressure stabilizes. Risk of acute cardiac events begins to drop.': 'La '
                                                                                                                     'pressione '
                                                                                                                     'arteriosa '
                                                                                                                     'si '
                                                                                                                     'stabilizza. '
                                                                                                                     'Calano '
                                                                                                                     'i '
                                                                                                                     'rischi '
                                                                                                                     'cardiovascolari.',
                                          'Breathe until it fades on its own.': 'Respira dolcemente fino a quando non '
                                                                                'scema da sola.',
                                          'CRAVING INTENSITY': "INTENSITÀ DELL'IMPULSO",
                                          'Cravings are waves.': 'Le voglie sono come onde.',
                                          'Deep REM Sleep': 'Sonno REM profondo',
                                          'Dopamine Re-sensitizing': 'Ricalibrazione della dopamina',
                                          'From evening craving relief to long-term milestones.': 'Dal gestire la '
                                                                                                  'tentazione serale '
                                                                                                  'ai grandi '
                                                                                                  'traguardi.',
                                          'Heart & Circulation': 'Cuore e circolazione',
                                          'Immune & Neural Clarity': 'Sistema immunitario e lucidità',
                                          'Liver & Gut Repair': 'Rigenerazione epatica e intestinale',
                                          'Liver fat drops up to 15%. Gut lining begins rebuilding.': 'Il grasso '
                                                                                                      'epatico cala '
                                                                                                      'fino al 15%. La '
                                                                                                      'barriera '
                                                                                                      'intestinale si '
                                                                                                      'ricostituisce.',
                                          'Long-Term Cellular Health': 'Salute cellulare a lungo termine',
                                          'Metabolism & Skin': 'Metabolismo e aspetto della pelle',
                                          'Natural pleasure responses start coming back. Anxiety begins receding.': 'Torna '
                                                                                                                    'il '
                                                                                                                    'piacere '
                                                                                                                    'spontaneo '
                                                                                                                    'delle '
                                                                                                                    'piccole '
                                                                                                                    'cose. '
                                                                                                                    "L'ansia "
                                                                                                                    'si '
                                                                                                                    'attenua.',
                                          "Notice it in your body. Don't argue with it.": 'Osserva la sensazione nel '
                                                                                          'corpo senza combatterla.',
                                          'Pass': 'Calo',
                                          'Peak': 'Picco',
                                          'Repair begins hours after your last drink.': 'La rigenerazione comincia '
                                                                                        "poche ore dopo l'ultimo "
                                                                                        'bicchiere.',
                                          'Rise': 'Salita',
                                          'Significantly lower lifetime cancer, cardiovascular, and liver disease risk.': 'Rischio '
                                                                                                                          'notevolmente '
                                                                                                                          'inferiore '
                                                                                                                          'di '
                                                                                                                          'cancro, '
                                                                                                                          'malattie '
                                                                                                                          'cardiache '
                                                                                                                          'ed '
                                                                                                                          'epatiche.',
                                          'Sleep architecture begins to reset. Dreams return. Morning brain fog lifts.': "L'architettura "
                                                                                                                         'del '
                                                                                                                         'sonno '
                                                                                                                         'si '
                                                                                                                         'ripristina. '
                                                                                                                         'Tornano '
                                                                                                                         'i '
                                                                                                                         'sogni '
                                                                                                                         'vividi. '
                                                                                                                         'Meno '
                                                                                                                         'nebbia '
                                                                                                                         'al '
                                                                                                                         'mattino.',
                                          'TIME &rarr;': 'PASSARE DEL TEMPO →',
                                          'TIME →': 'PASSARE DEL TEMPO →',
                                          'The old way broke your spirit. The new way protects your momentum.': 'Il '
                                                                                                                'vecchio '
                                                                                                                'approccio '
                                                                                                                'demoralizzava. '
                                                                                                                'Il '
                                                                                                                'nostro '
                                                                                                                'tutela '
                                                                                                                'la '
                                                                                                                'tua '
                                                                                                                'motivazione.',
                                          'Traditional Sobriety Apps': 'App tradizionali',
                                          'Visceral fat drops. Facial redness and systemic puffiness clear noticeably.': 'Diminuisce '
                                                                                                                         'il '
                                                                                                                         'grasso '
                                                                                                                         'viscerale. '
                                                                                                                         'Rossori '
                                                                                                                         'e '
                                                                                                                         'gonfiori '
                                                                                                                         'al '
                                                                                                                         'viso '
                                                                                                                         'spariscono.',
                                          'White blood cell counts normalize. Neurogenesis accelerates. Focus locks in.': 'I '
                                                                                                                          'globuli '
                                                                                                                          'bianchi '
                                                                                                                          'si '
                                                                                                                          'normalizzano. '
                                                                                                                          'La '
                                                                                                                          'neurogenesi '
                                                                                                                          'accelera. '
                                                                                                                          'Concentrazione '
                                                                                                                          'al '
                                                                                                                          'top.',
                                          'Your body is already healing.': 'Il tuo corpo sta già guarendo.',
                                          'Your personal tracking does not need an audience.': 'Il tuo percorso '
                                                                                               'personale non ha '
                                                                                               'bisogno di pubblico.'},
                                'ja': {   '01 · URGE SURFING': '01 · アージサーフィン（渇望の波乗り）',
                                          '02 · BODY RECOVERY': '02 · 身体回復タイムライン',
                                          '1 Year': '1年',
                                          '14 Days': '14日',
                                          '24 Hours': '24時間',
                                          '30 Days': '30日',
                                          '7 Days': '7日',
                                          '72 Hours': '72時間',
                                          '8 Hours': '8時間',
                                          '90 Days': '90日',
                                          'A cue — 5 PM, the fridge, a bad day.': 'きっかけ — 夕方5時、冷蔵庫を開けた時、疲れた日。',
                                          'Acute Detox': '急性デトックス',
                                          'Alcohol Free Tracker': 'Alcohol Free Tracker',
                                          'An urge rises, peaks, and passes — if you let it.': '欲求は高まり、頂点に達し、やがて消えていきます。',
                                          'Answers when you need them.': 'よくある質問とサポート',
                                          'Blood alcohol reaches zero. Blood oxygen levels begin normalizing.': '血中アルコール濃度がゼロになり、血中酸素濃度が正常化し始めます。',
                                          'Blood pressure stabilizes. Risk of acute cardiac events begins to drop.': '血圧が安定し、急性心血管リスクが低下し始めます。',
                                          'Breathe until it fades on its own.': '波が静まるまで、ゆっくりと呼吸を続ける。',
                                          'CRAVING INTENSITY': '渇望の強さ',
                                          'Cravings are waves.': '飲酒欲求は波のように満ち引きします。',
                                          'Deep REM Sleep': '深いレム睡眠',
                                          'Dopamine Re-sensitizing': 'ドーパミン受容体の回復',
                                          'From evening craving relief to long-term milestones.': '夕方の飲酒欲求の緩和から、長期の健康目標まで。',
                                          'Heart & Circulation': '心臓と血流',
                                          'Immune & Neural Clarity': '免疫力向上とクリアな思考',
                                          'Liver & Gut Repair': '肝臓と腸内環境の修復',
                                          'Liver fat drops up to 15%. Gut lining begins rebuilding.': '肝脂肪が最大15%減少し、腸内バリア機能の再建が始まります。',
                                          'Long-Term Cellular Health': '細胞レベルの健康と長寿',
                                          'Metabolism & Skin': '代謝改善とお肌の透明感',
                                          'Natural pleasure responses start coming back. Anxiety begins receding.': '日常の小さな喜びを感じられるようになり、不安感が軽減します。',
                                          "Notice it in your body. Don't argue with it.": '身体の感覚をただ観察し、無理に抗わない。',
                                          'Pass': '消退',
                                          'Peak': '頂点',
                                          'Repair begins hours after your last drink.': '最後の一杯から数時間後、修復は即座に始まります。',
                                          'Rise': '上昇',
                                          'Significantly lower lifetime cancer, cardiovascular, and liver disease risk.': 'がんや心血管疾患、肝疾患の生涯リスクが大幅に低減します。',
                                          'Sleep architecture begins to reset. Dreams return. Morning brain fog lifts.': '睡眠サイクルが正常化。夢を見るようになり、朝の頭のモヤが晴れます。',
                                          'TIME &rarr;': '時間経過 →',
                                          'TIME →': '時間経過 →',
                                          'The old way broke your spirit. The new way protects your momentum.': '従来のアプリは心を折るだけでした。新しい方法はあなたの意欲を守ります。',
                                          'Traditional Sobriety Apps': '従来の断酒アプリ',
                                          'Visceral fat drops. Facial redness and systemic puffiness clear noticeably.': '内臓脂肪が減少し、顔の赤らみや全身のむくみがすっきり取れます。',
                                          'White blood cell counts normalize. Neurogenesis accelerates. Focus locks in.': '白血球数が正常化し、神経新生が進み、集中力が劇的に高まります。',
                                          'Your body is already healing.': '身体はすでに回復を始めています。',
                                          'Your personal tracking does not need an audience.': '個人の禁酒記録に、他人の視線は必要ありません。'},
                                'ko': {   '01 · URGE SURFING': '01 · 갈망 서핑(Urge Surfing)',
                                          '02 · BODY RECOVERY': '02 · 신체 회복 타임라인',
                                          '1 Year': '1년',
                                          '14 Days': '14일',
                                          '24 Hours': '24시간',
                                          '30 Days': '30일',
                                          '7 Days': '7일',
                                          '72 Hours': '72시간',
                                          '8 Hours': '8시간',
                                          '90 Days': '90일',
                                          'A cue — 5 PM, the fridge, a bad day.': '신호 — 오후 5시, 냉장고 앞, 고단했던 하루.',
                                          'Acute Detox': '급성 해독',
                                          'Alcohol Free Tracker': 'Alcohol Free Tracker',
                                          'An urge rises, peaks, and passes — if you let it.': '갈망은 솟아오르고, 정점에 도달한 뒤, '
                                                                                               '가만히 지켜보면 저절로 지나갑니다.',
                                          'Answers when you need them.': '자주 묻는 질문 및 지원',
                                          'Blood alcohol reaches zero. Blood oxygen levels begin normalizing.': '혈중 '
                                                                                                                '알코올 '
                                                                                                                '농도가 '
                                                                                                                '0에 '
                                                                                                                '도달하고 '
                                                                                                                '혈중 산소 '
                                                                                                                '수치가 '
                                                                                                                '정상화되기 '
                                                                                                                '시작합니다.',
                                          'Blood pressure stabilizes. Risk of acute cardiac events begins to drop.': '혈압이 '
                                                                                                                     '안정되고 '
                                                                                                                     '급성 '
                                                                                                                     '심혈관 '
                                                                                                                     '질환 '
                                                                                                                     '위험이 '
                                                                                                                     '감소하기 '
                                                                                                                     '시작합니다.',
                                          'Breathe until it fades on its own.': '스스로 잦아들 때까지 호흡에 집중하세요.',
                                          'CRAVING INTENSITY': '갈망 강도',
                                          'Cravings are waves.': '갈망은 파도처럼 밀려왔다 사라집니다.',
                                          'Deep REM Sleep': '깊은 렘수면',
                                          'Dopamine Re-sensitizing': '도파민 수용체 회복',
                                          'From evening craving relief to long-term milestones.': '저녁 음주 충동 완화부터 장기 건강 '
                                                                                                  '목표 달성까지.',
                                          'Heart & Circulation': '심장 및 혈액 순환',
                                          'Immune & Neural Clarity': '면역력 강화 및 명료한 두뇌',
                                          'Liver & Gut Repair': '간 및 장 기능 회복',
                                          'Liver fat drops up to 15%. Gut lining begins rebuilding.': '간 지방이 최대 15% '
                                                                                                      '감소하고 장 점막 장벽이 '
                                                                                                      '재건되기 시작합니다.',
                                          'Long-Term Cellular Health': '세포 수준의 건강',
                                          'Metabolism & Skin': '신진대사 및 피부 개선',
                                          'Natural pleasure responses start coming back. Anxiety begins receding.': '일상의 '
                                                                                                                    '소소한 '
                                                                                                                    '즐거움이 '
                                                                                                                    '돌아오고 '
                                                                                                                    '원인 '
                                                                                                                    '모를 '
                                                                                                                    '불안감이 '
                                                                                                                    '줄어듭니다.',
                                          "Notice it in your body. Don't argue with it.": '신체의 감각을 알아차리세요. 억지로 싸우려 하지 '
                                                                                          '마세요.',
                                          'Pass': '소멸',
                                          'Peak': '정점',
                                          'Repair begins hours after your last drink.': '마지막 술잔을 비운 지 몇 시간 만에 치유가 '
                                                                                        '시작됩니다.',
                                          'Rise': '상승',
                                          'Significantly lower lifetime cancer, cardiovascular, and liver disease risk.': '암, '
                                                                                                                          '심혈관 '
                                                                                                                          '질환 '
                                                                                                                          '및 '
                                                                                                                          '간 '
                                                                                                                          '질환 '
                                                                                                                          '발생 '
                                                                                                                          '위험이 '
                                                                                                                          '현저히 '
                                                                                                                          '낮아집니다.',
                                          'Sleep architecture begins to reset. Dreams return. Morning brain fog lifts.': '수면 '
                                                                                                                         '구조가 '
                                                                                                                         '재설정됩니다. '
                                                                                                                         '꿈을 '
                                                                                                                         '꾸기 '
                                                                                                                         '시작하고 '
                                                                                                                         '아침 '
                                                                                                                         '브레인포그가 '
                                                                                                                         '걷힙니다.',
                                          'TIME &rarr;': '시간 흐름 →',
                                          'TIME →': '시간 흐름 →',
                                          'The old way broke your spirit. The new way protects your momentum.': '기존 '
                                                                                                                '방식은 '
                                                                                                                '의지를 '
                                                                                                                '꺾었지만, '
                                                                                                                '우리의 '
                                                                                                                '방식은 '
                                                                                                                '진전을 '
                                                                                                                '지켜줍니다.',
                                          'Traditional Sobriety Apps': '기존 금주 앱',
                                          'Visceral fat drops. Facial redness and systemic puffiness clear noticeably.': '내장 '
                                                                                                                         '지방이 '
                                                                                                                         '감소하고 '
                                                                                                                         '얼굴의 '
                                                                                                                         '붉은 '
                                                                                                                         '기와 '
                                                                                                                         '붓기가 '
                                                                                                                         '눈에 '
                                                                                                                         '띄게 '
                                                                                                                         '빠집니다.',
                                          'White blood cell counts normalize. Neurogenesis accelerates. Focus locks in.': '백혈구 '
                                                                                                                          '수가 '
                                                                                                                          '정상화되고 '
                                                                                                                          '신경 '
                                                                                                                          '생성이 '
                                                                                                                          '촉진되며 '
                                                                                                                          '집중력이 '
                                                                                                                          '크게 '
                                                                                                                          '향상됩니다.',
                                          'Your body is already healing.': '당신의 신체는 이미 회복을 시작했습니다.',
                                          'Your personal tracking does not need an audience.': '개인의 절주 여정에 타인의 시선은 필요 '
                                                                                               '없습니다.'},
                                'zh-tw': {   '01 · URGE SURFING': '01 · 衝動衝浪法',
                                             '02 · BODY RECOVERY': '02 · 生理修復時間軸',
                                             '1 Year': '1 年',
                                             '100% on-device privacy': '100% 離線本地儲存',
                                             '14 Days': '14 天',
                                             '24 Hours': '24 小時',
                                             '30 Days': '30 天',
                                             '7 Days': '7 天',
                                             '72 Hours': '72 小時',
                                             '8 Hours': '8 小時',
                                             '90 Days': '90 天',
                                             'A cue — 5 PM, the fridge, a bad day.': '觸發點——傍晚 5 點、打開冰箱、疲憊的一天。',
                                             'Actionable timelines, craving management protocols, and honest guides for sober-curious and mindful drinkers.': '提供具體時間軸、抗渴應對指南，陪伴每一位好奇清醒生活的實踐者。',
                                             'Acute Detox': '急性排毒期',
                                             'Aggressive $80/yr paywalls': '昂貴年費訂閱陷阱',
                                             'Alcohol Free Tracker': 'Alcohol Free Tracker',
                                             'An urge rises, peaks, and passes — if you let it.': '衝動會升起、抵達頂峰，隨後自然退去——只要你靜靜覺察。',
                                             'Answers when you need them.': '隨時解答你的疑問。',
                                             'Blood alcohol reaches zero. Blood oxygen levels begin normalizing.': '血液酒精濃度歸零，血液含氧量開始恢復正常。',
                                             'Blood pressure stabilizes. Risk of acute cardiac events begins to drop.': '血壓趨於平穩，急性心血管負擔顯著減輕。',
                                             'Breathe until it fades on its own.': '保持緩慢深呼吸，直到渴望自行平息。',
                                             'CRAVING INTENSITY': '渴望強度',
                                             'Can I export or backup my drinking history?': '我可以匯出或備份我的飲酒歷史記錄嗎？',
                                             'Can I use Alcohol Free Tracker for moderation or Dry January instead of quitting completely?': '我可以用這款 '
                                                                                                                                             'App '
                                                                                                                                             '來節制飲酒或進行 '
                                                                                                                                             '30 '
                                                                                                                                             '天挑戰，而不是完全戒絕嗎？',
                                             'Cloud tracking & data brokers': '雲端追蹤與數據販賣',
                                             'Cravings are waves.': '渴望如海浪般起伏。',
                                             'Deep REM Sleep': '深度 REM 睡眠',
                                             'Dopamine Re-sensitizing': '多巴胺受體重設',
                                             'Explore the latest iOS experience. Swipe or scroll horizontally to inspect all 10 screens.': '探索精緻的 '
                                                                                                                                           'iOS '
                                                                                                                                           '原生體驗。水平滑動查看全部 '
                                                                                                                                           '10 '
                                                                                                                                           '個核心畫面。',
                                             'Forces email signups and sends spam notifications.': '強制索取 Email '
                                                                                                   '並推送擾人廣告通知。',
                                             'Free core features with optional flexible Pro and Lifetime ownership.': '核心功能永久免費，並提供彈性 '
                                                                                                                      'Pro '
                                                                                                                      '與買斷終身方案。',
                                             'From evening craving relief to long-term milestones.': '從抵擋傍晚飲酒衝動，到見證長期健康里程碑。',
                                             'Heart & Circulation': '心臟與血液循環',
                                             'Honest indie pricing': '良心獨立開發者定價',
                                             'How do I request a feature or get support?': '如果我有功能建議或需要客服支援，該如何聯絡？',
                                             'How does Alcohol Free Tracker calculate money saved?': 'App '
                                                                                                     '是如何計算我省下多少錢的？',
                                             'How does the 3-minute Urge Surfing feature work?': '3 分鐘衝動衝浪呼吸引導是如何運作的？',
                                             'Immune & Neural Clarity': '免疫力激增與神經清明',
                                             'Is Alcohol Free Tracker a replacement for medical treatment?': 'Alcohol '
                                                                                                             'Free '
                                                                                                             'Tracker '
                                                                                                             '可以替代專業醫療或戒斷治療嗎？',
                                             'Is Alcohol Free Tracker completely free?': 'Alcohol Free Tracker '
                                                                                         '是完全免費的嗎？',
                                             'Liver & Gut Repair': '肝臟與腸道修復',
                                             'Liver fat drops up to 15%. Gut lining begins rebuilding.': '肝臟脂肪堆積減少高達 '
                                                                                                         '15%，腸道黏膜屏障逐步重建。',
                                             'Locks basic day counting behind deceptive subscription trials.': '將最基本的計日功能鎖在昂貴的自動扣款試用期之後。',
                                             'Log alcohol-free, light, or moderate days without losing your reflection streak.': '自由記錄無酒日、微醺或適量飲酒，絕不抹滅你的反思連續紀錄。',
                                             'Long-Term Cellular Health': '長期細胞抗病力',
                                             'Mandatory account registration': '強制註冊帳號',
                                             'Metabolism & Skin': '代謝煥新與膚況改善',
                                             'Natural pleasure responses start coming back. Anxiety begins receding.': '對日常生活瑣事的愉悅感恢復，無端焦慮感明顯消退。',
                                             'No feeds, no influencers, no ads. Just your progress.': '沒有社交動態、沒有網紅推銷、零廣告，專注於你的進步。',
                                             'Non-judgmental check-ins': '溫和客觀的每日簽到',
                                             "Notice it in your body. Don't argue with it.": '在身體中覺察它，無需爭辯或對抗。',
                                             'Pass': '退去',
                                             'Peak': '頂峰',
                                             'Practical science for cutting back & staying alcohol-free.': '實用醫學指南：幫助你減少飲酒或徹底維持清醒。',
                                             "Protected by Apple local storage. We couldn't sell your data even if we tried.": '受 '
                                                                                                                               'Apple '
                                                                                                                               '本地沙盒嚴密保護，我們就算想賣也根本拿不到資料。',
                                             'Quiet personal sanctuary': '安靜私密的個人天地',
                                             'Repair begins hours after your last drink.': '放下最後一杯酒幾小時內，修復即已啟動。',
                                             'Resets to Day 0 in red text, triggering the "Abstinence Violation Effect" (bingeing).': '以刺眼的紅色重設為第 '
                                                                                                                                      '0 '
                                                                                                                                      '天，容易引發「破戒後暴飲暴食效應」。',
                                             'Rise': '升起',
                                             'Sensitive drinking logs uploaded to third-party databases.': '將極具隱私的飲酒紀錄上傳到第三方雲端資料庫。',
                                             'Significantly lower lifetime cancer, cardiovascular, and liver disease risk.': '長期罹患癌症、心血管疾病與肝病風險大幅下降。',
                                             'Sleep architecture begins to reset. Dreams return. Morning brain fog lifts.': '睡眠結構開始重塑，生動夢境重現，早晨大腦不再昏沉。',
                                             'Streak-shaming on slip-ups': '中斷記錄時羞辱懲罰',
                                             'TIME &rarr;': '時間軸 →',
                                             'TIME →': '時間軸 →',
                                             'The old way broke your spirit. The new way protects your momentum.': '傳統方式只會打擊意志，全新模式守護你的進步動能。',
                                             'Track honestly, watch your body recover, and see your savings add up—100% privately.': '誠實記錄每一步，見證身體修復與荷包增長——100% '
                                                                                                                                     '屬於你個人的隱私。',
                                             'Traditional Sobriety Apps': '傳統戒酒 App',
                                             'Visceral fat drops. Facial redness and systemic puffiness clear noticeably.': '內臟脂肪下降，臉部泛紅水腫消退，皮膚重現光澤。',
                                             'Where is my alcohol tracker data stored?': '我的戒酒追蹤數據儲存在哪裡？',
                                             'White blood cell counts normalize. Neurogenesis accelerates. Focus locks in.': '白血球免疫功能正常化，神經新生加速，專注力大幅躍升。',
                                             "Why doesn't Alcohol Free Tracker have social feeds or community forums?": '為什麼 '
                                                                                                                        'Alcohol '
                                                                                                                        'Free '
                                                                                                                        'Tracker '
                                                                                                                        '沒有社交動態牆或社群論壇？',
                                             'Your body is already healing.': '你的身體正在自我修復。',
                                             'Your personal tracking does not need an audience.': '個人健康記錄，本就不需要向任何人公開。'}},
    'pill-reminder': {   'de': {   'A calendar, not just a checklist': 'Ein Kalender, nicht nur eine einfache '
                                                                       'Checkliste',
                                   'An urge rises, peaks, and passes — if you let it.': 'Ein Verlangen steigt auf, '
                                                                                        'erreicht seinen Höhepunkt und '
                                                                                        'vergeht — wenn du es zulässt.',
                                   'Answers when you need them.': 'Häufig gestellte Fragen',
                                   'Built for a real medicine cabinet': 'Entwickelt für den echten Medizinschrank',
                                   'Clean export for doctor visits': 'Sauberer PDF-Export für den Arztbesuch',
                                   'Critical alerts you actually hear': 'Dringende Alarme, die man wirklich hört',
                                   'Every day, every X days or hours, specific dates, on/off cycles, or as-needed — with a live preview of your next reminders before you save.': 'Täglich, '
                                                                                                                                                                                  'alle '
                                                                                                                                                                                  'X '
                                                                                                                                                                                  'Tage '
                                                                                                                                                                                  'oder '
                                                                                                                                                                                  'Stunden, '
                                                                                                                                                                                  'bestimmte '
                                                                                                                                                                                  'Daten, '
                                                                                                                                                                                  'Zyklen '
                                                                                                                                                                                  'oder '
                                                                                                                                                                                  'nach '
                                                                                                                                                                                  'Bedarf '
                                                                                                                                                                                  '— '
                                                                                                                                                                                  'mit '
                                                                                                                                                                                  'Vorschau '
                                                                                                                                                                                  'vor '
                                                                                                                                                                                  'dem '
                                                                                                                                                                                  'Speichern.',
                                   "Everything a reminder app should do. Nothing it shouldn't.": 'Alles, was eine '
                                                                                                 'Erinnerungs-App '
                                                                                                 'können muss. Und '
                                                                                                 'nichts '
                                                                                                 'Überflüssiges.',
                                   'Flexible schedules that fit real life': 'Flexible Pläne für den echten Alltag',
                                   "From today's doses to your full medicine list.": 'Von den heutigen Einnahmen bis '
                                                                                     'zur kompletten '
                                                                                     'Medikamentenübersicht.',
                                   'Generate a clean, formatted PDF of your dose adherence history to bring to doctor appointments or share with caregivers.': 'Erstelle '
                                                                                                                                                               'eine '
                                                                                                                                                               'übersichtliche '
                                                                                                                                                               'PDF-Historie '
                                                                                                                                                               'deiner '
                                                                                                                                                               'Einnahmen '
                                                                                                                                                               'für '
                                                                                                                                                               'das '
                                                                                                                                                               'nächste '
                                                                                                                                                               'Arztgespräch.',
                                   'Home groups every dose by time and lets you browse backward and forward through your history — mark a dose taken or skipped right from the day it happened.': 'Sortiert '
                                                                                                                                                                                                  'Dosen '
                                                                                                                                                                                                  'nach '
                                                                                                                                                                                                  'Uhrzeit '
                                                                                                                                                                                                  'und '
                                                                                                                                                                                                  'erlaubt '
                                                                                                                                                                                                  'den '
                                                                                                                                                                                                  'Blick '
                                                                                                                                                                                                  'in '
                                                                                                                                                                                                  'die '
                                                                                                                                                                                                  'Vergangenheit '
                                                                                                                                                                                                  '— '
                                                                                                                                                                                                  'abhaken '
                                                                                                                                                                                                  'oder '
                                                                                                                                                                                                  'überspringen '
                                                                                                                                                                                                  'direkt '
                                                                                                                                                                                                  'am '
                                                                                                                                                                                                  'Tag.',
                                   'Lock the app behind Face ID, hide medication names from lock screen notifications, and rest easy knowing zero data leaves your phone.': 'Face '
                                                                                                                                                                            'ID '
                                                                                                                                                                            'Schutz, '
                                                                                                                                                                            'Ausblenden '
                                                                                                                                                                            'von '
                                                                                                                                                                            'Medikamentennamen '
                                                                                                                                                                            'auf '
                                                                                                                                                                            'dem '
                                                                                                                                                                            'Sperrbildschirm '
                                                                                                                                                                            'und '
                                                                                                                                                                            '100% '
                                                                                                                                                                            'lokale '
                                                                                                                                                                            'Daten.',
                                   "Loud alarms that can't be ignored": 'Laute Alarme, die man nicht überhören kann',
                                   'Never run out, refill on time': 'Rechtzeitige Vorrats-Warnungen',
                                   'No medical advice, no dosage recommendations, no drug-interaction claims — just a dependable way to track what you take and when.': 'Kein '
                                                                                                                                                                        'medizinischer '
                                                                                                                                                                        'Rat, '
                                                                                                                                                                        'keine '
                                                                                                                                                                        'Dosierungsbehauptungen '
                                                                                                                                                                        '— '
                                                                                                                                                                        'nur '
                                                                                                                                                                        'ein '
                                                                                                                                                                        'verlässlicher '
                                                                                                                                                                        'Weg, '
                                                                                                                                                                        'deine '
                                                                                                                                                                        'Einnahmen '
                                                                                                                                                                        'zu '
                                                                                                                                                                        'timen.',
                                   'On iOS 26 or later, missed reminders can escalate into full alarms that ring even through silent mode, so you never miss a dose.': 'Verpasste '
                                                                                                                                                                       'Erinnerungen '
                                                                                                                                                                       'können '
                                                                                                                                                                       'zu '
                                                                                                                                                                       'vollen '
                                                                                                                                                                       'Alarmen '
                                                                                                                                                                       'eskalieren, '
                                                                                                                                                                       'die '
                                                                                                                                                                       'sogar '
                                                                                                                                                                       'den '
                                                                                                                                                                       'Stummschaltmodus '
                                                                                                                                                                       'durchdringen.',
                                   'One tap to check in': 'Mit einem Tippen auf dem Sperrbildschirm abhaken',
                                   'Pill Reminder is on the App Store.': 'Pill Reminder ist im App Store verfügbar.',
                                   "Privacy you don't have to think about": 'Privatsphäre, über die du dir keine '
                                                                            'Sorgen machen musst',
                                   'Refill tracking that speaks up early': 'Rechtzeitige Warnung vor leeren Packungen',
                                   'Schedules that match real prescriptions': 'Einnahmepläne, die zu echten Rezepten '
                                                                              'passen',
                                   "Set a pill count and a low-stock threshold per medicine. A banner flags refills before you're down to your last dose.": 'Pillenzahl '
                                                                                                                                                            'und '
                                                                                                                                                            'Mindestbestand '
                                                                                                                                                            'erfassen. '
                                                                                                                                                            'Eine '
                                                                                                                                                            'Warnung '
                                                                                                                                                            'meldet '
                                                                                                                                                            'sich, '
                                                                                                                                                            'bevor '
                                                                                                                                                            'die '
                                                                                                                                                            'letzte '
                                                                                                                                                            'Tablette '
                                                                                                                                                            'genommen '
                                                                                                                                                            'wird.',
                                   'Take your data anywhere': 'PDF-Export deiner Einnahme-Historie für den Arzt',
                                   'Track all your meds effortlessly': 'Alle Medikamente mühelos im Blick',
                                   'Your history at a glance': 'Deine Historie auf einen Blick im Monatskalender',
                                   'Your medication list does not need an audience.': 'Deine Medikamente gehen '
                                                                                      'niemanden etwas an.',
                                   'Your privacy matters': 'Deine Privatsphäre zählt — mit Face ID Schutz'},
                         'es': {   'A calendar, not just a checklist': 'Un calendario, no una simple lista de tareas',
                                   'An urge rises, peaks, and passes — if you let it.': 'Un ansia sube, llega al pico '
                                                                                        'y pasa — si la dejas fluir.',
                                   'Answers when you need them.': 'Preguntas frecuentes',
                                   'Built for a real medicine cabinet': 'Pensado para tu botiquín real',
                                   'Clean export for doctor visits': 'Exportación limpia en PDF para llevar al médico',
                                   'Critical alerts you actually hear': 'Alertas audibles que no podrás pasar por alto',
                                   'Every day, every X days or hours, specific dates, on/off cycles, or as-needed — with a live preview of your next reminders before you save.': 'A '
                                                                                                                                                                                  'diario, '
                                                                                                                                                                                  'cada '
                                                                                                                                                                                  'X '
                                                                                                                                                                                  'días '
                                                                                                                                                                                  'u '
                                                                                                                                                                                  'horas, '
                                                                                                                                                                                  'fechas '
                                                                                                                                                                                  'fijas, '
                                                                                                                                                                                  'ciclos '
                                                                                                                                                                                  'o '
                                                                                                                                                                                  'según '
                                                                                                                                                                                  'necesidad '
                                                                                                                                                                                  '— '
                                                                                                                                                                                  'con '
                                                                                                                                                                                  'vista '
                                                                                                                                                                                  'previa.',
                                   "Everything a reminder app should do. Nothing it shouldn't.": 'Todo lo que una app '
                                                                                                 'de pastillas debe '
                                                                                                 'hacer. Nada de lo '
                                                                                                 'que no deba.',
                                   'Flexible schedules that fit real life': 'Horarios flexibles adaptados a tu vida '
                                                                            'real',
                                   "From today's doses to your full medicine list.": 'Desde las tomas de hoy hasta tu '
                                                                                     'lista completa de medicinas.',
                                   'Generate a clean, formatted PDF of your dose adherence history to bring to doctor appointments or share with caregivers.': 'Genera '
                                                                                                                                                               'un '
                                                                                                                                                               'informe '
                                                                                                                                                               'PDF '
                                                                                                                                                               'con '
                                                                                                                                                               'tu '
                                                                                                                                                               'cumplimiento '
                                                                                                                                                               'terapéutico '
                                                                                                                                                               'para '
                                                                                                                                                               'enseñárselo '
                                                                                                                                                               'a '
                                                                                                                                                               'tu '
                                                                                                                                                               'doctor.',
                                   'Home groups every dose by time and lets you browse backward and forward through your history — mark a dose taken or skipped right from the day it happened.': 'Agrupa '
                                                                                                                                                                                                  'cada '
                                                                                                                                                                                                  'toma '
                                                                                                                                                                                                  'por '
                                                                                                                                                                                                  'hora '
                                                                                                                                                                                                  'y '
                                                                                                                                                                                                  'te '
                                                                                                                                                                                                  'permite '
                                                                                                                                                                                                  'consultar '
                                                                                                                                                                                                  'el '
                                                                                                                                                                                                  'historial '
                                                                                                                                                                                                  'fácilmente '
                                                                                                                                                                                                  'con '
                                                                                                                                                                                                  'un '
                                                                                                                                                                                                  'solo '
                                                                                                                                                                                                  'toque.',
                                   'Lock the app behind Face ID, hide medication names from lock screen notifications, and rest easy knowing zero data leaves your phone.': 'Bloqueo '
                                                                                                                                                                            'con '
                                                                                                                                                                            'Face '
                                                                                                                                                                            'ID, '
                                                                                                                                                                            'oculta '
                                                                                                                                                                            'nombres '
                                                                                                                                                                            'de '
                                                                                                                                                                            'fármacos '
                                                                                                                                                                            'en '
                                                                                                                                                                            'notificaciones '
                                                                                                                                                                            'y '
                                                                                                                                                                            '100% '
                                                                                                                                                                            'de '
                                                                                                                                                                            'datos '
                                                                                                                                                                            'en '
                                                                                                                                                                            'tu '
                                                                                                                                                                            'móvil.',
                                   "Loud alarms that can't be ignored": 'Alarmas audibles imposibles de pasar por alto',
                                   'Never run out, refill on time': 'Avisos de recarga para no quedarte sin pastillas',
                                   'No medical advice, no dosage recommendations, no drug-interaction claims — just a dependable way to track what you take and when.': 'Sin '
                                                                                                                                                                        'diagnósticos '
                                                                                                                                                                        'médicos: '
                                                                                                                                                                        'solo '
                                                                                                                                                                        'una '
                                                                                                                                                                        'forma '
                                                                                                                                                                        'fiable '
                                                                                                                                                                        'de '
                                                                                                                                                                        'recordar '
                                                                                                                                                                        'qué '
                                                                                                                                                                        'tomas '
                                                                                                                                                                        'y '
                                                                                                                                                                        'a '
                                                                                                                                                                        'qué '
                                                                                                                                                                        'hora.',
                                   'On iOS 26 or later, missed reminders can escalate into full alarms that ring even through silent mode, so you never miss a dose.': 'Los '
                                                                                                                                                                       'avisos '
                                                                                                                                                                       'no '
                                                                                                                                                                       'respondidos '
                                                                                                                                                                       'pueden '
                                                                                                                                                                       'sonar '
                                                                                                                                                                       'como '
                                                                                                                                                                       'alarmas '
                                                                                                                                                                       'incluso '
                                                                                                                                                                       'con '
                                                                                                                                                                       'el '
                                                                                                                                                                       'móvil '
                                                                                                                                                                       'en '
                                                                                                                                                                       'silencio.',
                                   'One tap to check in': 'Marca la toma con un solo toque en pantalla de bloqueo',
                                   'Pill Reminder is on the App Store.': 'Pill Reminder está en la App Store.',
                                   "Privacy you don't have to think about": 'Privacidad absoluta sin complicaciones',
                                   'Refill tracking that speaks up early': 'Avisos de recarga antes de la última '
                                                                           'pastilla',
                                   'Schedules that match real prescriptions': 'Horarios adaptados a prescripciones '
                                                                              'reales',
                                   "Set a pill count and a low-stock threshold per medicine. A banner flags refills before you're down to your last dose.": 'Indica '
                                                                                                                                                            'el '
                                                                                                                                                            'recuento '
                                                                                                                                                            'de '
                                                                                                                                                            'pastillas '
                                                                                                                                                            'y '
                                                                                                                                                            'recibe '
                                                                                                                                                            'un '
                                                                                                                                                            'aviso '
                                                                                                                                                            'con '
                                                                                                                                                            'tiempo '
                                                                                                                                                            'para '
                                                                                                                                                            'ir '
                                                                                                                                                            'a '
                                                                                                                                                            'la '
                                                                                                                                                            'farmacia.',
                                   'Take your data anywhere': 'Exporta tu historial en PDF para llevarlo al médico',
                                   'Track all your meds effortlessly': 'Gestiona todas tus medicinas sin esfuerzo',
                                   'Your history at a glance': 'Tu historial de un vistazo con vista de calendario',
                                   'Your medication list does not need an audience.': 'Tus medicamentos no necesitan '
                                                                                      'público.',
                                   'Your privacy matters': 'Máxima privacidad protegida con Face ID'},
                         'fr': {   'A calendar, not just a checklist': 'Un vrai calendrier, pas une simple to-do list',
                                   'An urge rises, peaks, and passes — if you let it.': 'Une envie monte, culmine et '
                                                                                        'disparaît — si vous la '
                                                                                        'laissez faire.',
                                   'Answers when you need them.': 'Questions fréquentes',
                                   'Built for a real medicine cabinet': 'Conçu pour votre armoire à pharmacie',
                                   'Clean export for doctor visits': 'Export PDF clair pour vos rendez-vous médicaux',
                                   'Critical alerts you actually hear': 'Des alertes importantes impossibles à manquer',
                                   'Every day, every X days or hours, specific dates, on/off cycles, or as-needed — with a live preview of your next reminders before you save.': 'Tous '
                                                                                                                                                                                  'les '
                                                                                                                                                                                  'jours, '
                                                                                                                                                                                  'toutes '
                                                                                                                                                                                  'les '
                                                                                                                                                                                  'X '
                                                                                                                                                                                  'heures, '
                                                                                                                                                                                  'dates '
                                                                                                                                                                                  'précises, '
                                                                                                                                                                                  'cycles '
                                                                                                                                                                                  'ou '
                                                                                                                                                                                  'au '
                                                                                                                                                                                  'besoin '
                                                                                                                                                                                  '— '
                                                                                                                                                                                  'avec '
                                                                                                                                                                                  'aperçu '
                                                                                                                                                                                  'en '
                                                                                                                                                                                  'direct.',
                                   "Everything a reminder app should do. Nothing it shouldn't.": "Tout ce qu'une "
                                                                                                 'application de '
                                                                                                 'rappel doit faire. '
                                                                                                 'Sans rien de '
                                                                                                 'superflu.',
                                   'Flexible schedules that fit real life': 'Des plannings adaptés à votre vraie vie',
                                   "From today's doses to your full medicine list.": 'De vos prises du jour à votre '
                                                                                     'liste complète de médicaments.',
                                   'Generate a clean, formatted PDF of your dose adherence history to bring to doctor appointments or share with caregivers.': 'Générez '
                                                                                                                                                               'un '
                                                                                                                                                               'rapport '
                                                                                                                                                               'PDF '
                                                                                                                                                               'soigné '
                                                                                                                                                               'de '
                                                                                                                                                               'votre '
                                                                                                                                                               'historique '
                                                                                                                                                               'de '
                                                                                                                                                               'prises '
                                                                                                                                                               'pour '
                                                                                                                                                               'votre '
                                                                                                                                                               'médecin '
                                                                                                                                                               'ou '
                                                                                                                                                               'vos '
                                                                                                                                                               'proches.',
                                   'Home groups every dose by time and lets you browse backward and forward through your history — mark a dose taken or skipped right from the day it happened.': 'Regroupe '
                                                                                                                                                                                                  'les '
                                                                                                                                                                                                  'prises '
                                                                                                                                                                                                  'par '
                                                                                                                                                                                                  'heure '
                                                                                                                                                                                                  'et '
                                                                                                                                                                                                  'permet '
                                                                                                                                                                                                  'de '
                                                                                                                                                                                                  'parcourir '
                                                                                                                                                                                                  "l'historique "
                                                                                                                                                                                                  '— '
                                                                                                                                                                                                  'cochez '
                                                                                                                                                                                                  'vos '
                                                                                                                                                                                                  'prises '
                                                                                                                                                                                                  'facilement.',
                                   'Lock the app behind Face ID, hide medication names from lock screen notifications, and rest easy knowing zero data leaves your phone.': 'Verrouillage '
                                                                                                                                                                            'Face '
                                                                                                                                                                            'ID, '
                                                                                                                                                                            'masquage '
                                                                                                                                                                            'des '
                                                                                                                                                                            'noms '
                                                                                                                                                                            'sur '
                                                                                                                                                                            "l'écran "
                                                                                                                                                                            'verrouillé '
                                                                                                                                                                            'et '
                                                                                                                                                                            'zéro '
                                                                                                                                                                            'donnée '
                                                                                                                                                                            'envoyée.',
                                   "Loud alarms that can't be ignored": 'Des alarmes puissantes impossibles à manquer',
                                   'Never run out, refill on time': 'Alertes de renouvellement pour ne jamais manquer',
                                   'No medical advice, no dosage recommendations, no drug-interaction claims — just a dependable way to track what you take and when.': 'Pas '
                                                                                                                                                                        'de '
                                                                                                                                                                        'conseils '
                                                                                                                                                                        'médicaux '
                                                                                                                                                                        '— '
                                                                                                                                                                        'juste '
                                                                                                                                                                        'une '
                                                                                                                                                                        'méthode '
                                                                                                                                                                        'infaillible '
                                                                                                                                                                        'pour '
                                                                                                                                                                        'suivre '
                                                                                                                                                                        'ce '
                                                                                                                                                                        'que '
                                                                                                                                                                        'vous '
                                                                                                                                                                        'prenez '
                                                                                                                                                                        'et '
                                                                                                                                                                        'quand.',
                                   'On iOS 26 or later, missed reminders can escalate into full alarms that ring even through silent mode, so you never miss a dose.': 'Les '
                                                                                                                                                                       'rappels '
                                                                                                                                                                       'ignorés '
                                                                                                                                                                       'peuvent '
                                                                                                                                                                       'se '
                                                                                                                                                                       'transformer '
                                                                                                                                                                       'en '
                                                                                                                                                                       'alarmes '
                                                                                                                                                                       'retentissant '
                                                                                                                                                                       'même '
                                                                                                                                                                       'en '
                                                                                                                                                                       'mode '
                                                                                                                                                                       'silencieux.',
                                   'One tap to check in': "Validez votre prise en un geste sur l'écran verrouillé",
                                   'Pill Reminder is on the App Store.': "Pill Reminder est disponible sur l'App "
                                                                         'Store.',
                                   "Privacy you don't have to think about": 'Une confidentialité totale sans y penser',
                                   'Refill tracking that speaks up early': 'Alertes de renouvellement avant la '
                                                                           'dernière pilule',
                                   'Schedules that match real prescriptions': 'Des plannings fidèles aux vraies '
                                                                              'ordonnances',
                                   "Set a pill count and a low-stock threshold per medicine. A banner flags refills before you're down to your last dose.": 'Comptez '
                                                                                                                                                            'vos '
                                                                                                                                                            'comprimés '
                                                                                                                                                            'et '
                                                                                                                                                            'fixez '
                                                                                                                                                            'un '
                                                                                                                                                            'seuil '
                                                                                                                                                            "d'alerte "
                                                                                                                                                            'pour '
                                                                                                                                                            'renouveler '
                                                                                                                                                            'votre '
                                                                                                                                                            'ordonnance '
                                                                                                                                                            'à '
                                                                                                                                                            'temps.',
                                   'Take your data anywhere': 'Exportez votre historique en PDF pour votre médecin',
                                   'Track all your meds effortlessly': 'Gérez tous vos médicaments facilement',
                                   'Your history at a glance': "Votre historique en un coup d'œil sur le calendrier",
                                   'Your medication list does not need an audience.': "Votre ordonnance n'a pas besoin "
                                                                                      'de spectateurs.',
                                   'Your privacy matters': 'Protection stricte avec Face ID'},
                         'it': {   'A calendar, not just a checklist': 'Un calendario chiaro, non una semplice lista',
                                   'An urge rises, peaks, and passes — if you let it.': 'Un impulso cresce, tocca il '
                                                                                        'picco e svanisce — se glielo '
                                                                                        'permetti.',
                                   'Answers when you need them.': 'Domande frequenti',
                                   'Built for a real medicine cabinet': 'Creato per il tuo armadietto dei medicinali',
                                   'Clean export for doctor visits': 'Esportazione PDF chiara per le visite mediche',
                                   'Critical alerts you actually hear': 'Allarmi potenti impossibili da non sentire',
                                   'Every day, every X days or hours, specific dates, on/off cycles, or as-needed — with a live preview of your next reminders before you save.': 'Tutti '
                                                                                                                                                                                  'i '
                                                                                                                                                                                  'giorni, '
                                                                                                                                                                                  'ogni '
                                                                                                                                                                                  'X '
                                                                                                                                                                                  'giorni '
                                                                                                                                                                                  'o '
                                                                                                                                                                                  'ore, '
                                                                                                                                                                                  'date '
                                                                                                                                                                                  'specifiche '
                                                                                                                                                                                  'o '
                                                                                                                                                                                  'al '
                                                                                                                                                                                  'bisogno '
                                                                                                                                                                                  '— '
                                                                                                                                                                                  'con '
                                                                                                                                                                                  'anteprima '
                                                                                                                                                                                  'in '
                                                                                                                                                                                  'tempo '
                                                                                                                                                                                  'reale.',
                                   "Everything a reminder app should do. Nothing it shouldn't.": 'Tutto ciò che un '
                                                                                                 'promemoria farmaci '
                                                                                                 'deve fare. Niente di '
                                                                                                 'superfluo.',
                                   'Flexible schedules that fit real life': 'Orari flessibili per adattarsi alla tua '
                                                                            'vita',
                                   "From today's doses to your full medicine list.": "Dalle dosi di oggi all'elenco "
                                                                                     'completo dei farmaci.',
                                   'Generate a clean, formatted PDF of your dose adherence history to bring to doctor appointments or share with caregivers.': 'Genera '
                                                                                                                                                               'un '
                                                                                                                                                               'comodo '
                                                                                                                                                               'PDF '
                                                                                                                                                               'con '
                                                                                                                                                               'il '
                                                                                                                                                               'riepilogo '
                                                                                                                                                               'delle '
                                                                                                                                                               'tue '
                                                                                                                                                               'assunzioni '
                                                                                                                                                               'da '
                                                                                                                                                               'mostrare '
                                                                                                                                                               'al '
                                                                                                                                                               'tuo '
                                                                                                                                                               'medico '
                                                                                                                                                               'curante.',
                                   'Home groups every dose by time and lets you browse backward and forward through your history — mark a dose taken or skipped right from the day it happened.': 'Raggruppa '
                                                                                                                                                                                                  'le '
                                                                                                                                                                                                  'dosi '
                                                                                                                                                                                                  'per '
                                                                                                                                                                                                  'orario '
                                                                                                                                                                                                  'e '
                                                                                                                                                                                                  'ti '
                                                                                                                                                                                                  'permette '
                                                                                                                                                                                                  'di '
                                                                                                                                                                                                  'scorrere '
                                                                                                                                                                                                  'la '
                                                                                                                                                                                                  'cronologia '
                                                                                                                                                                                                  'avanti '
                                                                                                                                                                                                  'e '
                                                                                                                                                                                                  'indietro.',
                                   'Lock the app behind Face ID, hide medication names from lock screen notifications, and rest easy knowing zero data leaves your phone.': 'Blocco '
                                                                                                                                                                            'Face '
                                                                                                                                                                            'ID, '
                                                                                                                                                                            'nascondi '
                                                                                                                                                                            'i '
                                                                                                                                                                            'nomi '
                                                                                                                                                                            'dei '
                                                                                                                                                                            'farmaci '
                                                                                                                                                                            'sul '
                                                                                                                                                                            'display '
                                                                                                                                                                            'e '
                                                                                                                                                                            'zero '
                                                                                                                                                                            'dati '
                                                                                                                                                                            'trasmessi '
                                                                                                                                                                            "all'esterno.",
                                   "Loud alarms that can't be ignored": 'Allarmi potenti impossibili da ignorare',
                                   'Never run out, refill on time': 'Avvisi scorte per non restare mai senza farmaci',
                                   'No medical advice, no dosage recommendations, no drug-interaction claims — just a dependable way to track what you take and when.': 'Nessuna '
                                                                                                                                                                        'diagnosi '
                                                                                                                                                                        'medica: '
                                                                                                                                                                        'solo '
                                                                                                                                                                        'un '
                                                                                                                                                                        'metodo '
                                                                                                                                                                        'infallibile '
                                                                                                                                                                        'per '
                                                                                                                                                                        'gestire '
                                                                                                                                                                        'le '
                                                                                                                                                                        'tue '
                                                                                                                                                                        'assunzioni '
                                                                                                                                                                        'quotidiane.',
                                   'On iOS 26 or later, missed reminders can escalate into full alarms that ring even through silent mode, so you never miss a dose.': 'I '
                                                                                                                                                                       'promemoria '
                                                                                                                                                                       'non '
                                                                                                                                                                       'confermati '
                                                                                                                                                                       'possono '
                                                                                                                                                                       'diventare '
                                                                                                                                                                       'veri '
                                                                                                                                                                       'allarmi '
                                                                                                                                                                       'anche '
                                                                                                                                                                       'con '
                                                                                                                                                                       'suoneria '
                                                                                                                                                                       'disattivata.',
                                   'One tap to check in': "Segna l'assunzione con un tocco dal blocco schermo",
                                   'Pill Reminder is on the App Store.': 'Pill Reminder è disponibile su App Store.',
                                   "Privacy you don't have to think about": 'Privacy totale senza pensieri',
                                   'Refill tracking that speaks up early': "Avviso scorte prima dell'ultima pillola",
                                   'Schedules that match real prescriptions': 'Piani terapeutici adatti a ricette '
                                                                              'reali',
                                   "Set a pill count and a low-stock threshold per medicine. A banner flags refills before you're down to your last dose.": 'Imposta '
                                                                                                                                                            'il '
                                                                                                                                                            'numero '
                                                                                                                                                            'di '
                                                                                                                                                            'pillole '
                                                                                                                                                            'e '
                                                                                                                                                            'ricevi '
                                                                                                                                                            'un '
                                                                                                                                                            'promemoria '
                                                                                                                                                            'per '
                                                                                                                                                            'tempo '
                                                                                                                                                            'per '
                                                                                                                                                            'andare '
                                                                                                                                                            'in '
                                                                                                                                                            'farmacia.',
                                   'Take your data anywhere': 'Esporta la cronologia in PDF per il tuo medico',
                                   'Track all your meds effortlessly': 'Gestisci tutti i tuoi farmaci senza sforzo',
                                   'Your history at a glance': "Tutta la cronologia a colpo d'occhio nel calendario",
                                   'Your medication list does not need an audience.': 'La tua lista di medicine non ha '
                                                                                      'bisogno di spettatori.',
                                   'Your privacy matters': 'Massima riservatezza protetta da Face ID'},
                         'ja': {   'A calendar, not just a checklist': 'ただのチェックリストではないカレンダー表示',
                                   'An urge rises, peaks, and passes — if you let it.': '欲求は高まり、頂点に達し、やがて消えていきます。',
                                   'Answers when you need them.': 'よくある質問',
                                   'Built for a real medicine cabinet': '日々の服薬管理のために設計',
                                   'Clean export for doctor visits': '医師に見せられる服薬履歴のPDF出力',
                                   'Critical alerts you actually hear': '聞き逃さない確実な大音量アラーム',
                                   'Every day, every X days or hours, specific dates, on/off cycles, or as-needed — with a live preview of your next reminders before you save.': '毎日、○日/時間ごと、特定日、休薬サイクル、頓服まで柔軟に対応。保存前に次回の予定を確認可能。',
                                   "Everything a reminder app should do. Nothing it shouldn't.": 'お薬リマインダーに必要なすべてを。不要なものは一切削ぎ落としました。',
                                   'Flexible schedules that fit real life': '日々の生活リズムに合わせた柔軟なスケジュール',
                                   "From today's doses to your full medicine list.": '今日飲む薬から、常備薬の一覧リストまで。',
                                   'Generate a clean, formatted PDF of your dose adherence history to bring to doctor appointments or share with caregivers.': '通院時や家族との共有に最適な、見やすい服薬履歴PDFをワンタップで作成。',
                                   'Home groups every dose by time and lets you browse backward and forward through your history — mark a dose taken or skipped right from the day it happened.': '時間帯ごとに服用薬を整理。履歴を前後に確認でき、その場で服用済みやスキップを記録できます。',
                                   'Lock the app behind Face ID, hide medication names from lock screen notifications, and rest easy knowing zero data leaves your phone.': 'Face '
                                                                                                                                                                            'IDロックに対応し、通知で薬の名前を非表示に。データが外部に送信されることは一切ありません。',
                                   "Loud alarms that can't be ignored": '聞き逃さない確実な大音量アラーム',
                                   'Never run out, refill on time': '残薬アラートで処方箋の補充忘れを防止',
                                   'No medical advice, no dosage recommendations, no drug-interaction claims — just a dependable way to track what you take and when.': '医療判断や投与推奨は行いません。何をいつ服用したかを確実に記録する信頼のツールです。',
                                   'On iOS 26 or later, missed reminders can escalate into full alarms that ring even through silent mode, so you never miss a dose.': '見落とした通知をマナーモード貫通のアラームに昇格させ、確実な服用を促します。',
                                   'One tap to check in': 'ロック画面からワンタップで服用チェック',
                                   'Pill Reminder is on the App Store.': 'Pill ReminderはApp Storeで好評配信中。',
                                   "Privacy you don't have to think about": '意識せずとも守られる完全なプライバシー',
                                   'Refill tracking that speaks up early': '残薬アラートで薬切れを事前に防止',
                                   'Schedules that match real prescriptions': '実際の処方に合わせた柔軟なスケジュール',
                                   "Set a pill count and a low-stock threshold per medicine. A banner flags refills before you're down to your last dose.": '薬ごとに残数と警告のしきい値を設定。最後の1錠になる前に補充リマインダーでお知らせ。',
                                   'Take your data anywhere': '医師に見せられる服用履歴のPDF出力',
                                   'Track all your meds effortlessly': 'あらゆる医薬品と服用量を手軽に一括管理',
                                   'Your history at a glance': 'カレンダー表示で服薬履歴を一目で確認',
                                   'Your medication list does not need an audience.': 'あなたのお薬情報に、他人の視線は不要です。',
                                   'Your privacy matters': 'Face ID対応で徹底したプライバシー保護'},
                         'ko': {   'A calendar, not just a checklist': '단순한 체크리스트를 넘어선 캘린더',
                                   'An urge rises, peaks, and passes — if you let it.': '갈망은 솟아오르고, 정점에 도달한 뒤, 가만히 '
                                                                                        '지켜보면 저절로 지나갑니다.',
                                   'Answers when you need them.': '자주 묻는 질문',
                                   'Built for a real medicine cabinet': '실제 복약 관리를 위해 세심하게 설계',
                                   'Clean export for doctor visits': '진료 시 제출하기 좋은 깔끔한 PDF 내보내기',
                                   'Critical alerts you actually hear': '놓칠 수 없는 강력한 복약 알람',
                                   'Every day, every X days or hours, specific dates, on/off cycles, or as-needed — with a live preview of your next reminders before you save.': '매일, '
                                                                                                                                                                                  '며칠/몇 '
                                                                                                                                                                                  '시간 '
                                                                                                                                                                                  '간격, '
                                                                                                                                                                                  '특정 '
                                                                                                                                                                                  '요일, '
                                                                                                                                                                                  '주기적 '
                                                                                                                                                                                  '복용, '
                                                                                                                                                                                  '필요 '
                                                                                                                                                                                  '시 '
                                                                                                                                                                                  '복용 '
                                                                                                                                                                                  '등 '
                                                                                                                                                                                  '모든 '
                                                                                                                                                                                  '복약 '
                                                                                                                                                                                  '패턴을 '
                                                                                                                                                                                  '지원합니다.',
                                   "Everything a reminder app should do. Nothing it shouldn't.": '복약 알림 앱에 필요한 모든 기능은 '
                                                                                                 '담고, 불필요한 번거로움은 모두 '
                                                                                                 '없앴습니다.',
                                   'Flexible schedules that fit real life': '실제 일상에 맞춘 유연한 복용 스케줄',
                                   "From today's doses to your full medicine list.": '오늘의 복약 시간표부터 전체 보유 약품 목록까지.',
                                   'Generate a clean, formatted PDF of your dose adherence history to bring to doctor appointments or share with caregivers.': '의사 '
                                                                                                                                                               '진료나 '
                                                                                                                                                               '보호자 '
                                                                                                                                                               '공유를 '
                                                                                                                                                               '위해 '
                                                                                                                                                               '복약 '
                                                                                                                                                               '이력을 '
                                                                                                                                                               '깔끔한 '
                                                                                                                                                               'PDF '
                                                                                                                                                               '보고서로 '
                                                                                                                                                               '즉시 '
                                                                                                                                                               '내보냅니다.',
                                   'Home groups every dose by time and lets you browse backward and forward through your history — mark a dose taken or skipped right from the day it happened.': '시간대별로 '
                                                                                                                                                                                                  '복용할 '
                                                                                                                                                                                                  '약을 '
                                                                                                                                                                                                  '묶어 '
                                                                                                                                                                                                  '보여주며, '
                                                                                                                                                                                                  '날짜별 '
                                                                                                                                                                                                  '복용 '
                                                                                                                                                                                                  '여부를 '
                                                                                                                                                                                                  '달력에서 '
                                                                                                                                                                                                  '한눈에 '
                                                                                                                                                                                                  '확인하고 '
                                                                                                                                                                                                  '기록합니다.',
                                   'Lock the app behind Face ID, hide medication names from lock screen notifications, and rest easy knowing zero data leaves your phone.': 'Face '
                                                                                                                                                                            'ID '
                                                                                                                                                                            '잠금 '
                                                                                                                                                                            '및 '
                                                                                                                                                                            '잠금 '
                                                                                                                                                                            '화면 '
                                                                                                                                                                            '알림 '
                                                                                                                                                                            '내 '
                                                                                                                                                                            '약품명 '
                                                                                                                                                                            '숨김 '
                                                                                                                                                                            '기능으로 '
                                                                                                                                                                            '기기 '
                                                                                                                                                                            '외부로 '
                                                                                                                                                                            '데이터가 '
                                                                                                                                                                            '절대 '
                                                                                                                                                                            '유출되지 '
                                                                                                                                                                            '않습니다.',
                                   "Loud alarms that can't be ignored": '놓칠 수 없는 확실한 대음량 알람',
                                   'Never run out, refill on time': '처방약 잔여량 알림으로 제때 약품 보충',
                                   'No medical advice, no dosage recommendations, no drug-interaction claims — just a dependable way to track what you take and when.': '의학적 '
                                                                                                                                                                        '처방이 '
                                                                                                                                                                        '아닌, '
                                                                                                                                                                        '언제 '
                                                                                                                                                                        '어떤 '
                                                                                                                                                                        '약을 '
                                                                                                                                                                        '복용해야 '
                                                                                                                                                                        '하는지 '
                                                                                                                                                                        '가장 '
                                                                                                                                                                        '신뢰할 '
                                                                                                                                                                        '수 '
                                                                                                                                                                        '있게 '
                                                                                                                                                                        '알려주는 '
                                                                                                                                                                        '트래커입니다.',
                                   'On iOS 26 or later, missed reminders can escalate into full alarms that ring even through silent mode, so you never miss a dose.': '확인하지 '
                                                                                                                                                                       '않은 '
                                                                                                                                                                       '알림은 '
                                                                                                                                                                       '무음 '
                                                                                                                                                                       '모드도 '
                                                                                                                                                                       '뚫고 '
                                                                                                                                                                       '울리는 '
                                                                                                                                                                       '풀 '
                                                                                                                                                                       '알람으로 '
                                                                                                                                                                       '전환되어 '
                                                                                                                                                                       '중요한 '
                                                                                                                                                                       '약을 '
                                                                                                                                                                       '절대 '
                                                                                                                                                                       '거르지 '
                                                                                                                                                                       '않습니다.',
                                   'One tap to check in': '잠금 화면에서 원터치로 간편 체크',
                                   'Pill Reminder is on the App Store.': 'Pill Reminder를 App Store에서 만나보세요.',
                                   "Privacy you don't have to think about": '신경 쓰지 않아도 완벽한 개인정보 보호',
                                   'Refill tracking that speaks up early': '약이 떨어지기 전 미리 알려주는 보충 알림',
                                   'Schedules that match real prescriptions': '실제 처방전에 맞춘 유연한 일정 설정',
                                   "Set a pill count and a low-stock threshold per medicine. A banner flags refills before you're down to your last dose.": '약품별 '
                                                                                                                                                            '잔여 '
                                                                                                                                                            '수량과 '
                                                                                                                                                            '최소 '
                                                                                                                                                            '수량을 '
                                                                                                                                                            '지정하여, '
                                                                                                                                                            '마지막 '
                                                                                                                                                            '약을 '
                                                                                                                                                            '먹기 '
                                                                                                                                                            '전 '
                                                                                                                                                            '미리 '
                                                                                                                                                            '처방전을 '
                                                                                                                                                            '보충하도록 '
                                                                                                                                                            '안내합니다.',
                                   'Take your data anywhere': '진료 시 보여줄 수 있는 복용 기록 PDF 내보내기',
                                   'Track all your meds effortlessly': '모든 복용 약물과 용량을 간편하게 기록',
                                   'Your history at a glance': '월간 캘린더로 한눈에 확인하는 복약 기록',
                                   'Your medication list does not need an audience.': '당신의 약 복용 기록은 누구에게도 공개될 필요가 '
                                                                                      '없습니다.',
                                   'Your privacy matters': 'Face ID 지원으로 완벽한 개인정보 보안'},
                         'zh-tw': {   'A calendar, not just a checklist': '日曆視覺化全覽，而非單調的代辦清單',
                                      'An urge rises, peaks, and passes — if you let it.': '衝動會升起、抵達頂峰，隨後自然退去——只要你靜靜覺察。',
                                      'Answers when you need them.': '隨時為您解答常見疑問。',
                                      'Built for a real medicine cabinet': '專為真實家庭藥箱而設計',
                                      'Clean export for doctor visits': '一鍵匯出就診服藥歷史 PDF',
                                      'Critical alerts you actually hear': '響亮防漏鬧鐘，確保絕不錯過',
                                      'Every day, every X days or hours, specific dates, on/off cycles, or as-needed — with a live preview of your next reminders before you save.': '每日固定、間隔 '
                                                                                                                                                                                     'X '
                                                                                                                                                                                     '天或小時、特定日期、吃幾天停幾天的週期，或按需服用——保存前即可預覽下次提醒時間。',
                                      "Everything a reminder app should do. Nothing it shouldn't.": '一款用藥提醒 App '
                                                                                                    '該有的功能它全都有。不該有的多餘干擾一概沒有。',
                                      'Flexible schedules that fit real life': '彈性自訂排程，完美契合真實生活',
                                      "From today's doses to your full medicine list.": '從今天的服藥時間表，到完整藥品庫存清單。',
                                      'Generate a clean, formatted PDF of your dose adherence history to bring to doctor appointments or share with caregivers.': '一鍵生成排版乾淨清晰的服藥遵循率 '
                                                                                                                                                                  'PDF '
                                                                                                                                                                  '報告，方便就醫問診或與照護家人分享。',
                                      'Home groups every dose by time and lets you browse backward and forward through your history — mark a dose taken or skipped right from the day it happened.': '首頁按時間精準分組每次用藥，隨心前後翻閱歷史記錄——在當天直接標記已服藥或跳過。',
                                      'Lock the app behind Face ID, hide medication names from lock screen notifications, and rest easy knowing zero data leaves your phone.': '支援 '
                                                                                                                                                                               'Face '
                                                                                                                                                                               'ID '
                                                                                                                                                                               '快速上鎖、通知中隱藏藥品敏感細節，所有健康數據 '
                                                                                                                                                                               '100% '
                                                                                                                                                                               '保存在您的手機端。',
                                      "Loud alarms that can't be ignored": '響亮防漏鬧鐘，確保絕不錯過',
                                      'Never run out, refill on time': '貼心庫存提醒，及時補充藥品',
                                      'No medical advice, no dosage recommendations, no drug-interaction claims — just a dependable way to track what you take and when.': '不提供未經證實的醫療診斷，只為您提供最可靠、準時的用藥排程與服藥追蹤。',
                                      'On iOS 26 or later, missed reminders can escalate into full alarms that ring even through silent mode, so you never miss a dose.': '在 '
                                                                                                                                                                          'iOS '
                                                                                                                                                                          '系統上，未確認的服藥通知可自動升級為穿透靜音模式的響亮鬧鐘，杜絕漏服。',
                                      'One tap to check in': '鎖定畫面一鍵快速簽到服藥',
                                      'Pill Reminder is on the App Store.': 'Pill Reminder 已在 App Store 上架。',
                                      "Privacy you don't have to think about": '無需多慮的極致隱私保證',
                                      'Refill tracking that speaks up early': '貼心藥品庫存預警，及時補充足夠藥品',
                                      'Schedules that match real prescriptions': '完全契合真實處方簽的彈性週期',
                                      "Set a pill count and a low-stock threshold per medicine. A banner flags refills before you're down to your last dose.": '為每種藥品設定庫存數量與低存量警戒值。在剩最後幾顆之前主動提醒您前往藥局補充。',
                                      'Take your data anywhere': '隨時匯出就醫服藥歷史 PDF',
                                      'Track all your meds effortlessly': '輕鬆管理所有藥品與劑量細節',
                                      'Your history at a glance': '月曆視覺化全覽，歷史紀錄一目了然',
                                      'Your medication list does not need an audience.': '你的用藥隱私，絕不需要任何旁觀者。',
                                      'Your privacy matters': '極致隱私保護，支援 Face ID 解鎖'}},
    'quit-vaping': {   'de': {   '01 · URGE SURFING': '01 · URGE SURFING',
                                 '02 · BODY RECOVERY': '02 · KÖRPERLICHE ERHOLUNG',
                                 '1 Month': '1 Monat',
                                 '2 Weeks': '2 Wochen',
                                 '20 Minutes': '20 Minuten',
                                 '24 Hours': '24 Stunden',
                                 '3 Months': '3 Monate',
                                 '48 Hours': '48 Stunden',
                                 '72 Hours': '72 Stunden',
                                 '8 Hours': '8 Stunden',
                                 'A quiet companion for your quit journey.': 'Ein ruhiger Begleiter für deinen '
                                                                             'Rauchstopp.',
                                 'An urge rises, peaks, and passes — if you let it.': 'Ein Verlangen steigt auf, '
                                                                                      'erreicht seinen Höhepunkt und '
                                                                                      'vergeht — wenn du es zulässt.',
                                 'Built for cigarettes': 'Für Zigaretten konzipiert',
                                 'Built for pods & disposables': 'Für Pods & Einweg-Vapes entwickelt',
                                 'Built for vapers. Not cigarette smokers from 1995.': 'Gebaut für Vaper. Nicht für '
                                                                                       'Raucher aus dem Jahr 1995.',
                                 'Carbon Monoxide & Oxygen': 'Kohlenmonoxid & Sauerstoff',
                                 'Cilia Regeneration': 'Flimmerhärchen regenerieren sich',
                                 'Clinical insights, dopamine science & practical recovery.': 'Klinische Einblicke, '
                                                                                              'Dopamin-Wissenschaft & '
                                                                                              'Erholung.',
                                 'Cravings last 3 minutes.': 'Das Verlangen dauert nur 3 Minuten.',
                                 'Designed for calm, dignified progress.': 'Entwickelt für gelassenen, würdevollen '
                                                                           'Fortschritt.',
                                 'Dopamine Baseline Resets': 'Dopamin-Basislinie normalisiert sich',
                                 'Heart Attack Risk Drops': 'Herzinfarktrisiko sinkt',
                                 'Lung Function Improves': 'Lungenfunktion verbessert sich',
                                 'Nicotine Completely Flushed': 'Nikotin vollständig abgebaut',
                                 'Pulse and Blood Pressure': 'Puls und Blutdruck',
                                 'Quit Vaping': 'Quit Vaping',
                                 'Ready to breathe clean air again?': 'Bereit, wieder saubere Luft zu atmen?',
                                 'Ride the 3-minute crest': 'Reite die 3-Minuten-Welle',
                                 'Taste and Smell Return': 'Geschmack & Geruch kehren zurück',
                                 'Traditional Quit Apps': 'Herkömmliche Rauchstopp-Apps',
                                 "We're here for you.": 'Wir sind für dich da.',
                                 'Your biology begins healing in 20.': 'Dein Körper beginnt in 20 Minuten zu heilen.',
                                 'Your quit journey belongs to you alone.': 'Dein Weg gehört dir ganz allein.'},
                       'es': {   '01 · URGE SURFING': '01 · TÉCNICA URGE SURFING',
                                 '02 · BODY RECOVERY': '02 · RECUPERACIÓN CORPORAL',
                                 '1 Month': '1 Mes',
                                 '2 Weeks': '2 Semanas',
                                 '20 Minutes': '20 Minutos',
                                 '24 Hours': '24 Horas',
                                 '3 Months': '3 Meses',
                                 '48 Hours': '48 Horas',
                                 '72 Hours': '72 Horas',
                                 '8 Hours': '8 Horas',
                                 'A quiet companion for your quit journey.': 'Un compañero sereno en tu camino para '
                                                                             'dejarlo.',
                                 'An urge rises, peaks, and passes — if you let it.': 'Un ansia sube, llega al pico y '
                                                                                      'pasa — si la dejas fluir.',
                                 'Built for cigarettes': 'Pensadas para cigarrillos de combustión',
                                 'Built for pods & disposables': 'Creado para vapeadores y pods',
                                 'Built for vapers. Not cigarette smokers from 1995.': 'Hecho para vapeadores, no para '
                                                                                       'fumadores de 1995.',
                                 'Carbon Monoxide & Oxygen': 'Monóxido de carbono y oxígeno',
                                 'Cilia Regeneration': 'Regeneración de los cilios pulmonares',
                                 'Clinical insights, dopamine science & practical recovery.': 'Datos clínicos, '
                                                                                              'neurociencia de la '
                                                                                              'dopamina y '
                                                                                              'recuperación.',
                                 'Cravings last 3 minutes.': 'El ansia solo dura 3 minutos.',
                                 'Designed for calm, dignified progress.': 'Diseñado para un progreso tranquilo y con '
                                                                           'dignidad.',
                                 'Dopamine Baseline Resets': 'Reajuste de la dopamina',
                                 'Heart Attack Risk Drops': 'Baja el riesgo cardíaco',
                                 'Lung Function Improves': 'Mejora la capacidad pulmonar',
                                 'Nicotine Completely Flushed': 'Nicotina eliminada por completo',
                                 'Pulse and Blood Pressure': 'Pulso y presión arterial',
                                 'Quit Vaping': 'Quit Vaping',
                                 'Ready to breathe clean air again?': '¿Listo para volver a respirar aire puro?',
                                 'Ride the 3-minute crest': 'Supera la ola de 3 minutos',
                                 'Taste and Smell Return': 'Recuperas el gusto y el olfato',
                                 'Traditional Quit Apps': 'Apps de tabaco tradicionales',
                                 "We're here for you.": 'Estamos aquí para ayudarte.',
                                 'Your biology begins healing in 20.': 'Tu cuerpo empieza a sanar a los 20 minutos.',
                                 'Your quit journey belongs to you alone.': 'Tu camino te pertenece exclusivamente a '
                                                                            'ti.'},
                       'fr': {   '01 · URGE SURFING': "01 · SURF SUR L'ENVIE",
                                 '02 · BODY RECOVERY': '02 · RÉCUPÉRATION DU CORPS',
                                 '1 Month': '1 Mois',
                                 '2 Weeks': '2 Semaines',
                                 '20 Minutes': '20 Minutes',
                                 '24 Hours': '24 Heures',
                                 '3 Months': '3 Mois',
                                 '48 Hours': '48 Heures',
                                 '72 Hours': '72 Heures',
                                 '8 Hours': '8 Heures',
                                 'A quiet companion for your quit journey.': 'Un compagnon discret pour votre sevrage.',
                                 'An urge rises, peaks, and passes — if you let it.': 'Une envie monte, culmine et '
                                                                                      'disparaît — si vous la laissez '
                                                                                      'faire.',
                                 'Built for cigarettes': 'Pensé pour le tabac traditionnel',
                                 'Built for pods & disposables': 'Spécifique aux puffs et e-cigarettes',
                                 'Built for vapers. Not cigarette smokers from 1995.': 'Conçu pour les vapoteurs. Pas '
                                                                                       'pour les fumeurs de 1995.',
                                 'Carbon Monoxide & Oxygen': 'Monoxyde de carbone & oxygène',
                                 'Cilia Regeneration': 'Régénération des cils bronchiques',
                                 'Clinical insights, dopamine science & practical recovery.': 'Avis cliniques, '
                                                                                              'dopamine et '
                                                                                              'récupération.',
                                 'Cravings last 3 minutes.': "L'envie ne dure que 3 minutes.",
                                 'Designed for calm, dignified progress.': 'Conçu pour un progrès serein et digne.',
                                 'Dopamine Baseline Resets': 'La dopamine se rééquilibre',
                                 'Heart Attack Risk Drops': 'Le risque cardiaque diminue',
                                 'Lung Function Improves': "La fonction pulmonaire s'améliore",
                                 'Nicotine Completely Flushed': 'Nicotine totalement éliminée',
                                 'Pulse and Blood Pressure': 'Pouls et tension artérielle',
                                 'Quit Vaping': 'Quit Vaping',
                                 'Ready to breathe clean air again?': 'Prêt à respirer à nouveau un air pur ?',
                                 'Ride the 3-minute crest': 'Domptez la vague de 3 minutes',
                                 'Taste and Smell Return': "Le goût et l'odorat reviennent",
                                 'Traditional Quit Apps': 'Applications classiques',
                                 "We're here for you.": 'Nous sommes là pour vous répondre.',
                                 'Your biology begins healing in 20.': 'Votre corps commence à guérir en 20 minutes.',
                                 'Your quit journey belongs to you alone.': 'Votre parcours vous appartient à vous '
                                                                            'seul.'},
                       'it': {   '01 · URGE SURFING': "01 · DOMARE L'IMPULSO",
                                 '02 · BODY RECOVERY': '02 · RECUPERO DEL CORPO',
                                 '1 Month': '1 Mese',
                                 '2 Weeks': '2 Settimane',
                                 '20 Minutes': '20 Minuti',
                                 '24 Hours': '24 Ore',
                                 '3 Months': '3 Mesi',
                                 '48 Hours': '48 Ore',
                                 '72 Hours': '72 Ore',
                                 '8 Hours': '8 Ore',
                                 'A quiet companion for your quit journey.': 'Un alleato discreto per smettere di '
                                                                             'svapare.',
                                 'An urge rises, peaks, and passes — if you let it.': 'Un impulso cresce, tocca il '
                                                                                      'picco e svanisce — se glielo '
                                                                                      'permetti.',
                                 'Built for cigarettes': 'Progettate per le sigarette normali',
                                 'Built for pods & disposables': 'Su misura per pod e usa e getta',
                                 'Built for vapers. Not cigarette smokers from 1995.': 'Creato per chi svapa. Non per '
                                                                                       'i fumatori del 1995.',
                                 'Carbon Monoxide & Oxygen': 'Monossido di carbonio e ossigeno',
                                 'Cilia Regeneration': 'Rigenerazione ciliare polmonare',
                                 'Clinical insights, dopamine science & practical recovery.': 'Evidenze cliniche, '
                                                                                              'dopamina e recupero '
                                                                                              'pratico.',
                                 'Cravings last 3 minutes.': "L'impulso dura solo 3 minuti.",
                                 'Designed for calm, dignified progress.': 'Pensato per un percorso dignitoso e '
                                                                           'sereno.',
                                 'Dopamine Baseline Resets': 'La dopamina si stabilizza',
                                 'Heart Attack Risk Drops': 'Cala il rischio cardiaco',
                                 'Lung Function Improves': 'La funzionalità polmonare migliora',
                                 'Nicotine Completely Flushed': 'Nicotina eliminata del tutto',
                                 'Pulse and Blood Pressure': 'Battito e pressione arteriosa',
                                 'Quit Vaping': 'Quit Vaping',
                                 'Ready to breathe clean air again?': 'Pronto a respirare di nuovo aria pulita?',
                                 'Ride the 3-minute crest': 'Supera il picco dei 3 minuti',
                                 'Taste and Smell Return': 'Gusto e olfatto ritornano',
                                 'Traditional Quit Apps': 'App per smettere tradizionali',
                                 "We're here for you.": 'Siamo a tua completa disposizione.',
                                 'Your biology begins healing in 20.': 'Il tuo corpo comincia a rigenerarsi dopo 20 '
                                                                       'minuti.',
                                 'Your quit journey belongs to you alone.': 'Il tuo percorso appartiene solo a te.'},
                       'ja': {   '01 · URGE SURFING': '01 · アージサーフィン',
                                 '02 · BODY RECOVERY': '02 · 身体回復タイムライン',
                                 '1 Month': '1ヶ月',
                                 '2 Weeks': '2週間',
                                 '20 Minutes': '20分',
                                 '24 Hours': '24時間',
                                 '3 Months': '3ヶ月',
                                 '48 Hours': '48時間',
                                 '72 Hours': '72時間',
                                 '8 Hours': '8時間',
                                 'A quiet companion for your quit journey.': 'あなたの禁煙に寄り添う静かなパートナー。',
                                 'An urge rises, peaks, and passes — if you let it.': '欲求は高まり、頂点に達し、やがて消えていきます。',
                                 'Built for cigarettes': '紙巻きタバコ専用',
                                 'Built for pods & disposables': '使い捨てベイプ・ポッド専用設計',
                                 'Built for vapers. Not cigarette smokers from 1995.': '紙巻きタバコではなく、現代のベイプ愛用者のために。',
                                 'Carbon Monoxide & Oxygen': '一酸化炭素と血中酸素',
                                 'Cilia Regeneration': '肺の線毛が再生',
                                 'Clinical insights, dopamine science & practical recovery.': '臨床知見、ドーパミン科学、回復のヒント。',
                                 'Cravings last 3 minutes.': 'ニコチンの渇望は3分間で収まります。',
                                 'Designed for calm, dignified progress.': '穏やかで前向きな進歩のためのデザイン。',
                                 'Dopamine Baseline Resets': 'ドーパミンの基準値がリセット',
                                 'Heart Attack Risk Drops': '心臓への負担が軽減',
                                 'Lung Function Improves': '肺機能が向上',
                                 'Nicotine Completely Flushed': 'ニコチンが体内から完全に排出',
                                 'Pulse and Blood Pressure': '脈拍と血圧',
                                 'Quit Vaping': 'Quit Vaping',
                                 'Ready to breathe clean air again?': 'もう一度、澄んだ空気を胸いっぱいに吸い込みませんか？',
                                 'Ride the 3-minute crest': '3分間の波を乗り越える',
                                 'Taste and Smell Return': '味覚と嗅覚が復活',
                                 'Traditional Quit Apps': '従来の禁煙アプリ',
                                 "We're here for you.": 'いつでもあなたをサポートします。',
                                 'Your biology begins healing in 20.': '身体は20分以内に回復を始めます。',
                                 'Your quit journey belongs to you alone.': '禁煙の道のりは、あなただけのものです。'},
                       'ko': {   '01 · URGE SURFING': '01 · 갈망 서핑 호흡',
                                 '02 · BODY RECOVERY': '02 · 신체 회복 타임라인',
                                 '1 Month': '1개월',
                                 '2 Weeks': '2주',
                                 '20 Minutes': '20분',
                                 '24 Hours': '24시간',
                                 '3 Months': '3개월',
                                 '48 Hours': '48시간',
                                 '72 Hours': '72시간',
                                 '8 Hours': '8시간',
                                 'A quiet companion for your quit journey.': '금연 여정을 묵묵히 지켜주는 든든한 동반자.',
                                 'An urge rises, peaks, and passes — if you let it.': '갈망은 솟아오르고, 정점에 도달한 뒤, 가만히 지켜보면 '
                                                                                      '저절로 지나갑니다.',
                                 'Built for cigarettes': '일반 연초 중심',
                                 'Built for pods & disposables': '팟 및 일회용 전자담배 전용 설계',
                                 'Built for vapers. Not cigarette smokers from 1995.': '1995년의 연초 흡연자가 아닌 현대의 전자담배 '
                                                                                       '사용자를 위한 앱.',
                                 'Carbon Monoxide & Oxygen': '일산화탄소 배출 및 산소 회복',
                                 'Cilia Regeneration': '기관지 섬모 재생',
                                 'Clinical insights, dopamine science & practical recovery.': '임상 인사이트, 도파민 과학 및 실질적인 '
                                                                                              '회복 가이드.',
                                 'Cravings last 3 minutes.': '흡연 충동은 3분이면 지나갑니다.',
                                 'Designed for calm, dignified progress.': '자책감 없이 차분하고 자존감 넘치는 성장을 돕습니다.',
                                 'Dopamine Baseline Resets': '도파민 보상 회로 재설정',
                                 'Heart Attack Risk Drops': '심장마비 위험 감소',
                                 'Lung Function Improves': '폐 기능 대폭 개선',
                                 'Nicotine Completely Flushed': '체내 니코틴 완전 배출',
                                 'Pulse and Blood Pressure': '맥박 및 혈압 정상화',
                                 'Quit Vaping': 'Quit Vaping',
                                 'Ready to breathe clean air again?': '다시 깨끗한 공기를 깊이 들이마실 준비가 되셨나요?',
                                 'Ride the 3-minute crest': '3분의 파도를 지혜롭게 넘기세요',
                                 'Taste and Smell Return': '미각과 후각의 회복',
                                 'Traditional Quit Apps': '기존 금연 앱',
                                 "We're here for you.": '질문이 있으신가요? 언제든 도와드립니다.',
                                 'Your biology begins healing in 20.': '당신의 신체는 20분 만에 치유를 시작합니다.',
                                 'Your quit journey belongs to you alone.': '당신의 금연 여정은 오직 당신만을 위한 것입니다.'},
                       'zh-tw': {   '01 · URGE SURFING': '01 · 衝動衝浪法',
                                    '02 · BODY RECOVERY': '02 · 身體修復時間軸',
                                    '1 Month': '1 個月',
                                    '2 Weeks': '2 週',
                                    '20 Minutes': '20 分鐘',
                                    '24 Hours': '24 小時',
                                    '3 Months': '3 個月',
                                    '48 Hours': '48 小時',
                                    '72 Hours': '72 小時',
                                    '8 Hours': '8 小時',
                                    'A quiet companion for your quit journey.': '陪伴你重獲自由的安靜夥伴。',
                                    'An urge rises, peaks, and passes — if you let it.': '衝動會升起、抵達頂峰，隨後自然退去——只要你靜靜覺察。',
                                    'Built for cigarettes': '專為傳統紙煙設計',
                                    'Built for pods & disposables': '專為煙彈與拋棄式煙具打造',
                                    'Built for vapers. Not cigarette smokers from 1995.': '專為現代電子煙打造，而非 1995 年的傳統紙煙。',
                                    'Carbon Monoxide & Oxygen': '一氧化碳與血氧',
                                    'Cilia Regeneration': '肺部纖毛再生完成',
                                    'Clinical insights, dopamine science & practical recovery.': '臨床實證洞察、多巴胺醫學與戒除康復指南。',
                                    'Cravings last 3 minutes.': '煙癮衝動只持續 3 分鐘。',
                                    'Designed for calm, dignified progress.': '專為平靜、有尊嚴的進步而設計。',
                                    'Dopamine Baseline Resets': '多巴胺基準線重設完畢',
                                    'Heart Attack Risk Drops': '心臟病發作風險下降',
                                    'Lung Function Improves': '肺功能大幅提升',
                                    'Nicotine Completely Flushed': '體內尼古丁完全排出',
                                    'Pulse and Blood Pressure': '脈搏與血壓',
                                    'Quit Vaping': 'Quit Vaping',
                                    'Ready to breathe clean air again?': '準備好再次呼吸純淨清新的空氣了嗎？',
                                    'Ride the 3-minute crest': '駕馭 3 分鐘的欲望浪潮',
                                    'Taste and Smell Return': '味覺與嗅覺敏銳度重現',
                                    'Traditional Quit Apps': '傳統戒煙 App',
                                    "We're here for you.": '我們隨時在此為你解答。',
                                    'Your biology begins healing in 20.': '身體機能在 20 分鐘內立即展開修復。',
                                    'Your quit journey belongs to you alone.': '戒煙是你的個人歷程，無須向外界交代。'}}}
