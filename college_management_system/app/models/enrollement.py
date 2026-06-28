from datetime import datetime
from uuid import UUID
from enum import Enum

from sqlalchemy import DateTime, Enum as SQLEnum, ForeignKey, func, text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


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

    course_id: Mapped[UUID] = mapped_column(
        ForeignKey("courses.id"),
        nullable=False
    )

    enrolled_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    status: Mapped[EnrollmentStatus] = mapped_column(
        SQLEnum(EnrollmentStatus, name="enroll_status"),
        nullable=False
    )