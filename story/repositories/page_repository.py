from story.models import Page
from story.schemas import PageCreate
from repository import Repository
from sqlalchemy.orm import Session
from typing import Optional


class PageRepository(Repository):

    def __init__(self, db: Session):
        self.db = db

    def get(self, id: int) -> Optional[Page]:
        return self.db.query(Page).filter(Page.id == id).first()

    def create(self, page: PageCreate) -> Page:
        db_page = Page(**page.dict())
        self.db.add(db_page)
        self.db.commit()
        self.db.refresh(db_page)
        return db_page
