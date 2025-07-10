# app.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server.app.api import chat_routes

app = FastAPI(title="EVA 2.0  AI Assistant")

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(chat_routes.router, prefix="/chat")

@app.get("/")
def home():
    return {"msg": "EVA 2.0 backend is running"}
