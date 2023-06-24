from domain.models.choice_model import Choice
from interfaces.schemas.choice_schema import ChoiceCreate
from protocols.repository import Repository
from sqlalchemy.orm import Session
from typing import Optional


class ChoiceRepository(Repository):
    def __init__(self, db: Session):
        self.db = db

    def get(self, id: int) -> Optional[Choice]:
        return self.db.query(Choice).filter(Choice.id == id).first()

    def create(self, choice: ChoiceCreate) -> Choice:
        db_choice = Choice(**choice.dict())
        self.db.add(db_choice)
        self.db.commit()
        self.db.refresh(db_choice)
        return db_choice

    def create_choice(self, page_id: int, choice: ChoiceCreate) -> Choice:
        db_choice = Choice(**choice.dict(), page_id=page_id)
        self.db.add(db_choice)
        self.db.commit()
        self.db.refresh(db_choice)
        return db_choice
