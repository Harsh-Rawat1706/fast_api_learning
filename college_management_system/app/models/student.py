from datetime import date, datetime
from uuid import UUID

from sqlalchemy import Date, DateTime, ForeignKey, Integer, String, func, text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class Student(Base):
    __tablename__ = "students"

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

    roll_number: Mapped[str] = mapped_column(
        String(15),
        unique=True,
        nullable=False
    )

   