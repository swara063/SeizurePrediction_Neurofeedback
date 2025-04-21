import streamlit as st

# ✅ Page Setup
st.set_page_config(page_title="Real-Time Monitoring", page_icon="assets/logo.png", layout="wide")

# ✅ Inject CSS
with open("assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ✅ Page Title
st.title("📡 Real-Time Monitoring & Preemptive Prediction")
st.markdown("Stay informed with real-time brainwave and wearable data.")

st.markdown("---")

# ✅ Live EEG Monitoring Section
st.subheader("🧠 Live EEG Monitoring")
st.markdown("**Brainwave Activity**: Alpha: 45% | Beta: 30% | Delta: 25%")

col1, col2, col3 = st.columns(3)
col1.metric("Alpha Waves", "45%")
col2.metric("Beta Waves", "30%")
col3.metric("Delta Waves", "25%")

if st.button("🔄 Refresh EEG Data"):
    st.success("EEG data updated successfully!")

st.markdown("---")

# ✅ AI-Powered Risk Prediction Section
st.subheader("🤖 AI-Powered Risk Prediction")
col4, col5 = st.columns(2)
col4.metric("Seizure Risk", "Moderate (60%)")
col5.progress(0.6, text="60% Risk Level")

if st.button("🔄 Update Prediction"):
    st.info("AI risk prediction updated.")

# ✅ Full Model Prediction Section
st.markdown("### 📊 Full Model Prediction (EEG + Wearables)")
st.metric("Prediction Accuracy", "85%")
st.progress(0.85, text="85% Accuracy")

if st.button("🔁 Refresh Full Prediction"):
    st.info("Full model prediction refreshed!")

st.markdown("---")

# ✅ Wearable-Only Prediction
st.subheader("⌚ Wearable-Only Prediction")
st.metric("Accuracy", "50% (Limited Accuracy)")
st.progress(0.5, text="50% Accuracy")

if st.button("🔄 Update Wearable Prediction"):
    st.warning("Wearable prediction updated with limited accuracy.")

st.markdown("---")

# ✅ Emergency Alert System
st.subheader("🚨 Emergency Alert System")
alert_col1, alert_col2 = st.columns(2)
with alert_col1:
    if st.button("📢 Send Manual Alert"):
        st.error("⚠️ Manual SOS sent!")
with alert_col2:
    if st.button("🧭 Start Auto-SOS Countdown"):
        st.warning("Auto-SOS initiated. Countdown: 5 seconds...")

st.markdown("---")

