from server.app.services.speech_recognition_service import transcribe_from_mic
from server.app.services.chatbot_services import get_gemini_response
from server.app.services.text_to_speech_service import speak_text
from server.app.services.object_detection_service import detect_objects
from server.app.services.gesture_detection_service import detect_gesture


# ──────────────────────────────────────────────────────────────
# Main EVA Assistant Loop
# ──────────────────────────────────────────────────────────────
def run_assistant():
    # Step 1: Transcribe voice
    voice_input = transcribe_from_mic()

    if "error" in voice_input:
        return {"status": "failed", "message": voice_input["error"]}

    user_message = voice_input["transcription"].lower()

    # ──────────────────────────────────────────────────────────────
    # Define Trigger Keywords
    # ──────────────────────────────────────────────────────────────
    vision_keywords = [
        "what do you see", "look around", "do you see anything", "describe the scene"
    ]

    gesture_keywords = [
        "check my gesture", "look at my hand", "analyze gesture",
        "what gesture do you see", "what is my hand doing",
        "detect hand sign", "observe my hand", "interpret my gesture", "track my gesture"
    ]

    # ──────────────────────────────────────────────────────────────
    # Vision Triggered
    # ──────────────────────────────────────────────────────────────
    if any(phrase in user_message for phrase in vision_keywords):
        detection = detect_objects()

        if detection.get("status") != "success" or detection["detected_count"] == 0:
            prompt = "Describe a scene where nothing is visible through the camera."
        else:
            objects = [d["object"] for d in detection["detections"]]
            joined = ", ".join(objects)
            prompt = f"There are the following objects visible: {joined}. Describe the scene in a calm and intelligent tone, as EVA would."

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

    # ──────────────────────────────────────────────────────────────
    # Gesture Triggered
    # ──────────────────────────────────────────────────────────────
    if any(phrase in user_message for phrase in gesture_keywords):
        gesture_result = detect_gesture()
        gesture = gesture_result.get("gesture", "Unknown")
        eva_reply = f"Your gesture looks like: {gesture}"
        speak_text(eva_reply)

        return {
            "status": "success",
            "trigger": "gesture",
            "user_message": user_message,
            "gesture": gesture,
            "eva_reply": eva_reply
        }

    # ──────────────────────────────────────────────────────────────
    # Default → Chat with Gemini
    # ──────────────────────────────────────────────────────────────
    eva_reply = get_gemini_response(user_message)
    speak_text(eva_reply)

    return {
        "status": "success",
        "trigger": "chat",
        "user_message": user_message,
        "eva_reply": eva_reply
    }


# ──────────────────────────────────────────────────────────────
# Direct Gesture Action Loop (via API / button)
# ──────────────────────────────────────────────────────────────
def run_gesture_assistant():
    gesture_data = detect_gesture()

    if gesture_data["status"] != "success":
        return gesture_data

    gesture = gesture_data["gesture"]
    eva_reply = ""

    # ----- Map Gesture → Action -----
    if "Fist" in gesture:
        eva_reply = "Okay, entering standby mode."
    elif "Open Hand" in gesture:
        eva_reply = "Hello Dhruv! How can I help you?"
    elif "Thumbs Up" in gesture:
        eva_reply = "Scanning the environment now."
        detection = detect_objects()
        if detection["detected_count"]:
            objs = ", ".join(d['object'] for d in detection["detections"])
            prompt = f"I see {objs}. Describe the scene briefly."
            eva_reply = get_gemini_response(prompt)
        else:
            eva_reply += " I don't see anything clearly."
    else:
        eva_reply = f"Detected gesture: {gesture}. No action assigned."

    speak_text(eva_reply)

    return {
        "status": "success",
        "trigger": "gesture",
        "gesture": gesture,
        "eva_reply": eva_reply
    }
