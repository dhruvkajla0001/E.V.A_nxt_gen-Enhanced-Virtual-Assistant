from server.app.db.mongo import get_collection
from server.app.models.user_model import UserCreate, UserInDB
from passlib.hash import bcrypt
from datetime import datetime

users_col = get_collection("users")

async def register_user(user_data: UserCreate):
    existing = await users_col.find_one({"email": user_data.email})
    if existing:
        return {"status": "fail", "message": "Email already registered."}

    hashed_pw = bcrypt.hash(user_data.password)

    user = UserInDB(
        username=user_data.username,
        email=user_data.email,
        hashed_password=hashed_pw,
    )

    await users_col.insert_one(user.model_dump())
    return {"status": "success", "message": "User registered successfully ✅"}

async def authenticate_user(email: str, password: str):
    user = await users_col.find_one({"email": email})
    if not user or not bcrypt.verify(password, user["hashed_password"]):
        return None
    return user
