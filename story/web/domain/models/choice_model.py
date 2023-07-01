from sqlalchemy import Column, ForeignKey, Integer, Text, DateTime
from sqlalchemy.orm import relationship
from infrastructure.database import Base


class Choice(Base):
    __tablename__ = "choices"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    story_id = Column(Integer, ForeignKey("stories.id"))
    page_id = Column(Integer, nullable=True)
    image_id = Column(Integer, ForeignKey("images.id"), nullable=True)
    prompt = Column(Text)
    page_order = Column(Integer)
    created_at = Column(DateTime)
