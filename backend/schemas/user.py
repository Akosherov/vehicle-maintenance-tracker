from pydantic import BaseModel, EmailStr, Field, ConfigDict

from common.enums import UserRole


class User(BaseModel):
    full_name: str = Field(min_length=4, max_length=32, pattern=r"^[a-zA-ZÀ-ÿ'\- ]+$")
    email: EmailStr
    username: str = Field(min_length=6, max_length=16, pattern=r"^\w+$")


class UserCreate(User):
    password: str = Field(min_length=4, max_length=32, pattern=r"^\S+$")


class UserUpdate(BaseModel):
    full_name: str | None = Field(None, min_length=4, max_length=32, pattern=r"^[a-zA-ZÀ-ÿ'\- ]+$")
    email: EmailStr | None = None
    password: str | None = Field(None, min_length=4, max_length=32, pattern=r"^\S+$")
    role: UserRole | None = None


class UserResponse(User):
    id: int
    role: UserRole

    model_config = ConfigDict(from_attributes=True)
