from datetime import datetime
import random
from typing import List, Optional
from uuid import uuid4

from fastapi import Depends, HTTPException, APIRouter, status
from sqlalchemy.orm import Session

import crud
import jwt_token
import models
import schemas
from database import get_db

router = APIRouter()


@router.get("/genre", response_model=List[schemas.Genre])
def read_genres(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    genres = db.query(models.Genre).offset(skip).limit(limit).all()
    return genres


@router.get("/topic/{topic_id}", response_model=schemas.Topic)
def read_topic(topic_id: int, db: Session = Depends(get_db)):
    topic = db.query(models.Topic).filter(models.Topic.id == topic_id).first()
    if topic is None:
        raise HTTPException(status_code=404, detail="Topic not found")
    return topic


@router.get("/all", response_model=List[schemas.Topic])
def read_topics(genre_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    topics = db.query(models.Topic).filter(models.Genre.id == genre_id).offset(skip).limit(limit).all()
    return topics


@router.post("/topic", response_model=schemas.Topic)
def create_topic(topic: schemas.TopicBase, db: Session = Depends(get_db)):
    try:
        db_topic = models.Topic(**topic.dict())
        db.add(db_topic)
        db.commit()
        db.refresh(db_topic)
        return db_topic
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
