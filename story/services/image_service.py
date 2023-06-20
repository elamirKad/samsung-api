from sqlalchemy.orm import Session
from story.schemas import ImageCreate, Image
from story.repositories.image_repository import ImageRepository
from service import Service
from faker import Faker

fake = Faker()


class ImageService(Service):

    def __init__(self, db: Session):
        self.repository = ImageRepository(db)

    def create(self) -> Image:
        image = ImageCreate(path=fake.file_path())
        db_image = Image(**image.dict())
        return self.repository.create(db_image)
