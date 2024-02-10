from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Table, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()


class Note(Base):
    __tablename__ = "note"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    created_date = Column(DateTime, default=func.now())
    finished_date = Column(DateTime)
    done = Column(Boolean, default=False)
    expired = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("user.id"))

    user = relationship("user", back_populates="note")