@echo off
echo 正在創建虛擬環境...

:: 檢查 Python 是否已安裝
python --version >nul 2>&1
if errorlevel 1 (
    echo Python 未安裝！請先安裝 Python。
    pause
    exit /b 1
)

:: 創建虛擬環境
python -m venv venv

:: 啟動虛擬環境
call venv\Scripts\activate.bat

:: 安裝依賴
echo 正在安裝依賴套件...
pip install -r requirements.txt

echo 環境設置完成！
echo 使用 'run.bat' 來啟動應用程式
pause 