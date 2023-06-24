from datetime import datetime
from domain.models import story_model
from interfaces.schemas.story_schema import Story, StoryResponse
from domain.repositories.story_repository import StoryRepository
from typing import List


class StoryService:
    def __init__(self, story_repo: StoryRepository):
        self.story_repo = story_repo

    def get_stories_by_user(self, user_id: int) -> List[story_model.Story]:
        return self.story_repo.get_all_by_user(user_id=user_id)

    def create_story(self, user_id: int, topic_id: int) -> story_model.Story:
        story = Story(user_id=user_id, topic_id=topic_id, created_at=datetime.now())
        return self.story_repo.create(story)
