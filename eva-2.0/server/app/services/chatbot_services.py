# server/app/services/chatbot_service.py

import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Correct model name with full path
model = genai.GenerativeModel("models/gemini-2.0-flash")



def get_gemini_response(user_input: str) -> str:
    try:
        response = model.generate_content(user_input)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
