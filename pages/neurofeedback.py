import streamlit as st

def show():
    st.image("assets/logo.png", width=50)
    st.title("NeuraCare")
    st.header("Neurofeedback")
    st.markdown("Engage in neurofeedback sessions to improve your health.")

    st.subheader("Neurofeedback Dashboard")
    st.line_chart([1, 2, 3, 4])  # Placeholder for training progress

    st.subheader("Manual Neurofeedback Session")
    st.button("Start Session")

    st.subheader("Preemptive Seizure Prevention Mode")
    st.checkbox("Enable Mode")

    st.subheader("AI-Personalized Feedback")
    st.text("Feedback based on brainwave data.")

    st.subheader("Threshold-Based Activation")
    st.slider("Set Threshold", 0, 100, 50)

    st.text("Backend Integrations: Session Management, AI Feedback")
