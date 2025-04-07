import streamlit as st

# Set up the Streamlit page
st.set_page_config(
    page_title="Workforce Development Portal",
    page_icon="👥",
    layout="wide"
)

# Main title with custom styling
st.markdown("""
    <h1 style='text-align: center; color: #2e6c80;'>Welcome to Workforce Development Portal</h1>
    """, unsafe_allow_html=True)

# Introduction text
st.markdown("""
    <div style='text-align: center; padding: 20px;'>
        <h3>Empowering Organizations Through Data-Driven Workforce Analytics</h3>
        <p style='font-size: 18px;'>
            Transform your workforce management with our advanced analytics platform. 
            Make informed decisions, optimize performance, and drive organizational success.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Key features in columns
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div style='text-align: center; padding: 20px; background-color: #f0f2f6; border-radius: 10px;'>
            <h4>Performance Analytics</h4>
            <p>Track and analyze employee performance metrics to drive improvement</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div style='text-align: center; padding: 20px; background-color: #f0f2f6; border-radius: 10px;'>
            <h4>Predictive Insights</h4>
            <p>Leverage AI to predict workforce trends and employee satisfaction</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div style='text-align: center; padding: 20px; background-color: #f0f2f6; border-radius: 10px;'>
            <h4>Data Visualization</h4>
            <p>Interactive dashboards for better decision-making</p>
        </div>
    """, unsafe_allow_html=True)

# Analysis Options
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
    <div style='text-align: center;'>
        <h2>Choose Your Analysis</h2>
    </div>
    """, unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    if st.button("Start Workforce Analysis", use_container_width=True):
        st.switch_page("pages/Workforce_main.py")

with col2:
    if st.button("Workforce Insights: Engagement & Well-being", use_container_width=True):
        st.switch_page("pages/workforce_insights.py")

with col1:
    if st.button("Education and Experience Insights", use_container_width=True):
        st.switch_page("pages/educational.py")

with col2:
    if st.button("Workforce Metrics:statistical distributions", use_container_width=True):
        st.switch_page("pages/workfoece_matrix.py")

with col1:
    if st.button("Al-Powered Resume Screening", use_container_width=True):
        st.switch_page("pages/resuma.py")

with col2:
    if st.button("predict the required skills", use_container_width=True):
        st.switch_page("pages/job.py")

with col1:
    if st.button("Workforce Chatbot", use_container_width=True):
        st.switch_page("pages/workforce_analysis_chatbot.py")

# Footer
st.markdown("""
    <div style='text-align: center; padding: 20px; margin-top: 50px; background-color: #f0f2f6;'>
        <p>© 2024 Workforce Development Portal. All rights reserved.</p>
    </div>
    """, unsafe_allow_html=True) 