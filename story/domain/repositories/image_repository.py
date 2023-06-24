from domain.models.image_model import Image
from interfaces.schemas.image_schema import ImageCreate
from protocols.repository import Repository
from sqlalchemy.orm import Session
from typing import Optional


class ImageRepository(Repository):
    def __init__(self, db: Session):
        self.db = db

    def create(self, image: ImageCreate) -> Image:
        db_image = Image(**image.dict())
        self.db.add(db_image)
        self.db.commit()
        self.db.refresh(db_image)
        return db_image
