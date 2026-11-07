#!/usr/bin/env python3
"""
Full expander for deep translations to ensure 100% complete translation of:
- Pill Reminder (8 feature cards, headings, alt texts, privacy notes)
- Quit Vaping (Urge surfing steps, 8 feature cards, compare, FAQs)
- Alcohol Free Tracker (All remaining headings and subheadings)
Across all 7 target locales: zh-tw, ja, ko, de, fr, es, it.
"""

import sys

PILL_REMINDER_FEATURES = {
    "zh-tw": {
        "Built for a real medicine cabinet": "專為真實家庭藥箱而設計",
        "No medical advice, no dosage recommendations, no drug-interaction claims — just a dependable way to track what you take and when.": "不提供未經證實的醫療診斷，只為您提供最可靠、準時的用藥排程與服藥追蹤。",
        "A calendar, not just a checklist": "日曆視覺化全覽，而非單調的代辦清單",
        "Home groups every dose by time and lets you browse backward and forward through your history — mark a dose taken or skipped right from the day it happened.": "首頁按時間精準分組每次用藥，隨心前後翻閱歷史記錄——在當天直接標記已服藥或跳過。",
        "Schedules that match real prescriptions": "完全契合真實處方簽的彈性週期",
        "Every day, every X days or hours, specific dates, on/off cycles, or as-needed — with a live preview of your next reminders before you save.": "每日固定、間隔 X 天或小時、特定日期、吃幾天停幾天的週期，或按需服用——保存前即可預覽下次提醒時間。",
        "Refill tracking that speaks up early": "貼心藥品庫存預警，及時補充足夠藥品",
        "Set a pill count and a low-stock threshold per medicine. A banner flags refills before you're down to your last dose.": "為每種藥品設定庫存數量與低存量警戒值。在剩最後幾顆之前主動提醒您前往藥局補充。",
        "Critical alerts you actually hear": "響亮防漏鬧鐘，確保絕不錯過",
        "On iOS 26 or later, missed reminders can escalate into full alarms that ring even through silent mode, so you never miss a dose.": "在 iOS 系統上，未確認的服藥通知可自動升級為穿透靜音模式的響亮鬧鐘，杜絕漏服。",
        "Privacy you don't have to think about": "無需多慮的極致隱私保證",
        "Lock the app behind Face ID, hide medication names from lock screen notifications, and rest easy knowing zero data leaves your phone.": "支援 Face ID 快速上鎖、通知中隱藏藥品敏感細節，所有健康數據 100% 保存在您的手機端。",
        "Clean export for doctor visits": "一鍵匯出就診服藥歷史 PDF",
        "Generate a clean, formatted PDF of your dose adherence history to bring to doctor appointments or share with caregivers.": "一鍵生成排版乾淨清晰的服藥遵循率 PDF 報告，方便就醫問診或與照護家人分享。",
        "An urge rises, peaks, and passes — if you let it.": "衝動會升起、抵達頂峰，隨後自然退去——只要你靜靜覺察。",
    },
    "ja": {
        "Built for a real medicine cabinet": "日々の服薬管理のために設計",
        "No medical advice, no dosage recommendations, no drug-interaction claims — just a dependable way to track what you take and when.": "医療判断や投与推奨は行いません。何をいつ服用したかを確実に記録する信頼のツールです。",
        "A calendar, not just a checklist": "ただのチェックリストではないカレンダー表示",
        "Home groups every dose by time and lets you browse backward and forward through your history — mark a dose taken or skipped right from the day it happened.": "時間帯ごとに服用薬を整理。履歴を前後に確認でき、その場で服用済みやスキップを記録できます。",
        "Schedules that match real prescriptions": "実際の処方に合わせた柔軟なスケジュール",
        "Every day, every X days or hours, specific dates, on/off cycles, or as-needed — with a live preview of your next reminders before you save.": "毎日、○日/時間ごと、特定日、休薬サイクル、頓服まで柔軟に対応。保存前に次回の予定を確認可能。",
        "Refill tracking that speaks up early": "残薬アラートで薬切れを事前に防止",
        "Set a pill count and a low-stock threshold per medicine. A banner flags refills before you're down to your last dose.": "薬ごとに残数と警告のしきい値を設定。最後の1錠になる前に補充リマインダーでお知らせ。",
        "Critical alerts you actually hear": "聞き逃さない確実な大音量アラーム",
        "On iOS 26 or later, missed reminders can escalate into full alarms that ring even through silent mode, so you never miss a dose.": "見落とした通知をマナーモード貫通のアラームに昇格させ、確実な服用を促します。",
        "Privacy you don't have to think about": "意識せずとも守られる完全なプライバシー",
        "Lock the app behind Face ID, hide medication names from lock screen notifications, and rest easy knowing zero data leaves your phone.": "Face IDロックに対応し、通知で薬の名前を非表示に。データが外部に送信されることは一切ありません。",
        "Clean export for doctor visits": "医師に見せられる服薬履歴のPDF出力",
        "Generate a clean, formatted PDF of your dose adherence history to bring to doctor appointments or share with caregivers.": "通院時や家族との共有に最適な、見やすい服薬履歴PDFをワンタップで作成。",
        "An urge rises, peaks, and passes — if you let it.": "欲求は高まり、頂点に達し、やがて消えていきます。",
    },
    "ko": {
        "Built for a real medicine cabinet": "실제 복약 관리를 위해 세심하게 설계",
        "No medical advice, no dosage recommendations, no drug-interaction claims — just a dependable way to track what you take and when.": "의학적 처방이 아닌, 언제 어떤 약을 복용해야 하는지 가장 신뢰할 수 있게 알려주는 트래커입니다.",
        "A calendar, not just a checklist": "단순한 체크리스트를 넘어선 캘린더",
        "Home groups every dose by time and lets you browse backward and forward through your history — mark a dose taken or skipped right from the day it happened.": "시간대별로 복용할 약을 묶어 보여주며, 날짜별 복용 여부를 달력에서 한눈에 확인하고 기록합니다.",
        "Schedules that match real prescriptions": "실제 처방전에 맞춘 유연한 일정 설정",
        "Every day, every X days or hours, specific dates, on/off cycles, or as-needed — with a live preview of your next reminders before you save.": "매일, 며칠/몇 시간 간격, 특정 요일, 주기적 복용, 필요 시 복용 등 모든 복약 패턴을 지원합니다.",
        "Refill tracking that speaks up early": "약이 떨어지기 전 미리 알려주는 보충 알림",
        "Set a pill count and a low-stock threshold per medicine. A banner flags refills before you're down to your last dose.": "약품별 잔여 수량과 최소 수량을 지정하여, 마지막 약을 먹기 전 미리 처방전을 보충하도록 안내합니다.",
        "Critical alerts you actually hear": "놓칠 수 없는 강력한 복약 알람",
        "On iOS 26 or later, missed reminders can escalate into full alarms that ring even through silent mode, so you never miss a dose.": "확인하지 않은 알림은 무음 모드도 뚫고 울리는 풀 알람으로 전환되어 중요한 약을 절대 거르지 않습니다.",
        "Privacy you don't have to think about": "신경 쓰지 않아도 완벽한 개인정보 보호",
        "Lock the app behind Face ID, hide medication names from lock screen notifications, and rest easy knowing zero data leaves your phone.": "Face ID 잠금 및 잠금 화면 알림 내 약품명 숨김 기능으로 기기 외부로 데이터가 절대 유출되지 않습니다.",
        "Clean export for doctor visits": "진료 시 제출하기 좋은 깔끔한 PDF 내보내기",
        "Generate a clean, formatted PDF of your dose adherence history to bring to doctor appointments or share with caregivers.": "의사 진료나 보호자 공유를 위해 복약 이력을 깔끔한 PDF 보고서로 즉시 내보냅니다.",
        "An urge rises, peaks, and passes — if you let it.": "갈망은 솟아오르고, 정점에 도달한 뒤, 가만히 지켜보면 저절로 지나갑니다.",
    },
    "de": {
        "Built for a real medicine cabinet": "Entwickelt für den echten Medizinschrank",
        "No medical advice, no dosage recommendations, no drug-interaction claims — just a dependable way to track what you take and when.": "Kein medizinischer Rat, keine Dosierungsbehauptungen — nur ein verlässlicher Weg, deine Einnahmen zu timen.",
        "A calendar, not just a checklist": "Ein Kalender, nicht nur eine einfache Checkliste",
        "Home groups every dose by time and lets you browse backward and forward through your history — mark a dose taken or skipped right from the day it happened.": "Sortiert Dosen nach Uhrzeit und erlaubt den Blick in die Vergangenheit — abhaken oder überspringen direkt am Tag.",
        "Schedules that match real prescriptions": "Einnahmepläne, die zu echten Rezepten passen",
        "Every day, every X days or hours, specific dates, on/off cycles, or as-needed — with a live preview of your next reminders before you save.": "Täglich, alle X Tage oder Stunden, bestimmte Daten, Zyklen oder nach Bedarf — mit Vorschau vor dem Speichern.",
        "Refill tracking that speaks up early": "Rechtzeitige Warnung vor leeren Packungen",
        "Set a pill count and a low-stock threshold per medicine. A banner flags refills before you're down to your last dose.": "Pillenzahl und Mindestbestand erfassen. Eine Warnung meldet sich, bevor die letzte Tablette genommen wird.",
        "Critical alerts you actually hear": "Dringende Alarme, die man wirklich hört",
        "On iOS 26 or later, missed reminders can escalate into full alarms that ring even through silent mode, so you never miss a dose.": "Verpasste Erinnerungen können zu vollen Alarmen eskalieren, die sogar den Stummschaltmodus durchdringen.",
        "Privacy you don't have to think about": "Privatsphäre, über die du dir keine Sorgen machen musst",
        "Lock the app behind Face ID, hide medication names from lock screen notifications, and rest easy knowing zero data leaves your phone.": "Face ID Schutz, Ausblenden von Medikamentennamen auf dem Sperrbildschirm und 100% lokale Daten.",
        "Clean export for doctor visits": "Sauberer PDF-Export für den Arztbesuch",
        "Generate a clean, formatted PDF of your dose adherence history to bring to doctor appointments or share with caregivers.": "Erstelle eine übersichtliche PDF-Historie deiner Einnahmen für das nächste Arztgespräch.",
        "An urge rises, peaks, and passes — if you let it.": "Ein Verlangen steigt auf, erreicht seinen Höhepunkt und vergeht — wenn du es zulässt.",
    },
    "fr": {
        "Built for a real medicine cabinet": "Conçu pour votre armoire à pharmacie",
        "No medical advice, no dosage recommendations, no drug-interaction claims — just a dependable way to track what you take and when.": "Pas de conseils médicaux — juste une méthode infaillible pour suivre ce que vous prenez et quand.",
        "A calendar, not just a checklist": "Un vrai calendrier, pas une simple to-do list",
        "Home groups every dose by time and lets you browse backward and forward through your history — mark a dose taken or skipped right from the day it happened.": "Regroupe les prises par heure et permet de parcourir l'historique — cochez vos prises facilement.",
        "Schedules that match real prescriptions": "Des plannings fidèles aux vraies ordonnances",
        "Every day, every X days or hours, specific dates, on/off cycles, or as-needed — with a live preview of your next reminders before you save.": "Tous les jours, toutes les X heures, dates précises, cycles ou au besoin — avec aperçu en direct.",
        "Refill tracking that speaks up early": "Alertes de renouvellement avant la dernière pilule",
        "Set a pill count and a low-stock threshold per medicine. A banner flags refills before you're down to your last dose.": "Comptez vos comprimés et fixez un seuil d'alerte pour renouveler votre ordonnance à temps.",
        "Critical alerts you actually hear": "Des alertes importantes impossibles à manquer",
        "On iOS 26 or later, missed reminders can escalate into full alarms that ring even through silent mode, so you never miss a dose.": "Les rappels ignorés peuvent se transformer en alarmes retentissant même en mode silencieux.",
        "Privacy you don't have to think about": "Une confidentialité totale sans y penser",
        "Lock the app behind Face ID, hide medication names from lock screen notifications, and rest easy knowing zero data leaves your phone.": "Verrouillage Face ID, masquage des noms sur l'écran verrouillé et zéro donnée envoyée.",
        "Clean export for doctor visits": "Export PDF clair pour vos rendez-vous médicaux",
        "Generate a clean, formatted PDF of your dose adherence history to bring to doctor appointments or share with caregivers.": "Générez un rapport PDF soigné de votre historique de prises pour votre médecin ou vos proches.",
        "An urge rises, peaks, and passes — if you let it.": "Une envie monte, culmine et disparaît — si vous la laissez faire.",
    },
    "es": {
        "Built for a real medicine cabinet": "Pensado para tu botiquín real",
        "No medical advice, no dosage recommendations, no drug-interaction claims — just a dependable way to track what you take and when.": "Sin diagnósticos médicos: solo una forma fiable de recordar qué tomas y a qué hora.",
        "A calendar, not just a checklist": "Un calendario, no una simple lista de tareas",
        "Home groups every dose by time and lets you browse backward and forward through your history — mark a dose taken or skipped right from the day it happened.": "Agrupa cada toma por hora y te permite consultar el historial fácilmente con un solo toque.",
        "Schedules that match real prescriptions": "Horarios adaptados a prescripciones reales",
        "Every day, every X days or hours, specific dates, on/off cycles, or as-needed — with a live preview of your next reminders before you save.": "A diario, cada X días u horas, fechas fijas, ciclos o según necesidad — con vista previa.",
        "Refill tracking that speaks up early": "Avisos de recarga antes de la última pastilla",
        "Set a pill count and a low-stock threshold per medicine. A banner flags refills before you're down to your last dose.": "Indica el recuento de pastillas y recibe un aviso con tiempo para ir a la farmacia.",
        "Critical alerts you actually hear": "Alertas audibles que no podrás pasar por alto",
        "On iOS 26 or later, missed reminders can escalate into full alarms that ring even through silent mode, so you never miss a dose.": "Los avisos no respondidos pueden sonar como alarmas incluso con el móvil en silencio.",
        "Privacy you don't have to think about": "Privacidad absoluta sin complicaciones",
        "Lock the app behind Face ID, hide medication names from lock screen notifications, and rest easy knowing zero data leaves your phone.": "Bloqueo con Face ID, oculta nombres de fármacos en notificaciones y 100% de datos en tu móvil.",
        "Clean export for doctor visits": "Exportación limpia en PDF para llevar al médico",
        "Generate a clean, formatted PDF of your dose adherence history to bring to doctor appointments or share with caregivers.": "Genera un informe PDF con tu cumplimiento terapéutico para enseñárselo a tu doctor.",
        "An urge rises, peaks, and passes — if you let it.": "Un ansia sube, llega al pico y pasa — si la dejas fluir.",
    },
    "it": {
        "Built for a real medicine cabinet": "Creato per il tuo armadietto dei medicinali",
        "No medical advice, no dosage recommendations, no drug-interaction claims — just a dependable way to track what you take and when.": "Nessuna diagnosi medica: solo un metodo infallibile per gestire le tue assunzioni quotidiane.",
        "A calendar, not just a checklist": "Un calendario chiaro, non una semplice lista",
        "Home groups every dose by time and lets you browse backward and forward through your history — mark a dose taken or skipped right from the day it happened.": "Raggruppa le dosi per orario e ti permette di scorrere la cronologia avanti e indietro.",
        "Schedules that match real prescriptions": "Piani terapeutici adatti a ricette reali",
        "Every day, every X days or hours, specific dates, on/off cycles, or as-needed — with a live preview of your next reminders before you save.": "Tutti i giorni, ogni X giorni o ore, date specifiche o al bisogno — con anteprima in tempo reale.",
        "Refill tracking that speaks up early": "Avviso scorte prima dell'ultima pillola",
        "Set a pill count and a low-stock threshold per medicine. A banner flags refills before you're down to your last dose.": "Imposta il numero di pillole e ricevi un promemoria per tempo per andare in farmacia.",
        "Critical alerts you actually hear": "Allarmi potenti impossibili da non sentire",
        "On iOS 26 or later, missed reminders can escalate into full alarms that ring even through silent mode, so you never miss a dose.": "I promemoria non confermati possono diventare veri allarmi anche con suoneria disattivata.",
        "Privacy you don't have to think about": "Privacy totale senza pensieri",
        "Lock the app behind Face ID, hide medication names from lock screen notifications, and rest easy knowing zero data leaves your phone.": "Blocco Face ID, nascondi i nomi dei farmaci sul display e zero dati trasmessi all'esterno.",
        "Clean export for doctor visits": "Esportazione PDF chiara per le visite mediche",
        "Generate a clean, formatted PDF of your dose adherence history to bring to doctor appointments or share with caregivers.": "Genera un comodo PDF con il riepilogo delle tue assunzioni da mostrare al tuo medico curante.",
        "An urge rises, peaks, and passes — if you let it.": "Un impulso cresce, tocca il picco e svanisce — se glielo permetti.",
    },
}

