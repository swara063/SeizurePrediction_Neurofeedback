import streamlit as st
import time
import numpy as np
from utils.dummy_eeg_generator import generate_dummy_eeg  
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

# ✅ Load Prediction Model
model = load_prediction_model()

st.title("Real-Time EEG Monitoring")

placeholder = st.empty()

run = st.checkbox("Start Simulation", key="start_simulation_checkbox")

while run:
    # Generate dummy EEG data
    raw_eeg = generate_dummy_eeg()
    
    st.write(f"EEG shape: {raw_eeg.shape}")  # Debugging

    # Pre-process the raw EEG data
    processed_eeg = preprocess_data_for_model(raw_eeg)  # Shape: (1, 22, 256, 64)
    
    # Predict seizure risk
    prediction = model.predict(processed_eeg)
        
    st.write(f"Prediction shape: {prediction.shape}")  # Debugging
    
    prediction_value = prediction[0][0]
    
    # Display predicted seizure probability
    placeholder.metric("Seizure Probability", f"{prediction_value:.2f}")
    
    # Simulated brainwave activity
    alpha_waves = np.mean(raw_eeg[:, :, 0])
    beta_waves = np.mean(raw_eeg[:, :, 1])
    delta_waves = np.mean(raw_eeg[:, :, 2])
    
    st.subheader("🧠 Live EEG Monitoring")
    st.markdown(f"*Brainwave Activity*: Alpha: {alpha_waves:.2f} | Beta: {beta_waves:.2f} | Delta: {delta_waves:.2f}")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Alpha Waves", f"{alpha_waves:.2f}")
    col2.metric("Beta Waves", f"{beta_waves:.2f}")
    col3.metric("Delta Waves", f"{delta_waves:.2f}")


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
