from sqlalchemy import Column, ForeignKey, Integer, Text, DateTime
from sqlalchemy.orm import relationship
from infrastructure.database import Base


class Topic(Base):
    __tablename__ = "topics"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    genre_id = Column(Integer, ForeignKey("genres.id"))
    description = Column(Text)
    created_at = Column(DateTime)
