import random
import string

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
from typing import List, Optional
from core.text_generation_core import generate_story
from core.image_generation_core import generate_image
import requests


class PageService(Service):
    def __init__(self, page_repo: PageRepository, image_service: ImageService, audio_service: AudioService, choice_service: ChoiceService):
        self.page_repo = page_repo
        self.image_service = image_service
        self.audio_service = audio_service
        self.choice_service = choice_service

    def get_page(self, page_id: int) -> Page:
        return self.page_repo.get(page_id=page_id)

    def create(self):
        pass

    def create_initial_page(self, prompt: str, story_id: int) -> Page:
        content, choices = generate_story(prompt, story_id)

        random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

        url = 'http://162.19.255.208/audio'
        headers = {'Content-Type': 'application/json'}
        data = {'path': random_string, 'sentences': content}
        response = requests.post(url, headers=headers, json=data)

        audio_path = f"http://162.19.255.208/audio/{response.json()['id']}"
        audio_obj = AudioCreate(path=audio_path)
        audio = self.audio_service.create(audio_obj)

        image_path = generate_image(content)
        image_obj = ImageCreate(path=image_path)
        image = self.image_service.create(image_obj)

        page = self.page_repo.create(PageCreate(content=content), image_id=image.id, audio_id=audio.id, story_id=story_id)

        for choice in choices:
            choice_obj = ChoiceCreate(
                page_id=page.id,
                prompt=choice,
                page_order=1,
                story_id=story_id
            )
            self.choice_service.create_choice(page_id=page.id, choice=choice_obj)

        return page

    def create_page(self, choice_init: Choice) -> Page:
        content, choices = generate_story(choice_init.prompt, choice_init.story_id)

        random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

        url = 'http://162.19.255.208/audio'
        headers = {'Content-Type': 'application/json'}
        data = {'path': random_string, 'sentences': content}
        response = requests.post(url, headers=headers, json=data)

        audio_path = f"http://162.19.255.208/audio/{response.json()['id']}"
        audio_obj = AudioCreate(path=audio_path)
        audio = self.audio_service.create(audio_obj)

        image_path = generate_image(content)
        image_obj = ImageCreate(path=image_path)
        image = self.image_service.create(image_obj)

        page = self.page_repo.create(PageCreate(content=content), image_id=image.id, audio_id=audio.id, story_id=choice_init.story_id)

        for choice in choices:
            choice = ChoiceCreate(
                page_id=page.id,
                prompt=choice,
                page_order=choice_init.page_order + 1,
                story_id=choice_init.story_id
            )
            self.choice_service.create_choice(page_id=page.id, choice=choice)

        return page

    def get_page_with_choices(self, page_id: int) -> Optional[Page]:
        page = self.page_repo.get(page_id=page_id)
        if page:
            page.choices = self.choice_service.get_choices_by_page_id(page_id=page_id)
        return page
