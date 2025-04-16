import streamlit as st
from datetime import datetime

# ✅ Page title and favicon
st.set_page_config(page_title="Profile & Data", page_icon="assets/logo.png", layout="wide")

# ✅ Inject CSS
with open("assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ✅ Title
st.title("🧑‍⚕️ User Profile & Data Collection")
st.markdown("Manage your health data and personalize your experience.")

st.markdown("---")

# ✅ Profile Section
st.subheader("👤 Create Your Profile")
with st.form("profile_form"):
    col1, col2 = st.columns(2)
    name = col1.text_input("Name")
    age = col2.number_input("Age", min_value=1, max_value=120, step=1)
    medical_history = st.text_area("Medical History", height=100)
    submitted = st.form_submit_button("💾 Save Profile")
    if submitted:
        st.success("✅ Profile saved successfully!")

st.markdown("---")

# ✅ EEG Metrics
st.subheader("📊 EEG Metrics")
eeg_col1, eeg_col2, eeg_col3 = st.columns(3)
eeg_col1.metric("Alpha Waves", "Moderate")
eeg_col2.metric("Beta Waves", "High Focus")
eeg_col3.metric("Seizure Risk", "Low (12%)")

st.markdown("---")

# ✅ Wearables Data Dashboard
st.subheader("⌚ Wearables Data Dashboard")
wear1, wear2, wear3 = st.columns(3)
wear1.metric("Heart Rate", "72 bpm")
wear2.metric("Blood Pressure", "120/80 mmHg")
wear3.metric("SpO2", "98%")
wear4, wear5, wear6 = st.columns(3)
wear4.metric("Sleep", "7.5 hrs")
wear5.metric("Stress Level", "Moderate")

st.markdown("---")

# ✅ AI Training Progress
st.subheader("🧠 AI Training Progress")
st.write("Your AI assistant is becoming more personalized each day!")
st.progress(0.65, text="65% Personalized")

st.markdown("---")

# ✅ Data Source Customization
st.subheader("🛠 Data Source Customization")
with st.form("data_sources_form"):
    eeg = st.checkbox("EEG Device", value=True)
    wearable = st.checkbox("Wearable Watch", value=True)
    sleep = st.checkbox("Sleep Monitor", value=True)
    save_data = st.form_submit_button("💾 Save Settings")
    if save_data:
        st.success("✅ Data source settings saved!")



