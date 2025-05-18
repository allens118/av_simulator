import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

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
fig, ax = plt.subplots(figsize=(8, 3))
frames = 20
car_positions = np.linspace(initial_distance, 0, frames)
ped_positions = np.linspace(0, initial_distance, frames)

for i in range(frames):
    ax.clear()
    ax.set_xlim(0, initial_distance)
    ax.set_ylim(-1, 1)
    ax.plot(car_positions[i], 0.5, 'ro', label='🚗 車輛 Vehicle')
    if ttg >= reaction_threshold:
        ax.plot(ped_positions[i], -0.5, 'go', label='🚶 行人 Pedestrian')
    else:
        ax.plot(ped_positions[0], -0.5, 'go', label='🚶 行人 Pedestrian')
    ax.axvline(initial_distance/2, color='gray', linestyle='--', label='斑馬線 Crosswalk')
    ax.legend(loc='upper right')
    st.pyplot(fig)

# 說明文字
st.markdown("### ℹ️ 模型說明 Model Explanation")
st.markdown(f"""
- 當 `Time to Gap < Reaction Threshold`，車輛會「讓行」。
- 合作度 q 越高，代表行人越願意等待，車輛越可能選擇「穿越」。
- 可動態調整參數以觀察策略變化。
""") 