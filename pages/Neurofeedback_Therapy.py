import streamlit as st

# ✅ Page Setup
st.set_page_config(page_title="Neurofeedback Therapy", page_icon="assets/logo.png", layout="wide")

# ✅ Inject CSS
with open("assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ✅ Page Title
st.title("🧘 Neurofeedback Treatment & Prevention")
st.markdown("Train your brain with real-time feedback for better health.")

st.markdown("---")

# ✅ Manual Neurofeedback Session
st.subheader("🧠 Manual Neurofeedback Session")
session_status = st.radio("Session Status:", ["Not Started", "In Progress", "Completed"], index=0, horizontal=True)

col1, col2 = st.columns(2)
with col1:
    if st.button("▶️ Start Session"):
        st.success("Session started.")
with col2:
    if st.button("💾 Save Session Data"):
        st.success("Session data saved.")

st.markdown("---")

# ✅ Preemptive Seizure Prevention Mode
st.subheader("🛡️ Preemptive Seizure Prevention Mode")
st.markdown("**Status:** Inactive")

if st.button("⚡ Activate Mode"):
    st.info("Seizure prevention mode activated!")

st.markdown("---")

# ✅ Neurofeedback Dashboard
st.subheader("📊 Neurofeedback Dashboard")
st.markdown("**Current Training Progress:** 65%")
st.progress(0.65, text="65% Complete")

if st.button("🔄 Refresh Progress"):
    st.success("Training progress updated!")

st.markdown("---")

# ✅ AI-Personalized Feedback
st.subheader("🤖 AI-Personalized Feedback")
st.markdown("Real-time Brainwave Adaptation: **Ongoing**")

st.progress(0.70, text="Adaptive Feedback 70%")

if st.button("🔄 Update Feedback"):
    st.success("Adaptive feedback updated.")

st.markdown("---")

# ✅ Threshold-Based Activation
st.subheader("📉 Threshold-Based Activation")
st.markdown("Seizure Threshold Detected: **No**")

if st.button("📶 Monitor Threshold"):
    st.warning("Monitoring seizure threshold...")

st.markdown("---")

# ✅ Navigation
colA, colB, colC = st.columns([1, 2, 1])
with colA:
    if st.button("⬅️ Back to Real-Time Monitoring"):
        st.switch_page("pages/RealTime_Monitoring.py")
with colC:
    if st.button("➡️ Next: Reports & History"):
        st.switch_page("pages/Reports_And_History.py")
