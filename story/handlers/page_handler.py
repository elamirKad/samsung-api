from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from domain.repositories.audio_repository import AudioRepository
from domain.repositories.image_repository import ImageRepository
from domain.services.audio_service import AudioService
from domain.services.image_service import ImageService
from interfaces.schemas.page_schema import Page
from domain.services.page_service import PageService
from domain.repositories.page_repository import PageRepository
from domain.services.choice_service import ChoiceService
from domain.repositories.choice_repository import ChoiceRepository
from infrastructure.database import get_db


router = APIRouter()


def get_page_service(db: Session = Depends(get_db)) -> PageService:
    page_repo = PageRepository(db=db)
    choice_repo = ChoiceRepository(db=db)
    image_repo = ImageRepository(db=db)
    audio_repo = AudioRepository(db=db)
    image_service = ImageService(image_repo=image_repo)
    audio_service = AudioService(audio_repo=audio_repo)
    choice_service = ChoiceService(choice_repo=choice_repo, image_repo=image_repo)
    return PageService(page_repo=page_repo, choice_service=choice_service, image_service=image_service, audio_service=audio_service)


@router.get("", response_model=Page)
def get_page(
    page_id: int,
    page_service: PageService = Depends(get_page_service)
):
    page = page_service.get_page_with_choices(page_id=page_id)
    if not page:
        raise HTTPException(status_code=404, detail="Page not found")
    return page
