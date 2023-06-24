from sqlalchemy.orm import Session
from sqlalchemy import desc
from domain.models.choice_model import Choice
from interfaces.schemas.choice_schema import ChoiceCreate
from typing import List, Optional
from protocols.repository import Repository


class ChoiceRepository(Repository):

    def __init__(self, db: Session):
        self.db = db

    def get(self, id: int) -> Optional[Choice]:
        return self.db.query(Choice).filter(Choice.id == id).first()

    def get_by_story_id(self, story_id: int) -> List[Optional[Choice]]:
        return self.db.query(Choice).filter(Choice.story_id == story_id).order_by(desc(Choice.page_order)).all()

    def create(self, choice: ChoiceCreate) -> Choice:
        db_choice = Choice(**choice.dict())
        self.db.add(db_choice)
        self.db.commit()
        self.db.refresh(db_choice)
        return db_choice
