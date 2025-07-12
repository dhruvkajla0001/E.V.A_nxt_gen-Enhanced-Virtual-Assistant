from server.app.db.mongo import get_collection
from server.app.models.log_model import LogCreate, LogInDB
from datetime import datetime

logs_col = get_collection("logs")


# Save a log to MongoDB
async def save_log(log_data: LogCreate):
    log = LogInDB(**log_data.dict())
    await logs_col.insert_one(log.model_dump())
    return {"status": "success", "log_id": log.id}


# Get all logs (optionally filter by user_id)
async def get_logs(user_id: str = None):
    query = {"user_id": user_id} if user_id else {}
    cursor = logs_col.find(query).sort("timestamp", -1)
    return [doc async for doc in cursor]
