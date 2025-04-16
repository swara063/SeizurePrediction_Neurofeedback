import streamlit as st

def home_page():
    st.set_page_config(page_title="NeuroFlow Dashboard", layout="wide")
    
    # --- Header remains unchanged ---
    st.title("NeuroFlow Dashboard")
    st.markdown("---")
    
    # === Modified Stats Section ===
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div style='border: 1px solid #e0e0e0; border-radius: 10px; padding: 20px; margin: 10px;'>
            <h3 style='color: #1e88e5; margin-bottom: 15px;'>Today's Goal</h3>
            <div style='font-size: 32px; font-weight: bold; color: #43a047;'>70%</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style='border: 1px solid #e0e0e0; border-radius: 10px; padding: 20px; margin: 10px;'>
            <h3 style='color: #1e88e5; margin-bottom: 15px;'>Seizure Risk Level</h3>
            <div style='font-size: 24px; font-weight: bold; color: #43a047;'>
                Low <span style='font-size: 16px; color: #757575;'>(15%)</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style='border: 1px solid #e0e0e0; border-radius: 10px; padding: 20px; margin: 10px;'>
            <h3 style='color: #1e88e5; margin-bottom: 15px;'>AI Training Progress</h3>
            <div style='font-size: 32px; font-weight: bold; color: #43a047;'>68%</div>
        </div>
        """, unsafe_allow_html=True)

    # === Modified Connected Devices ===
    st.markdown("---")
    st.subheader("Connected Devices")
    with st.container():
        st.markdown("""
        <div style='border-left: 4px solid #1e88e5; padding: 15px; margin: 10px; background-color: #f5f5f5;'>
            <div style='font-size: 18px; font-weight: bold;'>Strava API</div>
            <div style='color: #757575;'>Last synced: 2h ago</div>
        </div>
        """, unsafe_allow_html=True)

    # === Modified Activity Feed ===
    st.markdown("---")
    st.subheader("Activity Feed")
    activities = [
        {"title": "Morning Run", "time": "7:30 AM", "duration": "42 mins", "distance": "5.2 km"},
        {"title": "Cycling Session", "time": "4:15 PM", "duration": "1h 18m", "distance": "18.3 km"}
    ]
    
    for activity in activities:
        with st.container():
            st.markdown(f"""
            <div style='border: 1px solid #e0e0e0; border-radius: 8px; padding: 15px; margin: 10px;'>
                <div style='font-size: 16px; font-weight: bold;'>{activity['title']}</div>
                <div style='display: flex; justify-content: space-between; color: #757575;'>
                    <span>{activity['time']}</span>
                    <span>{activity['duration']}</span>
                    <span>{activity['distance']}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

if __name__ == "__main__":
    home_page()
