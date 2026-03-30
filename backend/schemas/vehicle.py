from pydantic import BaseModel, EmailStr, Field
from datetime import date
from enum import IntEnum


class VehicleFluidType(BaseModel):
    fluid_name: str = Field(min_length=2, max_length=16)     # Gas, Coolant, Brake Fluid, Power Steering Fluid
    fluid_type: str = Field(min_length=2, max_length=16)     # Viscosity or for example DOT 3 etc..
    part_number_oem: str
    part_number_aftermarket: str | None = None
    brand: str
    capacity: int
    replaced_last: date | None = None


class Vehicle(BaseModel):
    vehicle_id: int
    brand: str = Field(min_length=2, max_length=32)
    model: str = Field(min_length=2, max_length=32)
    vin: str | None = Field(None, min_length=11, max_length=17)
    production_year: int = Field(ge=1886, le=2100)
    production_month: int | None = Field(None, ge=1, le=12)
    color: str
    color_code: str
    engine_code: str
    engine_displacement: int
    engine_power: int
    emission_standard: str
    drivetrain: str
    transmission: str
    wheel_size: str
    tire_size: str
    fluids: list[VehicleFluidType]
    license_plate: str
    body_type: str
    dry_weight: int
    wet_weight: int
    service_history: list["ServiceRecord"]
    odometer: int
    next_service: int
    next_service_date: date
    last_inspection_date: date
    next_inspection_date: date
    battery_type: str
    notes: str


class UserRole(IntEnum):
    ADMIN = 1
    MASTER_TECH = 2
    TECH = 3


class Part(BaseModel):
    id: int
    name: str
    part_number: str
    manufacturer: str
    type: str
    unit: str


class VehiclePartRequirement(BaseModel):
    vehicle_id: int
    part_id: int
    quantity: float
