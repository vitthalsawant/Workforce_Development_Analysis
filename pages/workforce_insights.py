# Importing libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import base64

# Set up the Streamlit page
st.set_page_config(page_title="Workforce Insights", page_icon="📈", layout="wide")

# Title
st.title("Workforce Insights: Engagement & Well-being")

# File upload
uploaded_file = st.file_uploader("Upload your Engagement Survey CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the data
    data = pd.read_csv(uploaded_file)
    
    # Convert Survey Date to datetime with the correct format (DD-MM-YYYY)
    try:
        data['Survey Date'] = pd.to_datetime(data['Survey Date'], format='%d-%m-%Y')
    except ValueError:
        st.error("Error: Please ensure your dates are in DD-MM-YYYY format (e.g., 30-07-2023)")
        st.stop()
    
    # Display summary statistics
    st.subheader("Overview Dashboard")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        avg_engagement = data['Engagement Score'].mean()
        st.metric("Average Engagement Score", f"{avg_engagement:.2f}")
    
    with col2:
        avg_satisfaction = data['Satisfaction Score'].mean()
        st.metric("Average Satisfaction Score", f"{avg_satisfaction:.2f}")
    
    with col3:
        avg_wlb = data['Work-Life Balance Score'].mean()
        st.metric("Average Work-Life Balance Score", f"{avg_wlb:.2f}")

    # Time series analysis
    st.subheader("Trend Analysis")
    
    # Aggregate scores by date
    daily_scores = data.groupby('Survey Date').mean().reset_index()
    
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(x=daily_scores['Survey Date'], y=daily_scores['Engagement Score'],
                             name='Engagement', line=dict(color='blue')))
    fig1.add_trace(go.Scatter(x=daily_scores['Survey Date'], y=daily_scores['Satisfaction Score'],
                             name='Satisfaction', line=dict(color='green')))
    fig1.add_trace(go.Scatter(x=daily_scores['Survey Date'], y=daily_scores['Work-Life Balance Score'],
                             name='Work-Life Balance', line=dict(color='orange')))
    
    fig1.update_layout(title='Score Trends Over Time',
                      xaxis_title='Date',
                      yaxis_title='Score',
                      hovermode='x unified')
    
    st.plotly_chart(fig1, use_container_width=True)

    # Correlation Analysis
    st.subheader("Score Correlations")
    
    fig2 = px.scatter_matrix(data,
                            dimensions=['Engagement Score', 'Satisfaction Score', 'Work-Life Balance Score'],
                            title='Score Correlations Matrix')
    st.plotly_chart(fig2, use_container_width=True)

    # Distribution Analysis
    st.subheader("Score Distributions")
    
    fig3 = go.Figure()
    fig3.add_trace(go.Box(y=data['Engagement Score'], name='Engagement'))
    fig3.add_trace(go.Box(y=data['Satisfaction Score'], name='Satisfaction'))
    fig3.add_trace(go.Box(y=data['Work-Life Balance Score'], name='Work-Life Balance'))
    
    fig3.update_layout(title='Score Distributions',
                      yaxis_title='Score',
                      showlegend=False)
    
    st.plotly_chart(fig3, use_container_width=True)

    # Employee Insights Table
    st.subheader("Employee-Level Insights")
    
    # Calculate average scores per employee
    employee_insights = data.groupby('Employee ID').agg({
        'Engagement Score': 'mean',
        'Satisfaction Score': 'mean',
        'Work-Life Balance Score': 'mean'
    }).round(2)
    
    st.dataframe(employee_insights)

    # Download functionality
    employee_insights.to_csv('employee_insights.csv')
    
    def get_download_link(filename):
        with open(filename, 'rb') as f:
            data = f.read()
        b64 = base64.b64encode(data).decode()
        href = f'data:file/csv;base64,{b64}'
        return href
    
    st.markdown("### Download Employee Insights")
    st.markdown(f'<a href="data:file/csv;base64,{get_download_link("employee_insights.csv")}" download="employee_insights.csv">Download Employee Insights CSV</a>', unsafe_allow_html=True)

else:
    st.info("Please upload a CSV file containing employee engagement survey data")
    st.markdown("""
    The CSV file should include the following columns:
    - Employee ID
    - Survey Date (in DD-MM-YYYY format)
    - Engagement Score
    - Satisfaction Score
    - Work-Life Balance Score
    """) 