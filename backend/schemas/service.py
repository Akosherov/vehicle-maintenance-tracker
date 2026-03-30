from pydantic import BaseModel, EmailStr, Field
from datetime import date
from enum import IntEnum


class Service(BaseModel):
    pass


class ServiceRecord(BaseModel):
    service_date: date
    service_type: str
    notes: str | None = None
    km: int
