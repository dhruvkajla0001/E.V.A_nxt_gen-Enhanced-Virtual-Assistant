# server/app/api/auth_routes.py

from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from server.app.models.user_model import UserCreate
from server.app.services.auth_service import register_user, authenticate_user
from server.app.utils.security import create_access_token

router = APIRouter()


@router.post("/register")
async def register(user: UserCreate):
    result = await register_user(user)
    if result["status"] == "fail":
        raise HTTPException(status_code=400, detail=result["message"])
    return result


@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user["email"]})
    return {"access_token": token, "token_type": "bearer"}
