Write-Host "正在啟動自動駕駛模擬器..."

# 啟動虛擬環境
& .\venv\Scripts\Activate.ps1

# 啟動應用程式
streamlit run app.py

# 關閉虛擬環境
deactivate 