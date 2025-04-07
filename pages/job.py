import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
if not GOOGLE_API_KEY:
    st.error("API key not found. Please check your .env file.")
    st.stop()
genai.configure(api_key=GOOGLE_API_KEY)

# Set default parameters for the model
generation_config = {
    "temperature": 0.7,
    "top_p": 0.95,
    "top_k": 50,
    "max_output_tokens": 1024,  # Limit to concise and relevant outputs
}

# Initialize Gemini model with configuration
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    generation_config=generation_config
)

# Setting up Streamlit interface
st.title("Skill Prediction Tool")
st.write("Select a job profile to see the skills required and why they are important.")

# Job profiles for dropdown selection
job_profiles = [
    "Data Scientist",
    "Software Developer",
    "Digital Marketer",
    "Product Manager",
    "Cybersecurity Analyst",
]

# Dropdown for job profile selection
selected_profile = st.selectbox("Choose a Job Profile", options=job_profiles)

# Function to generate skills using Gemini
def generate_skills(profile):
    try:
        context = f"You are an expert in workforce analysis. Provide a detailed list of essential skills and explain why these skills are important for the job profile: {profile}."
        response = model.generate_content(context)
        if response.text:
            return response.text
        else:
            return "No response generated."
    except Exception as e:
        return f"Error: {str(e)}"

# Display skills and their importance based on the selected profile
if selected_profile:
    with st.spinner(f"Generating skills and insights for {selected_profile}..."):
        skills_response = generate_skills(selected_profile)
    
    st.subheader(f"Skills Required for {selected_profile}:")
    if skills_response.startswith("Error:"):
        st.error(skills_response)
    else:
        st.write(skills_response)
        st.success("Skills and explanations generated successfully!")