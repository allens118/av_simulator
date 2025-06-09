@echo off
echo 正在啟動自動駕駛模擬器...

:: 啟動虛擬環境
call venv\Scripts\activate.bat

:: 啟動應用程式
streamlit run app.py

:: 關閉虛擬環境
call venv\Scripts\deactivate.bat 