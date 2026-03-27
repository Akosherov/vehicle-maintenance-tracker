from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from datetime import date, datetime, timezone

from data.database import Base


class Vehicle(Base):
    __tablename__ = "vehicles"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    vin: Mapped[str] = mapped_column(unique=True)
    license_plate: Mapped[str | None]
    brand: Mapped[str]
    model: Mapped[str]
    year: Mapped[int]
    month: Mapped[int | None]
    color: Mapped[str | None]
    color_code: Mapped[str | None]
    vehicle_type: Mapped[str | None]
    fuel_type: Mapped[str | None]
    engine_code: Mapped[str | None]
    engine_displacement: Mapped[int | None]
    engine_power: Mapped[int | None]
    drivetrain: Mapped[str | None]
    transmission: Mapped[str | None]
    odometer: Mapped[int | None]
    notes: Mapped[str | None]
    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc)
    )
    maintenance_logs: Mapped[list["MaintenanceLog"]] = relationship(back_populates="vehicle")
    reminders: Mapped[list["Reminder"]] = relationship(back_populates="vehicle")


class MaintenanceLog(Base):
    __tablename__ = "maintenancelogs"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    vehicle_id: Mapped[int] = mapped_column(ForeignKey("vehicles.id"), nullable=False)
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
    vehicle_id: Mapped[int] = mapped_column(ForeignKey("vehicles.id"), nullable=False)
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
