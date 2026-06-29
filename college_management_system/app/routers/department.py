from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.schemas.department import (
    DepartmentCreate,
    DepartmentResponse,
)
from app.services.department_services import (
    create_department,
    get_departments,
)

router = APIRouter(
    prefix="/departments",
    tags=["Departments"],
)


@router.post(
    "",
    response_model=DepartmentResponse,
    status_code=201,
)
def create_department_api(
    department: DepartmentCreate,
    db: Session = Depends(get_db),
):

    return create_department(
        db,
        department,
    )


@router.get(
    "",
    response_model=list[DepartmentResponse],
)
def get_departments_api(
    db: Session = Depends(get_db),
):

    return get_departments(db)