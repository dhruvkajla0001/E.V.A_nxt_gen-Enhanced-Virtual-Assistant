"""
chatbot_service.py
Gemini‑powered conversational logic for EVA 2.0
"""

import os
from typing import List

import google.generativeai as genai
from dotenv import load_dotenv

# ─────────────────────────────────────────────────────────────────────────────
# Environment & Gemini setup
# ─────────────────────────────────────────────────────────────────────────────
load_dotenv()  # Reads .env at project root

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

PERSONA_SYSTEM_PROMPT = """
You are **EVA**, a futuristic, friendly, and highly capable personal AI assistant.

Persona rules
1. NEVER call yourself a language model, LLM, or mention Google, Gemini, or OpenAI.
2. When asked "Who are you?" or anything similar, reply:  
   **"I am EVA, your personal AI assistant."**
3. Keep replies concise, calm, and helpful. Use first‑person voice ("I").
4. If the user explicitly asks for highly technical details or long explanations, oblige,
   but still follow rule 1.
"""

# You can tweak temperature/top_p for more/less creativity.
MODEL = genai.GenerativeModel(
    model_name="models/gemini-2.0-flash",
    system_instruction=PERSONA_SYSTEM_PROMPT,
)

# ─────────────────────────────────────────────────────────────────────────────
# Helper to build chat history (future‑proofing)
# ─────────────────────────────────────────────────────────────────────────────
def _build_chat_messages(history: List[dict], user_input: str) -> List[dict]:
    """
    Gemini expects a list like:
      [{"role":"user","parts":[{"text": ...}]}]
    This helper keeps the API call clean and lets us add history later.
    """
    messages = history.copy() if history else []
    messages.append({"role": "user", "parts": [{"text": user_input}]})
    return messages


# ─────────────────────────────────────────────────────────────────────────────
# Public function used by the FastAPI route
# ─────────────────────────────────────────────────────────────────────────────
def get_gemini_response(user_input: str, history: List[dict] | None = None) -> str:
    """
    Generate an EVA‑style response to `user_input`.
    `history` is optional and can hold previous turns for multi‑turn context.
    """
    try:
        messages = _build_chat_messages(history or [], user_input)

        response = MODEL.generate_content(
            messages,
            generation_config={
                "temperature": 0.6,
                "top_p": 0.9,
            },
        )
        return response.text.strip()
    except Exception as e:
        # You might want to log errors in production
        return f"❗ EVA error: {str(e)}"
