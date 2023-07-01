from domain.models.image_model import Image
from interfaces.schemas.image_schema import ImageCreate
from domain.repositories.image_repository import ImageRepository
from protocols.service import Service


class ImageService(Service):
    def __init__(self, image_repo: ImageRepository):
        self.image_repo = image_repo

    def get(self, id: int) -> Image:
        return self.image_repo.get(id)

    def create(self, image: ImageCreate) -> Image:
        return self.image_repo.create(image)
