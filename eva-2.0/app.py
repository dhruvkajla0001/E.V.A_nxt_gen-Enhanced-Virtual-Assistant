from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import all route files
from server.app.api import chat_routes
from server.app.api import voice_routes
from server.app.api import tts_routes
from server.app.api import assistant_routes
from server.app.api import object_routes
from server.app.api import gesture_routes
from server.app.api import log_routes  # ✅ New
from server.app.api import health_routes

# Initialize FastAPI
app = FastAPI(
    title="EVA 2.0 – AI Assistant",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes with unique prefixes
app.include_router(chat_routes.router, prefix="/chat", tags=["Chat"])
app.include_router(voice_routes.router, prefix="/voice", tags=["Voice"])
app.include_router(tts_routes.router, prefix="/tts", tags=["Text-to-Speech"])
app.include_router(assistant_routes.router, prefix="/assistant", tags=["Assistant"])
app.include_router(object_routes.router, prefix="/object", tags=["Object Detection"])
app.include_router(gesture_routes.router, prefix="/gesture", tags=["Gesture"])
app.include_router(log_routes.router, prefix="/logs", tags=["Logs"])  # ✅ Added
app.include_router(health_routes.router, tags=["Health"])

# Health Check Endpoints
@app.get("/", tags=["Health"])
def root():
    return {"message": "EVA 2.0 backend is running 🎉"}

@app.get("/health", tags=["Health"])
def health():
    return {"status": "ok"}

# Run app if executed directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
