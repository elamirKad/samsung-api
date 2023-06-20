from story.models import Image
from story.schemas import ImageCreate
from repository import Repository
from sqlalchemy.orm import Session
from typing import Optional


class ImageRepository(Repository):

    def __init__(self, db: Session):
        self.db = db

    def get(self, id: int) -> Optional[Image]:
        return self.db.query(Image).filter(Image.id == id).first()

    def create(self, image: ImageCreate) -> Image:
        db_image = Image(**image.dict())
        self.db.add(db_image)
        self.db.commit()
        self.db.refresh(db_image)
        return db_image
