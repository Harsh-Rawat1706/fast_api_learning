from datetime import datetime
from uuid import UUID
from enum import Enum

from sqlalchemy import DateTime, Enum as SQLEnum, ForeignKey, func, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.models.student import Student
    from app.models.course import Course
    from app.models.attendence import Attendance
    from app.models.mark import Marks
class EnrollmentStatus(str, Enum):
    ACTIVE = "active"
    DROPPED = "dropped"
    COMPLETED = "completed"


class Enrollment(Base):
    __tablename__ = "enrollement"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )

    student_id: Mapped[UUID] = mapped_column(
        ForeignKey("students.id"),
        nullable=False
    )
    
    student: Mapped["Student"] = relationship(
    back_populates="enrollments"
    )
    
    course_id: Mapped[UUID] = mapped_column(
        ForeignKey("courses.id"),
        nullable=False
    )
    
    course: Mapped["Course"] = relationship(
    back_populates="enrollments"
    )
    enrolled_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    status: Mapped[EnrollmentStatus] = mapped_column(
        SQLEnum(EnrollmentStatus, name="enroll_status"),
        nullable=False
    )
    
    attendance_records: Mapped[list["Attendance"]] = relationship(
    back_populates="enrollment"
    )
    
    marks: Mapped[list["Marks"]] = relationship(
    back_populates="enrollment"
    )