from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class GenreBase(BaseModel):
    name: str


class GenreCreate(GenreBase):
    pass


class Genre(GenreBase):
    id: int

    class Config:
        orm_mode = True


class TopicBase(BaseModel):
    genre_id: int
    description: str
    created_at: Optional[datetime]


class TopicCreate(TopicBase):
    pass


class Topic(TopicBase):
    id: int

    class Config:
        orm_mode = True


class AudioBase(BaseModel):
    path: str
    created_at: Optional[datetime]


class AudioCreate(AudioBase):
    pass


class Audio(AudioBase):
    id: int

    class Config:
        orm_mode = True


class ImageBase(BaseModel):
    path: str
    created_at: Optional[datetime]


class ImageCreate(ImageBase):
    pass


class Image(ImageBase):
    id: int

    class Config:
        orm_mode = True
