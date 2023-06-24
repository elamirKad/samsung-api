from sqlalchemy.orm import relationship

from domain.models.genre_model import Genre
from domain.models.topic_model import Topic
from domain.models.story_model import Story
from domain.models.page_model import Page
from domain.models.choice_model import Choice
from domain.models.audio_model import Audio
from domain.models.image_model import Image


Genre.topics = relationship("Topic", order_by=Topic.id, back_populates="genre")
Topic.stories = relationship("Story", order_by=Story.id, back_populates="topic")
Story.choices = relationship("Choice", order_by=Choice.id, back_populates="story")
