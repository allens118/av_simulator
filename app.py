import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
import numpy as np
import pandas as pd
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
matplotlib.rcParams['axes.unicode_minus'] = False

# ImageIO 正確匯入方式
import imageio.v2 as imageio
import os
import time

# 設置頁面配置 / Page Configuration
st.set_page_config(
    page_title="AV Simulator | 自動駕駛模擬器",
    page_icon="🚗",
    layout="wide"
)

# 語言選擇 / Language Selection
language = st.sidebar.selectbox(
    "Language / 語言",
    ["English", "中文"]
)

# 文字字典 / Text Dictionary
texts = {
    "title": {
        "English": "🚗 Interaction-Aware AV Simulator",
        "中文": "🚗 互動感知自動駕駛模擬器"
    },
    "subtitle": {
        "English": "Decision-Making Simulator for Autonomous Vehicles",
        "中文": "基於決策的自動駕駛模擬系統"
    },
    "parameters": {
        "English": "Parameters",
        "中文": "參數設定"
    },
    "simulation": {
        "English": "Simulation",
        "中文": "模擬顯示"
    },
    "model_explanation": {
        "English": "Model Explanation",
        "中文": "模型說明"
    },
    "vehicle_speed": {
        "English": "Vehicle Speed (m/s)",
        "中文": "車輛速度 (m/s)"
    },
    "ped_speed": {
        "English": "Pedestrian Speed (m/s)",
        "中文": "行人速度 (m/s)"
    },
    "initial_distance": {
        "English": "Initial Distance (m)",
        "中文": "初始距離 (m)"
    },
    "pedestrian_count": {
        "English": "Number of Pedestrians",
        "中文": "行人數量"
    },
    "hesitation_prob": {
        "English": "Hesitation Probability",
        "中文": "猶豫機率"
    },
    "deaccel_rate": {
        "English": "Deceleration Rate (m/s²)",
        "中文": "減速率 (m/s²)"
    },
    "distance": {
        "English": "Distance X (m)",
        "中文": "距離 X (m)"
    },
    "position": {
        "English": "Position Y",
        "中文": "位置 Y"
    },
    "time": {
        "English": "Time",
        "中文": "時間"
    },
    "speed": {
        "English": "Speed",
        "中文": "速度"
    },
    "vehicle": {
        "English": "Vehicle",
        "中文": "車輛"
    },
    "crossing": {
        "English": "Crossing",
        "中文": "過馬路中"
    },
    "waiting": {
        "English": "Waiting",
        "中文": "等待中"
    },
    "finished": {
        "English": "Finished",
        "中文": "已完成"
    },
    "collision": {
        "English": "Collision",
        "中文": "碰撞"
    },
    "detecting": {
        "English": "Detecting",
        "中文": "偵測中"
    },
    "current_speed": {
        "English": "Current Speed",
        "中文": "當前速度"
    },
    "deceleration_params": {
        "English": "Deceleration Parameters",
        "中文": "減速參數設定"
    },
    "detection_distance": {
        "English": "Detection Distance (m)",
        "中文": "偵測距離 (m)"
    },
    "accel_rate": {
        "English": "Acceleration Rate (m/s²)",
        "中文": "加速率 (m/s²)"
    },
    "deaccel_factor_close": {
        "English": "Close Range Deceleration Factor",
        "中文": "近距離減速係數"
    },
    "deaccel_factor_far": {
        "English": "Far Range Deceleration Factor",
        "中文": "遠距離減速係數"
    },
    "normal_driving": {
        "English": "Normal Driving",
        "中文": "正常行駛"
    },
    "detecting_pedestrian": {
        "English": "Detecting Pedestrian",
        "中文": "偵測到行人"
    },
    "accelerating": {
        "English": "Accelerating",
        "中文": "加速行駛"
    }
}

# 標題區域 / Title Area
st.title(texts["title"][language])
st.subheader(texts["subtitle"][language])

