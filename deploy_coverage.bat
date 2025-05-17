@echo off
echo [1/4] ✅ 執行 pytest 產生覆蓋率報表...
pytest --cov=. --cov-report=html

echo [2/4] 🔁 清除舊 docs/
rmdir /S /Q docs

echo [3/4] 📁 複製 htmlcov 到 docs/
xcopy htmlcov docs /E /I /Y

echo [4/4] 🚀 推送報表至 GitHub Pages
git add docs
git commit -m "更新測試覆蓋率報表"
git push origin main

echo ✅ 完成！可至 GitHub Pages 檢視報表。
pause