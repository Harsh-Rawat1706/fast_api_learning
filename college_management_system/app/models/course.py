from datetime import datetime
from uuid import UUID

from sqlalchemy import DateTime, ForeignKey, Integer, String, func, text
from sqlalchemy.orm import Mapped, mapped_column,relationship

from app.db.database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.teacher import Teacher
    from app.models.department import Department
    from app.models.enrollement import Enrollment
class Course(Base):
    __tablename__ = "courses"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )

    course_code: Mapped[str] = mapped_column(
        String(15),
        unique=True,
        nullable=False
    )

    course_name: Mapped[str] = mapped_column(
        String(15),
        unique=True,
        nullable=False
    )

    semmester: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    department_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("departments.id")
    )
    
    department: Mapped["Department"] = relationship(
    back_populates="courses"
    )

    teacher_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("teachers.id")
    )
    
    teacher: Mapped["Teacher"] = relationship(
    back_populates="courses"
    )
    
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    
    enrollments: Mapped[list["Enrollment"]] = relationship(
    back_populates="course"
    )