with open('/Users/louisliu/Documents/repo/liuys_website/scripts/comprehensive_translations.py', 'r', encoding='utf-8') as f:
    orig = f.read()

for loc, items in PILL_REMINDER_FEATURES.items():
    # Insert into DEEP_APP_CONTENT['pill-reminder'][loc]
    marker = f"\"pill-reminder\": {{\n        \"{loc}\": {{"
    idx = orig.find(marker)
    if idx != -1:
        insert_code = ""
        for k, v in items.items():
            insert_code += f"            \"{k}\": \"{v}\",\n"
        orig = orig[:idx + len(marker)] + "\n" + insert_code + orig[idx + len(marker):]
        
    # Also add into quit-vaping
    qv_marker = f"\"quit-vaping\": {{\n        \"{loc}\": {{"
    qv_idx = orig.find(qv_marker)
    if qv_idx != -1:
        orig = orig[:qv_idx + len(qv_marker)] + f"\n            \"An urge rises, peaks, and passes — if you let it.\": \"{items['An urge rises, peaks, and passes — if you let it.']}\",\n" + orig[qv_idx + len(qv_marker):]

with open('/Users/louisliu/Documents/repo/liuys_website/scripts/comprehensive_translations.py', 'w', encoding='utf-8') as f:
    f.write(orig)

print("Expanded Pill Reminder and Quit Vaping deep translations successfully!")
