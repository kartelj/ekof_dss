"""
A RESTful service for actors and countries, with the data in a SQLite database.

    GET     /api/actors         all the actors
    GET     /api/actors/5       the actor 5
    POST    /api/actors         adds an actor (the data is in the body of the request)
    PUT     /api/actors/5       changes the actor 5
    DELETE  /api/actors/5       deletes the actor 5

and the same for /api/countries.

Start it with      python main.py
and then open      http://localhost:8001/docs      the interactive documentation:
                                                    every operation can be tried there
"""

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, RedirectResponse
from sqlalchemy.exc import IntegrityError

from database import create_database
from routers import actors, countries

app = FastAPI(title="ActorsRestService")

create_database()

app.include_router(actors.router)
app.include_router(countries.router)


@app.exception_handler(IntegrityError)
def change_refused(request: Request, error: IntegrityError):
    """
    The database refuses a change that would break its rules - for example an actor
    of a country that does not exist, or deleting a country that still has actors.
    """
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
