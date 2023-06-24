from domain.models.audio_model import Audio
from interfaces.schemas.audio_schema import AudioCreate
from protocols.repository import Repository
from sqlalchemy.orm import Session
from typing import Optional


class AudioRepository(Repository):

    def __init__(self, db: Session):
        self.db = db

    def get(self, id: int) -> Optional[Audio]:
        return self.db.query(Audio).filter(Audio.id == id).first()

    def create(self, audio: AudioCreate) -> Audio:
        db_audio = Audio(**audio.dict())
        self.db.add(db_audio)
        self.db.commit()
        self.db.refresh(db_audio)
        return db_audio
