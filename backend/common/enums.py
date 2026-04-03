from enum import IntEnum, Enum


class UserRole(IntEnum):
    TECH = 0
    MASTER_TECH = 1
    ADMIN = 2


class VehicleStatus(str, Enum):
    WAITING = "waiting"
    IN_SHOP = "in_shop"
    COMPLETED = "completed"
