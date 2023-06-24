from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel
from interfaces.schemas.choice_schema import Choice


class PageBase(BaseModel):
    content: str


class PageCreate(PageBase):
    pass


class Page(PageBase):
    id: int
    image_id: Optional[int]
    audio_id: Optional[int]
    created_at: Optional[datetime]
    choices: List[Choice] = []

    class Config:
        orm_mode = True
