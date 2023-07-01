from fastapi import APIRouter, Depends, HTTPException, status, Header
from typing import List, Optional
from sqlalchemy.orm import Session

from domain.repositories.choice_repository import ChoiceRepository
from domain.repositories.image_repository import ImageRepository
from domain.repositories.story_repository import StoryRepository
from domain.repositories.topic_repository import TopicRepository
from domain.repositories.page_repository import PageRepository
from domain.repositories.audio_repository import AudioRepository
from domain.services.choice_service import ChoiceService
from domain.services.story_service import StoryService
from domain.services.topic_service import TopicService
from domain.services.page_service import PageService
from domain.services.image_service import ImageService
from domain.services.audio_service import AudioService
from interfaces.schemas.story_schema import StoryCreate, Story, StoryResponse, StoryWithChoices
from infrastructure.database import get_db
from infrastructure.jwt_token import decode_access_token

router = APIRouter()


def get_story_service(db: Session = Depends(get_db)) -> StoryService:
    story_repo = StoryRepository(db=db)
    choice_repo = ChoiceRepository(db=db)
    image_repo = ImageRepository(db=db)
    image_service = ImageService(image_repo=image_repo)
    audio_repo = AudioRepository(db=db)
    audio_service = AudioService(audio_repo=audio_repo)
    choice_service = ChoiceService(choice_repo=choice_repo, image_repo=image_repo)
    page_repo = PageRepository(db=db)
    page_service = PageService(page_repo=page_repo, choice_service=choice_service, image_service=image_service, audio_service=audio_service)
    topic_repo = TopicRepository(db=db)
    topic_service = TopicService(topic_repo=topic_repo)
    return StoryService(story_repo=story_repo, page_service=page_service, topic_service=topic_service)


@router.get("", response_model=List[StoryResponse])
def get_stories_by_user(
    user_id: int = Depends(decode_access_token),
    story_service: StoryService = Depends(get_story_service),
):
    stories = story_service.get_stories_by_user(user_id=user_id)
    return stories


@router.post("", response_model=StoryResponse)
def create_story(
    story: StoryCreate,
    user_id: int = Depends(decode_access_token),
    story_service: StoryService = Depends(get_story_service)
):
    created_story = story_service.create_story(user_id=user_id, topic_id=story.topic_id)
    return created_story


@router.get("/{story_id}", response_model=StoryWithChoices)
def get_story(
    story_id: int,
    story_service: StoryService = Depends(get_story_service),
):
    story = story_service.get_story(story_id=story_id)
    if story is None:
        raise HTTPException(status_code=404, detail="Story not found")
    return story
