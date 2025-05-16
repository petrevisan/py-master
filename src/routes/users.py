from fastapi import APIRouter
from sqlalchemy.orm import Session
from src.database import session, User
from pydantic import BaseModel

router = APIRouter()

class UserCreate(BaseModel):
  name: str
  email: str
  password: str

@router.get("/users")
async def get_users():
    users = session.query(User).all()
    return users

@router.post("/users/new")
async def create_user(user: UserCreate):
   new_user = User(
      name=user.name,
      email=user.email,
      password=user.password
   )

   session.add(new_user)
   session.commit()
   session.refresh(new_user)

   return {"message": "Usuário criado com sucesso", "user": {
        "id": new_user.id,
        "name": new_user.name,
        "email": new_user.email
    }}
