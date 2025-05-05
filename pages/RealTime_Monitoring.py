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
eeg_buffer = np.zeros(1024)
chart_placeholder = st.empty()
prediction_placeholder = st.empty()

# ---- Real-time Loop ----
while True:
    # Get new EEG window + label
    eeg_window, true_label = next(stream)

    # Update buffer
    eeg_buffer = np.roll(eeg_buffer, -256)
    eeg_buffer[-256:] = eeg_window

    # Model Prediction
    model_input = eeg_window.reshape(1, 256, 1)
    prediction = model.predict(model_input)[0][0]
    risk_level = "High" if prediction > 0.6 else "Moderate" if prediction > 0.3 else "Low"

    # Plot EEG with seizure color
    df = pd.DataFrame({"EEG": eeg_buffer})
    line_color = "red" if true_label == 1 else "blue"
    chart_placeholder.line_chart(df, use_container_width=True)

    # Display prediction results
    with prediction_placeholder.container():
        st.subheader("🤖 Real-Time Seizure Prediction")
        st.metric("Predicted Risk", f"{risk_level} ({prediction*100:.2f}%)")
        st.progress(float(prediction), text=f"{float(prediction)*100:.2f}% Risk Score")

        if true_label == 1:
            st.error("⚠️ Ground Truth: Seizure Detected!")

    time.sleep(0.5)
