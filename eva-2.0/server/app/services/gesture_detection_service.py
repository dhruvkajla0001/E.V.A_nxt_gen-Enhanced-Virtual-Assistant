import cv2
import mediapipe as mp
from datetime import datetime
from server.app.services.text_to_speech_service import speak_text
from server.app.services.object_detection_service import detect_objects
from server.app.services.chatbot_services import get_gemini_response

# Initialize MediaPipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# ───────────────────────────────────────────────────────────────
def classify_gesture(landmarks):
    if not landmarks or len(landmarks) < 21:
        return "No hand detected ❌"

    fingers_open = []

    # Thumb (compare x-coordinates for left/right hand)
    if landmarks[4].x < landmarks[3].x:
        fingers_open.append("Thumb")

    # Index, Middle, Ring, Pinky (compare y-coordinates)
    tip_ids = [8, 12, 16, 20]
    pip_ids = [6, 10, 14, 18]

    for tip, pip in zip(tip_ids, pip_ids):
        if landmarks[tip].y < landmarks[pip].y:
            fingers_open.append("Finger")

    # DEBUG PRINT (optional)
    # print("Fingers Open:", fingers_open)

    # Improved mapping
    if len(fingers_open) >= 5:
        return "Open Hand 🖐️"
    elif "Thumb" in fingers_open and len(fingers_open) == 1:
        return "Thumbs Up 👍"
    elif len(fingers_open) == 0:
        return "Fist 👊"
    else:
        return f"Gesture with {len(fingers_open)} finger(s)"

# ───────────────────────────────────────────────────────────────
def detect_gesture():
    cap = cv2.VideoCapture(0)

    with mp_hands.Hands(
        max_num_hands=1,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.7
    ) as hands:
        success, frame = cap.read()
        if not success:
            cap.release()
            return {"status": "error", "message": "Camera not accessible"}

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = hands.process(image)

        gesture_result = "No hand detected"
        action_result = None

        if results.multi_hand_landmarks:
            hand_landmarks = results.multi_hand_landmarks[0]
            gesture_result = classify_gesture(hand_landmarks.landmark)

            # MAP: Gesture to Action
            if gesture_result == "Open Hand 🖐️":
                now = datetime.now().strftime("%I:%M %p")
                action_result = f"Hello, Dhruv! The time is {now}."
                speak_text(action_result)

            elif gesture_result == "Thumbs Up 👍":
                objects = detect_objects()
                if not objects["detections"]:
                    action_result = "I don't see anything interesting right now."
                else:
                    obj_names = ', '.join([d['object'] for d in objects["detections"]])
                    prompt = f"I see: {obj_names}. Describe the scene shortly."
                    action_result = get_gemini_response(prompt)
                speak_text(action_result)

            elif gesture_result == "Fist 👊":
                action_result = "Okay, entering standby mode."
                speak_text(action_result)

            else:
                action_result = "Gesture detected but no mapped action."
                speak_text(action_result)

        cap.release()

        return {
            "status": "success",
            "gesture": gesture_result,
            "action_reply": action_result or "No action triggered."
        }
