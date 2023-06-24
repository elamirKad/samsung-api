from sqlalchemy import Column, Integer, String, DateTime
from infrastructure.database import Base


class Audio(Base):
    __tablename__ = "audios"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    path = Column(String)
    created_at = Column(DateTime)
