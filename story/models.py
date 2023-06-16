from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text, text, UniqueConstraint, Table
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from database import Base


class Genre(Base):
    __tablename__ = "genre"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)


class Topic(Base):
    __tablename__ = "topic"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    genre_id = Column(Integer, ForeignKey("genre.id"))
    description = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    genre = relationship("Genre")


class Story(Base):
    __tablename__ = "story"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    user_id = Column(Integer)
    genre_id = Column(Integer, ForeignKey("genre.id"))
    topic_id = Column(Integer, ForeignKey("topic.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    genre = relationship("Genre")
    topic = relationship("Topic")


class StoryChoice(Base):
    __tablename__ = "story_choice"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    story_id = Column(UUID(as_uuid=True), ForeignKey("story.id"))
    image_id = Column(UUID(as_uuid=True), ForeignKey("image.id"))
    page = Column(Integer)
    prompt = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    story = relationship("Story")
    image = relationship("Image")


class ChoiceResult(Base):
    __tablename__ = "choice_result"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    story_id = Column(UUID(as_uuid=True), ForeignKey("story.id"))
    choice_id = Column(UUID(as_uuid=True), ForeignKey("story_choice.id"))
    image_id = Column(UUID(as_uuid=True), ForeignKey("image.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    story = relationship("Story")
    story_choice = relationship("StoryChoice")
    image = relationship("Image")


class ResultSentence(Base):
    __tablename__ = "result_sentence"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    result_id = Column(UUID(as_uuid=True), ForeignKey("choice_result.id"))
    audio_id = Column(UUID(as_uuid=True), ForeignKey("audio.id"))
    content = Column(Text)

    choice_result = relationship("ChoiceResult")
    audio = relationship("Audio")


class Audio(Base):
    __tablename__ = "audio"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    path = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Image(Base):
    __tablename__ = "image"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    path = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