# 創建兩列布局 / Create Two-Column Layout
col1, col2 = st.columns([1, 2])

# 左側參數設定 / Left Column Parameters
with col1:
    st.header(texts["parameters"][language])
    vehicle_speed = st.slider(texts["vehicle_speed"][language], 1.0, 15.0, 8.0)
    ped_speed = st.slider(texts["ped_speed"][language], 1.0, 3.0, 1.5)
    initial_distance = st.slider(texts["initial_distance"][language], 5.0, 30.0, 20.0)
    n_pedestrians = st.slider(texts["pedestrian_count"][language], 1, 5, 3)
    hesitation_prob = st.slider(texts["hesitation_prob"][language], 0.0, 1.0, 0.3)
    
    # 新增減速相關參數
    st.subheader(texts["deceleration_params"][language])
    detection_distance = st.slider(texts["detection_distance"][language], 5.0, 20.0, 15.0)
    deaccel_rate = st.slider(texts["deaccel_rate"][language], 0.5, 5.0, 2.0)
    accel_rate = st.slider(texts["accel_rate"][language], 0.5, 5.0, 1.0)
    deaccel_factor_close = st.slider(texts["deaccel_factor_close"][language], 1.0, 3.0, 1.5)
    deaccel_factor_far = st.slider(texts["deaccel_factor_far"][language], 0.1, 1.0, 0.5)

# 模擬參數 / Simulation Parameters
frames = 100
simulation_time = 10.0  # 增加模擬時間
ped_speed_range = (ped_speed * 0.8, ped_speed * 1.2)
reaction_threshold_range = (2.0, 4.5)
safe_gap = 1.5

# 初始化 / Initialization
time_points = np.linspace(0, simulation_time, frames)
car_positions = np.zeros(frames)
car_positions[0] = initial_distance
car_v = vehicle_speed
car_acc = 0

# 行人參數 / Pedestrian Parameters
pedestrians = []
for _ in range(n_pedestrians):
    ped = {
        'started': False,
        'hesitated': False,
        'start_time': None,
        'y': -1.5 - np.random.rand() * 0.5,
        'speed': np.random.uniform(*ped_speed_range),
        'reaction_threshold': np.random.uniform(*reaction_threshold_range),
        'color': 'gray',
        'collision': False
    }
    pedestrians.append(ped)

# 數據紀錄 / Data Logging
log = []

# 右側顯示區域 / Right Column Display
with col2:
    st.header(texts["simulation"][language])
    animation_placeholder = st.empty()

# 創建圖表 / Create Plot
fig, ax = plt.subplots(figsize=(10, 5))

