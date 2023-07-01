from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

from interfaces.schemas.choice_schema import Choice
from interfaces.schemas.page_schema import Page


class StoryBase(BaseModel):
    topic_id: int


class StoryCreate(StoryBase):
    pass


class Story(StoryBase):
    user_id: int
    created_at: Optional[datetime] = datetime.now()


class StoryResponse(Story):
    id: int

    class Config:
        orm_mode = True


class StoryWithChoices(StoryResponse):
    related_choices: Optional[List[Choice]] = []

    class Config:
        orm_mode = True


class StoryWithChoicesAndPages(StoryWithChoices):
    related_pages: Optional[List[Page]] = []

    class Config:
        orm_mode = True
