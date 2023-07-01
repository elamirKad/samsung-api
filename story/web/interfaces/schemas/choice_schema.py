from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ChoiceBase(BaseModel):
    story_id: int
    page_id: Optional[int]
    prompt: str
    page_order: int


class ChoiceCreate(ChoiceBase):
    pass


class ChoiceCreateImage(ChoiceBase):
    image_id: int


class Choice(ChoiceCreateImage):
    id: int
    created_at: Optional[datetime]

    class Config:
        orm_mode = True
