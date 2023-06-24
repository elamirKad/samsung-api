from interfaces.schemas.choice_schema import ChoiceCreate, Choice
from domain.repositories.choice_repository import ChoiceRepository
from protocols.service import Service
from sqlalchemy.orm import Session


class ChoiceService(Service):

    def __init__(self, db: Session):
        self.repository = ChoiceRepository(db)

    def get_by_story_id(self, story_id: int):
        return self.repository.get_by_story_id(story_id)

    # TODO: add prompt, page_order, and story_id to ChoiceCreate, also create page
    def create(self, choice: ChoiceCreate) -> Choice:
        return self.repository.create(choice)
