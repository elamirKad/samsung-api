from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class StoryBase(BaseModel):
    topic_id: int


class StoryCreate(StoryBase):
    pass


class Story(StoryBase):
    id: int
    user_id: int
    created_at: Optional[datetime] = datetime.now()

    class Config:
        orm_mode = True
