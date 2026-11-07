import re

with open('/Users/louisliu/Documents/repo/liuys_website/app-i18n.js', 'r', encoding='utf-8') as f:
    content = f.read()

FEATURES_DATA = {
    "inkstone": {
        "zh-tw": ["即時 PDF 匯入與相機文件掃描", "支援手寫簽名、縮寫、日期與表單欄位", "分享加密瀏覽器簽署連結，對方零門檻秒簽", "SHA-256 數位憑證與完整稽核紀錄軌跡"],
        "ja": ["瞬時のPDF取り込みとカメラ文書スキャン", "手書き署名、イニシャル、日付、フォーム入力対応", "暗号化リンクを共有し、ブラウザ上で即座に署名", "SHA-256電子証明書と監査証跡を完備"],
        "ko": ["즉각적인 PDF 가져오기 및 카메라 문서 스캔", "서명, 이니셜, 날짜 및 텍스트 폼 입력", "암호화된 브라우저 서명 링크 공유로 상대방 즉시 서명", "SHA-256 디지털 인증서 및 감사 추적 기록"],
        "de": ["Blitzschneller PDF-Import & Kamera-Dokumentenscan", "Unterschriften, Initialen, Datumsangaben & Formularfelder", "Verschlüsselte Browser-Links ganz ohne Barrieren für den Empfänger", "SHA-256 Digitalzertifikat & revisionssicherer Prüfpfad"],
        "fr": ["Import PDF instantané et numérisation par appareil photo", "Signatures, initiales, dates et champs de formulaire", "Liens de signature chiffrés sur navigateur sans friction", "Certificat numérique SHA-256 et piste d'audit"],
        "es": ["Importación instantánea de PDF y escaneo con cámara", "Firmas, iniciales, fechas y campos de formulario", "Enlaces cifrados de firma en navegador sin fricción", "Certificado digital SHA-256 y pista de auditoría"],
        "it": ["Importazione PDF istantanea e scansione documenti da fotocamera", "Firme, sigle, date e campi modulo", "Link di firma crittografati da browser senza alcuna difficoltà", "Certificato digitale SHA-256 e traccia di audit"]
    },
    "pill-reminder": {
        "zh-tw": ["智慧週期用藥與維他命排程", "藥品即將用罄前自動發送補藥提醒", "支援醫師門診所需的 PDF 與 CSV 健康紀錄匯出", "100% 本機端離線儲存，零隱私追蹤"],
        "ja": ["お薬やサプリメントの柔軟な繰り返しリマインダー", "薬が切れる前の残薬補充アラート", "医師の診察にそのまま提出できるPDF・CSV出力", "完全ローカル保存・個人情報追跡ゼロ"],
        "ko": ["스마트 복약 및 영양제 반복 스케줄", "약이 떨어지기 전 잔여량 부족 알림", "의사 상담용 맞춤형 PDF 및 CSV 건강 내보내기", "100% 기기 내 저장으로 개인정보 추적 제로"],
        "de": ["Intelligente Einnahmepläne für Medikamente & Vitamine", "Warnungen bei niedrigem Vorrat vor dem Aufbrauchen", "Arztfertiger PDF- & CSV-Gesundheitsexport", "100 % lokaler Datenschutz ganz ohne Tracking"],
        "fr": ["Rappels récurrents pour médicaments et vitamines", "Alertes de stock bas avant la fin du traitement", "Export de santé PDF et CSV pour votre médecin", "Confidentialité 100 % sur l'appareil sans suivi"],
        "es": ["Horarios inteligentes y recurrentes para medicación y vitaminas", "Alertas de existencias bajas antes de que se acaben", "Exportación de salud en PDF y CSV lista para el médico", "Privacidad 100% en el dispositivo sin rastreo"],
        "it": ["Orari intelligenti e ricorrenti per farmaci e integratori", "Avvisi di scorta bassa prima che il medicinale finisca", "Esportazione della cartella in PDF e CSV per il medico", "Privacy al 100% sul dispositivo senza alcun tracciamento"]
    },
    "grocery-price": {
        "zh-tw": ["相機標籤掃描與 OCR 價格自動辨識", "自動換算統一單位成本（$/盎司、$/磅、$/公斤）", "多間超市歷史比價與通膨價格紀錄", "專為超市走道快速查詢打造的本機秒開速度"],
        "ja": ["カメラでの値札スキャン＆OCR価格自動認識", "単位あたりの価格を自動正規化（$/oz、$/lb、$/kg）", "複数店舗の価格比較とインフレ推移ログ", "スーパーの売り場でも待たずに使える高速ローカル動作"],
        "ko": ["카메라 가격표 스캔 및 OCR 가격 자동 인식", "단위당 비용 자동 환산 ($/oz, $/lb, $/kg)", "여러 마트 간 가격 비교 및 물가 상승 추적", "매장 통로에서도 막힘없는 초고속 로컬 구동"],
        "de": ["Kamera-Preisschild-Scan & OCR-Preiserkennung", "Automatische Normalisierung der Grundpreise (€/kg, €/l)", "Preisvergleich über mehrere Märkte & Inflationsprotokoll", "Blitzschnelle Offline-Nutzung direkt im Supermarktzweig"],
        "fr": ["Numérisation d'étiquettes par caméra et OCR instantané", "Calcul automatique du prix à l'unité (€/kg, €/L)", "Comparateur multi-magasins et suivi de l'inflation", "Vitesse hors ligne instantanée dans les rayons"],
        "es": ["Escaneo de etiquetas con cámara y reconocimiento OCR", "Normalización automática del precio por unidad (€/kg, €/l)", "Comparación entre tiendas y registro de inflación", "Velocidad ultrarrápida sin conexión en el pasillo del súper"],
        "it": ["Scansione cartellini con fotocamera e riconoscimento OCR", "Normalizzazione automatica del prezzo unitario (€/kg, €/l)", "Confronto prezzi tra punti vendita e archivio rincari", "Velocità istantanea offline tra le corsie del supermercato"]
    },
    "alcohol-free-tracker": {
        "zh-tw": ["即時記錄無酒天數與清醒時數", "精算已省下的金錢開銷與卡路里攝取", "私密反思筆記與個人飲酒誘因追蹤", "重要里程碑徽章與可自訂主畫面小工具"],
        "ja": ["休肝日数と清醒時間のリアルタイムカウンター", "節約できた金額とカロリーの自動計算", "非公開の振り返り日記と飲酒トリガー分析", "達成バッジと自由にカスタマイズできるウィジェット"],
        "ko": ["무음주 일수 및 시간 실시간 카운터", "절약한 지출과 칼로리 계산기", "프라이빗 반성 일기 및 음주 유혹 트리거 추적", "마일스톤 배지 및 홈 화면 맞춤 위젯"],
        "de": ["Echtzeit-Zähler für alkoholfreie Tage und Stunden", "Ersparnis-Rechner für Geld und eingesparte Kalorien", "Privates Tagebuch & Erkennung persönlicher Auslöser", "Meilenstein-Abzeichen und anpassbare Startbildschirm-Widgets"],
        "fr": ["Compteur en temps réel des jours et heures de sobriété", "Calculateur des économies d'argent et de calories", "Journal de réflexion intime et suivi des déclencheurs", "Badges d'étapes et widgets d'écran d'accueil personnalisables"],
        "es": ["Contador en tiempo real de días y horas sin alcohol", "Calculadoras de dinero y calorías ahorradas", "Diario de reflexión privado y registro de detonantes", "Insignias de logros y widgets personalizables para la pantalla de inicio"],
        "it": ["Conteggio in tempo reale di giorni e ore senza alcol", "Calcolatori del risparmio economico e delle calorie evitate", "Diario personale di riflessione e mappa dei trigger", "Distintivi per i traguardi e widget personalizzabili per la Home"]
    },
    "quit-weed": {
        "zh-tw": ["4-7-8 迷走神經蓮花呼吸引導 SOS", "CB1 受體重新上調與多巴胺修復時間軸", "雙模式支援：30 天耐受度重置或徹底戒除", "即時計算已省下的大麻專賣店花費"],
        "ja": ["衝動を鎮める4-7-8迷走神経ロータス呼吸SOS", "CB1受容体活性化とドーパミン回復タイムライン", "選べる2つのモード：30日間リセットまたは完全断禁", "大麻の購入費用と節約金額をリアルタイム計算"],
        "ko": ["갈망 완화를 위한 4-7-8 미주신경 연꽃 호흡 SOS", "CB1 수용체 재활성화 및 도파민 회복 타임라인", "듀얼 모드 지원: 30일 내성 휴식기 또는 완전 금연", "절약한 대마초 구매 비용 실시간 계산기"],
        "de": ["4-7-8 Vagusnerv-Lotus-Atmung als Soforthilfe bei Verlangen", "Zeitleiste für CB1-Rezeptoren & Dopamin-Regeneration", "Dual-Modus: 30-Tage-T-Break oder dauerhafter Ausstieg", "Echtzeit-Ersparnis-Rechner für Ausgaben"],
        "fr": ["Respiration du lotus 4-7-8 pour calmer l'envie aiguë", "Chronologie de restauration des récepteurs CB1 et de la dopamine", "Double mode : pause de 30 jours (T-Break) ou arrêt définitif", "Compteur en direct des économies réalisées sur le cannabis"],
        "es": ["Respiración de loto 4-7-8 para calmar el deseo intenso", "Cronología de restauración de receptores CB1 y dopamina", "Modo dual: pausa de 30 días (T-Break) o cese definitivo", "Contador en tiempo real del dinero ahorrado en dispensarios"],
        "it": ["Respirazione loto 4-7-8 per calmare l'impulso acuto", "Cronologia del recupero dei recettori CB1 e della dopamina", "Doppia modalità: pausa di 30 giorni (T-Break) o stop definitivo", "Contatore in tempo reale delle spese risparmiate"]
    },
    "quit-vaping": {
        "zh-tw": ["專為拋棄式電子煙與煙彈打造的無煙日追蹤", "20 分鐘至 30 天人體器官生理修復時間軸", "3 分鐘渴望衝浪呼吸引導平息尼古丁衝動", "100% 本機離線運作，無須註冊帳號"],
        "ja": ["使い捨てやポッドに特化した断煙トラッカー", "20分から30日までの身体回復タイムライン", "ニコチン欲求を乗り切る3分間アージ・サーフィン呼吸", "アカウント不要・完全ローカル＆オフライン動作"],
        "ko": ["일회용 전자담배 및 팟 맞춤형 금연 추적", "20분부터 30일까지의 신체 기능 회복 타임라인", "니코틴 갈망을 넘겨주는 3분 파도타기 호흡법", "가입 없이 100% 기기 내에서만 오프라인 작동"],
        "de": ["Vape-freie Tage für Einweggeräte und Pods erfassen", "Körperliche Erholungs-Zeitleiste von 20 Minuten bis 30 Tagen", "3-Minuten Urge Surfing gegen akutes Nikotinverlangen", "100 % privat & offline, ohne jedes Konto"],
        "fr": ["Suivi des jours sans vape pour puffs et recharges", "Chronologie de récupération corporelle de 20 minutes à 30 jours", "Surf de l'envie en 3 minutes contre le besoin de nicotine", "100 % privé et hors ligne, sans inscription"],
        "es": ["Seguimiento de días sin vapear para desechables y pods", "Cronología de recuperación corporal de 20 minutos a 30 días", "Surfeo del deseo en 3 minutos contra el mono de nicotina", "100% privado y sin conexión, sin crear cuenta"],
        "it": ["Tracciamento dei giorni senza svapo per usa e getta e pod", "Cronologia di recupero del corpo da 20 minuti a 30 giorni", "Tecnica di 3 minuti per cavalcare la voglia di nicotina", "100% privato e offline, senza alcun account"]
    },
    "levain": {
        "zh-tw": ["從水解到出爐一氣呵成的全流程烘焙時間軸", "穿透靜音模式的階段強效鬧鐘提醒", "Apple Watch 與 iPhone 鎖定畫面即時倒數", "精準烘焙百分比計算與圖文烘焙日誌"],
        "ja": ["オートリーズから焼成までを1本のタイムラインで管理", "マナーモードでも確実に鳴るステージ別アラーム", "Apple Watch およびロック画面でのリアルタイムカウントダウン", "ベーカーズパーセント計算機と写真付き製パン日誌"],
        "ko": ["오토리즈부터 굽기까지 전 과정을 아우르는 단일 타임라인", "무음 모드에서도 확실하게 울리는 단계별 알람", "Apple Watch 및 잠금 화면 실시간 카운트다운", "베이커스 퍼센트 계산기 및 비주얼 사진 일지"],
        "de": ["Eine durchgehende Zeitleiste von der Autolyse bis zum Ofen", "Alarme, die zuverlässig auch im Stummschaltmodus klingeln", "Apple Watch- und Sperrbildschirm-Countdown", "Bäckerprozente und ein visuelles Fototagebuch auf dem Gerät"],
        "fr": ["Une seule chronologie complète de l'autolyse à la sortie du four", "Alarmes sonores retentissant même en mode silencieux", "Compte à rebours sur écran verrouillé et Apple Watch", "Calculateur de pourcentage du boulanger et journal photo"],
        "es": ["Una única cronología desde la autólisis hasta el horneado", "Alarmas que suenan incluso con el modo silencio activo", "Cuenta atrás en la pantalla de bloqueo y en el Apple Watch", "Porcentajes de panadero y diario fotográfico en el dispositivo"],
        "it": ["Un'unica sequenza dall'autolisi fino all'uscita dal forno", "Allarmi che suonano anche con la suoneria silenziosa", "Conto alla rovescia su Apple Watch e schermata di blocco", "Percentuali del fornaio e diario fotografico sul dispositivo"]
    },
    "agricola-scorer": {
        "zh-tw": ["取代繁瑣紙筆計分表的數位計分板", "完整支援全系列擴充與沼澤農夫規則", "對局歷史存檔、積分排行榜與最高分紀錄", "專為桌遊聚會打造的極速觸控輸入"],
        "ja": ["紙のスコアシートを置き換える直感的なデジタル計算板", "各種拡張セットおよび『泥沼からの出発』ルールに完全対応", "対戦履歴の保存、リーダーボード、ハイスコア記録", "オフラインで手軽に入力できるスムーズな操作感"],
        "ko": ["종이 점수표를 완벽히 대체하는 디지털 스코어보드", "모든 확장판 및 늪지 농부 룰 완벽 지원", "게임 전적 보관, 리더보드 및 최고 득점 통계", "오프라인에서도 막힘없이 빠른 원터치 입력"],
        "de": ["Digitaler Wertungsblock als Ersatz für Papierbögen", "Volle Unterstützung für Erweiterungen und 'Die Moorbauern'", "Spielhistorie, Bestenlisten und Rekord-Wertungen", "Schnelle, berührungsoptimierte Bedienung ohne Internet"],
        "fr": ["Bloc de score numérique remplaçant les feuilles de papier", "Prise en charge des extensions et des 'Fermiers de la Lande'", "Historique des parties, classement et meilleurs scores", "Saisie tactile ultra-rapide et totalement hors ligne"],
        "es": ["Marcador digital que sustituye las hojas de papel", "Compatible con expansiones y 'Los granjeros del pantano'", "Historial de partidas, clasificaciones y récords de puntos", "Entrada táctil rápida y sin fricción sin conexión"],
        "it": ["Segnapunti digitale che sostituisce i blocchetti cartacei", "Supporto per tutte le espansioni e 'I Contadini della Brughiera'", "Archivio partite, classifica e punteggi record", "Inserimento tattile rapido e immediato senza rete"]
    }
}

# Duplicate for grocery-price-scanner
FEATURES_DATA["grocery-price-scanner"] = FEATURES_DATA["grocery-price"]

import json
# Insert features into APPS_I18N in content
for app_id, locs in FEATURES_DATA.items():
    for loc, feats in locs.items():
        # find the block for app_id and loc
        feats_js = json.dumps(feats, ensure_ascii=False)
        # Search pattern: "app_id": { ... "loc": { ... desc: "..."
        pattern = rf'(\"{app_id}\":\s*\{{[^}}]*?\"{loc}\":\s*\{{[^}}]*?desc:\s*\"[^\"]*\",?)'
        match = re.search(pattern, content, re.DOTALL)
        if match:
            orig = match.group(1)
            if 'features:' not in orig:
                repl = f'{orig}\n      features: {feats_js},'
                content = content.replace(orig, repl)

# Also ensure grocery-price-scanner is an alias if not present
if '"grocery-price-scanner":' not in content and '"grocery-price":' in content:
    content = content.replace('"grocery-price": {', '"grocery-price-scanner": APPS_I18N_GROCERY,\n  "grocery-price": {')

with open('/Users/louisliu/Documents/repo/liuys_website/app-i18n.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated app-i18n.js with localized feature bullets!")
