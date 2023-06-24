from typing import List
from domain.models import genre_model
from domain.repositories.genre_repository import GenreRepository


class GenreService:
    def __init__(self, genre_repo: GenreRepository):
        self.genre_repo = genre_repo

    def get_all(self) -> List[genre_model.Genre]:
        return self.genre_repo.get_all()
