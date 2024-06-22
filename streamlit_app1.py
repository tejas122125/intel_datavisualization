import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# Function to fetch data from the Node.js API
def fetch_data():
    try:
        response = requests.get('http://127.0.0.1:5000/data')
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return None

# Streamlit app
st.title("Interactive Dashboard from CSV Data")

data = fetch_data()
if data:
    try:
        df = pd.DataFrame(data)

        # Display data
        st.subheader("Data")
        st.write(df)

        # Display Bar Chart
        st.subheader("Bar Chart")
        selected_column = st.selectbox("Select Column for Bar Chart", df.columns)
        if selected_column:
            bar_chart = px.bar(df, x=selected_column, title=f'{selected_column} Distribution')
            st.plotly_chart(bar_chart)

        # Display Pie Chart
        st.subheader("Pie Chart")
        selected_pie_column = st.selectbox("Select Column for Pie Chart", df.columns)
        if selected_pie_column:
            pie_chart = px.pie(df, names=selected_pie_column, title=f'{selected_pie_column} Distribution')
            st.plotly_chart(pie_chart)
    except ValueError as e:
        st.error(f"Error processing data: {e}")
        st.write(data)
else:
    st.warning("No data available to display.")
