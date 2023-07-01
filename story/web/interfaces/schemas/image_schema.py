from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ImageBase(BaseModel):
    path: str


class ImageCreate(ImageBase):
    pass


class Image(ImageBase):
    id: int
    created_at: Optional[datetime]

    class Config:
        orm_mode = True
