from typing import List
from domain.models import topic_model
from domain.repositories.topic_repository import TopicRepository
from interfaces.schemas.topic_schema import TopicCreate


class TopicService:
    def __init__(self, topic_repo: TopicRepository):
        self.topic_repo = topic_repo

    def get(self, topic_id: int) -> topic_model.Topic:
        return self.topic_repo.get(id=topic_id)

    def get_all(self) -> List[topic_model.Topic]:
        return self.topic_repo.get_all()

    def get_by_genre(self, genre_id: int) -> List[topic_model.Topic]:
        return self.topic_repo.get_all_by_genre(genre_id=genre_id)

    def create(self, topic: TopicCreate) -> topic_model.Topic:
        return self.topic_repo.create(topic=topic)