for i in range(frames):
    ax.clear()
    ax.set_xlim(0, initial_distance)
    ax.set_ylim(-2.5, 2.5)
    current_time = time_points[i]
    time_step = simulation_time / frames  # 計算每個時間步長

    # 車輛位置更新 / Vehicle Position Update
    car_x = car_positions[i - 1] if i > 0 else car_positions[0]
    closest_ped = None
    min_dist = float('inf')

    for ped in pedestrians:
        distance_to_crossing = car_x - initial_distance / 2
        ttg_now = distance_to_crossing / car_v if car_v > 0 else float('inf')

        # 行人決策邏輯 / Pedestrian Decision Logic
        if not ped['started'] and ttg_now <= ped['reaction_threshold']:
            if np.random.rand() > hesitation_prob:
                ped['started'] = True
                ped['start_time'] = current_time
            else:
                ped['hesitated'] = True

        # 行人移動 / Pedestrian Movement
        if ped['started']:
            elapsed = current_time - ped['start_time']
            ped['y'] = min(-1.5 + ped['speed'] * elapsed, 1.5)
            ped['color'] = 'green' if ped['y'] < 1.5 else 'blue'
        else:
            ped['color'] = 'gray'

        # 碰撞判斷 / Collision Detection
        if ped['started'] and -0.2 <= ped['y'] <= 0.2:
            # 增加安全距離，避免碰撞
            if abs(car_x - initial_distance / 2) <= 3.0:
                ped['collision'] = True
                ped['color'] = 'red'
                # 如果發生碰撞，立即停止車輛
                car_v = 0
                car_acc = 0
                car_x = car_positions[i-1]  # 保持在上一個位置
                car_positions[i] = car_x

        # 找出最近行人 / Find Closest Pedestrian
        if ped['started'] and ped['y'] < 1.5:
            d = abs(car_x - initial_distance / 2)
            if d < min_dist:
                min_dist = d
                closest_ped = ped

    # 車輛減速邏輯 / Vehicle Deceleration Logic
    car_color = 'blue'  # 預設顏色（正常行駛）
    car_status = texts["normal_driving"][language]  # 預設狀態

    # 計算車輛到斑馬線的距離
    distance_to_crossing = car_x - initial_distance / 2

    # 只在車輛接近斑馬線時才進行偵測
    if distance_to_crossing > 0 and distance_to_crossing < detection_distance:
        if closest_ped:
            # 計算與行人的實際距離（考慮Y軸距離）
            distance_to_ped = np.sqrt((distance_to_crossing)**2 + (closest_ped['y'] + 1.5)**2)
            
            # 如果行人正在過馬路或準備過馬路
            if (closest_ped['started'] and closest_ped['y'] < 1.5) or \
               (not closest_ped['started'] and distance_to_ped < detection_distance and closest_ped['y'] > -2.0):
                car_color = 'orange'  # 偵測到行人時變為橙色
                car_status = texts["detecting_pedestrian"][language]
                
                # 確保車輛一定會減速
                if distance_to_crossing < 3.0:  # 非常接近斑馬線時
                    car_acc = -deaccel_rate * 2.0  # 強力減速
                elif distance_to_crossing < 5.0:  # 接近斑馬線時
                    car_acc = -deaccel_rate * 1.5
                elif distance_to_crossing < 8.0:  # 較近時
                    car_acc = -deaccel_rate
                else:  # 較遠時開始緩慢減速
                    car_acc = -deaccel_rate * 0.8

                # 確保速度不會太快
                if car_v > 3.0 and distance_to_crossing < 5.0:
                    car_acc = min(car_acc, -deaccel_rate * 1.5)
            else:
                # 如果行人已經通過或距離足夠遠，可以加速回到原速
                if car_v < vehicle_speed:
                    car_acc = accel_rate  # 使用設定的加速率
                    car_color = 'green'  # 加速時變為綠色
                    car_status = texts["accelerating"][language]
                else:
                    car_acc = 0
                    car_color = 'blue'  # 正常速度時為藍色
                    car_status = texts["normal_driving"][language]
        else:
            # 沒有行人時，保持原速
            if car_v < vehicle_speed:
                car_acc = accel_rate
                car_color = 'green'
                car_status = texts["accelerating"][language]
            else:
                car_acc = 0
                car_color = 'blue'
                car_status = texts["normal_driving"][language]
    else:
        # 已經通過斑馬線或距離太遠，保持正常速度
        if car_v < vehicle_speed:
            car_acc = accel_rate
            car_color = 'green'
            car_status = texts["accelerating"][language]
        else:
            car_acc = 0
            car_color = 'blue'
            car_status = texts["normal_driving"][language]

    # 更新車輛速度和位置
    car_v = max(min(car_v + car_acc * time_step, vehicle_speed), 0)
    car_x = max(car_x - car_v * time_step, 0)
    car_positions[i] = car_x

    # 繪圖區域 / Drawing Area
    road = Rectangle((0, -0.8), initial_distance, 1.6, facecolor='#e0e0e0', alpha=0.8)
    ax.add_patch(road)
    for stripe_y in np.linspace(-0.8, 0.8, 10):
        stripe = Rectangle((initial_distance / 2 - 0.4, stripe_y), 0.8, 0.1, facecolor='white')
        ax.add_patch(stripe)

    # 車輛圖形 / Vehicle Drawing
    car = Rectangle((car_x - 1, 0.3), 2, 0.4, facecolor=car_color, edgecolor='black', alpha=0.9)
    ax.add_patch(car)

    # 添加速度標記和距離標記 / Add Speed and Distance Labels
    speed_text = f"{texts['current_speed'][language]}: {car_v:.1f} m/s"
    ax.text(car_x, 0.8, speed_text, ha='center', va='bottom', 
            bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', pad=2))
    
    # 如果有最近的行人且車輛在偵測範圍內，顯示距離
    if closest_ped and distance_to_crossing > 0 and distance_to_crossing < detection_distance:
        distance_text = f"Distance to crossing: {distance_to_crossing:.1f}m"
        ax.text(car_x, 1.0, distance_text, ha='center', va='bottom',
                bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', pad=2))

    # 行人圖形 / Pedestrian Drawing
    for j, ped in enumerate(pedestrians):
        ped_circle = Circle((initial_distance / 2 + j * 0.4 - 0.4, ped['y']), 0.2,
                            facecolor=ped['color'], edgecolor='black', alpha=0.9)
        ax.add_patch(ped_circle)

    # 標籤 / Labels
    ax.set_xlabel(texts["distance"][language])
    ax.set_ylabel(texts["position"][language])
    ax.set_title(f"{texts['time'][language]}: {current_time:.2f}s | {car_status}")

    # 圖例 / Legend
    ax.legend(handles=[
        plt.Line2D([0], [0], marker='s', color='w', label=texts["normal_driving"][language], markerfacecolor='blue'),
        plt.Line2D([0], [0], marker='s', color='w', label=texts["detecting_pedestrian"][language], markerfacecolor='orange'),
        plt.Line2D([0], [0], marker='s', color='w', label=texts["accelerating"][language], markerfacecolor='green'),
        plt.Line2D([0], [0], marker='o', color='w', label=texts["crossing"][language], markerfacecolor='green'),
        plt.Line2D([0], [0], marker='o', color='w', label=texts["waiting"][language], markerfacecolor='gray'),
        plt.Line2D([0], [0], marker='o', color='w', label=texts["finished"][language], markerfacecolor='blue'),
        plt.Line2D([0], [0], marker='o', color='w', label=texts["collision"][language], markerfacecolor='red'),
    ], loc='upper right')

    # 記錄 / Logging
    log.append({
        'time': current_time,
        'car_x': car_x,
        'car_speed': car_v,
        'car_acc': car_acc,
        'min_ttc': min_dist / car_v if car_v > 0 else float('inf'),
        'collision': any(p['collision'] for p in pedestrians)
    })

    # 更新 Streamlit 顯示 / Update Streamlit Display
    animation_placeholder.pyplot(fig)
    time.sleep(0.02)

# 底部說明區域 / Bottom Explanation Area
st.markdown("---")
st.markdown(f"### {texts['model_explanation'][language]}")
st.markdown("""
- When vehicle approaches pedestrians, it makes decisions based on distance and speed
- Pedestrians decide whether to cross based on vehicle's approach
- Adjust parameters to observe different interaction scenarios
- Animation speed reflects actual vehicle and pedestrian speeds
- Real-time position and speed information is displayed

當車輛接近行人時，會根據距離和速度進行決策
行人會根據車輛的接近程度決定是否過馬路
可以調整參數觀察不同情境下的互動行為
動畫速度反映實際的車輛和行人速度
即時顯示位置和速度資訊
""")

# 儲存紀錄為 CSV / Save Log as CSV
df_log = pd.DataFrame(log)
df_log.to_csv("simulation_log.csv", index=False)
