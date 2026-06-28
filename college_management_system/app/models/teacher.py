from datetime import date, datetime
from uuid import UUID

from sqlalchemy import Date, DateTime, ForeignKey, String, func, text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class Teacher(Base):
    __tablename__ = "teachers"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )

    user_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id"),
        unique=True
    )

    department_id: Mapped[UUID] = mapped_column(
        ForeignKey("departments.id")
    )

    employee_code: Mapped[str] = mapped_column(
        String(15),
        unique=True,
        nullable=False
    )

    hire_date: Mapped[date | None] = mapped_column(
        Date
    )

    phone: Mapped[str | None] = mapped_column(
        String(15)
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )