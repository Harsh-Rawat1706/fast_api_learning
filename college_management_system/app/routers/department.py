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
    get_department_by_code,
)

router = APIRouter(
    prefix="/departments",
    tags=["Departments"],
)

# router code for add data in department table 
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

# router code for get all data from department table
@router.get(
    "",
    response_model=list[DepartmentResponse],
)
def get_departments_api(
    db: Session = Depends(get_db),
):

    return get_departments(db)


# router code for get data by id from department table
@router.get(
    "/{department_id}",
    response_model=DepartmentResponse,
)
def get_department_by_code_api(
    department_code: str,
    db: Session = Depends(get_db),
):
    return get_department_by_code(
        db,
        department_code,
    )