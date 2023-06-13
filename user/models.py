from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from main import Base
from datetime import datetime


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class Code(Base):
    __tablename__ = "codes"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    code = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="codes")
