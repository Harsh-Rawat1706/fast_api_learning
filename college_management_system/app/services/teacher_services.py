from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy import or_, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.teacher import Teacher
from app.schemas.teacher import TeacherCreate, TeacherUpdate


def create_teacher(
    db: Session,
    teacher: TeacherCreate,
):
    existing_teacher = db.execute(
        select(Teacher).where(
            or_(
                Teacher.employee_code == teacher.employee_code,
                Teacher.user_id == teacher.user_id,
            )
        )
    ).scalar_one_or_none()

    if existing_teacher:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Teacher already exists.",
        )

    new_teacher = Teacher(
        user_id=teacher.user_id,
        department_id=teacher.department_id,
        employee_code=teacher.employee_code,
        hire_date=teacher.hire_date,
        phone=teacher.phone,
    )

    try:
        db.add(new_teacher)
        db.commit()
        db.refresh(new_teacher)

    except IntegrityError:
        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Database constraint violated.",
        )

    return new_teacher


def get_teachers(db: Session):
    return db.execute(
        select(Teacher)
    ).scalars().all()


def get_teacher_by_id(
    db: Session,
    teacher_id: UUID,
):
    teacher = db.execute(
        select(Teacher).where(
            Teacher.id == teacher_id
        )
    ).scalar_one_or_none()

    if not teacher:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Teacher not found.",
        )

    return teacher.department.name


def update_teacher(
    db: Session,
    teacher_id: UUID,
    teacher: TeacherUpdate,
):
    existing_teacher = db.execute(
        select(Teacher).where(
            Teacher.id == teacher_id
        )
    ).scalar_one_or_none()

    if not existing_teacher:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Teacher not found.",
        )

    if teacher.employee_code:

        duplicate_teacher = db.execute(
            select(Teacher).where(
                Teacher.employee_code == teacher.employee_code,
                Teacher.id != teacher_id,
            )
        ).scalar_one_or_none()

        if duplicate_teacher:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Employee code already exists.",
            )

    update_data = teacher.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(existing_teacher, key, value)

    db.commit()
    db.refresh(existing_teacher)

    return existing_teacher


def delete_teacher(
    db: Session,
    teacher_id: UUID,
):
    teacher = db.execute(
        select(Teacher).where(
            Teacher.id == teacher_id
        )
    ).scalar_one_or_none()

    if not teacher:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Teacher not found.",
        )

    db.delete(teacher)
    db.commit()