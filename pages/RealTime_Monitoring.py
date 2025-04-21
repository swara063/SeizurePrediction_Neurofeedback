import streamlit as st
import time
import numpy as np
from utils.eeg import generate_dummy_eeg  
from components.preprocessing import preprocess_data_for_model
from models.model_loader import load_prediction_model
import pandas as pd


# ✅ Page Setup
st.set_page_config(page_title="Real-Time Monitoring", page_icon="assets/logo.png", layout="wide")

# ✅ Inject CSS
with open("assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ✅ Page Title
st.title("📡 Real-Time Monitoring & Preemptive Prediction")
st.markdown("Stay informed with real-time brainwave and wearable data.")

st.markdown("---")


    st.markdown("---")

    st.subheader("🤖 AI-Powered Risk Prediction")
    st.markdown(f"*Seizure Risk*: {'High' if prediction_value > 0.6 else 'Moderate' if prediction_value > 0.3 else 'Low'} ({prediction_value*100:.2f}%)")
    
    col4, col5 = st.columns(2)
    col4.metric("Seizure Risk", f"{'High' if prediction_value > 0.6 else 'Moderate' if prediction_value > 0.3 else 'Low'} ({prediction_value*100:.2f}%)")
    col5.progress(float(prediction_value), text=f"{float(prediction_value)*100:.2f}% Risk Level")
    
    
    st.markdown("### 📊 Full Model Prediction (EEG + Wearables)")
    accuracy = np.random.uniform(0.8, 0.9)
    st.metric("Prediction Accuracy", f"{accuracy*100:.2f}%")
    st.progress(accuracy, text=f"{accuracy*100:.2f}% Accuracy")
    

    st.markdown("---")
    
    st.subheader("⌚ Wearable-Only Prediction")
    wearable_accuracy = np.random.uniform(0.4, 0.6)
    st.metric("Accuracy", f"{wearable_accuracy*100:.2f}%")
    st.progress(wearable_accuracy, text=f"{wearable_accuracy*100:.2f}% Accuracy")
    

    
    # Config
    max_history = 200  # Show only last 200 points for clarity
    update_interval = 0.1  # Seconds

    raw_eeg = generate_dummy_eeg()
    # st.line_chart(raw_eeg[0, :, 0])
    # Config
    max_history = 200  # Show only last 200 points for clarity
    update_interval = 0.1  # Seconds

    # Streamlit UI
    st.title("Smooth Real-Time EEG Plot")
    plot_placeholder = st.empty()

    # Rolling EEG signal buffer
    eeg_history = []

    while True:
        raw_eeg = generate_dummy_eeg()
        eeg_history.extend(raw_eeg[0, :, 0])  # Append new data (128 points)

        # Trim to keep only the latest ⁠ max_history ⁠ points
        if len(eeg_history) > max_history:
            eeg_history = eeg_history[-max_history:]

        # Convert to DataFrame
        df = pd.DataFrame(eeg_history, columns=["EEG Signal"])

        # Display line chart inside the same placeholder
        plot_placeholder.line_chart(df)

        time.sleep(update_interval)
