from pydantic import BaseModel, ConfigDict, Field
from datetime import date


class VehicleBase(BaseModel):
    vin: str | None = Field(None, min_length=11, max_length=17)
    license_plate: str
    make: str = Field(min_length=2, max_length=32)
    model: str = Field(min_length=2, max_length=32)
    odometer_km: int
    year: int = Field(ge=1886, le=2100)
    month: int | None = Field(None, ge=1, le=12)
    body_type: str
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
    fluids: list["VehicleFluidType"]
    dry_weight: int
    wet_weight: int
    service_history: list["ServiceRecord"]
    battery_type: str
    next_service: int
    next_service_date: date
    last_inspection_date: date
    next_inspection_date: date
    notes: str


class VehicleCreate(VehicleBase):
    owner_name: str


class VehicleUpdate(BaseModel):


class VehicleResponse(VehicleBase):

    model_config = ConfigDict(from_attributes=True)


class VehicleFluidType(BaseModel):
    fluid_name: str = Field(min_length=2, max_length=16)     # Gas, Coolant, Brake Fluid, Power Steering Fluid
    fluid_type: str = Field(min_length=2, max_length=16)     # Viscosity or for example DOT 3 etc..
    part_number_oem: str
    part_number_aftermarket: str | None = None
    brand: str
    capacity: int
    replaced_last: date | None = None


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
