from domain.models.page_model import Page
from interfaces.schemas.audio_schema import AudioCreate
from interfaces.schemas.choice_schema import ChoiceCreate, Choice
from interfaces.schemas.image_schema import ImageCreate
from interfaces.schemas.page_schema import PageCreate
from domain.repositories.page_repository import PageRepository
from domain.services.image_service import ImageService
from domain.services.audio_service import AudioService
from domain.services.choice_service import ChoiceService
from protocols.service import Service
from typing import List


class PageService(Service):
    def __init__(self, page_repo: PageRepository, image_service: ImageService, audio_service: AudioService, choice_service: ChoiceService):
        self.page_repo = page_repo
        self.image_service = image_service
        self.audio_service = audio_service
        self.choice_service = choice_service

    def get_page(self, page_id: int) -> Page:
        return self.page_repo.get(id=page_id)

    def create(self):
        pass

    def create_page(self, page: PageCreate, choice_init: Choice) -> Page:
        # TODO: implement apis
        image_path = 'default.png'
        audio_path = 'default.mp3'
        image_obj = ImageCreate(path=image_path)
        audio_obj = AudioCreate(path=audio_path)
        image = self.image_service.create(image_obj)
        audio = self.audio_service.create(audio_obj)

        page = self.page_repo.create(page, image_id=image.id, audio_id=audio.id)

        for _ in range(3):
            prompt = 'default'
            choice = ChoiceCreate(
                page_id=page.id,
                prompt=prompt,
                page_order=choice_init.page_order + 1,
                story_id=choice_init.story_id
            )
            self.choice_service.create_choice(page_id=page.id, choice=choice)

        return page
