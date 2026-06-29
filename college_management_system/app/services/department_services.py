from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.department import Department
from app.schemas.department import DepartmentCreate


def create_department(
    db: Session,
    department: DepartmentCreate,
):

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

    db.commit()

    db.refresh(new_department)

    return new_department


def get_departments(db: Session):

    return db.execute(
        select(Department)
    ).scalars().all()