from sqlalchemy import func, select
from sqlalchemy.orm import Session

from common.security import hash_password
from common.exceptions import ConflictError, NotFoundError, BusinessRuleViolation
from data.models import User
from schemas.user import UserCreate, UserUpdate


def create_user(db: Session, data: UserCreate) -> User:
    existing = db.scalars(select(User).where((User.email == data.email) | (User.username == data.username))).first()
    if existing:
        raise ConflictError("A user with that email or username already exists")
    user = User(**data.model_dump(exclude={"password"}), hashed_password=hash_password(data.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_users(db: Session) -> list[User]:
    return list(db.scalars(select(User)).all())


def get_by_id(db: Session, user_id: int) -> User:
    user = db.scalars(select(User).where(User.id == user_id)).first()
    if not user:
        raise NotFoundError(f"User with ID {user_id} not found")
    return user


def update_user(db: Session, user_id: int, data: UserUpdate) -> User:
    user = get_by_id(db, user_id)
    if is_last_admin(db, user_id) and data.role is not None and data.role != user.role:
        raise BusinessRuleViolation("Cannot demote the last admin")
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(user, field, value)
    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, user_id: int) -> None:
    user = get_by_id(db, user_id)
    if is_last_admin(db, user_id):
        raise BusinessRuleViolation("Cannot delete the last admin")
    db.delete(user)
    db.commit()


def is_last_admin(db: Session, user_id: int) -> bool:
    admin_count = db.scalars(select(func.count()).where(User.role == 2)).one()
    return admin_count == 1 and get_by_id(db, user_id).role == 2
