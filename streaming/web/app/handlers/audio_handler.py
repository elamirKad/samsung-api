import os
import asyncio
from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from app.domain.repositories.audio_repository import AudioRepository
from app.domain.services.audio_service import AudioService
from app.infrastructure.database import get_db
from app.interfaces.schemas.audio_schema import AudioCreate, Audio

audio_router = APIRouter()


def get_audio_service(db: Session = Depends(get_db)) -> AudioService:
    audio_repository = AudioRepository(db=db)
    return AudioService(audio_repo=audio_repository)


async def stream_audio(directory: str, sentences: int):
    for i in range(1, sentences + 1):
        file_path = f"./{directory}/{i}.mp3"
        tries = 0
        while not os.path.exists(file_path) and tries < 10:
            tries += 1
            await asyncio.sleep(1)
        if os.path.exists(file_path):
            with open(file_path, "rb") as f:
                while chunk := f.read(8192):
                    yield chunk


@audio_router.get("/audio/{id}", response_model=None)
async def audio_endpoint(id: int, audio_service: AudioService = Depends(get_audio_service)):
    audio = await audio_service.get(id)
    return StreamingResponse(stream_audio(audio.path, audio.sentences), media_type="audio/mpeg")


@audio_router.post("/audio", response_model=Audio)
async def create_audio(audio: AudioCreate, audio_service: AudioService = Depends(get_audio_service)):
    new_audio = await audio_service.create(audio)
    return new_audio
