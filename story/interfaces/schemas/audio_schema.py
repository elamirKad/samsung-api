from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class AudioBase(BaseModel):
    path: str
    created_at: Optional[datetime]


class AudioCreate(AudioBase):
    pass


class Audio(AudioBase):
    id: int

    class Config:
        orm_mode = True
