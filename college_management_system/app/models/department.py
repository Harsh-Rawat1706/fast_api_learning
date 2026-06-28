from datetime import datetime
from uuid import UUID

from sqlalchemy import String, DateTime, func, text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class Department(Base):
    __tablename__ = "departments"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )

    name: Mapped[str] = mapped_column(
        String(50),
        unique=True
    )

    code: Mapped[str] = mapped_column(
        String(5),
        unique=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )
