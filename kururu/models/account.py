from base import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class Account(Base):
    __tablename__ = 'accounts'
    username: Mapped[str] = mapped_column(String(256), primary_key=True)
    password: Mapped[str] = mapped_column(String(256))
