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
eeg_buffer = np.zeros(256)  # For display
chart_placeholder = st.empty()
prediction_placeholder = st.empty()

# ---- Real-time Loop ----
while True:
    eeg_window, true_label = next(stream)  # eeg_window shape: (22, 256, 64)

    # Prediction
    model_input = eeg_window.reshape(1, 22, 256, 64)
    prediction = model.predict(model_input)[0][0]
    risk_level = "High" if prediction > 0.6 else "Moderate" if prediction > 0.3 else "Low"

    # Update buffer for a single channel (e.g., channel 0 for chart)
    display_channel = eeg_window[0, :, 0]  # shape: (256,)
    eeg_buffer = np.roll(eeg_buffer, -256)
    eeg_buffer[-256:] = display_channel

    # Plot EEG
    df = pd.DataFrame({"EEG": eeg_buffer})
    line_color = "red" if true_label == 1 else "blue"
    chart_placeholder.line_chart(df, use_container_width=True)

    # Display prediction
    with prediction_placeholder.container():
        st.subheader("🤖 Real-Time Seizure Prediction")
        st.metric("Predicted Risk", f"{risk_level} ({prediction*100:.2f}%)")
        st.progress(float(prediction), text=f"{float(prediction)*100:.2f}% Risk Score")

        if true_label == 1:
            st.error("⚠️ Ground Truth: Seizure Detected!")

    time.sleep(0.5)
