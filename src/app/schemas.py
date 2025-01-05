from fastapi_users import schemas
import uuid
from typing import Optional
from enum import Enum


class RoleEnum(str, Enum):
    DOCTOR = "doctor"
    PATIENT = "patient"
    RECEPTIONIST = "receptionist"


class UserRead(schemas.BaseUser[uuid.UUID]):
    first_name: str
    last_name: str
    role: RoleEnum


class UserCreate(schemas.BaseUserCreate):
    first_name: str
    last_name: str
    role: RoleEnum


class UserUpdate(schemas.BaseUserUpdate):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    role: Optional[RoleEnum] = None
