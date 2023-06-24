from fastapi import APIRouter, Depends
from typing import List
from domain.services.genre_service import GenreService
from interfaces.schemas.genre_schema import Genre, GenreCreate
from domain.repositories.genre_repository import GenreRepository
from infrastructure.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()


def get_genre_service(db: Session = Depends(get_db)):
    return GenreService(genre_repo=GenreRepository(db))


@router.get("", response_model=List[Genre])
def read_genres(genre_service: GenreService = Depends(get_genre_service)):
    genres = genre_service.get_all()
    return genres


@router.post("", response_model=Genre)
def create_genre(genre: GenreCreate, genre_service: GenreService = Depends(get_genre_service)):
    return genre_service.create(genre)
