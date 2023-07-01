from sqlalchemy.orm import Session
from domain.models.page_model import Page
from interfaces.schemas.page_schema import PageCreate
from protocols.repository import Repository
from typing import Optional


class PageRepository(Repository):
    def __init__(self, db: Session):
        self.db = db

    def get(self, page_id: int) -> Optional[Page]:
        return self.db.query(Page).filter(Page.id == page_id).first()

    def create(self, page: PageCreate, image_id: Optional[int] = None, audio_id: Optional[int] = None, story_id: Optional[int] = None) -> Page:
        db_page = Page(image_id=image_id, audio_id=audio_id, story_id=story_id, **page.dict())
        self.db.add(db_page)
        self.db.commit()
        self.db.refresh(db_page)
        return db_page
