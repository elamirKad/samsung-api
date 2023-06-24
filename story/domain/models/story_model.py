from sqlalchemy import Column, ForeignKey, Integer, DateTime
from sqlalchemy.orm import relationship
from infrastructure.database import Base


class Story(Base):
    __tablename__ = "stories"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer)
    topic_id = Column(Integer, ForeignKey("topics.id"))
    created_at = Column(DateTime)
    choices = relationship("Choice", back_populates="story")
