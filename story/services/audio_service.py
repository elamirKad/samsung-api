from story.schemas import AudioCreate
from story.repositories.repository import Repository
from service import Service
from faker import Faker

fake = Faker()


class AudioService(Service):

    def __init__(self, repository: Repository):
        self.repository = repository

    def create(self) -> AudioCreate:
        audio = AudioCreate(path=fake.file_path())
        return self.repository.create(audio)
