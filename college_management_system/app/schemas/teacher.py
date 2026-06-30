from datetime import date, datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class TeacherCreate(BaseModel):
    user_id: UUID
    department_id: UUID
    employee_code: str = Field(max_length=15)
    hire_date: date | None = None
    phone: str | None = Field(
        max_length=15,
        default=None,
    )


class TeacherUpdate(BaseModel):
    department_id: UUID | None = None
    employee_code: str | None = Field(
        default=None,
        max_length=15,
    )
    hire_date: date | None = None
    phone: str | None = Field(
        default=None,
        max_length=15,
    )


class TeacherResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: UUID
    user_id: UUID
    department_id: UUID
    employee_code: str
    hire_date: date | None
    phone: str | None
    created_at: datetime