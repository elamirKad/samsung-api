from domain.models.choice_model import Choice
from interfaces.schemas.choice_schema import ChoiceCreate
from domain.repositories.choice_repository import ChoiceRepository
from domain.repositories.image_repository import ImageRepository
from domain.services.image_service import ImageService
from interfaces.schemas.image_schema import ImageCreate
from protocols.service import Service


class ChoiceService(Service):
    def __init__(self, choice_repo: ChoiceRepository, image_repo: ImageRepository):
        self.choice_repo = choice_repo
        self.image_service = ImageService(image_repo)

    def create(self, choice: ChoiceCreate) -> Choice:
        # TODO: implement image generation
        image = ImageCreate(path='default.png')
        created_image = self.image_service.create(image)

        choice.dict().update({"image_id": created_image.id})
        created_choice = self.choice_repo.create(choice)

        return created_choice

    def create_choice(self, page_id: int, choice: ChoiceCreate) -> Choice:
        # TODO: implement image generation
        image = ImageCreate(path='default.png')
        created_image = self.image_service.create(image)

        choice.dict().update({"image_id": created_image.id})
        created_choice = self.choice_repo.create_choice(page_id, choice)

        return created_choice
