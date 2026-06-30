from datetime import date, datetime
from uuid import UUID

from sqlalchemy import (
    Date,
    DateTime,
    ForeignKey,
    Integer,
    String,
    func,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column,relationship

from app.db.database import Base

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.models.department import Department
    from app.models.enrollement import Enrollment
class Student(Base):

    __tablename__ = "students"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        server_default=text("gen_random_uuid()"),
    )

    user_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id"),
        unique=True,
    )

    department_id: Mapped[UUID] = mapped_column(
        ForeignKey("departments.id"),
    )
    
    department: Mapped["Department"] = relationship(
    back_populates="students"
    )
    
    roll_number: Mapped[str] = mapped_column(
        String(15),
        unique=True,
        nullable=False,
    )

    admission_year: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    date_of_birth: Mapped[date] = mapped_column(
        Date,
        nullable=True,
    )

    phone: Mapped[str | None] = mapped_column(
        String(15),
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    
    enrollments: Mapped[list["Enrollment"]] = relationship(
    back_populates="student"
    )