from server.app.services.speech_recognition_service import transcribe_from_mic
from server.app.services.chatbot_services import get_gemini_response
from server.app.services.text_to_speech_service import speak_text
from server.app.services.object_detection_service import detect_objects


def run_assistant():
    # Step 1: Transcribe from mic
    voice_input = transcribe_from_mic()

    if "error" in voice_input:
        return {"status": "failed", "message": voice_input["error"]}

    user_message = voice_input["transcription"].lower()

    # Step 2: Check if user wants EVA to use vision
    vision_keywords = ["what do you see", "look around", "do you see anything", "describe the scene"]

    if any(phrase in user_message for phrase in vision_keywords):
        # Step 2a: Run object detection
        detection = detect_objects()

        if detection.get("status") != "success" or detection["detected_count"] == 0:
            prompt = "Describe a scene where nothing is visible through the camera."
        else:
            objects = [d["object"] for d in detection["detections"]]
            joined = ", ".join(objects)
            prompt = f"There are the following objects visible: {joined}. Describe the scene in a calm and intelligent tone, as EVA would."

        # Step 2b: Use Gemini to describe the vision
        eva_reply = get_gemini_response(prompt)
        speak_text(eva_reply)

        return {
            "status": "success",
            "trigger": "vision",
            "user_message": user_message,
            "vision_prompt": prompt,
            "eva_reply": eva_reply,
            "detected_objects": detection["detections"]
        }

    # Step 3: Default — normal LLM conversation
    eva_reply = get_gemini_response(user_message)
    speak_text(eva_reply)

    return {
        "status": "success",
        "trigger": "chat",
        "user_message": user_message,
        "eva_reply": eva_reply
    }
