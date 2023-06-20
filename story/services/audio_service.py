from sqlalchemy.orm import Session
from repositories.audio_repository import AudioRepository
from story.schemas import AudioCreate, Audio
from service import Service
from faker import Faker

fake = Faker()


class AudioService(Service):

    def __init__(self, db: Session):
        self.repository = AudioRepository(db)

    def create(self) -> Audio:
        audio = AudioCreate(path=fake.file_path())
        db_audio = Audio(**audio.dict())
        return self.repository.create(db_audio)
