# YS Liu Studio — Programmatic SEO 矩陣擴展策略與驗證指南

> **建立時間**：2026-10-27  
> **作者**：Louis Liu (Automated Programmatic SEO Editor)  
> **目標**：記錄多 App 矩陣 SEO 的架構思考、核心假設、已落地改進，以及未來 1~4 週的驗證與迭代準則。

---

## 一、 現況診斷與產品矩陣分級

### 1.1 App 產品潛力分級 (SEO Strategy Matrix)
| 優先級 | 包含產品 | 搜尋特徵與關鍵詞範例 | 核心戰略定位 |
| :--- | :--- | :--- | :--- |
| **Tier 1 (頂級轉化)** | **Alcohol Free Tracker**<br>**Quit Weed (Unfog)**<br>**Quit Vaping** | • 戒除症狀、排毒時間線、身體修復歷程<br>• `alcohol recovery timeline day by day`<br>• `thc detox timeline what happens to body`<br>• `how to stop 5pm alcohol cravings urge surfing` | **醫學/神經科學深度科普 pSEO**<br>利用高意圖痛苦點驅動下載與付費訂閱。 |
| **Tier 2 (剛需工具)** | **Supplement & Pill Reminder**<br>**Grocery Price Scanner**<br>**Levain (Sourdough)** | • 保健品服用時間、搭配禁忌、單位價格計算<br>• `best time to take magnesium glycinate`<br>• `unit price calculator per ounce`<br>• `sourdough hydration percentage calculator` | **用藥指南 + 互動式 Web 計算器**<br>長尾詞豐富，工具型頁面容易獲得外鏈與長留存。 |
| **Tier 3 (小眾長尾)** | **Inkstone (Sign PDF)**<br>**Agricola Score Sheet** | • 離線本地 PDF 簽名、桌遊計分規則 | 避開巨頭紅海，維持極致隱私長尾定位。 |

### 1.2 GSC 冷啟動數據實測診斷
* **Sitemap 狀態**：`https://ysliustudio.com/sitemap.xml` 於 `2026-10-26 19:08 UTC` 提交，包含 36+ 網址，狀態為 `Discovered - currently not indexed`。
* **歷史數據積累**：`sc-domain:ysliustudio.com` 僅累積 1 天數據（2026-10-25），全站曝光 (Impressions) 與點擊為 0。
* **診斷結論**：當前 Strike Zone 回傳 0 筆是新網域冷啟動的正常現象，需以高品質種子佇列持續發布，並啟動內部連結與推播機制加速 Google 索引。

---

## 二、 核心策略思考與待驗證假設 (Hypotheses)

### 假設 1：戒除健康 App 的矩陣協同效應 (Cross-App Synergy)
* **思考**：戒酒 (AFT)、戒大麻 (Unfog)、戒電子煙 (Quit Vaping) 三者的受眾特質與神經遞質修復規律高度重疊（多巴胺、GABA、睡眠紊亂、戒斷焦慮）。
* **實踐**：
  * 在主站首頁 (`index.html`) 新增專屬的「健康與戒除習慣研究指南 (Health & Habit Recovery Guides)」區塊，直接將首頁高權重分配給三款 App 的頂級指南。
  * 頁尾 (Footer) 增加常駐 Guides 連結。
* **驗證指標**：首頁權重傳遞後，各子目錄的 URL 在 GSC 中從 `Discovered` 轉變為 `Crawled - currently not indexed` / `Indexed` 的平均耗時是否小於 10 天。

### 假設 2：動態分級 Strike Zone 策略 (Dual-Tier Strike Zone)
* **思考**：原腳本固定門檻 `impr >= 10, pos 15..55`。在網站剛上線的第 2～4 週，Google 往往會先給出少量曝光測試（1~5 次 impressions）。
* **實踐**：新增第二層 `Emerging Strike Zone`（門檻：`pos 10..60 且 impr >= 2`）。若無成熟 Strike Zone，優先捕捉剛有苗頭的關鍵字，其次才退回靜態種子佇列。
* **驗證指標**：第一筆由 GSC 自動驅動的主題何時出現？預期比純靜態門檻提前 10-14 天觸發。

