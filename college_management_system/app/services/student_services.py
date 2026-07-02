from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.student import Student
from app.schemas.student import StudentCreate



def create_student(
    db: Session,
    student: StudentCreate,
):
    try:
        with db.add():
            existing_student = db.execute(
                select(Student).where(
                    Student.roll_number == student.roll_number
                )
            ).scalar_one_or_none()

            if existing_student:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Roll number already exists.",
                )

            new_student = Student(
                user_id=student.user_id,
                department_id=student.department_id,
                roll_number=student.roll_number,
                admission_year=student.admission_year,
                date_of_birth=student.date_of_birth,
                phone=student.phone,
            )

            db.add(new_student)
        db.refresh(new_student)

    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Database constraint violated.",
        )

    return new_student


def get_students(db: Session):
    return db.execute(
        select(Student)
    ).scalars().all()
