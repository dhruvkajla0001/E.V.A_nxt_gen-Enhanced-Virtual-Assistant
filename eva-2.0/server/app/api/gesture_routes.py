# server/app/api/gesture_routes.py

from fastapi import APIRouter
from server.app.services.assistant_loop_service import run_gesture_assistant

router = APIRouter()

@router.get("/assistant/gesture-action")
def gesture_action():
    return run_gesture_assistant()
