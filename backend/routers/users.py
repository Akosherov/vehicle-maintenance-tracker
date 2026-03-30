from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from data.database import get_db
from schemas.user import UserCreate, UserResponse, UserUpdate
from services import user_service


users_router = APIRouter(prefix="/users", tags=["Users"])


@users_router.post("/", response_model=UserResponse, status_code=201)
def create_user(data: UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db, data)


@users_router.get("/", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return user_service.get_users(db)


@users_router.get("/{user_id}", response_model=UserResponse)
def get_by_id(user_id: int, db: Session = Depends(get_db)):
    return user_service.get_by_id(db, user_id)


@users_router.patch("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, data: UserUpdate, db: Session = Depends(get_db)):
    return user_service.update_user(db, user_id, data)


@users_router.delete("/{user_id}", status_code=204)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user_service.delete_user(db, user_id)
