from domain.models.topic_model import Topic
from interfaces.schemas.topic_schema import TopicCreate
from sqlalchemy import desc
from protocols.repository import Repository
from typing import Optional, List
from sqlalchemy.orm import Session


class TopicRepository(Repository):

    def __init__(self, db: Session):
        self.db = db

    def get(self, id: int) -> Optional[Topic]:
        return self.db.query(Topic).filter(Topic.id == id).first()

    def get_all_by_genre(self, genre_id: int) -> List[Topic]:
        return self.db.query(Topic).filter(Topic.genre_id == genre_id).order_by(desc(Topic.created_at)).all()

    def create(self, topic: TopicCreate) -> Topic:
        db_topic = Topic(**topic.dict())
        self.db.add(db_topic)
        self.db.commit()
        self.db.refresh(db_topic)
        return db_topic
