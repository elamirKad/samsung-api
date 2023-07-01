from datetime import datetime
from domain.services.page_service import PageService
from interfaces.schemas.story_schema import Story, StoryResponse, StoryWithChoices
from domain.repositories.story_repository import StoryRepository
from domain.services.topic_service import TopicService
from typing import List, Optional


class StoryService:
    def __init__(self, story_repo: StoryRepository, topic_service: TopicService, page_service: PageService):
        self.story_repo = story_repo
        self.topic_service = topic_service
        self.page_service = page_service

    def get_stories_by_user(self, user_id: int) -> List[StoryResponse]:
        return self.story_repo.get_all_by_user(user_id=user_id)

    def create_story(self, user_id: int, topic_id: int) -> StoryResponse:
        story = Story(user_id=user_id, topic_id=topic_id, created_at=datetime.now())
        created_story = self.story_repo.create(story)
        prompt = self.topic_service.get(topic_id=topic_id).description
        self.page_service.create_initial_page(prompt, created_story.id)

        return created_story

    def get_story(self, story_id: int) -> Optional[StoryWithChoices]:
        return self.story_repo.get_story_with_related_choices(story_id=story_id)
