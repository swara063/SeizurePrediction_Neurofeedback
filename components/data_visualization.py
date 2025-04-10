# components/data_visualization.py

import streamlit as st
import pandas as pd

def display_line_chart(data, title="Line Chart"):
    # Placeholder for displaying a line chart
    df = pd.DataFrame(data, columns=["Value"])
    st.line_chart(df)
    print("Displaying line chart:", title)

def display_bar_chart(data, title="Bar Chart"):
    # Placeholder for displaying a bar chart
    df = pd.DataFrame(data, columns=["Value"])
    st.bar_chart(df)
    print("Displaying bar chart:", title)
