from domain.models.genre_model import Genre
from interfaces.schemas.genre_schema import GenreCreate
from protocols.repository import Repository
from typing import Optional
from sqlalchemy.orm import Session


class GenreRepository(Repository):

    def __init__(self, db: Session):
        self.db = db

    def get(self, id: int) -> Optional[Genre]:
        return self.db.query(Genre).filter(Genre.id == id).first()

    def create(self, genre: GenreCreate) -> Genre:
        db_genre = Genre(**genre.dict())
        self.db.add(db_genre)
        self.db.commit()
        self.db.refresh(db_genre)
        return db_genre
