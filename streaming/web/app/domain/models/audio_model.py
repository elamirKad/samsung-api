from sqlalchemy import Column, Integer, String, DateTime
from app.infrastructure.database import Base


class Audio(Base):
    __tablename__ = "audios"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    path = Column(String)
    sentences = Column(Integer)
    created_at = Column(DateTime)
