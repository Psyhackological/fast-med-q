from enum import Enum
from sqlmodel import SQLModel, Field
from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from typing import Optional
from uuid import UUID, uuid4


class RoleEnum(str, Enum):
    DOCTOR = "doctor"
    PATIENT = "patient"
    RECEPTIONIST = "receptionist"


class User(SQLAlchemyBaseUserTableUUID, SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    first_name: str = Field(nullable=False)
    last_name: str = Field(nullable=False)
    role: RoleEnum = Field(nullable=False)
