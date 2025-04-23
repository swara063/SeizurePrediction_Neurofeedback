import streamlit as st
from streamlit_option_menu import option_menu
import firebase_admin
from firebase_admin import credentials, auth, db
import tempfile
import requests
from datetime import datetime, timedelta
import pandas as pd
import altair as alt
import os

# ✅ Page title and favicon
st.set_page_config(page_title="NeuraCare", page_icon="assets/logo.png", layout="wide")

# ✅ Inject CSS
with open("assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ✅ Hide default Streamlit elements
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# ✅ App Header
st.title("🛠 Welcome to Neurofeedback Onboarding")
st.write("Let's get you set up!")

# ✅ Firebase Auth
st.subheader("🔐 Login / Sign Up to Your Account")
uploaded_file = st.file_uploader("Upload your Firebase credentials (.json)", type=["json"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_file_path = tmp_file.name

    try:
        if not firebase_admin._apps:
            cred = credentials.Certificate(tmp_file_path)
            firebase_admin.initialize_app(cred, {
                'databaseURL': "https://seizurepredictionneurofeedback-default-rtdb.asia-southeast1.firebasedatabase.app"
            })

        # Auth Flow
        selected = option_menu(
            menu_title=None,
            options=["Login", "Sign Up"],
            icons=["box-arrow-in-right", "person-plus"],
            orientation="horizontal"
        )

        if selected == "Login":
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            if st.button("Login"):
                try:
                    user = auth.get_user_by_email(email)
                    st.success(f"✅ Welcome back, {user.email}!")
                    st.session_state['logged_in'] = True
                except auth.UserNotFoundError:
                    st.error("❌ User not found. Please sign up first.")
                except ValueError:
                    st.error("❌ Invalid email format.")
                except Exception as e:
                    st.error(f"❌ Login failed: {str(e)}")

        elif selected == "Sign Up":
            new_email = st.text_input("New Email")
            new_password = st.text_input("New Password", type="password")
            if st.button("Sign Up"):
                try:
                    if len(new_password) < 6:
                        st.error("❌ Password must be at least 6 characters")
                    else:
                        user = auth.create_user(
                            email=new_email,
                            password=new_password,
                            email_verified=False
                        )
                        st.success(f"✅ Account created for {user.email}!")
                        st.session_state['logged_in'] = True
                except auth.EmailAlreadyExistsError:
                    st.error("❌ Email already in use. Please login instead.")
                except ValueError as e:
                    st.error(f"❌ Invalid input: {str(e)}")
                except Exception as e:
                    st.error(f"❌ Account creation failed: {str(e)}")

        # --- Onboarding Steps ---
        st.markdown("---")
        st.subheader("🚀 Onboarding Steps")
        onboarding_step = st.radio(
            "Select Onboarding Step:",
            ["Device Pairing", "Device Calibration", "AI Training & Strava"],
            horizontal=True
        )

        # --- Step 1: Device Pairing
        if onboarding_step == "Device Pairing":
            st.subheader("🔌 Device Pairing")
            col1, col2 = st.columns(2)
            with col1:
                if st.button("🧠 Connect EEG Headset"):
                    st.success("EEG Headset connected!")
            with col2:
                if st.button("⌚ Connect Wearable Watch"):
                    st.success("Wearable Watch connected!")

        # --- Step 2: Calibration
        elif onboarding_step == "Device Calibration":
            st.subheader("🎛️ Device Calibration")
            st.write("Calibrating sensors for accurate tracking...")
            st.progress(80, text="80% Calibrated")
            st.button("✅ Complete Calibration")

        # --- Step 3: AI Training + Strava
        elif onboarding_step == "AI Training & Strava":
            st.subheader("🧠 AI Training Progress")
            st.write("Your AI adapts with your brain activity.")
            data = pd.DataFrame({
                'Session': ['Session 1', 'Session 2', 'Session 3', 'Session 4'],
                'Accuracy': [65, 70, 75, 80]
            })
            chart = alt.Chart(data).mark_line(point=True).encode(
                x='Session', y='Accuracy'
            ).properties(height=300)
            st.altair_chart(chart, use_container_width=True)

            st.markdown("---")
            st.subheader("🚴 Connect with Strava")

            # STRAVA SETUP
            ACCESS_TOKEN = "8332cc686e43b010cd9a9a48334172715b56ec76"  # Replace if needed
            HEADERS = {"Authorization": f"Bearer {ACCESS_TOKEN}"}

            def fetch_profile():
                res = requests.get("https://www.strava.com/api/v3/athlete", headers=HEADERS)
                res.raise_for_status()
                return res.json()

            def fetch_activities(pages=2):
                all_activities = []
                for page in range(1, pages + 1):
                    r = requests.get(
                        f"https://www.strava.com/api/v3/athlete/activities?per_page=50&page={page}",
                        headers=HEADERS
                    )
                    if r.status_code != 200:
                        return []
                    all_activities.extend(r.json())
                return all_activities

            try:
                profile = fetch_profile()
                st.write(f"**Name:** {profile['firstname']} {profile['lastname']}")
                st.write(f"**City:** {profile.get('city', 'N/A')}")
                st.write(f"**Country:** {profile.get('country', 'N/A')}")

                activities = fetch_activities()
                st.markdown("### 📊 Recent Activities")
                st.write(f"Total Activities: {len(activities)}")

                if activities:
                    latest = activities[0]
                    st.write(f"**Latest Activity:** {latest['name']} on {latest['start_date']}")
                    st.write(f"Distance: {latest['distance']/1000:.2f} km")
                    st.write(f"Time: {latest['elapsed_time']/60:.1f} min")

                    df = pd.DataFrame([{
                        "Name": act['name'],
                        "Date": act['start_date'],
                        "Distance (km)": act['distance'] / 1000,
                        "Time (min)": act['elapsed_time'] / 60,
                        "Speed (km/h)": act['average_speed'] * 3.6,
                    } for act in activities])

                    st.dataframe(df)
                    st.altair_chart(
                        alt.Chart(df).mark_line(point=True).encode(
                            x="Date:T", y="Distance (km):Q",
                            tooltip=["Name", "Distance (km)", "Speed (km/h)"]
                        ).interactive(),
                        use_container_width=True
                    )
                else:
                    st.warning("No Strava activities found.")

            except Exception as e:
                st.error(f"Error fetching Strava data: {e}")

    except Exception as e:
        st.error(f"Firebase initialization failed: {e}")
    finally:
        try:
            os.unlink(tmp_file_path)
        except:
            pass
else:
    st.warning("👆 Upload Firebase credentials to proceed with onboarding.")
