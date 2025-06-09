# 互動感知決策模擬系統 (Interaction-Aware Decision Making Simulation)

## 專案概述 (Project Overview)
本專案實現了一個基於互動感知的決策模擬系統，用於研究行人與自駕車之間的互動行為。系統模擬了行人過馬路場景，並根據互動感知模型進行決策。

This project implements an interaction-aware decision-making simulation system for studying interactions between pedestrians and autonomous vehicles. The system simulates pedestrian crossing scenarios and makes decisions based on an interaction-aware model.

## 使用技術 (Technologies Used)

### 主要框架 (Main Framework)
- **Streamlit**: Web 應用程式框架，用於建立互動式使用者介面
  - Web application framework for building interactive user interfaces
- **Plotly**: 互動式資料視覺化
  - Interactive data visualization

### 核心功能庫 (Core Libraries)
- **NumPy**: 數值計算和陣列操作
  - Numerical computing and array operations
- **Pandas**: 資料處理和分析
  - Data manipulation and analysis
- **Matplotlib**: 靜態圖表繪製
  - Static plotting and visualization

### 模擬相關 (Simulation Related)
- **ImageIO**: 圖像處理和動畫生成
  - Image processing and animation generation
- **OpenCV**: 電腦視覺處理
  - Computer vision processing

### 使用者介面元件 (UI Components)
- **Streamlit Plotly Events**: 互動式圖表事件處理
  - Interactive chart event handling
- **Streamlit Option Menu**: 選單介面
  - Menu interface
- **Streamlit Extras**: 額外 UI 元件
  - Additional UI components
- **Streamlit AgGrid**: 資料表格顯示
  - Data grid display

## 主要功能 (Main Features)
1. 行人過馬路模擬
   - Pedestrian crossing simulation
2. 自駕車決策系統
   - Autonomous vehicle decision system
3. 互動感知模型
   - Interaction-aware model
4. 即時視覺化
   - Real-time visualization
5. 參數調整介面
   - Parameter adjustment interface

## 模擬參數說明 (Simulation Parameters)

### 基本參數 (Basic Parameters)
- **車輛初始速度 (Vehicle Initial Speed)**
  - 範圍：1.0 - 5.0 m/s
  - 預設值：3.0 m/s
  - 控制車輛的起始速度
  - Controls the initial speed of the vehicle

- **行人速度 (Pedestrian Speed)**
  - 範圍：0.5 - 2.0 m/s
  - 預設值：1.0 m/s
  - 設定行人的行走速度
  - Sets the walking speed of pedestrians

- **行人數量 (Number of Pedestrians)**
  - 範圍：1 - 5
  - 預設值：2
  - 控制同時出現的行人數量
  - Controls the number of simultaneous pedestrians

### 互動參數 (Interaction Parameters)
- **檢測距離 (Detection Distance)**
  - 範圍：5.0 - 20.0 公尺
  - 預設值：10.0 公尺
  - 車輛開始檢測行人的距離
  - Distance at which the vehicle starts detecting pedestrians

- **減速率 (Deceleration Rate)**
  - 範圍：0.5 - 3.0 m/s²
  - 預設值：1.5 m/s²
  - 車輛檢測到行人時的減速程度
  - Rate at which the vehicle decelerates when detecting pedestrians

- **加速率 (Acceleration Rate)**
  - 範圍：0.5 - 2.0 m/s²
  - 預設值：1.0 m/s²
  - 行人通過後車輛的加速程度
  - Rate at which the vehicle accelerates after pedestrians pass

### 視覺化說明 (Visualization Guide)

#### 車輛狀態顏色 (Vehicle Status Colors)
- **藍色 (Blue)**
  - 正常行駛狀態
  - Normal driving state

- **橙色 (Orange)**
  - 檢測到行人，正在減速
  - Detected pedestrians, decelerating

- **綠色 (Green)**
  - 行人通過後，正在加速
  - Pedestrians passed, accelerating

#### 行人狀態 (Pedestrian Status)
- **紅色圓點 (Red Dot)**
  - 行人位置
  - Pedestrian position

- **黃色區域 (Yellow Area)**
  - 斑馬線區域
  - Zebra crossing area

#### 距離顯示 (Distance Display)
- 車輛上方顯示與最近行人的距離
- Distance to nearest pedestrian shown above vehicle

## 安裝說明 (Installation)
1. 建立虛擬環境：
   ```bash
   python -m venv venv
   ```

2. 啟動虛擬環境：
   - Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

3. 安裝依賴套件：
   ```bash
   pip install -r requirements.txt
   ```

## 執行方式 (How to Run)
1. 啟動應用程式：
   ```bash
   streamlit run app.py
   ```

2. 打包成執行檔：
   ```bash
   python build.py
   ```

## 系統需求 (System Requirements)
- Python 3.9 或以上版本
  - Python 3.9 or above
- 支援的作業系統：Windows、Linux、MacOS
  - Supported OS: Windows, Linux, MacOS

## 授權條款 (License)
MIT License 