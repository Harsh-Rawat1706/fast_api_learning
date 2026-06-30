from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.schemas.teacher import (
    TeacherCreate,
    TeacherResponse,
    TeacherUpdate,
)
from app.services.teacher_services import (
    create_teacher,
    delete_teacher,
    get_teacher_by_id,
    get_teachers,
    update_teacher,
)

router = APIRouter(
    prefix="/teachers",
    tags=["Teachers"],
)


@router.post(
    "",
    response_model=TeacherResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_teacher_api(
    teacher: TeacherCreate,
    db: Session = Depends(get_db),
):
    return create_teacher(db, teacher)


@router.get(
    "",
    response_model=list[TeacherResponse],
)
def get_teachers_api(
    db: Session = Depends(get_db),
):
    return get_teachers(db)


@router.get(
    "/{teacher_id}",
    response_model=TeacherResponse,
)
def get_teacher_by_id_api(
    teacher_id: UUID,
    db: Session = Depends(get_db),
):
    return get_teacher_by_id(
        db,
        teacher_id,
    )


@router.patch(
    "/{teacher_id}",
    response_model=TeacherResponse,
)
def update_teacher_api(
    teacher_id: UUID,
    teacher: TeacherUpdate,
    db: Session = Depends(get_db),
):
    return update_teacher(
        db,
        teacher_id,
        teacher,
    )


@router.delete(
    "/{teacher_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_teacher_api(
    teacher_id: UUID,
    db: Session = Depends(get_db),
):
    delete_teacher(
        db,
        teacher_id,
    )