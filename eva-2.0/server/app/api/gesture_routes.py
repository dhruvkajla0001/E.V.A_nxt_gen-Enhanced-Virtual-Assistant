from fastapi import APIRouter
from server.app.services.gesture_detection_service import detect_gesture

router = APIRouter()

@router.get("/gesture")
def get_gesture():
    return detect_gesture()
    