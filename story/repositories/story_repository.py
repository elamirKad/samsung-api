from story.models import Story
from repository import Repository
from sqlalchemy.orm import Session
from typing import List, Optional


class StoryRepository(Repository):

    def __init__(self, db: Session):
        self.db = db

    def get(self, id: int) -> Optional[Story]:
        return self.db.query(Story).filter(Story.id == id).first()

    def get_all_by_user(self, user_id: int) -> List[Story]:
        return self.db.query(Story).filter(Story.user_id == user_id).all()

    def create(self, obj: object) -> object:
        pass
    