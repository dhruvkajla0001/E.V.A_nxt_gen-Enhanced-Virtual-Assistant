from fastapi import APIRouter, Query
from server.app.models.log_model import LogCreate
from server.app.services.log_service import save_log, get_logs

router = APIRouter()

@router.post("/add")
async def add_log(log_data: LogCreate):
    return await save_log(log_data)

@router.get("/all")
async def fetch_logs(user_id: str = Query(None)):
    try:
        logs = await get_logs(user_id)
        return {"status": "success", "count": len(logs), "logs": logs}
    except Exception as e:
        return {"status": "error", "message": str(e)}
