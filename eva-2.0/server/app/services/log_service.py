from server.app.db.mongo import get_collection
from server.app.models.log_model import LogCreate, LogInDB
from bson import ObjectId

# Get the MongoDB logs collection
logs_col = get_collection("logs")

# ──────────────────────────────────────────────────────
# Save a log entry to the MongoDB logs collection
# ──────────────────────────────────────────────────────
async def save_log(log_data: LogCreate):
    log = LogInDB(**log_data.dict())
    await logs_col.insert_one(log.model_dump())
    return {"status": "success", "log_id": log.id}

# ──────────────────────────────────────────────────────
# Helper to convert MongoDB ObjectId into string
# ──────────────────────────────────────────────────────
def _clean_doc(doc: dict) -> dict:
    doc["id"] = str(doc.pop("_id"))  # Convert ObjectId to string
    return doc

# ──────────────────────────────────────────────────────
# Get all logs, or logs for a specific user_id
# ──────────────────────────────────────────────────────
async def get_logs(user_id: str = None):
    query = {"user_id": user_id} if user_id else {}
    cursor = logs_col.find(query).sort("timestamp", -1)
    return [_clean_doc(doc) async for doc in cursor]
