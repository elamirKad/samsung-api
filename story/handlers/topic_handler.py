from fastapi import APIRouter, Depends
from typing import List
from domain.services.topic_service import TopicService
from domain.repositories.topic_repository import TopicRepository
from infrastructure.database import get_db
from interfaces.schemas.topic_schema import TopicCreate, Topic
from sqlalchemy.orm import Session

router = APIRouter()


def get_topic_service(db: Session = Depends(get_db)):
    return TopicService(topic_repo=TopicRepository(db))


@router.get("", response_model=List[Topic])
def read_topics(topic_service: TopicService = Depends(get_topic_service)):
    topics = topic_service.get_all()
    return topics


@router.get("/{genre_id}", response_model=List[Topic])
def read_topics_by_genre(genre_id: int, topic_service: TopicService = Depends(get_topic_service)):
    topics = topic_service.get_by_genre(genre_id=genre_id)
    return topics


@router.post("", response_model=Topic)
def create_topic(topic: TopicCreate, topic_service: TopicService = Depends(get_topic_service)):
    return topic_service.create(topic=topic)
