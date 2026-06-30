from datetime import datetime
from uuid import UUID

from sqlalchemy import (
    DateTime,
    ForeignKey,
    Integer,
    CheckConstraint,
    func,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.models.enrollement import Enrollment

class Marks(Base):
    __tablename__ = "marks"

    __table_args__ = (
        CheckConstraint(
            "marks BETWEEN 0 AND 100",
            name="ck_marks_range",
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
    back_populates="marks"
    )
    marks: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )