from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from server.app.api import chat_routes
from server.app.api import voice_routes
from server.app.api import tts_routes
from server.app.api import assistant_routes
from server.app.api import object_routes  # 👈 New object detection route
from server.app.api import gesture_routes


app = FastAPI(
    title="EVA 2.0 – AI Assistant",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registering routes
app.include_router(chat_routes.router, prefix="/chat", tags=["Chat"])
app.include_router(voice_routes.router, prefix="/voice", tags=["Voice"])
app.include_router(tts_routes.router, prefix="/tts", tags=["Text-to-Speech"])
app.include_router(assistant_routes.router, prefix="/assistant", tags=["Assistant"])
app.include_router(object_routes.router, prefix="/object", tags=["Object Detection"])  # 👈 New
app.include_router(gesture_routes.router, prefix="/assistant", tags=["Gesture"])

@app.get("/", tags=["Health"])
def root():
    return {"message": "EVA 2.0 backend is running 🎉"}

@app.get("/health", tags=["Health"])
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
