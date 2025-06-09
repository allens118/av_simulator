import PyInstaller.__main__
import os
import sys
import site

# 確保當前目錄是腳本所在目錄
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 獲取 site-packages 路徑
site_packages = site.getsitepackages()[0]

# 獲取 Python DLL 路徑（使用系統 Python）
python_dll = os.path.join(os.path.dirname(sys.executable), 'python39.dll')
if not os.path.exists(python_dll):
    # 如果找不到，嘗試使用系統 Python 路徑
    python_dll = r'C:\Python39\python39.dll'

# 獲取 streamlit 路徑
streamlit_path = os.path.join(site_packages, 'streamlit')
if not os.path.exists(streamlit_path):
    # 如果找不到，嘗試使用虛擬環境路徑
    streamlit_path = os.path.join('venv', 'Lib', 'site-packages', 'streamlit')

# 打包參數
PyInstaller.__main__.run([
    'app.py',
    '--name=AV_Simulator',
    '--onefile',
    '--windowed',
    '--clean',
    '--noconfirm',
    '--icon=app.ico',
    '--add-data=README.md;.',
    '--collect-all=numpy',
    '--collect-all=pandas',
    '--collect-all=streamlit',
    '--collect-all=matplotlib',
    '--collect-all=imageio',
    '--hidden-import=streamlit',
    '--hidden-import=streamlit_plotly_events',
    '--hidden-import=streamlit_option_menu',
    '--hidden-import=streamlit_extras',
    '--hidden-import=streamlit_aggrid',
    '--hidden-import=plotly',
    '--hidden-import=imageio',
    '--hidden-import=imageio.plugins.pillow',
    '--hidden-import=imageio.plugins.ffmpeg',
    '--hidden-import=imageio.plugins.opencv',
])

