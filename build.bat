@echo off
echo 正在打包應用程式...

:: 啟動虛擬環境
call venv\Scripts\activate.bat

:: 執行打包腳本
python build.py

:: 關閉虛擬環境
call venv\Scripts\deactivate.bat

echo 打包完成！
echo 執行檔位於 dist 資料夾中。
pause 