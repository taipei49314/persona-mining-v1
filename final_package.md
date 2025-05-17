# 🧠 Persona Mining V1 - 專案總覽

整合心理測驗、抽卡、碎片合成、排行榜與 NLP 分析的互動系統。  
此專案支援多人登入、每日任務、商店兌換，並可部署至 Streamlit Cloud 與 GitHub Pages。

---

## 📁 專案結構說明

| 檔案／資料夾             | 說明                                  |
|--------------------------|---------------------------------------|
| `app.py`                 | Streamlit 主入口，支援登入與分頁模組       |
| `login_module.py`        | 使用者登入與帳號管理邏輯                  |
| `card_draw.py`           | 抽卡機制，含每日免費一次與稀有度控制邏輯     |
| `fragment_system.py`     | 卡片分解為碎片、SSR 合成功能               |
| `shop.py`                | 金幣商店，可兌換限定卡與新卡池              |
| `user_profile.py`        | 排行榜、稱號系統與使用者資料顯示             |
| `quiz_engine.py`         | NLP 心理測驗與人格標註邏輯                  |
| `daily_task.py`          | 每日任務模組，可觸發 bonus 抽卡、金幣         |
| `data/`                  | 卡池、使用者持卡紀錄、稀有度等資料儲存         |
| `logs/`                  | 抽卡與操作記錄檔案                        |
| `tests/`                 | `pytest` 測試模組                         |
| `docs/`                  | GitHub Pages 顯示測試覆蓋率報表（index.html） |
| `.streamlit/`            | 部署樣式與參數設定（config.toml）           |
| `.github/workflows/`     | CI 自動測試流程設定                        |

---

## 🚀 部署方式

### Streamlit Cloud

1. 登入 https://streamlit.io/cloud
2. 選擇 repo：`taipei49314/persona-mining-v1`
3. 指定 app file 為 `app.py`
4. 點選 [Deploy]

---

### GitHub Pages - 測試覆蓋率

1. 至 repo → Settings → Pages
2. 設定 branch 為 `main`，資料夾為 `docs`
3. 頁面連結類似：https://taipei49314.github.io/persona-mining-v1/

---

## 🧪 一鍵更新測試報表（Windows 用）

執行 `deploy_coverage.bat`，自動產出 `htmlcov → docs → git push`

---

## 💡 建議擴充

- 動態卡片顯示（依稀有度特效／邊框顏色）
- SSR 合成動畫效果
- 多人競賽抽卡總榜