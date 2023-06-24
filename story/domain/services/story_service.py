from domain.models.story_model import Story
from domain.repositories.story_repository import StoryRepository
from typing import List


class StoryService:
    def __init__(self, story_repo: StoryRepository):
        self.story_repo = story_repo

    def get_stories_by_user(self, user_id: int) -> List[Story]:
        return self.story_repo.get_all_by_user(user_id=user_id)

    def create_story(self, user_id: int, topic_id: int) -> Story:
        story = Story(user_id=user_id, topic_id=topic_id)
        return self.story_repo.create(story)
