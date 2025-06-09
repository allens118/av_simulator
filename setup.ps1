Write-Host "正在創建虛擬環境..."

# 檢查 Python 是否已安裝
try {
    python --version | Out-Null
}
catch {
    Write-Host "Python 未安裝！請先安裝 Python。"
    Read-Host "Press Enter to continue"
    exit 1
}

# 創建虛擬環境
python -m venv venv

# 啟動虛擬環境
& .\venv\Scripts\Activate.ps1

# 安裝依賴
Write-Host "正在安裝依賴套件..."
pip install -r requirements.txt

Write-Host "環境設置完成！"
Write-Host "使用 'run.ps1' 來啟動應用程式"
Read-Host "Press Enter to continue" 