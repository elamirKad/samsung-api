from story.schemas import ImageCreate
from story.repositories.repository import Repository
from service import Service
from faker import Faker

fake = Faker()


class ImageService(Service):

    def __init__(self, repository: Repository):
        self.repository = repository

    def create(self) -> ImageCreate:
        image = ImageCreate(path=fake.file_path())
        return self.repository.create(image)
