from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class TopicBase(BaseModel):
    genre_id: int
    description: str


class TopicCreate(TopicBase):
    pass


class Topic(TopicBase):
    id: int
    created_at: Optional[datetime] = datetime.now()

    class Config:
        orm_mode = True
