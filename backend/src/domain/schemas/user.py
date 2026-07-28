import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


# Base schema containing shared attributes
class UserBase(BaseModel):
    email: EmailStr


# DTO for incoming data (Creation)
class UserCreate(UserBase):
    password: str


# DTO for outgoing data (Response)
class UserResponse(UserBase):
    id: uuid.UUID
    is_active: bool
    created_at: datetime

    # CRITICAL: This tells Pydantic to read the data even if it's an SQLAlchemy ORM model,
    # not just a standard Python dictionary.
    model_config = ConfigDict(from_attributes=True)
