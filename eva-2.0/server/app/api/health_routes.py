from fastapi import APIRouter
from server.app.db.mongo import ping

router = APIRouter()

@router.get("/db-status")
async def db_status():
    connected = await ping()
    return {
        "mongo_connected": connected
    }
