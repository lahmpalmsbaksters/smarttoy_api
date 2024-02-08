# app/api/endpoints/user.py

from fastapi import APIRouter, Depends
from app.core.use_cases.create_user import CreateUserUseCase
from app.dependencies.database import get_db
from app.core.entities.user import User

router = APIRouter()

@router.post("/users/",)
async def create_user(payload: User, db=Depends(get_db)):
    print(payload.username)
    print(payload.email)
    use_case = CreateUserUseCase()
    user = use_case.execute(username=payload.username, email=payload.email)
    # Save user to the database (not implemented here)
    return user
