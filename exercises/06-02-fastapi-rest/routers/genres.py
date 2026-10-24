from fastapi import APIRouter, HTTPException, status
from sqlmodel import select

from database import SessionDep
from models.genre import Genre, GenreData
from models.movie import Movie, MovieData

router = APIRouter(prefix="/api/genres", tags=["genres"])


# GET: api/genres
@router.get("")
def get_genres(session: SessionDep) -> list[GenreData]:
    genres = session.exec(select(Genre)).all()
    return [GenreData.model_validate(genre) for genre in genres]


# GET: api/genres/4
@router.get("/{genre_id}")
def get_genre(genre_id: int, session: SessionDep) -> GenreData:
    genre = session.get(Genre, genre_id)
    if genre is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Genre not found")
    return GenreData.model_validate(genre)


# GET: api/genres/4/movies    (the bonus)
@router.get("/{genre_id}/movies")
def get_genre_movies(genre_id: int, session: SessionDep) -> list[MovieData]:
    """Returns the films of one genre."""
    if session.get(Genre, genre_id) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Genre not found")

    movies = session.exec(select(Movie)).all()
    return [MovieData.model_validate(movie) for movie in movies if movie.genre_id == genre_id]
