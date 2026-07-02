from datetime import date, datetime
from uuid import UUID

from sqlalchemy import Date, DateTime, ForeignKey, String, func, text
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship

from app.db.database import Base

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.department import Department
    from app.models.user import User
    from app.models.course import Course
    
    

class Teacher(Base):
    __tablename__ = "teachers"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )

    user_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id"),
        unique=True,
        nullable=False
    )
    
    user: Mapped["User"] = relationship(
    back_populates="teacher"
    )
    
    department_id: Mapped[UUID] = mapped_column(
        ForeignKey("departments.id"),
        nullable=False
    )
    
    department: Mapped["Department"] = relationship(
    back_populates="teachers"
    )
    
    employee_code: Mapped[str] = mapped_column(
        String(15),
        unique=True,
        nullable=False
    )

    hire_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True
    )

    phone: Mapped[str | None] = mapped_column(
        String(15),
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )
    
    courses: Mapped[list["Course"]] = relationship(
    back_populates="teacher"
    )