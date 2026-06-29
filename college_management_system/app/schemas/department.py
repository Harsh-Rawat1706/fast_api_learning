from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class DepartmentCreate(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=50
    )

    code: str = Field(
        min_length=2,
        max_length=5
    )


class DepartmentUpdate(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=2,
        max_length=50
    )

    code: str | None = Field(
        default=None,
        min_length=2,
        max_length=5
    )


class DepartmentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    name: str
    code: str
    created_at: datetime