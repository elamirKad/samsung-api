from fastapi import APIRouter, Depends, HTTPException, status
from typing import Optional
from sqlalchemy.orm import Session

from domain.repositories.audio_repository import AudioRepository
from domain.repositories.choice_repository import ChoiceRepository
from domain.repositories.image_repository import ImageRepository
from domain.repositories.page_repository import PageRepository
from domain.services.audio_service import AudioService
from domain.services.choice_service import ChoiceService
from domain.services.image_service import ImageService
from domain.services.page_service import PageService
from interfaces.schemas.choice_schema import ChoiceCreate, Choice
from interfaces.schemas.choice_page_schema import ChoiceWithPage
from interfaces.schemas.page_schema import PageCreate
from infrastructure.database import get_db
from infrastructure.jwt_token import decode_access_token

router = APIRouter()


def get_choice_service(db: Session = Depends(get_db)) -> ChoiceService:
    choice_repo = ChoiceRepository(db=db)
    image_repo = ImageRepository(db=db)
    return ChoiceService(choice_repo=choice_repo, image_repo=image_repo)


def get_page_service(db: Session = Depends(get_db)) -> PageService:
    page_repo = PageRepository(db=db)
    image_repo = ImageRepository(db=db)
    image_service = ImageService(image_repo=image_repo)
    audio_repo = AudioRepository(db=db)
    audio_service = AudioService(audio_repo=audio_repo)
    choice_service = get_choice_service(db=db)
    return PageService(
        page_repo=page_repo,
        image_service=image_service,
        audio_service=audio_service,
        choice_service=choice_service
    )


@router.post("", response_model=Choice)
def create_choice(
    choice_id: int,
    user_id: int = Depends(decode_access_token),
    choice_service: ChoiceService = Depends(get_choice_service),
    page_service: PageService = Depends(get_page_service)
):
    try:
        user_id = int(user_id)
    except ValueError:
        raise HTTPException(status_code=401, detail="Unauthorized")
    choice = choice_service.get_choice(choice_id=choice_id)
    page = PageCreate(content="New page")
    created_page = page_service.create_page(page=page, choice_init=choice)

    updated_choice = choice_service.update_choice_page_id(choice_id=choice_id, page_id=created_page.id)
    return updated_choice


@router.get("", response_model=ChoiceWithPage)
def get_choice(
    choice_id: int,
    choice_service: ChoiceService = Depends(get_choice_service),
    page_service: PageService = Depends(get_page_service)
):
    choice = choice_service.get_choice(choice_id=choice_id)
    if not choice:
        raise HTTPException(status_code=404, detail="Choice not found")
    if choice.page_id:
        page = page_service.get_page(page_id=choice.page_id)
    else:
        page = None
    result = ChoiceWithPage.from_orm(choice)
    result.page = page
    return result
