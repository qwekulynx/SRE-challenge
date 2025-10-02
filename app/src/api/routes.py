from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from typing import List
from pydantic import BaseModel, EmailStr
from src.services.db import put_user, list_users
from src.services.storage import upload_avatar


router = APIRouter()

class UserOut(BaseModel):
    name: str
    email: EmailStr
    avatar_url: str

@router.get("/users", response_model=List[UserOut])
def get_users():
    items = list_users()
    return items

@router.post("/user", response_model=UserOut)
def create_user(name: str = Form(...), email: EmailStr = Form(...), avatar: UploadFile = File(...)):
    # Basic validation
    if avatar.content_type.split("/")[0] != "image":
        raise HTTPException(status_code=400, detail="Avatar must be an image")
    avatar_url = upload_avatar(avatar)
    put_user(name=name, email=email, avatar_url=avatar_url)
    return {"name": name, "email": email, "avatar_url": avatar_url}

