from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routers
from server.app.api import chat_routes
from server.app.api import voice_routes  # 👈 New voice module

# Create app instance
app = FastAPI(
    title="EVA 2.0 – AI Assistant",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Middleware for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(chat_routes.router, prefix="/chat", tags=["Chat"])
app.include_router(voice_routes.router, prefix="/voice", tags=["Voice"])  # 👈 New

# Health & root check
@app.get("/", tags=["Health"])
def root():
    return {"message": "EVA 2.0 backend is running 🎉"}

@app.get("/health", tags=["Health"])
def health():
    return {"status": "ok"}

# Entry point when running with `python app.py`
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
