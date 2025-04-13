import streamlit as st
import time
import numpy as np
from utils.dummy_eeg_generator import generate_dummy_eeg  
from components.preprocessing import preprocess_data_for_model
from models.model_loader import load_prediction_model

# ✅ Page Setup
st.set_page_config(page_title="Real-Time Monitoring", page_icon="assets/logo.png", layout="wide")

# ✅ Inject CSS
with open("assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ✅ Page Title
st.title("📡 Real-Time Monitoring & Preemptive Prediction")
st.markdown("Stay informed with real-time brainwave and wearable data.")

st.markdown("---")

# ✅ Real-Time EEG Simulation & Prediction
model = load_prediction_model()

st.title("Real-Time EEG Monitoring (Simulated)")

placeholder = st.empty()

run = st.checkbox("Start Simulation")

while run:
    # Generate dummy EEG data (simulated)
    raw_eeg = generate_dummy_eeg()
    
    # Check the shape of the generated EEG data
    st.write(f"EEG shape: {raw_eeg.shape}")  # Debugging
    
    # Pre-process the raw EEG data
    processed_eeg = preprocess_data_for_model(raw_eeg)
    
    # Model input preparation
    model_input = processed_eeg[np.newaxis, ...]  # Shape: (1, 1, 22, 256, 64)
    
    # Predict the seizure risk
    prediction = model.predict(model_input)
    
    # Check the shape of the prediction output
    st.write(f"Prediction shape: {prediction.shape}")  # Debugging
    
    # Assuming binary prediction, and we need the first element
    prediction_value = prediction[0][0]
    
    # Display the predicted seizure probability
    placeholder.metric("Seizure Probability", f"{prediction_value:.2f}")
    
    # Extract features like alpha, beta, and delta from the raw EEG data
    # Assuming these are computed from the frequency band analysis of the EEG data
    alpha_waves = np.mean(raw_eeg[:, :, 0])  # Placeholder for alpha waves computation
    beta_waves = np.mean(raw_eeg[:, :, 1])  # Placeholder for beta waves computation
    delta_waves = np.mean(raw_eeg[:, :, 2])  # Placeholder for delta waves computation
    
    # Live EEG Monitoring Section
    st.subheader("🧠 Live EEG Monitoring")
    st.markdown(f"**Brainwave Activity**: Alpha: {alpha_waves:.2f} | Beta: {beta_waves:.2f} | Delta: {delta_waves:.2f}")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Alpha Waves", f"{alpha_waves:.2f}")
    col2.metric("Beta Waves", f"{beta_waves:.2f}")
    col3.metric("Delta Waves", f"{delta_waves:.2f}")

    if st.button("🔄 Refresh EEG Data"):
        st.success("EEG data updated successfully!")

    st.markdown("---")

    # AI-Powered Risk Prediction Section
    st.subheader("🤖 AI-Powered Risk Prediction")
    st.markdown(f"**Seizure Risk**: {'High' if prediction_value > 0.6 else 'Moderate' if prediction_value > 0.3 else 'Low'} ({prediction_value*100:.2f}%)")
    
    col4, col5 = st.columns(2)
    col4.metric("Seizure Risk", f"{'High' if prediction_value > 0.6 else 'Moderate' if prediction_value > 0.3 else 'Low'} ({prediction_value*100:.2f}%)")
    col5.progress(prediction_value, text=f"{prediction_value*100:.2f}% Risk Level")
    
    if st.button("🔄 Update Prediction"):
        st.info("AI risk prediction updated.")
    
    # Full Model Prediction Section
    st.markdown("### 📊 Full Model Prediction (EEG + Wearables)")
    accuracy = np.random.uniform(0.8, 0.9)  # Simulated accuracy value
    st.metric("Prediction Accuracy", f"{accuracy*100:.2f}%")
    st.progress(accuracy, text=f"{accuracy*100:.2f}% Accuracy")
    
    if st.button("🔁 Refresh Full Prediction"):
        st.info("Full model prediction refreshed!")
    
    st.markdown("---")
    
    # Wearable-Only Prediction
    st.subheader("⌚ Wearable-Only Prediction")
    wearable_accuracy = np.random.uniform(0.4, 0.6)  # Simulated wearable-only prediction accuracy
    st.metric("Accuracy", f"{wearable_accuracy*100:.2f}%")
    st.progress(wearable_accuracy, text=f"{wearable_accuracy*100:.2f}% Accuracy")
    
    if st.button("🔄 Update Wearable Prediction"):
        st.warning("Wearable prediction updated with limited accuracy.")
    
    st.markdown("---")
    
    # Emergency Alert System
    st.subheader("🚨 Emergency Alert System")
    alert_col1, alert_col2 = st.columns(2)
    with alert_col1:
        if st.button("📢 Send Manual Alert"):
            st.error("⚠️ Manual SOS sent!")
    with alert_col2:
        if st.button("🧭 Start Auto-SOS Countdown"):
            st.warning("Auto-SOS initiated. Countdown: 5 seconds...")

    st.markdown("---")
    
    # Show the raw EEG data for channel 0, feature 0
    st.line_chart(raw_eeg[0, :, 0])  # Show EEG data for channel 0, feature 0
    
    # Sleep for 1 second before next data update
    time.sleep(1)
