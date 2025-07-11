from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# ✅ This should exist: server/app/api/chat_routes.py
from server.app.api import chat_routes

app = FastAPI(
    title="EVA 2.0 – AI Assistant",
    version="1.0.0"
)

# Allow requests from all origins (React frontend etc.)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register the chat route
app.include_router(chat_routes.router, prefix="/chat", tags=["Chat"])

# Health check
@app.get("/", tags=["Health"])
def read_root():
    return {"message": "EVA 2.0 backend is running 🎉"}

# Allow direct Python run: `python app.py`
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
