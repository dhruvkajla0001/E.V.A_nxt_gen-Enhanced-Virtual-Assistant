from server.app.services.speech_recognition_service import transcribe_from_mic
from server.app.services.chatbot_services import get_gemini_response
from server.app.services.text_to_speech_service import speak_text

def run_assistant():
    # Step 1: Transcribe from mic
    voice_input = transcribe_from_mic()

    if "error" in voice_input:
        return {"status": "failed", "message": voice_input["error"]}

    user_message = voice_input["transcription"]

    # Step 2: Send to Gemini
    response = get_gemini_response(user_message)

    # Step 3: Speak the response
    speak_text(response)

    return {
        "status": "success",
        "user_message": user_message,
        "eva_reply": response
    }
