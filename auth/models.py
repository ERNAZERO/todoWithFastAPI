from sqlalchemy import Column, Integer, String, ForeignKey, Table, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import List

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    # id = Column(Integer, primary_key=True, index=True)
    # username = Column(String, unique=True, index=True)
    # email = Column(String, unique=True, index=True)
    # password = Column(String)
    # notes = relationship("Note", back_populates="user")

    id: Mapped[int] =mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(40))
    password: Mapped[str] = mapped_column(String(100))
    notes:  Mapped[List["Note"]] = relationship(back_populates="user", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, username={self.username!r}, email={self.email!r})"

# ...     addresses: Mapped[List["Address"]] = relationship(
    # ...         back_populates="user", cascade="all, delete-orphan"
    # ...     )
    # ...
