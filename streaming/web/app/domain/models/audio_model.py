from sqlalchemy import Column, Integer, String, DateTime, Text
from app.infrastructure.database import Base


class Audio(Base):
    __tablename__ = "audios"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    path = Column(String)
    sentences = Column(Text)
    created_at = Column(DateTime)
