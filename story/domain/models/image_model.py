from sqlalchemy import Column, Integer, String, DateTime
from infrastructure.database import Base


class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    path = Column(String)
    created_at = Column(DateTime)
