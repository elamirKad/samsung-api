import string
from datetime import datetime
from random import choice

from domain.models import story_model
from domain.services.choice_service import ChoiceService
from interfaces.schemas.choice_schema import ChoiceCreate
from interfaces.schemas.story_schema import Story, StoryResponse, StoryCreate, StoryWithChoices
from domain.repositories.story_repository import StoryRepository
from typing import List, Optional


class StoryService:
    def __init__(self, story_repo: StoryRepository, choice_service: ChoiceService):
        self.story_repo = story_repo
        self.choice_service = choice_service

    def get_stories_by_user(self, user_id: int) -> List[StoryResponse]:
        return self.story_repo.get_all_by_user(user_id=user_id)

    def create_story(self, user_id: int, topic_id: int) -> StoryResponse:
        story = Story(user_id=user_id, topic_id=topic_id, created_at=datetime.now())
        created_story = self.story_repo.create(story)

        for _ in range(3):
            prompt = self._generate_prompt()
            choice_obj = ChoiceCreate(story_id=created_story.id, prompt=prompt, page_order=1, page_id=None)
            self.choice_service.create(choice=choice_obj)

        return created_story

    def _generate_prompt(self) -> str:
        """Generate a random prompt for a choice."""
        letters = string.ascii_lowercase
        return ''.join(choice(letters) for i in range(10))

    def get_story(self, story_id: int) -> Optional[StoryWithChoices]:
        return self.story_repo.get_story_with_related_choices(story_id=story_id)
