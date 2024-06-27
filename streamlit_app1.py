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

            # Age distribution
        st.markdown("### Age Distribution")
        age_dist = px.histogram(df, x='Age', title='Age Distribution')
        st.plotly_chart(age_dist)

        # Gender distribution
        st.markdown("### Gender Distribution")
        gender_dist = px.pie(df, names='Gender', title='Gender Distribution')
        st.plotly_chart(gender_dist)

        # Ethnicity distribution
        st.markdown("### Ethnicity Distribution")
        ethnicity_dist = px.pie(df, names='Ethnicity', title='Ethnicity Distribution')
        st.plotly_chart(ethnicity_dist)

        # Average BMI
        st.markdown("### Average BMI")
        avg_bmi = df['BMI'].mean()
        st.metric(label="Average BMI", value=f"{avg_bmi:.2f}")

        # Smoking habits
        st.markdown("### Smoking Habits")
        smoking_dist = px.pie(df, names='Smoking', title='Smoking Habits')
        st.plotly_chart(smoking_dist)

        # Alcohol consumption
        st.markdown("### Alcohol Consumption")
        alcohol_dist = px.pie(df, names='AlcoholConsumption', title='Alcohol Consumption')
        st.plotly_chart(alcohol_dist)

        # Physical activity levels
        st.markdown("### Physical Activity Levels")
        physical_activity_dist = px.pie(df, names='PhysicalActivity', title='Physical Activity Levels')
        st.plotly_chart(physical_activity_dist)

        # Average Systolic and Diastolic Blood Pressure
        st.markdown("### Blood Pressure Levels")
        avg_systolic_bp = df['SystolicBP'].mean()
        avg_diastolic_bp = df['DiastolicBP'].mean()
        st.metric(label="Average Systolic BP", value=f"{avg_systolic_bp:.2f}")
        st.metric(label="Average Diastolic BP", value=f"{avg_diastolic_bp:.2f}")

        # Cholesterol levels
        st.markdown("### Cholesterol Levels")
        cholesterol_dist = px.histogram(df, x='CholesterolTotal', title='Cholesterol Total Distribution')
        st.plotly_chart(cholesterol_dist)
    except ValueError as e:
        st.error(f"Error processing data: {e}")
        st.write(data)
else:
    st.warning("No data available to display.")
