import streamlit as st

def show():
    st.image("assets/logo.png", width=50)
    st.title("NeuraCare")
    st.header("Real-Time Monitoring & Preemptive Prediction")
    st.markdown("Monitor your health data in real-time.")

    st.subheader("Real-Time EEG Monitoring")
    st.line_chart([1, 2, 3, 4])  # Placeholder for live brainwave data

    st.subheader("AI-Powered Risk Prediction Dashboard")
    st.metric("Seizure Risk Level", "Low")  # Placeholder for risk level

    st.subheader("Full-Model Prediction")
    st.text("Combining EEG and wearable data for predictions.")

    st.warning("Wearable-Only Predictions: Limited accuracy warning")

    st.subheader("Emergency Alert Activation")
    st.button("Send Alert")

    st.subheader("Auto-SOS")
    st.button("Trigger Auto-SOS")

    st.text("Backend Integrations: Real-Time Data Processing, Alert System")
