from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ImageBase(BaseModel):
    path: str
    created_at: Optional[datetime]


class ImageCreate(ImageBase):
    pass


class Image(ImageBase):
    id: int

    class Config:
        orm_mode = True