### 假設 3：IndexNow 即時推播破除搜尋引擎發現時滯
* **思考**：Google 爬取 Sitemap 週期不可控，而 Bing、Yandex 支援 IndexNow 協議，可在提交幾分鐘內啟動爬蟲。
* **實踐**：在 `liuys_website` 配置 IndexNow 專屬金鑰 `4a8f9c2d1b7e6a5d3f2c1e8b7a6d5c4e.txt` 與批次推播腳本 `scripts/submit_indexnow.py`。
* **驗證指標**：在 Bing Webmaster Tools 或 Bing 搜尋結果中，是否在發布 48 小時內即可檢索到新頁面。

### 假設 4：複製 pSEO 至 Pill Reminder (高意圖用藥長尾庫)
* **思考**：保健品與處方用藥的「最佳服用時間」與「交互作用」是極高意圖的長尾詞，用戶痛點明確且容易轉化。
* **實踐**：建立 `pill-reminder` 的 pSEO 管道，首發包含甘氨酸鎂、肌酸、避孕藥漏服、維生素 D3+K2、GLP-1 週期提醒等高意圖種子。
* **驗證指標**：觀察 30 天內是否能從醫療/營養長尾詞獲取自然搜尋曝光。

---

## 三、 本次已落地的改進成果 (Changelog: 2026-10-27)

1. **AFT 每日發布管道落實**：
   * 成功撰寫並發布：`30-day-dry-challenge-survival-blueprint`。
   * 包含神經科學對照表、每週生理恢復、防復飲策略、行事曆視覺動量 Pitch Card 與 5 組結構化 FAQ。
   * 更新 AFT 指南索引、主站與子站 Sitemap、`SEO-Content-Log.md`。
2. **搜尋引擎發現與內部連結全面強化**：
   * 主站首頁 `index.html` 嵌入精美手繪風格的「Evidence-Based Guides Hub」導覽區塊。
   * 主站頁尾嵌入直達 Alcohol-Free、Quit Weed、Quit Vaping 指南的錨文字連結。
3. **IndexNow 即時推播機制就緒**：
   * 生成並部署驗證金鑰 `4a8f9c2d1b7e6a5d3f2c1e8b7a6d5c4e.txt`。
   * 建立 `scripts/submit_indexnow.py`，支援一鍵將全站 44+ 網址推播至搜尋引擎。
4. **GSC Strike Zone 腳本升級**：
   * 同步升級 `alcohol-free-tracker`、`quit-weed`、`quit-vaping` 的 `select_next_topic.py`，加入雙層階梯式門檻（Primary + Emerging）。
5. **Pill Reminder 完整 pSEO 骨架搭建**：
   * 配置 `guides/seo_config.json`、5 組高轉化種子佇列 `guides/topic_queue.json`。
   * 完成專屬編譯腳本 `scripts/build_guide.py` 與選題腳本 `scripts/select_next_topic.py`。
   * 初始化 `published_manifest.json` 與 Research 歸因日誌。

---

## 四、 全矩陣每日晨間發布流水線標準作業程序 (8-App Anti-Content-Farm SOP)

為避免被 Google 判定為「機器人規模化垃圾內容 (Scaled Content Abuse / Content Farm)」，本管線嚴格執行 **「先強化既有曝光頁、每日限發 1 篇高密度工具/實證文、8 款 App 智慧輪替」** 原則：

```bash
# 1. 一鍵產生全 8 款 App 的每日防垃圾內容行動計畫 (1 篇舊文強化 + 1 篇新文輪替)
cd /Users/louisliu/Documents/repo/liuys_website
python3 scripts/master_daily_pipeline.py --recommend
```

