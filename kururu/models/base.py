from datetime import datetime

from sqlalchemy import DateTime, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.sql import func


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(
        Integer, autoincrement=True, primary_key=True
    )
    create_at: Mapped[datetime] = mapped_column(
        DateTime, default_factory=func.now
    )
    update_at: Mapped[datetime] = mapped_column(
        DateTime, default_factory=func.now, server_onupdate=func.now
    )
