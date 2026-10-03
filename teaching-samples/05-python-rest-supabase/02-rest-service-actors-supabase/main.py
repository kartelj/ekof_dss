"""
A RESTful service for actors, with the data in a Supabase project (a PostgreSQL database in the cloud).

    GET     /api/actors         all the actors
    GET     /api/actors/5       the actor 5
    POST    /api/actors         adds an actor (the data is in the body of the request)
    PUT     /api/actors/5       changes the actor 5
    DELETE  /api/actors/5       deletes the actor 5

Before the first run: create the tables with 04-python-db-supabase/database/create-tables.sql,
and write the address and the secret key of your project into the file .env.

Start it with      python main.py
and then open      http://localhost:8001/docs
"""

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, RedirectResponse
from postgrest.exceptions import APIError

from routers import actors

app = FastAPI(title="ActorsRestService")

app.include_router(actors.router)


@app.exception_handler(APIError)
def supabase_error(request: Request, error: APIError):
    """Supabase did not carry out a request - for example an actor of a country that does not exist."""
    # the error codes of PostgreSQL that start with 23 mean: the change would break the integrity of the data
    if str(error.code).startswith("23"):
        return JSONResponse(status_code=409, content={"detail": error.message})
    return JSONResponse(status_code=502, content={"detail": f"Supabase: {error.message}"})


@app.get("/", include_in_schema=False)
def index():
    """The home address leads to the documentation of the service."""
    return RedirectResponse("/docs")


if __name__ == "__main__":
    uvicorn.run("main:app", port=8001, reload=True)
