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
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

# Initialize Gemini model with configuration
model = genai.GenerativeModel(model_name="gemini-2.0-flash",  # Updated model name
                            generation_config=generation_config)

# Setting up Streamlit interface
st.title("Workforce Chatbot")
st.write("Welcome to your Workforce Chatbot powered by Gemini API!")

# Function to get response from Gemini
def get_gemini_response(question):
    try:
        context = "You are a workforce analysis expert. Please provide insights about: "
        formatted_prompt = f"{context}{question}"
        response = model.generate_content(formatted_prompt)
        return response.text if response.text else "No response generated"
    except Exception as e:
        return f"Error: {str(e)}"

# Input field for user query
user_input = st.text_input("Ask me a question:")

# Handle user input
if user_input:
    with st.spinner("Generating response..."):
        response = get_gemini_response(user_input)
        st.write(response)