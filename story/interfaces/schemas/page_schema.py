from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class PageBase(BaseModel):
    image_id: int
    audio_id: int
    content: str
    created_at: Optional[datetime]


class PageCreate(PageBase):
    pass


class Page(PageBase):
    id: int

    class Config:
        orm_mode = True
