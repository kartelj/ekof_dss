"""
A RESTful service for the films of VanityFair02 and their genres, with the data in a SQLite database.
The solution of the assignment of the lecture "RESTful services with FastAPI".

    GET     /api/genres             all the genres
    GET     /api/genres/4           the genre 4
    GET     /api/genres/4/movies    the films of the genre 4
    GET     /api/movies             all the films
    GET     /api/movies/4           the film 4
    POST    /api/movies             adds a film (the data is in the body of the request)
    PUT     /api/movies/4           changes the film 4
    DELETE  /api/movies/4           deletes the film 4

Start it with      python main.py
and then open      http://localhost:8001/docs      the interactive documentation
"""

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, RedirectResponse
from sqlalchemy.exc import IntegrityError

from database import create_database
from routers import genres, movies

app = FastAPI(title="MoviesRestService")

create_database()

app.include_router(genres.router)
app.include_router(movies.router)


@app.exception_handler(IntegrityError)
def change_refused(request: Request, error: IntegrityError):
    """The database refuses a change that would break its rules - for example a film of a genre that does not exist."""
    return JSONResponse(
        status_code=409,
        content={"detail": "The database refused the change, because it would break the integrity of the data"},
    )


@app.get("/", include_in_schema=False)
def index():
    """The home address leads to the documentation of the service."""
    return RedirectResponse("/docs")


if __name__ == "__main__":
    uvicorn.run("main:app", port=8001, reload=True)
