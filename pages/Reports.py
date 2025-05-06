import streamlit as st
import pandas as pd
import altair as alt
import time
import os

# ✅ Page Setup
st.set_page_config(page_title="Reports & Insights", page_icon="assets/logo.png", layout="wide")

# ✅ Inject CSS
with open("assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ✅ Title & Subtitle
st.title("📄 Reports & Insights")
st.markdown("Track your journey towards better brain health and wellbeing.")

st.markdown("---")

# ✅ Monthly Summary
st.subheader("📆 Monthly Summary")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Sessions Completed", "1")
col2.metric("Avg. Seizure Risk", "Low")
col3.metric("Sleep Quality", "7.2 hrs/night")
col4.metric("Stress Trends", "Mild variations")


st.markdown("---")

# ✅ Visual Insights
st.subheader("📊 Visual Insights")

# Simulated Seizure Risk Trend
st.markdown("*Seizure Risk Trend (Last 7 Days)*")
seizure_data = pd.DataFrame({
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "Seizure Risk (%)": [10, 20, 10, 0, 20, 25, 35]
})
seizure_chart = alt.Chart(seizure_data).mark_line(point=True).encode(
    x="Day",
    y="Seizure Risk (%)",
    tooltip=["Day", "Seizure Risk (%)"]
).properties(height=300)
st.altair_chart(seizure_chart, use_container_width=True)

# Simulated Sleep Quality Chart
st.markdown("*Sleep Quality (Hours Slept)*")
sleep_data = pd.DataFrame({
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "Hours Slept": [7, 8, 6.5, 7.5, 6, 8.5, 7]
})
sleep_chart = alt.Chart(sleep_data).mark_bar(color="#2a9d8f").encode(
    x="Day",
    y="Hours Slept",
    tooltip=["Day", "Hours Slept"]
).properties(height=300)
st.altair_chart(sleep_chart, use_container_width=True)

st.markdown("---")

# ✅ Recommendations
st.subheader("🧠 Insights & Recommendations")
st.markdown("""
- ✅ Maintain consistent sleep schedule for improved recovery.  
- ✅ Continue neurofeedback sessions at least 3 times a week.  
- ✅ Moderate daily stress levels through relaxation exercises.  
- ✅ Keep your devices connected for accurate tracking.
""")

st.markdown("---")

# ✅ Report Download Section
if st.button("⚡ Download Latest Report"):
    with st.spinner("Generating report..."):
        time.sleep(2)
    
        file_path = os.path.join("assets", "report3.pdf")
        with open(file_path, "rb") as file:
            st.download_button(
                label="Download Report",
                data=file,
                file_name="neurofeedback_report.pdf",
                mime="application/pdf"
            )

st.markdown("---")