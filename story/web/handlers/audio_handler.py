from domain.repositories.audio_repository import AudioRepository
from domain.services.audio_service import AudioService
from interfaces.schemas.audio_schema import AudioCreate, Audio
from infrastructure.database import get_db
from fastapi import APIRouter, Depends, HTTPException, status


router = APIRouter()


def get_audio_service(db = Depends(get_db)) -> AudioService:
    audio_repo = AudioRepository(db=db)
    return AudioService(audio_repo=audio_repo)


@router.get("/{audio_id}", response_model=Audio)
def get_audio(
    audio_id: int,
    audio_service: AudioService = Depends(get_audio_service)
):
    audio = audio_service.get(id=audio_id)
    if not audio:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Audio not found")
    return audio
