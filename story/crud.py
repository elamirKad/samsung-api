from sqlalchemy.orm import Session
import models
import schemas


def get_story_by_user_id(db: Session, user_id: int):
    return db.query(models.Story).filter(models.Story.user_id == user_id).first()


def create_story(db: Session, story: schemas.StoryBase):
    db_story = models.Story(**story.dict())
    db.add(db_story)
    db.commit()
    db.refresh(db_story)
    return db_story


def create_choice(db: Session, choice: schemas.StoryChoiceBase):
    db_choice = models.StoryChoice(**choice.dict())
    db.add(db_choice)
    db.commit()
    db.refresh(db_choice)
    return db_choice


def get_choices_by_result_id(db: Session, result_id: str):
    return db.query(models.StoryChoice).filter(models.StoryChoice.result_id == result_id).all()
