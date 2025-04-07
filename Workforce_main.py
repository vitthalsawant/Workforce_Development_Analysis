# Importing libraries
import streamlit as st
import pandas as pd
import datetime
import plotly.express as px
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import base64

# Set up the Streamlit page
st.set_page_config(page_title="Workforce Development Analysis", page_icon="bar_chart", layout='wide')

# Title
st.title("Workforce Development Analysis")

# Move file upload to main page
uploaded_file = st.file_uploader("Upload your input CSV file", type=["csv"])

# Sidebar for other user inputs (if needed)
st.sidebar.header('User Input Features')

# Rest of the code remains in the main section
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data.head())  # Displaying the first few rows of the dataset

    # Visualizations
    st.subheader('Job Satisfaction Analysis')
    fig1 = px.histogram(data, x='Performance Score')
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader('Overall Organizational Performance')
    fig2 = px.scatter(data, x='Performance Score', y='Current Employee Rating', color='DepartmentType')
    st.plotly_chart(fig2, use_container_width=True)

    # Model Training for Prediction
    # Ensure 'Tenure' column exists or handle accordingly
    if 'Tenure' not in data.columns:
        data['Tenure'] = 0  # Assign a default value or handle it as needed

    X = data[['Performance Score', 'DepartmentType', 'LocationCode', 'Tenure']]
    y = data['Current Employee Rating']
    X = pd.get_dummies(X, drop_first=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor()
    model.fit(X_train, y_train)

    # Making Predictions
    predictions = model.predict(X_test)
    results = pd.DataFrame({'Actual': y_test, 'Predicted': predictions})

    st.subheader('Prediction Results')
    st.dataframe(results)

    # Saving Predictions to CSV
    results.to_csv('predictions.csv', index=False)
    
    # Function to create download link
    def get_binary_file_downloader_html(bin_file, file_label='File'):
        with open(bin_file, 'rb') as f:
            data = f.read()
        bin_str = 'data:application/octet-stream;base64,' + base64.b64encode(data).decode()
        return f'<a href="{bin_str}" download="{bin_file}">{file_label}</a>'

    st.markdown("### Download Predictions CSV")
    st.markdown(get_binary_file_downloader_html('predictions.csv', 'Download CSV'), unsafe_allow_html=True)
else:
    st.write("Please upload a CSV file to proceed")
