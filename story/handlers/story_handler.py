from fastapi import APIRouter, Depends, HTTPException, status, Header
from typing import List, Optional
from sqlalchemy.orm import Session
from domain.repositories.story_repository import StoryRepository
from domain.services.story_service import StoryService
from interfaces.schemas.story_schema import StoryCreate, Story
from infrastructure.database import get_db
from infrastructure.jwt_token import decode_access_token

router = APIRouter()


def get_story_service(db: Session = Depends(get_db)) -> StoryService:
    story_repo = StoryRepository(db=db)
    return StoryService(story_repo=story_repo)


@router.get("", response_model=List[Story])
def get_stories_by_user(
    user_id: int = Depends(decode_access_token),
    story_service: StoryService = Depends(get_story_service),
):
    stories = story_service.get_stories_by_user(user_id=user_id)
    return stories


@router.post("", response_model=Story)
def create_story(
    story: StoryCreate,
    user_id: int = Depends(decode_access_token),
    story_service: StoryService = Depends(get_story_service)
):
    created_story = story_service.create_story(user_id=user_id, topic_id=story.topic_id)
    return created_story
