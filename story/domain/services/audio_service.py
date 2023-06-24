from domain.models.audio_model import Audio
from interfaces.schemas.audio_schema import AudioCreate
from domain.repositories.audio_repository import AudioRepository
from protocols.service import Service


class AudioService(Service):
    def __init__(self, audio_repo: AudioRepository):
        self.audio_repo = audio_repo

    def get(self, id: int) -> Audio:
        return self.audio_repo.get(id)

    def create(self, audio: AudioCreate) -> Audio:
        return self.audio_repo.create(audio)
