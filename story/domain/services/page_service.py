from domain.models.page_model import Page
from interfaces.schemas.audio_schema import AudioCreate
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

    def create_page(self, page: PageCreate) -> Page:
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
            self.choice_service.create_choice(page_id=page.id, prompt=prompt)

        return page
