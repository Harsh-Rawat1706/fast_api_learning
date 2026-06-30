from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class StudentCreate(BaseModel):
    user_id: UUID
    department_id: UUID
    roll_number: str = Field(max_length=15)
    admission_year: int
    date_of_birth: datetime | None = None
    phone: str | None = Field(max_length=15, default=None)
    

class StudentUpdate(BaseModel):
    department_id: UUID | None = None
    roll_number: str | None = Field(max_length=15, default=None)
    admission_year: int | None = None
    date_of_birth: datetime | None = None
    phone: str | None = Field(max_length=15, default=None)
    
class StudentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    user_id: UUID
    department_id: UUID
    roll_number: str
    admission_year: int
    date_of_birth: datetime | None = None
    phone: str | None = None
    created_at: datetime