from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate


def create_user(
    db: Session,
    user: UserCreate,
):

    try:

        with db.begin():

            existing_user = db.execute(
                select(User).where(
                    User.email == user.email
                )
            ).scalar_one_or_none()

            if existing_user:
                raise HTTPException(
                    status_code=400,
                    detail="Email already exists."
                )

            new_user = User(
                email=user.email,
                password_hash=user.password_hash,
                role=user.role,
            )

            db.add(new_user)

        db.refresh(new_user)

        return new_user

    except IntegrityError:

        raise HTTPException(
            status_code=400,
            detail="Database constraint violated."
        )


def get_users(db: Session):

    return db.execute(
        select(User)
    ).scalars().all()


def get_user_by_id(
    db: Session,
    user_id: UUID,
):
    user = db.execute(
        select(User).where(
            User.id == user_id
        )
    ).scalar_one_or_none()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found.",
        )

    return user


def update_user(
    db: Session,
    user_id: UUID,
    user: UserUpdate,
):
    existing_user = db.execute(
        select(User).where(
            User.id == user_id
        )
    ).scalar_one_or_none()

    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found.",
        )

    if user.email:

        duplicate_email = db.execute(
            select(User).where(
                User.email == user.email,
                User.id != user_id,
            )
        ).scalar_one_or_none()

        if duplicate_email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already exists.",
            )

    update_data = user.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(existing_user, key, value)

    db.commit()

    db.refresh(existing_user)

    return existing_user


def delete_user(
    db: Session,
    user_id: UUID,
):
    user = db.execute(
        select(User).where(
            User.id == user_id
        )
    ).scalar_one_or_none()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found.",
        )

    db.delete(user)
    db.commit()