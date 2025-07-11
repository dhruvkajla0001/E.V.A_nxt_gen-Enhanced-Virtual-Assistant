# server/app/api/voice_routes.py

from fastapi import APIRouter
from server.app.services.speech_recognition_service import transcribe_from_mic

router = APIRouter()

@router.get("/transcribe")
def transcribe_voice():
    result = transcribe_from_mic()
    return result
