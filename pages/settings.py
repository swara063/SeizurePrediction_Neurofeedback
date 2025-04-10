import streamlit as st

def show():
    st.image("assets/logo.png", width=50)
    st.title("NeuraCare")
    st.header("Settings & Customization")
    st.markdown("Configure your app settings.")

    st.subheader("Notification Settings")
    st.selectbox("Alert Preferences", ["All", "Critical Only", "None"])

    st.subheader("Privacy & Security")
    st.checkbox("Enable Data Sharing")

    st.subheader("Dark Mode & Accessibility")
    st.checkbox("Enable Dark Mode")

    st.subheader("Logout & Account Deletion")
    st.button("Logout")
    st.button("Delete Account")

    st.subheader("Wearable Device Management")
    st.selectbox("Manage Devices", ["EEG Headset", "Wearable Watch"])

    st.text("Backend Integrations: User Preferences, Device Management")
