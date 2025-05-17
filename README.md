# 🧠 Persona Mining V1

心理測驗互動 + 抽卡角色養成系統  
結合 NLP 分析、人格模型、自動碎片合成、稱號與排行榜。

---

## 🚀 部署指南（Streamlit Cloud）

1. 登入 https://streamlit.io/cloud
2. 點選 `New app`
3. 設定：
   - Repository: `taipei49314/persona-mining-v1`
   - Branch: `main`
   - App file: `app.py`
4. 點選 [Deploy] 完成

---

## 🧪 測試覆蓋率展示（GitHub Pages）

📄 頁面連結：  
👉 https://taipei49314.github.io/persona-mining-v1/

### 自動更新報表方法：
使用以下指令產生測試覆蓋率報表並同步：

```bash
pytest --cov=. --cov-report=html
rm -rf docs/
cp -r htmlcov/ docs/
git add docs/
git commit -m "更新測試覆蓋率報表"
git push origin main
```

Windows 使用者可執行：`deploy_coverage.bat`

---

## 📦 目錄說明

| 目錄／檔案           | 說明 |
|----------------------|------|
| `app.py`             | Streamlit 主畫面 |
| `quiz_engine.py`     | NLP 人格分析模組 |
| `card_draw.py`       | 抽卡邏輯與每日免費機制 |
| `fragment_system.py` | 分解碎片與 SSR 合成 |
| `shop.py`            | 金幣商店邏輯 |
| `logs/`              | 活動記錄與報表 |
| `.streamlit/`        | 部署與樣式設定 |
| `.github/`           | 自動測試 CI 流程 |
| `docs/`              | GitHub Pages 用覆蓋率報表 |