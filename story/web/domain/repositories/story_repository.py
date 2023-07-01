from domain.models.choice_model import Choice
from domain.models.page_model import Page
from interfaces.schemas.story_schema import Story, StoryCreate, StoryResponse, StoryWithChoices, \
    StoryWithChoicesAndPages
from domain.models import story_model
from protocols.repository import Repository
from sqlalchemy.orm import Session
from typing import List, Optional


class StoryRepository(Repository):

    def __init__(self, db: Session):
        self.db = db

    def get(self, id: int) -> Optional[StoryResponse]:
        story = self.db.query(story_model.Story).filter(story_model.Story.id == id).first()
        if story:
            return StoryResponse.from_orm(story)
        else:
            return None

    def get_all_by_user(self, user_id: int) -> List[story_model.Story]:
        return self.db.query(story_model.Story).filter(story_model.Story.user_id == user_id).all()

    def create(self, story: StoryCreate) -> StoryResponse:
        db_story = story_model.Story(**story.dict())
        self.db.add(db_story)
        self.db.commit()
        self.db.refresh(db_story)
        story_response = StoryResponse(**db_story.__dict__)
        return story_response

    def get_story_with_related_choices_and_pages(self, story_id: int) -> Optional[StoryWithChoicesAndPages]:
        story = self.db.query(story_model.Story).filter(story_model.Story.id == story_id).first()
        if story:
            story.related_choices = self.db.query(Choice).filter(
                Choice.story_id == story_id).all()
            story.related_pages = self.db.query(Page).filter(
                Page.story_id == story_id).all()
            return StoryWithChoicesAndPages.from_orm(story)
        else:
            return None
