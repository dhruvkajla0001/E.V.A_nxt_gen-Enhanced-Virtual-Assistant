# server/app/api/tts_routes.py

from fastapi import APIRouter
from pydantic import BaseModel
from server.app.services.text_to_speech_service import speak_text

router = APIRouter()

class TTSRequest(BaseModel):
    text: str

@router.post("/speak")
def text_to_speech(req: TTSRequest):
    return speak_text(req.text)
