from interfaces.schemas.story_schema import Story
from domain.models import story_model
from protocols.repository import Repository
from sqlalchemy.orm import Session
from typing import List, Optional


class StoryRepository(Repository):

    def __init__(self, db: Session):
        self.db = db

    def get(self, id: int) -> Optional[story_model.Story]:
        return self.db.query(Story).filter(Story.id == id).first()

    def get_all_by_user(self, user_id: int) -> List[story_model.Story]:
        return self.db.query(Story).filter(Story.user_id == user_id).all()

    def create(self, story: Story) -> story_model.Story:
        db_story = story_model.Story(**story.dict())
        self.db.add(db_story)
        self.db.commit()
        self.db.refresh(db_story)
        return db_story

    