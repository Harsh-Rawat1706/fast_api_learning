from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field

from app.models.user import UserRole


class UserCreate(BaseModel):
    email: str
    password_hash: str = Field(min_length=8)
    role: UserRole


class UserUpdate(BaseModel):
    email: str | None = None
    password_hash: str | None = Field(
        default=None,
        min_length=8,
    )
    role: UserRole | None = None
    is_active: bool | None = None


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    email: str
    role: UserRole
    is_active: bool
    created_at: datetime
    updated_at: datetime
    
class UserSimple(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )

    id: UUID

    email: str

    role: UserRole

    is_active: bool