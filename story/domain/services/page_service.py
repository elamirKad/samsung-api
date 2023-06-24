from sqlalchemy.orm import Session
from interfaces.schemas.page_schema import PageCreate, Page
from protocols.service import Service
from domain.repositories.page_repository import PageRepository
from audio_service import AudioService
from image_service import ImageService
from faker import Faker

fake = Faker()


class PageService(Service):

    def __init__(self, db: Session):
        self.repository = PageRepository(db)
        self.audio_service = AudioService(db)
        self.image_service = ImageService(db)

    def create(self) -> Page:
        audio = self.audio_service.create()
        image = self.image_service.create()
        content = fake.text()
        page = PageCreate(image_id=image.id, audio_id=audio.id, content=content)
        db_page = Page(**page.dict())
        return self.repository.create(db_page)
