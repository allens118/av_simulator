import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time
from matplotlib.patches import Rectangle, Circle
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.image as mpimg
from PIL import Image
import io

# UI 標題（中英文）
st.set_page_config(page_title="互動感知自駕車模擬器 | Interaction-Aware AV Simulator", layout="centered")
st.title("🚗 互動感知自駕車決策模擬器")
st.subheader("Interaction-Aware Decision-Making Simulator for Autonomous Vehicles")

# 側邊欄參數（可調）
st.sidebar.header("🔧 模擬參數設定 Parameters")
coop = st.sidebar.slider("行人合作度 (Cooperativeness q)", 0, 100, 50)
vehicle_speed = st.sidebar.slider("車輛初始速度 Vehicle Speed (m/s)", 1, 15, 8)
ped_speed = st.sidebar.slider("行人速度 Pedestrian Speed (m/s)", 1, 3, 1)
initial_distance = st.sidebar.slider("初始車-人距離 Initial Distance (m)", 5, 30, 15)

# 模擬計算
reaction_threshold = np.interp(coop, [0, 100], [8.0, 2.0])  # gap threshold by cooperativeness
ttg = initial_distance / vehicle_speed  # time-to-gap
decision = "讓行 Yield" if ttg < reaction_threshold else "穿越 Cross"
decision_en = "Yield" if ttg < reaction_threshold else "Cross"

# 顯示參數與預測
st.markdown("### 🧮 預測決策 Prediction")
st.write(f"**車-人預估時間差 Time to Gap**: {ttg:.2f} 秒")
st.write(f"**反應閾值 Reaction Threshold** (由合作度推得): {reaction_threshold:.2f} 秒")
st.success(f"👉 預測行為 Predicted Action: **{decision} ({decision_en})**")

# 動畫模擬圖
st.markdown("### 📉 模擬圖 Simulation Plot")
animation_placeholder = st.empty()

# 計算動畫參數
simulation_time = max(initial_distance / vehicle_speed, 3 / ped_speed)  # 總模擬時間
frames = 100  # 增加幀數使動畫更流暢
time_points = np.linspace(0, simulation_time, frames)

# 計算位置
car_positions = initial_distance - vehicle_speed * time_points
ped_positions = ped_speed * time_points

# 創建動畫
fig, ax = plt.subplots(figsize=(15, 6))

# 設置背景顏色
ax.set_facecolor('#f0f0f0')
fig.patch.set_facecolor('#f0f0f0')

ped_started = False
ped_y = -1.5  # 初始位置
ped_color = 'gray'
ped_start_time = None

for i in range(frames):
    ax.clear()
    ax.set_xlim(0, initial_distance)
    ax.set_ylim(-2, 2.5)

    # 繪製背景道路
    road = Rectangle((0, -0.8), initial_distance, 1.6, facecolor='#e0e0e0', alpha=0.8)
    ax.add_patch(road)

    # 繪製斑馬線（垂直行人方向）
    for stripe_y in np.linspace(-0.8, 0.8, 10):
        stripe = Rectangle((initial_distance / 2 - 0.4, stripe_y), 0.8, 0.1, facecolor='white')
        ax.add_patch(stripe)

    # 車輛位置更新
    car_x = car_positions[i]
    car = Rectangle((car_x - 1, 0.3), 2, 0.4, facecolor='red', edgecolor='black', alpha=0.9)
    ax.add_patch(car)

    # 動態判斷是否要開始行人移動
    current_time = time_points[i]
    distance_to_crossing = car_x - initial_distance / 2
    ttg_now = distance_to_crossing / vehicle_speed if vehicle_speed > 0 else 999

    if not ped_started and ttg_now <= reaction_threshold:
        ped_started = True
        ped_start_time = current_time

    # 行人移動邏輯
    if ped_started:
        elapsed = current_time - ped_start_time
        ped_y = min(-1.5 + ped_speed * elapsed, 1.5)
        ped_color = 'green' if ped_y < 1.5 else 'blue'
    else:
        ped_y = -1.5
        ped_color = 'gray'

    ped = Circle((initial_distance / 2, ped_y), 0.2, facecolor=ped_color, edgecolor='black', alpha=0.9)
    ax.add_patch(ped)

    # 車輛與行人圖例
    ax.plot([], [], 's', color='red', markersize=10, label='🚗 車輛 Vehicle')
    ax.plot([], [], 'o', color='green', markersize=10, label='🚶 行人 Crossing')
    ax.plot([], [], 'o', color='gray', markersize=10, label='🚶 行人 Waiting')
    ax.plot([], [], 'o', color='blue', markersize=10, label='🚶 行人 Finished')
    ax.legend(loc='upper right')

    # 坐標與即時參數標籤
    ax.set_xlabel('距離 X (m)')
    ax.set_ylabel('位置 Y (垂直方向)')
    ax.grid(True, linestyle='--', alpha=0.5)

    # 文字資訊顯示
    ax.text(0.02, 0.95, f"""
    ⏱ 時間 Time: {current_time:.2f}s
    🚗 車輛位置 Car X: {car_x:.2f} m
    🚶 行人位置 Ped Y: {ped_y:.2f} m
    🤖 預測決策 Decision: {decision}
    """, transform=ax.transAxes, fontsize=10, bbox=dict(facecolor='white', alpha=0.8))

    animation_placeholder.pyplot(fig)
    time.sleep(0.02)


# 說明文字
st.markdown("### ℹ️ 模型說明 Model Explanation")
st.markdown(f"""
- 當 `Time to Gap < Reaction Threshold`，車輛會「讓行」。
- 合作度 q 越高，代表行人越願意等待，車輛越可能選擇「穿越」。
- 可動態調整參數以觀察策略變化。
- 動畫速度反映實際設定的車輛和行人速度。
- 即時顯示位置、速度和距離資訊。
""") 