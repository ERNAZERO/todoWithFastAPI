from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Table, DateTime, Boolean
from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy.sql import func
from auth.models import User
Base = declarative_base()


class Note(Base):
    __tablename__ = "note"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(64), nullable=False)
    description: Mapped[str] = mapped_column(String(500))
    created_date: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    finished_date: Mapped[datetime] = mapped_column(DateTime)
    done: Mapped[bool] = mapped_column(Boolean, default=False)
    expired: Mapped[bool] = mapped_column(Boolean, default=False)
    user_id: Mapped["User"] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="notes")


    # >> >
    #
    # class Address(Base):
    #     ...
    #     __tablename__ = "address"
    #     id: Mapped[int] = mapped_column(primary_key=True)
    #      email_address: Mapped[str]
    #      user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    #      user: Mapped["User"] = relationship(back_populates="addresses")
    #       def __repr__(self) -> str:
    #     ...
    #     return f"Address(id={self.id!r}, email_address={self.email_address!r})"
