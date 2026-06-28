from uuid import UUID

from datetime import datetime

from sqlalchemy import String, Boolean, DateTime

from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class User(Base):

    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(
        primary_key=True
    )

    email: Mapped[str] = mapped_column(
        String,
        unique=True,
        nullable=False
    )

    password_hash: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    role: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True)
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True)
    )