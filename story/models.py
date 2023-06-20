from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship
from database import Base


class Genre(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)

    topics = relationship("Topic", back_populates="genre")


class Topic(Base):
    __tablename__ = "topics"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    genre_id = Column(Integer, ForeignKey("genres.id"))
    description = Column(Text)
    created_at = Column(DateTime)

    genre = relationship("Genre", back_populates="topics")
    stories = relationship("Story", back_populates="topic")


class Story(Base):
    __tablename__ = "stories"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer)
    topic_id = Column(Integer, ForeignKey("topics.id"))
    created_at = Column(DateTime)

    topic = relationship("Topic", back_populates="stories")
    choices = relationship("Choice", back_populates="story")


class Page(Base):
    __tablename__ = "pages"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    image_id = Column(Integer, ForeignKey("images.id"), nullable=True)
    audio_id = Column(Integer, ForeignKey("audios.id"), nullable=True)
    content = Column(Text)
    created_at = Column(DateTime)

    choices = relationship("Choice", back_populates="page")


class Choice(Base):
    __tablename__ = "choices"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    story_id = Column(Integer, ForeignKey("stories.id"))
    page_id = Column(Integer, ForeignKey("pages.id"), nullable=True)
    image_id = Column(Integer, ForeignKey("images.id"), nullable=True)
    prompt = Column(Text)
    page_order = Column(Integer)
    created_at = Column(DateTime)

    story = relationship("Story", back_populates="choices")
    page = relationship("Page", back_populates="choices")


class Audio(Base):
    __tablename__ = "audios"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    path = Column(String)
    created_at = Column(DateTime)


class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    path = Column(String)
    created_at = Column(DateTime)
