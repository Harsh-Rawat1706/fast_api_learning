from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.schemas.user import (
    UserCreate,
    UserResponse,
    UserUpdate,
)
from app.services.user_services import (
    create_user,
    delete_user,
    get_user_by_id,
    get_users,
    update_user,
)

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post(
    "",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_user_api(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    return create_user(db, user)


@router.get(
    "",
    response_model=list[UserResponse],
)
def get_users_api(
    db: Session = Depends(get_db),
):
    return get_users(db)


@router.get(
    "/{user_id}",
    response_model=UserResponse,
)
def get_user_by_id_api(
    user_id: UUID,
    db: Session = Depends(get_db),
):
    return get_user_by_id(db, user_id)


@router.patch(
    "/{user_id}",
    response_model=UserResponse,
)
def update_user_api(
    user_id: UUID,
    user: UserUpdate,
    db: Session = Depends(get_db),
):
    return update_user(
        db=db,
        user_id=user_id,
        user=user,
    )


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_user_api(
    user_id: UUID,
    db: Session = Depends(get_db),
):
    delete_user(db, user_id)