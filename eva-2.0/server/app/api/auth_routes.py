from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from server.app.services.auth_service import register_user, authenticate_user
from server.app.utils.security import create_access_token
from server.app.models.user_model import UserCreate

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

@router.post("/register")
async def register(user: UserCreate):
    result = await register_user(user)
    if result["status"] == "fail":
        raise HTTPException(status_code=400, detail=result["message"])
    return result

@router.post("/login")
async def login(login_data: LoginRequest):
    user = await authenticate_user(login_data.email, login_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user["email"]})
    return {"access_token": token, "token_type": "bearer"}
