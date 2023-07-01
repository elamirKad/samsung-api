from app.domain.models.audio_model import Audio
from app.interfaces.schemas.audio_schema import AudioCreate, AudioUpdate
from app.domain.repositories.audio_repository import AudioRepository
from app.protocols.service import Service
from app.core.audio_generation_core import generate
from typing import List, Optional


class AudioService(Service):
    def __init__(self, audio_repo: AudioRepository):
        self.audio_repo = audio_repo

    async def get(self, id: int) -> Optional[Audio]:
        return await self.audio_repo.get(id)

    async def get_all(self) -> List[Audio]:
        return await self.audio_repo.get_all()

    async def create(self, audio: AudioCreate) -> Audio:
        await generate(audio.path, audio.sentences)
        return await self.audio_repo.create(audio)

    async def update(self, id: int, audio: AudioUpdate) -> Audio:
        return await self.audio_repo.update(id, audio)

    async def delete(self, id: int) -> None:
        await self.audio_repo.delete(id)
