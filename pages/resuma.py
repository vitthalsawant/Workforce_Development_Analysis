import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader

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
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

# Initialize Gemini model with configuration
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    generation_config=generation_config
)

# Setting up Streamlit interface
st.title("AI-Powered Resume Reader and Suggestion Tool")
st.write("Upload your resume and receive AI-generated feedback for improvement!")

# Function to get response from Gemini
def get_gemini_response(resume_text):
    try:
        context = "You are a professional career coach and resume expert. Please analyze the following resume text: "
        task_details = """
        Focus on:
        1. Formatting and layout recommendations.
        2. Clear and logical structure suggestions.
        3. Emphasizing achievements and key skills.
        4. Industry-specific optimization tips to improve job prospects.
        """
        formatted_prompt = f"{context}{resume_text}\n\n{task_details}"
        response = model.generate_content(formatted_prompt)
        return response.text if response.text else "No response generated."
    except Exception as e:
        return f"Error: {str(e)}"

# Upload PDF resume
uploaded_file = st.file_uploader("Upload a Resume (PDF format)", type=["pdf"])

if uploaded_file:
    # Save uploaded file temporarily
    with st.spinner("Processing your resume..."):
        with open("uploaded_resume.pdf", "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Use PyPDFLoader to extract text from the PDF
        pdf_loader = PyPDFLoader("uploaded_resume.pdf")
        resume_pages = pdf_loader.load()
        resume_text = "\n".join([page.page_content for page in resume_pages])  # Combine all pages' text

    # Display extracted text
    st.subheader("Extracted Resume Content:")
    st.write(resume_text)

    # Generate AI suggestions for resume improvement
    with st.spinner("Generating AI suggestions for your resume..."):
        ai_suggestions = get_gemini_response(resume_text)

    # Display suggestions
    st.subheader("AI Suggestions for Resume Improvement:")
    if ai_suggestions.startswith("Error:"):
        st.error(ai_suggestions)
    else:
        st.write(ai_suggestions)
        st.success("Suggestions generated successfully! Use these recommendations to refine your resume.")
else:
    st.info("Please upload a PDF resume to proceed.")