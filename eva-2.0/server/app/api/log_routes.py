# server/app/api/log_routes.py

from fastapi import APIRouter, Query
from server.app.models.log_model import LogCreate
from server.app.services.log_service import save_log, get_logs

router = APIRouter()


@router.get("/all")
async def fetch_logs(user_id: str = Query(None)):
    logs = await get_logs(user_id)
    return {"status": "success", "count": len(logs), "logs": logs}


@router.post("/add")
async def add_log(log_data: LogCreate):
    result = await save_log(log_data)
    return result
