import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title of the app
st.title("Education and Experience Insights")

# Upload CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file:
    # Load data
    data = pd.read_csv(uploaded_file)
    st.write("Preview of uploaded data:")
    st.write(data.head())
    
    # Assuming columns are 'Education', 'Years_of_Experience', and 'Job_Title'
    if 'Education' in data.columns and 'Years_of_Experience' in data.columns and 'Job_Title' in data.columns:
        # Correlate Education and Years of Experience
        st.subheader("Correlation between Education and Years of Experience")
        education_experience = data.groupby('Education')['Years_of_Experience'].mean().reset_index()
        st.write(education_experience)

        # Plot correlation
        fig, ax = plt.subplots()
        sns.barplot(x='Education', y='Years_of_Experience', data=education_experience, ax=ax)
        plt.xticks(rotation=45)
        st.pyplot(fig)

        # Analyze trends in qualifications for job titles
        st.subheader("Qualification Trends for Specific Job Titles")
        job_title_education = data.groupby('Job_Title')['Education'].value_counts().unstack().fillna(0)
        st.write(job_title_education)

        # Skill gap identification
        st.subheader("Skill Gap Identification")
        job_title_experience = data.groupby('Job_Title')['Years_of_Experience'].mean().reset_index()
        st.write(job_title_experience)
        
        st.write("**Reasoning behind the insights:**")
        st.write("""
        1. The correlation between education and years of experience helps identify whether higher education translates to more experience or if certain job roles require specific levels of education.
        2. Analyzing qualification trends for job titles reveals which qualifications are most common for specific roles, showing potential gaps where candidates may need additional qualifications.
        3. Skill gap identification via years of experience averages can guide HR teams to tailor training or hiring strategies to address specific job requirements.
        """)
    else:
        st.error("The uploaded file must contain 'Education', 'Years_of_Experience', and 'Job_Title' columns.")
else:
    st.info("Please upload a CSV file to proceed.")