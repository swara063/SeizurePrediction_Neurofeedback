import streamlit as st

# ✅ Page Setup
st.set_page_config(page_title="Settings", page_icon="assets/logo.png", layout="wide")

# ✅ Inject CSS
with open("assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ✅ Title & Subtitle
st.title("⚙️ Settings & Preferences")
st.markdown("Manage your app settings and notifications.")

st.markdown("---")

# ✅ Profile Settings
st.subheader("👤 Profile Settings")
username = st.text_input("Username", value="JohnDoe")
email = st.text_input("Email", value="johndoe@example.com")

if st.button("💾 Save Profile"):
    st.success("Profile settings saved!")

st.markdown("---")

# ✅ Device Settings
st.subheader("🔌 Device Settings")
st.markdown("Manage your connected devices.")

col1, col2 = st.columns(2)
with col1:
    if st.button("🔗 Connect New Device"):
        st.success("New device connected.")
with col2:
    if st.button("❌ Disconnect Device"):
        st.warning("Device disconnected.")

st.markdown("---")

# ✅ Theme & Notification Settings
st.subheader("🎨 Theme Settings")
theme = st.selectbox("Select Theme", ["Default", "Dark Mode", "Light Mode"])
st.subheader("🔔 Notifications")
seizure_alerts = st.checkbox("Seizure Alerts", value=True)
daily_summary = st.checkbox("Daily Summary", value=True)
weekly_report = st.checkbox("Weekly Report", value=True)

if st.button("💾 Save Preferences"):
    st.success("Preferences saved successfully!")

st.markdown("---")

# ✅ Security Settings
st.subheader("🔒 Security Settings")
two_factor = st.checkbox("Enable Two-Factor Authentication")

if st.button("🔐 Update Security"):
    if two_factor:
        st.success("Two-Factor Authentication enabled.")
    else:
        st.info("Two-Factor Authentication disabled.")

st.markdown("---")

# ✅ About This App
st.subheader("ℹ️ About This App")
st.markdown("""
**Version**: 1.0.0  
Developed to help patients with epilepsy through advanced neurofeedback therapy.
""")

if st.button("🔄 Check for Updates"):
    st.info("You're using the latest version!")

st.caption("© 2025 Neurofeedback App. All rights reserved.")
