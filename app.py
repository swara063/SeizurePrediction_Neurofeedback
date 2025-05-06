import streamlit as st
from utils.dummy_eeg_generator import real_time_eeg_stream
import numpy as np
import pandas as pd
import time

# Page title and favicon
st.set_page_config(page_title="NeuraCare", page_icon="assets/logo.png", layout="wide")

# Inject CSS
with open("assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Session state initialization
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Main content
logo_col, title_col = st.columns([1, 6])
with logo_col:
    st.image("assets/logo.png", width=60)
with title_col:
    st.markdown("<h1 style='font-size: 50px; margin-bottom: 0;'>NeuraCare</h1>", unsafe_allow_html=True)
    st.subheader("For Seizure Prediction & Brainwave Redirection")

# Info box
st.markdown("""
    <div class="info-box">
        <h3>Welcome to Your Personal Brain Trainer</h3>
        <p>Our non-invasive neurofeedback system uses AI and real-time brain monitoring to help manage seizures and mental well-being.</p>
    </div>
""", unsafe_allow_html=True)

# Add space after info box
st.markdown("<br>", unsafe_allow_html=True)

# Uniform metric boxes
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("""
        <div class="metric-box">
            <h4>Today's Goal</h4>
            <p>0%</p>
        </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
        <div class="metric-box">
            <h4>Seizure Risk Level</h4>
            <p>Low (0%)</p>
        </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
        <div class="metric-box">
            <h4>AI Training Progress</h4>
            <p>0%</p>
        </div>
    """, unsafe_allow_html=True)
with col4:
    st.markdown("""
        <div class="metric-box">
            <h4>Connected Devices</h4>
            <p>No Devices</p>
        </div>
    """, unsafe_allow_html=True)

# Light green section for Brainwave Activity and Feed
st.markdown("""
    <div style="background-color: #e6f4ea; padding: 20px; border-radius: 10px;">
        <h3>Live Brainwave Activity</h3>
""", unsafe_allow_html=True)

# Set up real-time EEG stream
stream = real_time_eeg_stream()
buffer_size = 1024  # or 512
eeg_buffer = np.zeros(buffer_size)

# Plot placeholder
plot_placeholder = st.empty()

# Activity Feed
st.markdown("<h3>Activity Feed</h3>", unsafe_allow_html=True)
with st.container():
    st.markdown("- ✅ EEG Connected at 09:45 AM")
    st.markdown("- 📈 AI Training Progressed to 68%")
    st.markdown("- ⚠️ Low seizure risk detected at 10:00 AM")
    st.markdown("- 🎯 Last neurofeedback session: Successful")

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("---")
st.caption("© 2025 Neurofeedback System. All rights reserved.")

# Real-time loop
while True:
    eeg_window, true_label = next(stream)  # shape: (22, 256, 64)
    display_channel = eeg_window[0, :, 0]  # Take first channel, first feature

    # Update rolling buffer
    eeg_buffer = np.roll(eeg_buffer, -len(display_channel))
    eeg_buffer[-len(display_channel):] = display_channel

    # Update plot
    df = pd.DataFrame({"EEG": eeg_buffer})
    plot_placeholder.line_chart(df, use_container_width=True)

    # Sleep between updates
    time.sleep(0.3)  # Adjust as needed
