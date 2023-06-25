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


class Choice(ChoiceBase):
    id: int
    image_id: Optional[int]
    created_at: Optional[datetime]

    class Config:
        orm_mode = True


class ChoiceWithPage(Choice):
    page: Optional[int]

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True