from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.domain.models.audio_model import Audio
from app.interfaces.schemas.audio_schema import AudioCreate, AudioUpdate
from app.protocols.repository import Repository
from typing import Optional, List


class AudioRepository(Repository):
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get(self, id: int) -> Optional[Audio]:
        result = await self.db.execute(select(Audio).filter_by(id=id))
        return result.scalars().first()

    async def get_all(self) -> List[Audio]:
        result = await self.db.execute(select(Audio))
        return result.scalars().all()

    async def create(self, audio: AudioCreate) -> Audio:
        db_audio = Audio(**audio.dict())
        self.db.add(db_audio)
        await self.db.commit()
        await self.db.refresh(db_audio)
        return db_audio

    async def update(self, id: int, audio: AudioUpdate) -> Audio:
        db_audio = await self.get(id)
        for key, value in audio.dict().items():
            setattr(db_audio, key, value)
        await self.db.commit()
        await self.db.refresh(db_audio)
        return db_audio

    async def delete(self, id: int) -> None:
        db_audio = await self.get(id)
        self.db.delete(db_audio)
        await self.db.commit()
