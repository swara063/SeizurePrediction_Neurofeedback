import streamlit as st
import random
import time
from utils.dummy_eeg_generator import generate_dummy_eeg  # Importing the dummy EEG generator function
from components.preprocessing import preprocess_eeg_segment
from models.model_loader import load_prediction_model

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

# ✅ Dynamic Metric Boxes
goal = random.uniform(60, 80)  # Today's goal (dynamic, between 60% and 80%)
seizure_risk = random.uniform(10, 30)  # Seizure risk (dynamic, between 10% and 30%)
training_progress = random.uniform(50, 70)  # AI Training Progress (dynamic, between 50% and 70%)
connected_devices = ["EEG Headset", "Smartwatch"]  # Devices could be dynamically checked from actual connections

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(f"""
        <div class="metric-box">
            <h4>Today's Goal</h4>
            <p>{goal:.2f}%</p>
        </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown(f"""
        <div class="metric-box">
            <h4>Seizure Risk Level</h4>
            <p>Low ({seizure_risk:.2f}%)</p>
        </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown(f"""
        <div class="metric-box">
            <h4>AI Training Progress</h4>
            <p>{training_progress:.2f}%</p>
        </div>
    """, unsafe_allow_html=True)
with col4:
    st.markdown(f"""
        <div class="metric-box">
            <h4>Connected Devices</h4>
            <p>{', '.join(connected_devices)}</p>
        </div>
    """, unsafe_allow_html=True)

# ✅ Navigation to Neurofeedback Therapy Page
if st.button("🧘 Neurofeedback Therapy"):
    st.session_state.page = "neurofeedback"

# ✅ Real-Time EEG Simulation & Prediction Section
if st.session_state.page == 'neurofeedback':
    # Load the model
    model = load_prediction_model()

    st.title("Real-Time EEG Monitoring (Simulated)")
    placeholder = st.empty()

    run = st.checkbox("Start Simulation")

    while run:
        # Generate dummy EEG data (simulated)
        raw_eeg = generate_dummy_eeg()

        # Pre-process the raw EEG data
        processed_eeg = preprocess_eeg_segment(raw_eeg)

        # Model input preparation
        model_input = processed_eeg[np.newaxis, ...]  # Shape: (1, 22, 256, 4)

        # Predict the seizure risk
        prediction = model.predict(model_input)[0][0]  # Assuming binary prediction

        # Display the predicted seizure probability
        placeholder.metric("Seizure Probability", f"{prediction:.2f}")

        # Extract features like alpha, beta, and delta from the raw EEG data
        alpha_waves = np.mean(raw_eeg[:, :, 0])  # Placeholder for alpha waves computation
        beta_waves = np.mean(raw_eeg[:, :, 1])  # Placeholder for beta waves computation
        delta_waves = np.mean(raw_eeg[:, :, 2])  # Placeholder for delta waves computation

        # Live EEG Monitoring Section
        st.subheader("🧠 Live EEG Monitoring")
        st.markdown(f"**Brainwave Activity**: Alpha: {alpha_waves:.2f} | Beta: {beta_waves:.2f} | Delta: {delta_waves:.2f}")

        col1, col2, col3 = st.columns(3)
        col1.metric("Alpha Waves", f"{alpha_waves:.2f}")
        col2.metric("Beta Waves", f"{beta_waves:.2f}")
        col3.metric("Delta Waves", f"{delta_waves:.2f}")

        if st.button("🔄 Refresh EEG Data"):
            st.success("EEG data updated successfully!")

        st.markdown("---")

        # AI-Powered Risk Prediction Section
        st.subheader("🤖 AI-Powered Risk Prediction")
        st.markdown(f"**Seizure Risk**: {'High' if prediction > 0.6 else 'Moderate' if prediction > 0.3 else 'Low'} ({prediction*100:.2f}%)")

        col4, col5 = st.columns(2)
        col4.metric("Seizure Risk", f"{'High' if prediction > 0.6 else 'Moderate' if prediction > 0.3 else 'Low'} ({prediction*100:.2f}%)")
        col5.progress(prediction, text=f"{prediction*100:.2f}% Risk Level")

        if st.button("🔄 Update Prediction"):
            st.info("AI risk prediction updated.")

        # Full Model Prediction Section
        st.markdown("### 📊 Full Model Prediction (EEG + Wearables)")
        accuracy = np.random.uniform(0.8, 0.9)  # Simulated accuracy value
        st.metric("Prediction Accuracy", f"{accuracy*100:.2f}%")
        st.progress(accuracy, text=f"{accuracy*100:.2f}% Accuracy")

        if st.button("🔁 Refresh Full Prediction"):
            st.info("Full model prediction refreshed!")

        st.markdown("---")

        # Wearable-Only Prediction
        st.subheader("⌚ Wearable-Only Prediction")
        wearable_accuracy = np.random.uniform(0.4, 0.6)  # Simulated wearable-only prediction accuracy
        st.metric("Accuracy", f"{wearable_accuracy*100:.2f}%")
        st.progress(wearable_accuracy, text=f"{wearable_accuracy*100:.2f}% Accuracy")

        if st.button("🔄 Update Wearable Prediction"):
            st.warning("Wearable prediction updated with limited accuracy.")

        st.markdown("---")

        # Emergency Alert System
        st.subheader("🚨 Emergency Alert System")
        alert_col1, alert_col2 = st.columns(2)
        with alert_col1:
            if st.button("📢 Send Manual Alert"):
                st.error("⚠️ Manual SOS sent!")
        with alert_col2:
            if st.button("🧭 Start Auto-SOS Countdown"):
                st.warning("Auto-SOS initiated. Countdown: 5 seconds...")

        st.markdown("---")

        # Show the raw EEG data for channel 0, feature 0
        st.line_chart(raw_eeg[0, :, 0])  # Show EEG data for channel 0, feature 0

        # Sleep for 1 second before next data update
        time.sleep(1)
