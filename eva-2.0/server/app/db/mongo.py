"""
MongoDB connection helper for EVA 2.0 backend.
Uses Motor (async MongoDB driver) and values from .env
"""

import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

# Load environment variables
load_dotenv()

# Pull settings from .env (with sensible defaults)
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "eva_db")

# Create a single global AsyncIOMotorClient instance
client: AsyncIOMotorClient = AsyncIOMotorClient(MONGO_URI)

# Reference to the main database
db = client[MONGO_DB_NAME]

# Convenience helpers (optionally import these elsewhere)
def get_collection(name: str):
    """Return a MongoDB collection handle."""
    return db[name]

async def ping() -> bool:
    """Simple ping to verify MongoDB connection."""
    try:
        await client.admin.command("ping")
        return True
    except Exception:
        return False
