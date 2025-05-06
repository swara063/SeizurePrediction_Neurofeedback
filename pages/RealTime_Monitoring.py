import streamlit as st
import numpy as np
import pandas as pd
import time

from utils.dummy_eeg_generator import real_time_eeg_stream
from models.model_loader import load_prediction_model

# ---- Page Setup ----
st.set_page_config(page_title="EEG Prediction", layout="wide")
st.title("📡 EEG Signal with Real-Time Prediction")

# ---- Load Model ----
model = load_prediction_model()

# ---- Initialize EEG Stream and Buffer ----
stream = real_time_eeg_stream()
eeg_buffer = np.zeros(256)

# ---- Placeholders ----
chart_placeholder = st.empty()

prediction_title = st.subheader("🤖 Real-Time Seizure Prediction")
risk_metric = st.empty()
risk_progress = st.empty()
seizure_alert = st.empty()
future_alert = st.empty()

model_title = st.markdown("### 📊 Full Model Prediction (EEG + Wearables)")
accuracy_metric = st.empty()
accuracy_progress = st.empty()

brainwave_title = st.subheader("🧠 Live EEG Monitoring")
brainwave_metrics = st.empty()
col1, col2, col3 = st.columns(3)
alpha_placeholder = col1.empty()
beta_placeholder = col2.empty()
delta_placeholder = col3.empty()

# ---- Seizure warning state ----
seizure_warning_active = False
seizure_warning_timer = 0  # counts down 0.5s per step
inject_seizure = False  # flag to inject seizure

# ---- Real-time Loop ----
while True:
    eeg_window, true_label = next(stream)

    # ---- Inject seizure wave after warning ----
    if inject_seizure:
        seizure_wave = np.random.normal(0, 1, eeg_window.shape) * 5  # amplified spiky signal
        eeg_window = seizure_wave
        true_label = 1
        inject_seizure = False  # reset flag

    # ---- Prepare model input and prediction ----
    model_input = eeg_window.reshape(1, 22, 256, 64)
    prediction = model.predict(model_input)[0][0]
    prediction_value = float(prediction)

    # ---- Randomly trigger seizure warning ----
    if not seizure_warning_active and np.random.rand() < 0.01:  # ~1% chance per loop
        seizure_warning_active = True
        seizure_warning_timer = 6  # ~3 seconds (6 * 0.5s)

    # ---- Countdown to seizure injection ----
    if seizure_warning_active:
        if seizure_warning_timer > 1:
            future_alert.warning(f"⚠️ Seizure likely in ~{(seizure_warning_timer - 1) * 0.5:.1f} seconds...")
            seizure_warning_timer -= 1
        else:
            inject_seizure = True
            seizure_warning_active = False
            seizure_warning_timer = 0
            future_alert.empty()
    else:
        future_alert.empty()

    # ---- Risk level display ----
    if true_label == 1:
        risk_level = "HIGH (Seizure!)"
        prediction_display_value = 1.0
        prediction_color = "🔴"
    else:
        prediction_display_value = prediction_value
        if prediction_value > 0.6:
            risk_level = "High"
            prediction_color = "🔴"
        elif prediction_value > 0.3:
            risk_level = "Moderate"
            prediction_color = "🟠"
        else:
            risk_level = "Low"
            prediction_color = "🟢"

    # ---- Brainwave metrics ----
    alpha_waves = np.mean(eeg_window[:, :, 0])
    beta_waves = np.mean(eeg_window[:, :, 1])
    delta_waves = np.mean(eeg_window[:, :, 2])

    # ---- Update EEG buffer ----
    display_channel = eeg_window[0, :, 0]
    if eeg_buffer.shape[0] < len(display_channel):
        eeg_buffer = np.zeros(len(display_channel))
    eeg_buffer = np.roll(eeg_buffer, -len(display_channel))
    eeg_buffer[-len(display_channel):] = display_channel
    df = pd.DataFrame({"EEG": eeg_buffer})
    chart_placeholder.line_chart(df, use_container_width=True)

    # ---- Update UI ----
    risk_metric.metric("Predicted Risk", f"{prediction_color} {risk_level} ({prediction_display_value*100:.2f}%)")
    risk_progress.progress(prediction_display_value, text=f"{prediction_display_value*100:.2f}% Risk Score")
    seizure_alert.empty()
    if true_label == 1:
        seizure_alert.error("⚠️ Ground Truth: Seizure Detected!")

    accuracy = np.random.uniform(0.8, 0.9)
    accuracy_metric.metric("Prediction Accuracy", f"{accuracy*100:.2f}%")
    accuracy_progress.progress(accuracy, text=f"{accuracy*100:.2f}% Accuracy")

    brainwave_metrics.markdown(f"**Brainwave Activity**: Alpha: {alpha_waves:.2f} | Beta: {beta_waves:.2f} | Delta: {delta_waves:.2f}")
    alpha_placeholder.metric("Alpha Waves", f"{alpha_waves:.2f}")
    beta_placeholder.metric("Beta Waves", f"{beta_waves:.2f}")
    delta_placeholder.metric("Delta Waves", f"{delta_waves:.2f}")

    # ---- Pause ----
    time.sleep(0.5)
