import streamlit as st

def show():
    st.image("assets/logo.png", width=50)
    st.title("NeuraCare")
    st.header("User Profile & Data Collection")
    st.markdown("Create your profile and view your data.")

    st.subheader("Profile Creation")
    with st.form("profile_form"):
        st.text_input("Name")
        st.date_input("Date of Birth")
        st.form_submit_button("Save Profile")

    st.subheader("Wearables Data Dashboard")
    st.line_chart([1, 2, 3, 4])  # Placeholder for HR, BP data

    st.subheader("EEG-Based Metrics Dashboard")
    st.line_chart([1, 2, 3, 4])  # Placeholder for brainwave activity

    st.subheader("Reinforcement Learning Progress")
    st.progress(70)  # Placeholder for AI training progress

    st.subheader("Data Source Customization")
    st.checkbox("Enable EEG Sensor")
    st.checkbox("Enable Wearable Sensor")

    st.warning("Wearable Disconnection Warning: Placeholder for alert")

    st.text("Backend Integrations: Data Storage, Real-Time Data Fetching")
