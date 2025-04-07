import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set app title
st.title("Overall Workforce Metrics")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    # Read uploaded CSV file
    data = pd.read_csv(uploaded_file)
    st.write("Preview of uploaded data:")
    st.write(data.head())

    # Check if necessary columns exist
    if 'Education' in data.columns and 'Years_of_Experience' in data.columns:
        # Build profiles
        st.subheader("Workforce Profiles")
        
        # Aggregate typical education levels
        education_distribution = data['Education'].value_counts().reset_index()
        education_distribution.columns = ['Education', 'Count']
        st.write("Education Levels Distribution:")
        st.write(education_distribution)

        # Plot education distribution
        fig, ax = plt.subplots()
        sns.barplot(x='Count', y='Education', data=education_distribution, ax=ax)
        plt.xlabel("Number of Applicants")
        plt.ylabel("Education Level")
        plt.title("Education Levels Distribution")
        st.pyplot(fig)

        # Calculate average years of experience
        average_experience = data['Years_of_Experience'].mean()
        st.write(f"Average Years of Experience: **{average_experience:.2f} years**")

        # Generate statistical distributions
        st.subheader("Statistical Distributions")
        fig, ax = plt.subplots()
        sns.histplot(data['Years_of_Experience'], kde=True, ax=ax, bins=10, color="skyblue")
        plt.xlabel("Years of Experience")
        plt.ylabel("Frequency")
        plt.title("Years of Experience Distribution")
        st.pyplot(fig)

        st.write("""
        **Reasoning Behind These Metrics:**
        1. Aggregating applicant profiles (typical education levels and average years of experience) provides a comprehensive understanding of workforce composition.
        2. Statistical distributions help predict future workforce trends, aiding in strategic planning.
        3. Identifying patterns in education and experience can inform hiring decisions and training programs.
        """)
    else:
        st.error("The uploaded file must contain 'Education' and 'Years_of_Experience' columns.")
else:
    st.info("Please upload a CSV file to analyze workforce metrics.")