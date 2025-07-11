# server/app/api/object_routes.py

from fastapi import APIRouter
from server.app.services.object_detection_service import detect_objects

router = APIRouter()

@router.get("/detect")
def run_detection():
    return detect_objects()
