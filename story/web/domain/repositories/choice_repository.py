from domain.models.choice_model import Choice
from interfaces.schemas.choice_schema import ChoiceCreate, ChoiceCreateImage
from protocols.repository import Repository
from sqlalchemy.orm import Session
from typing import Optional


class ChoiceRepository(Repository):
    def __init__(self, db: Session):
        self.db = db

    def get(self, id: int) -> Optional[Choice]:
        return self.db.query(Choice).filter(Choice.id == id).first()

    def get_choices_by_page_id(self, page_id: int) -> list[Choice]:
        return self.db.query(Choice).filter(Choice.page_id == page_id).all()

    def create(self, choice: ChoiceCreateImage) -> Choice:
        db_choice = Choice(**choice.dict())
        self.db.add(db_choice)
        self.db.commit()
        self.db.refresh(db_choice)
        return db_choice

    def create_choice(self, page_id: int, choice: ChoiceCreateImage) -> Choice:
        choice.page_id = page_id
        db_choice = Choice(**choice.dict())
        self.db.add(db_choice)
        self.db.commit()
        self.db.refresh(db_choice)
        return db_choice

    def update_choice_page_id(self, choice_id: int, page_id: int) -> Choice:
        db_choice = self.db.query(Choice).filter(Choice.id == choice_id).first()
        db_choice.page_id = page_id
        self.db.commit()
        self.db.refresh(db_choice)
        return db_choice
