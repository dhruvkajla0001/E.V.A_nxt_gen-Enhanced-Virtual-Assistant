# server/app/api/chat_routes.py

from fastapi import APIRouter
from server.app.schemas.chat_schema import ChatRequest, ChatResponse
from server.app.services.chatbot_services import get_gemini_response

router = APIRouter()

@router.post("/ask", response_model=ChatResponse)
def chat_with_gemini(chat_request: ChatRequest):
    reply = get_gemini_response(chat_request.message)
    return ChatResponse(reply=reply)
