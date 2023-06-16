from datetime import datetime
from typing import Optional
from pydantic import BaseModel, UUID4
from uuid import UUID


class GenreBase(BaseModel):
    name: str


class Genre(GenreBase):
    id: int

    class Config:
        orm_mode = True


class TopicBase(BaseModel):
    genre_id: int
    description: str
    created_at: datetime


class Topic(TopicBase):
    id: int

    class Config:
        orm_mode = True


class StoryBase(BaseModel):
    user_id: int
    genre_id: int
    description_id: int
    created_at: datetime


class Story(StoryBase):
    id: UUID

    class Config:
        orm_mode = True


class StoryChoiceBase(BaseModel):
    story_id: UUID
    result_id: UUID
    image_id: UUID
    page: int
    prompt: str
    created_at: datetime


class StoryChoice(StoryChoiceBase):
    id: UUID

    class Config:
        orm_mode = True


class ChoiceResultBase(BaseModel):
    story_id: UUID
    choice_id: UUID
    image_id: UUID
    created_at: datetime


class ChoiceResult(ChoiceResultBase):
    id: UUID

    class Config:
        orm_mode = True


class ResultSentenceBase(BaseModel):
    result_id: UUID
    audio_id: UUID
    content: str


class ResultSentence(ResultSentenceBase):
    id: UUID

    class Config:
        orm_mode = True


class AudioBase(BaseModel):
    path: str
    created_at: datetime


class Audio(AudioBase):
    id: UUID

    class Config:
        orm_mode = True


class ImageBase(BaseModel):
    path: str
    created_at: datetime


class Image(ImageBase):
    id: UUID

    class Config:
        orm_mode = True
