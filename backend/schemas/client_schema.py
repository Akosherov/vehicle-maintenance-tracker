from pydantic import BaseModel, EmailStr, Field, ConfigDict


class ClientBase(BaseModel):
    first_name: str = Field(min_length=2, max_length=32)
    last_name: str = Field(min_length=2, max_length=32)
    email: EmailStr
    phone_number: str = Field(min_length=5, max_length=15)
    street_name: str | None = None
    city: str | None = None
    country: str | None = None
    zip_code: str | None = None
    notes: str | None = None


class ClientCreate(ClientBase):
    pass


class ClientUpdate(BaseModel):
    first_name: str | None = Field(None, min_length=2, max_length=32)
    last_name: str | None = Field(None, min_length=2, max_length=32)
    email: EmailStr | None = None
    phone_number: str | None = Field(None, min_length=5, max_length=15)
    street_name: str | None = None
    city: str | None = None
    country: str | None = None
    zip_code: str | None = None
    notes: str | None = None


class ClientResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr | None = None
    phone_number: str | None = None
    notes: str | None = None

    model_config = ConfigDict(from_attributes=True)
