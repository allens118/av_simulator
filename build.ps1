Write-Host "正在打包應用程式..."

# 啟動虛擬環境
& .\venv\Scripts\Activate.ps1

# 執行打包腳本
python build.py

# 關閉虛擬環境
deactivate

Write-Host "打包完成！"
Write-Host "執行檔位於 dist 資料夾中。"
Read-Host "Press Enter to continue" 