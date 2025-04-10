import streamlit as st

def show():
    st.image("assets/logo.png", width=50)
    st.title("NeuraCare")
    st.header("Onboarding & Device Connectivity")
    st.markdown("Welcome to the onboarding process. Here you will connect your devices and set up your profile.")

    st.subheader("Device Pairing")
    st.selectbox("Select Device", ["EEG Headset", "Wearable Watch"])
    st.button("Pair Device")

    st.subheader("Device Calibration")
    st.progress(50)  # Placeholder for calibration progress

    st.subheader("AI Training Introduction")
    st.markdown("Learn how AI personalizes itself over time for better seizure prediction.")

    st.subheader("Baseline Health Data Collection")
    with st.form("health_data"):
        st.text_input("Enter your age")
        st.selectbox("Select your gender", ["Male", "Female", "Other"])
        st.form_submit_button("Submit")

    st.text("Backend Integrations: Firebase Authentication, Device Integration")
