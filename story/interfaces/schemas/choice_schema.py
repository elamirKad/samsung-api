from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ChoiceBase(BaseModel):
    story_id: int
    prompt: str
    page_order: int


class ChoiceCreate(ChoiceBase):
    page_id: Optional[int] = None
    image_id: Optional[int] = None


class Choice(ChoiceBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
