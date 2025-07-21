# server/app/api/assistant_routes.py
from fastapi import APIRouter, HTTPException, Query
from server.app.services.assistant_loop_service import run_gesture_assistant

router = APIRouter(prefix="/assistant", tags=["Assistant"])

@router.get("/run")
async def assistant_run(query: str = Query(..., description="User message for EVA")):
    try:
        result = run_assistant_with_text(query)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/gesture")
async def assistant_gesture():
    try:
        result = run_gesture_assistant()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Helper wrapper for text input instead of mic
def run_assistant_with_text(text: str):
    from server.app.services.chatbot_services import get_gemini_response
    from server.app.services.text_to_speech_service import speak_text
    from server.app.services.object_detection_service import detect_objects
    from server.app.services.gesture_detection_service import detect_gesture

    # Trigger keywords
    vision_keywords = ["look around", "describe the scene", "what do you see"]
    gesture_keywords = ["look at my hand", "gesture", "detect hand sign"]

    text_lower = text.lower()

    # Object detection mode
    if any(k in text_lower for k in vision_keywords):
        detection = detect_objects()
        objs = ", ".join(d["object"] for d in detection.get("detections", []))
        prompt = f"I see: {objs}" if objs else "I don't see anything."
        eva_reply = get_gemini_response(prompt)
        speak_text(eva_reply)
        return {"trigger": "vision", "reply": eva_reply, "detected": objs}

    # Gesture detection mode
    elif any(k in text_lower for k in gesture_keywords):
        gesture = detect_gesture().get("gesture", "Unknown")
        eva_reply = f"Your gesture is: {gesture}"
        speak_text(eva_reply)
        return {"trigger": "gesture", "reply": eva_reply, "gesture": gesture}

    # Default → Chat mode
    eva_reply = get_gemini_response(text_lower)
    speak_text(eva_reply)
    return {"trigger": "chat", "reply": eva_reply}
