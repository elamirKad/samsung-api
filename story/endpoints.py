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


@router.get("/story/{story_id}", response_model=schemas.Story)
def read_story(story_id: str, db: Session = Depends(get_db)):
    story = db.query(models.Story).filter(models.Story.id == story_id).first()
    if story is None:
        raise HTTPException(status_code=404, detail="Story not found")
    return story


@router.get("/all", response_model=List[schemas.Story])
def read_stories(genre_id: Optional[int] = None, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    if genre_id is None:
        stories = db.query(models.Story).offset(skip).limit(limit).all()
    else:
        stories = db.query(models.Story).filter(models.Story.genre_id == genre_id).offset(skip).limit(limit).all()
    return stories
