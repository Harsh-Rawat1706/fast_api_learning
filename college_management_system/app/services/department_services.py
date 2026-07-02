from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.department import Department
from app.schemas.department import DepartmentCreate
from sqlalchemy.exc import IntegrityError


def create_department(
    db: Session,
    department: DepartmentCreate,
):
    try:
        with db.begin():
            existing_department = db.execute(
                select(Department).where(
                    Department.code == department.code
                )
            ).scalar_one_or_none()

            if existing_department:
                raise HTTPException(
                    status_code=400,
                    detail="Department code already exists."
                )

            new_department = Department(
                name=department.name,
                code=department.code,
            )
            db.add(new_department)
        db.refresh(new_department)
    except IntegrityError:
        raise HTTPException(
            status_code=400,
            detail="Database constraint violated."
        )
    return new_department


def get_departments(db: Session):

    return db.execute(
        select(Department)
    ).scalars().all()
    
def get_department_by_code(
    db: Session,
    department_code: str,
):

    department = db.execute(
        select(Department).where(
            Department.code == department_code
        )
    ).scalar_one_or_none()

    if not department:
        raise HTTPException(
            status_code=404,
            detail="Department not found."
        )

    return department
