from fastapi import APIRouter
from server.app.services.assistant_loop_service import run_assistant

router = APIRouter()

@router.get("/run")
def assistant_run():
    return run_assistant()
