from sqlalchemy import Column, ForeignKey, Integer, Text, DateTime
from sqlalchemy.orm import relationship
from infrastructure.database import Base


class Page(Base):
    __tablename__ = "pages"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    image_id = Column(Integer, ForeignKey("images.id"), nullable=True)
    audio_id = Column(Integer, ForeignKey("audios.id"), nullable=True)
    content = Column(Text)
    created_at = Column(DateTime)

    choices = relationship("Choice", back_populates="page")
