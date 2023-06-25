from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from infrastructure.database import Base


class Genre(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
