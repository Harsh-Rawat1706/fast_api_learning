from datetime import date, datetime
from enum import Enum
from uuid import UUID

from sqlalchemy import (
    Date,
    DateTime,
    Enum as SQLEnum,
    ForeignKey,
    UniqueConstraint,
    func,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column,relationship

from app.db.database import Base
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.models.enrollement import Enrollment

class AttendanceStatus(str, Enum):
    PRESENT = "present"
    ABSENT = "absent"


class Attendance(Base):
    __tablename__ = "attendence"

    __table_args__ = (
        UniqueConstraint(
            "enrollement_id",
            "attendence_date",
            name="uq_attendance_per_day",
        ),
    )

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        server_default=text("gen_random_uuid()"),
    )

    enrollement_id: Mapped[UUID] = mapped_column(
        ForeignKey("enrollement.id"),
        nullable=False,
    )
    
    enrollment: Mapped["Enrollment"] = relationship(
    back_populates="attendance_records"
    )
    attendence_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    is_present: Mapped[AttendanceStatus] = mapped_column(
        SQLEnum(
            AttendanceStatus,
            name="present",
        ),
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    
    