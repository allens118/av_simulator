# Interaction-Aware AV Simulator | 互動感知自動駕駛模擬器

A real-time interactive simulator for autonomous vehicle decision-making in pedestrian crossing scenarios.

一個用於行人過馬路情境下的自動駕駛決策即時互動模擬器。

## Features | 功能特點

- Real-time simulation with adjustable parameters | 可調整參數的即時模擬
- Bilingual interface (English/Chinese) | 雙語介面（英文/中文）
- Multiple pedestrian interactions | 多位行人互動
- Realistic vehicle and pedestrian behaviors | 真實的車輛和行人行為
- Collision detection and avoidance | 碰撞檢測與避免
- Data logging and analysis | 數據記錄與分析

## Installation | 安裝

1. Clone the repository | 複製儲存庫
```bash
git clone https://github.com/yourusername/InteractionAwareDecision.git
cd InteractionAwareDecision
```

2. Create and activate virtual environment | 建立並啟動虛擬環境
```bash
python -m venv av_sim
# Windows
av_sim\Scripts\activate
# Linux/Mac
source av_sim/bin/activate
```

3. Install dependencies | 安裝依賴套件
```bash
pip install -r requirements.txt
```

## Usage | 使用方式

Run the simulator | 執行模擬器
```bash
streamlit run app.py
```

### Parameters | 參數說明

- Vehicle Speed | 車輛速度: Adjust the speed of the autonomous vehicle
- Pedestrian Speed | 行人速度: Set the walking speed of pedestrians
- Initial Distance | 初始距離: Set the starting distance of the vehicle
- Number of Pedestrians | 行人數量: Control how many pedestrians appear
- Hesitation Probability | 猶豫機率: Set the probability of pedestrian hesitation
- Deceleration Rate | 減速率: Control how quickly the vehicle slows down

### Simulation Features | 模擬功能

- Real-time visualization | 即時視覺化
- Interactive parameter adjustment | 互動式參數調整
- Bilingual interface | 雙語介面
- Collision detection | 碰撞檢測
- Data logging | 數據記錄

## File Structure | 檔案結構

```
InteractionAwareDecision/
├── app.py              # Main application | 主程式
├── requirements.txt    # Dependencies | 依賴套件
├── README.md          # Documentation | 說明文件
├── simulation_log.csv # Simulation data | 模擬數據
└── av_sim/           # Virtual environment | 虛擬環境
```

## Dependencies | 依賴套件

- streamlit
- matplotlib
- numpy
- pandas

## Contributing | 貢獻

Feel free to submit issues and enhancement requests | 歡迎提交問題和改進建議

## License | 授權

This project is licensed under the MIT License | 本專案採用 MIT 授權條款 