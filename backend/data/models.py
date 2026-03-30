from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from datetime import date, datetime, timezone

from data.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    full_name: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    username: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str]
    role: Mapped[int] = mapped_column(default=0)
    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc)
    )


class Client(Base):
    __tablename__ = "clients"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    email: Mapped[str | None] = mapped_column(unique=True)
    phone_number: Mapped[str]
    street_name: Mapped[str | None]
    city: Mapped[str | None]
    country: Mapped[str | None]
    zip_code: Mapped[str | None]
    notes: Mapped[str | None]
    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc)
    )
    vehicles: Mapped[list["Vehicle"]] = relationship(back_populates="owner")


class Vehicle(Base):
    __tablename__ = "vehicles"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    owner_id: Mapped[int] = mapped_column(ForeignKey("clients.id"))
    vin: Mapped[str | None] = mapped_column(unique=True)
    license_plate: Mapped[str | None] = mapped_column(unique=True)
    make: Mapped[str]
    model: Mapped[str]
    odometer_km: Mapped[int | None]
    year: Mapped[int]
    month: Mapped[int | None]
    color: Mapped[str | None]
    color_code: Mapped[str | None]
    vehicle_type: Mapped[str | None]
    fuel_type: Mapped[str | None]
    fuel_tank_size: Mapped[float | None]
    engine_code: Mapped[str | None]
    engine_displacement: Mapped[float | None]
    engine_power: Mapped[int | None]
    engine_oil: Mapped[str | None]
    engine_oil_capacity: Mapped[float | None]
    engine_oil_filter: Mapped[str | None]
    drivetrain: Mapped[str | None]
    transfer_case_oil: Mapped[str | None]
    transfer_case_oil_capacity: Mapped[float | None]
    diff_oil: Mapped[str | None]
    diff_oil_capacity: Mapped[float | None]
    transmission: Mapped[str | None]
    transmission_oil: Mapped[str | None]
    transmission_oil_capacity: Mapped[float | None]
    power_steering_fluid: Mapped[str | None]
    power_steering_fluid_capacity: Mapped[float | None]
    brake_fluid: Mapped[str | None]
    brake_fluid_capacity: Mapped[float | None]
    coolant: Mapped[str | None]
    coolant_capacity: Mapped[float | None]
    is_active: Mapped[bool] = mapped_column(default=True)
    notes: Mapped[str | None]
    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc)
    )
    maintenance_logs: Mapped[list["MaintenanceLog"]] = relationship(back_populates="vehicle")
    reminders: Mapped[list["Reminder"]] = relationship(back_populates="vehicle")
    owner: Mapped["Client"] = relationship(back_populates="vehicles")


class MaintenanceLog(Base):
    __tablename__ = "maintenancelogs"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    vehicle_id: Mapped[int] = mapped_column(ForeignKey("vehicles.id"))
    service_date: Mapped[date]
    service_type: Mapped[str]
    odometer_at_service: Mapped[int]
    parts_cost: Mapped[float] = mapped_column(default=0)
    labor_cost: Mapped[float] = mapped_column(default=0)
    notes: Mapped[str | None]
    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc)
    )
    vehicle: Mapped["Vehicle"] = relationship(back_populates="maintenance_logs")


class Reminder(Base):
    __tablename__ = "reminders"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    vehicle_id: Mapped[int] = mapped_column(ForeignKey("vehicles.id"))
    reminder_type: Mapped[str]
    due_date: Mapped[date | None]
    due_odometer: Mapped[int | None]
    is_completed: Mapped[bool] = mapped_column(default=False)
    notes: Mapped[str | None]
    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc)
    )
    vehicle: Mapped["Vehicle"] = relationship(back_populates="reminders")
