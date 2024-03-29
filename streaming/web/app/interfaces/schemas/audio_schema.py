from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class AudioBase(BaseModel):
    path: str
    sentences: str


class AudioCreate(AudioBase):
    pass


class AudioUpdate(AudioBase):
    pass


class Audio(AudioBase):
    id: int
    created_at: Optional[datetime]

    class Config:
        orm_mode = True


class AudioOutput(Audio):
    amount: int
