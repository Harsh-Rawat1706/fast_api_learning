from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.schemas.student import (
    StudentCreate,
    StudentUpdate,
    StudentResponse
)
from app.services.student_services import (
    create_student,
    get_students,
)
router = APIRouter(
    prefix="/students",
    tags=["Students"],
)


@router.post(
    "",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_student_api(
    student: StudentCreate,
    db: Session = Depends(get_db),
):
    return create_student(db, student)

@router.get(
    "",
    response_model=list[StudentResponse],
)
def get_students_api(
    db: Session = Depends(get_db),
):
    # Implementation for fetching all students
    return get_students(db)