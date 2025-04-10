import streamlit as st

# Load custom CSS
def load_css():
    with open("assets/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Logo and App Name
st.sidebar.image("assets/logo.png", width=50)
st.sidebar.title("NeuraCare")

# Navigation
pages = {
    "Onboarding & Device Connectivity": "onboarding",
    "User Profile & Data Collection": "profile",
    "Real-Time Monitoring & Preemptive Prediction": "monitoring",
    "Neurofeedback": "neurofeedback",
    "Reports, Insights & AI Training": "reports",
    "Settings & Customization": "settings"
}

selection = st.sidebar.radio("Go to", list(pages.keys()))

if selection:
    page = pages[selection]
    module = __import__(f"pages.{page}", fromlist=[None])
    module.show()
