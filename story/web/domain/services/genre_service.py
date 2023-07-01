from typing import List
from domain.models import genre_model
from interfaces.schemas.genre_schema import GenreCreate, Genre
from domain.repositories.genre_repository import GenreRepository


class GenreService:
    def __init__(self, genre_repo: GenreRepository):
        self.genre_repo = genre_repo

    def get_all(self) -> List[Genre]:
        return self.genre_repo.get_all()

    def create(self, genre: GenreCreate) -> Genre:
        return self.genre_repo.create(genre)
