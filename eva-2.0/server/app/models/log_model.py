# server/app/models/log_model.py

from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import datetime
from uuid import uuid4


class LogCreate(BaseModel):
    user_id: Optional[str] = None  # Will come from frontend or token later
    type: Literal["chat", "object", "gesture"]
    input: str
    output: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class LogInDB(LogCreate):
    id: str = Field(default_factory=lambda: str(uuid4()))


class LogPublic(BaseModel):
    id: str
    type: str
    input: str
    output: str
    timestamp: datetime