### 防機器人農文 (Anti-Content-Farm) 四大鐵律：
1. **Refresh Before Spawn（零關鍵字內耗）**：
   * 只要 GSC 出現真實搜尋詞落在現有文章 (`pos 10..95`)，優先將該關鍵字與精準問答補入現有文章（更新 `updated_date` 與 `secondary_keywords` / `faqs`），絕不為同義詞重複開設低品質新網址。
2. **Natural Editorial Velocity（嚴格每日限額 1 篇新文章）**：
   * 全站每日最多僅針對 **1 款 App** 發布 **1 篇新指南**，由 `master_daily_pipeline.py --recommend` 依據「距離上次發文天數 + 已發篇數稀缺度 + 子目錄 GSC 活躍曝光」自動在 8 款 App 間公平輪替，杜絕單一子目錄短時間暴增大量頁面。
3. **High Information Gain & Concise Utility（拒絕 3000 字 AI 廢話長文）**：
   * 每篇嚴格控制在 **750～1,150 字** 的高密度結構：首段 50 字必須給出定量結論（`guide-callout` TL;DR Answer Box），內文至少 40% 價值來自 **結構化數據對照表、劑量/溫度/計分矩陣或互動式計算器連結**。
4. **Accurate Sitemap `lastmod`（誠實時間戳記）**：
   * 各 App 的 `sitemap.xml` 與主站 `sitemap.xml` 僅在文章實際新增或修改 (`updated_date`) 時更新 `lastmod`，絕不每日偽造全站 `lastmod = today`。

---

## 五、 每日晨間發布與舊文強化紀錄 (Portfolio Action Log)

| 日期 | 動作類型 | App | 指南標題與網址 | 目標關鍵字 / GSC 觸發詞 | ASC Token (`ct`) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **2026-11-03** | `REFRESH_EXISTING` | **Levain** (`levain`) | [Sourdough Bulk Fermentation Chart](https://ysliustudio.com/levain/guides/bulk-fermentation-temperature-time-chart.html) | `bulk fermentation chart` (GSC Pos 67.0, Page Impr 14) | `seo_bulk_ferment_temp` |
| **2026-11-03** | `PUBLISH_NEW` | **Quit Vaping** (`quit-vaping`) | [How to Cure Vaper's Tongue Fast: Causes, Reset Protocol & Recovery Timeline](https://ysliustudio.com/quit-vaping/guides/how-to-cure-vapers-tongue-fast.html) | `how to cure vapers tongue symptoms timeline` (8-App Rotation Score 93.0) | `seo_vapers_tongue_card` |

### 階段一：第 7 天檢查（2026-11-03）
* [ ] 檢查 GSC 涵蓋範圍（Coverage）：已提交的 36+ 網址是否有至少 30% 轉為 `Indexed`。
* [ ] 檢查 IndexNow 提交狀態：Bing 是否已成功抓取主要 Guides。
* [ ] 運行 `python3 scripts/select_next_topic.py`，確認是否有任何 Query 進入 `gsc_emerging_strike_zone`。

### 階段二：第 14 天檢查（2026-11-10）
* [ ] 檢查 GSC 關鍵字曝光分布：檢視是否有關鍵字出現在 50~90 名之間，評估是否調整文章 Meta Title 進行微調強化。
* [ ] 檢查 ASC 歸因轉化：透過 `ct=seo_*` 檢查是否有網頁流量下載 App。
* [ ] 啟動 `pill-reminder` 與 `quit-weed` 的週期發布。

### 階段三：第 30 天檢查（2026-11-26）
* [ ] 全站流量評估：月度自然搜尋曝光數是否突破 500 次。
* [ ] 針對排名在 15~30 名的「核心攻堅關鍵字」，進行現有文章內容擴寫與 FAQ 補充。
* [ ] 啟動工具型 SEO 專案：在 `grocery-price` 與 `levain` 導入互動式 Web 換算器。
