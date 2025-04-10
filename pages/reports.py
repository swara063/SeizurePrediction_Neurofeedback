import streamlit as st

def show():
    st.image("assets/logo.png", width=50)
    st.title("NeuraCare")
    st.header("Reports, Insights & AI Training")
    st.markdown("View detailed reports and insights.")

    st.subheader("AI Training Progress")
    st.progress(80)  # Placeholder for model confidence

    st.subheader("Seizure History & Pattern Analysis")
    st.line_chart([1, 2, 3, 4])  # Placeholder for historical data

    st.subheader("Weekly & Monthly Health Trends")
    st.area_chart([1, 2, 3, 4])  # Placeholder for graphical data

    st.subheader("Model Confidence Score")
    st.metric("Confidence", "High")  # Placeholder for AI certainty

    st.subheader("User Feedback")
    st.radio("Rate Prediction Accuracy", ["Poor", "Average", "Good"])

    st.subheader("Doctor’s Portal")
    st.text_area("Remote Data Review")

    st.subheader("Community & Support")
    st.text_area("Forum Discussions")

    st.subheader("AI Explainability Report")
    st.text("Explanation of predictions.")

    st.warning("Anomaly Detection Alerts: Placeholder for alert")

    st.text("Backend Integrations: Data Analysis, Feedback Collection")
