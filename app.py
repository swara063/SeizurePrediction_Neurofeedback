import streamlit as st
from datetime import datetime
from utils.eeg import generate_dummy_eeg  
from components.preprocessing import preprocess_data_for_model
from models.model_loader import load_prediction_model
import numpy as np
import pandas as pd
import time



# ✅ Page title and favicon
st.set_page_config(page_title="NeuraCare", page_icon="assets/logo.png", layout="wide")

# ✅ Inject CSS
with open("assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ✅ Session State Initialization
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# ✅ Main Content
logo_col, title_col = st.columns([1, 6])
with logo_col:
    st.image("assets/logo.png", width=60)  # Place your logo image in assets folder
with title_col:
    st.markdown("<h1 style='font-size: 50px; margin-bottom: 0;'>NeuraCare</h1>", unsafe_allow_html=True)
    st.subheader("For Seizure Prediction & Brainwave Redirection")

# ✅ Info Box
st.markdown("""
    <div class="info-box">
        <h3>Welcome to Your Personal Brain Trainer</h3>
        <p>Our non-invasive neurofeedback system uses AI and real-time brain monitoring to help manage seizures and mental well-being.</p>
    </div>
""", unsafe_allow_html=True)

# ✅ Add space after info box
st.markdown("<br>", unsafe_allow_html=True)

# ✅ Uniform Metric Boxes
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("""
        <div class="metric-box">
            <h4>Today's Goal</h4>
            <p>70%</p>
        </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
        <div class="metric-box">
            <h4>Seizure Risk Level</h4>
            <p>Low (15%)</p>
        </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
        <div class="metric-box">
            <h4>AI Training Progress</h4>
            <p>68%</p>
        </div>
    """, unsafe_allow_html=True)
with col4:
    st.markdown("""
        <div class="metric-box">
            <h4>Connected Devices</h4>
            <p>EEG Headset, Smartwatch</p>
        </div>
    """, unsafe_allow_html=True)


# ✅ Light Green Section for Brainwave Activity and Feed
st.markdown("""
    <div style="background-color: #e6f4ea; padding: 20px; border-radius: 10px;">
        <h3>Live Brainwave Activity</h3>
""", unsafe_allow_html=True)

raw_eeg = generate_dummy_eeg()
# st.line_chart(raw_eeg[0, :, 0])

# Config
max_history = 200  # Show only last 200 points for clarity
update_interval = 0.1  # Seconds

raw_eeg = generate_dummy_eeg()
# st.line_chart(raw_eeg[0, :, 0])
# Config
max_history = 200  # Show only last 200 points for clarity
update_interval = 0.1  # Seconds

# Streamlit UI
st.title("Smooth Real-Time EEG Plot")
plot_placeholder = st.empty()

# Rolling EEG signal buffer
eeg_history = []

while True:
    raw_eeg = generate_dummy_eeg()
    eeg_history.extend(raw_eeg[0, :, 0])  # Append new data (128 points)

    # Trim to keep only the latest ⁠ max_history ⁠ points
    if len(eeg_history) > max_history:
        eeg_history = eeg_history[-max_history:]

    # Convert to DataFrame
    df = pd.DataFrame(eeg_history, columns=["EEG Signal"])

    # Display line chart inside the same placeholder
    plot_placeholder.line_chart(df)

    time.sleep(update_interval)




st.markdown("<h3>Activity Feed</h3>", unsafe_allow_html=True)
with st.container():
    st.markdown("- ✅ EEG Connected at 09:45 AM")
    st.markdown("- 📈 AI Training Progressed to 68%")
    st.markdown("- ⚠️ Low seizure risk detected at 10:00 AM")
    st.markdown("- 🎯 Last neurofeedback session: Successful")


st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
st.caption("©️ 2025 Neurofeedback System. All rights reserved.")
