# 互動感知自駕車決策模擬器
## Interaction-Aware Decision-Making Simulator for Autonomous Vehicles

這是一個基於 Streamlit 開發的互動式自駕車決策模擬器，用於模擬自駕車與行人之間的互動決策過程。

### 功能特點
- 🚗 互動式參數調整
- 📊 即時視覺化模擬
- 🔄 動態決策預測
- 🌐 中英雙語介面

### 安裝需求
- Python 3.7+
- Streamlit
- Matplotlib
- NumPy

### 安裝步驟
1. 克隆專案
```bash
git clone git@github.com:allens118/av_simulator.git
cd av_simulator
```

2. 建立並啟動虛擬環境
```bash
python -m venv av_sim
# Windows
.\av_sim\Scripts\activate
# Linux/Mac
source av_sim/bin/activate
```

3. 安裝依賴套件
```bash
pip install -r requirements.txt
```

### 執行方式
```bash
streamlit run app.py
```

### 使用說明
1. 在側邊欄調整模擬參數：
   - 行人合作度 (Cooperativeness)
   - 車輛速度 (Vehicle Speed)
   - 行人速度 (Pedestrian Speed)
   - 初始距離 (Initial Distance)

2. 觀察模擬結果：
   - 預測決策
   - 動態模擬圖
   - 模型說明

### 參數說明
- **行人合作度**：影響車輛決策的關鍵參數，值越高表示行人越願意等待
- **車輛速度**：自駕車的初始速度（公尺/秒）
- **行人速度**：行人的移動速度（公尺/秒）
- **初始距離**：車輛與行人之間的初始距離（公尺）

### 決策邏輯
- 當 Time to Gap < Reaction Threshold 時，車輛會選擇讓行
- 反應閾值由行人合作度動態計算得出
- 合作度越高，反應閾值越低，車輛越可能選擇穿越

### 授權
MIT License

### 作者
Allen Su 