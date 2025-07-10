# server/app/services/chatbot_service.py

import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model once
model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(user_input: str) -> str:
    try:
        response = model.generate_content(user_input)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
