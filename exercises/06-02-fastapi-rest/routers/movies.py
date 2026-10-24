from fastapi import APIRouter, HTTPException, Response, status
from sqlmodel import select

from database import SessionDep
from models.movie import Movie, MovieData

router = APIRouter(prefix="/api/movies", tags=["movies"])


# GET: api/movies
@router.get("")
def get_movies(session: SessionDep) -> list[MovieData]:
    movies = session.exec(select(Movie)).all()
    return [MovieData.model_validate(movie) for movie in movies]


# GET: api/movies/4
@router.get("/{movie_id}")
def get_movie(movie_id: int, session: SessionDep) -> MovieData:
    movie = session.get(Movie, movie_id)
    if movie is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")
    return MovieData.model_validate(movie)


# PUT: api/movies/4
@router.put("/{movie_id}", status_code=status.HTTP_204_NO_CONTENT)
def put_movie(movie_id: int, data: MovieData, session: SessionDep) -> None:
    if movie_id != data.movie_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The id in the address and the movie_id in the body are different",
        )

    movie = session.get(Movie, movie_id)
    if movie is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")

    movie.title = data.title
    movie.year = data.year
    movie.lasting = data.lasting
    movie.genre_id = data.genre_id
    session.add(movie)
    session.commit()


# POST: api/movies
@router.post("", status_code=status.HTTP_201_CREATED)
def post_movie(data: MovieData, session: SessionDep, response: Response) -> MovieData:
    movie = Movie.model_validate(data)
    movie.movie_id = None  # the key of a new row is always assigned by the DBMS
    session.add(movie)
    session.commit()
    session.refresh(movie)

    response.headers["Location"] = f"/api/movies/{movie.movie_id}"
    return MovieData.model_validate(movie)


# DELETE: api/movies/4
@router.delete("/{movie_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_movie(movie_id: int, session: SessionDep) -> None:
    movie = session.get(Movie, movie_id)
    if movie is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")

    session.delete(movie)
    session.commit()
