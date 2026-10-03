"""
The complete system with Supabase, part 1: the RESTful service.

The service offers actors and countries to its clients as JSON. The data is kept in
a Supabase project (a PostgreSQL database in the cloud), so the service itself is
also a client - a client of Supabase.

    GET  /api/actors                  all the actors
    GET  /api/actors/with-country     all the actors, each with the name and the code of its country
    GET, PUT, DELETE /api/actors/5    one actor;          POST /api/actors adds an actor
    ... and the same operations for /api/countries

Before the first run: create the tables with 04-python-db-supabase/database/create-tables.sql,
and write the address and the secret key of your project into the file .env.

Start it with      python main.py
and then open      http://localhost:8001/docs

The second part of the system, the web application (the folder web-app),
is a client of this service - so start the service first.
"""

import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, RedirectResponse
from postgrest.exceptions import APIError

from routers import actors, countries

app = FastAPI(title="Vanity Fair - REST service")

# CORS: which web pages are allowed to call this service from JavaScript in a browser.
# Browsers refuse such calls from pages of another origin (address) unless the service
# permits them. Our web application calls the service from Python, on the server, where
# this rule does not apply - but a client that runs in a browser would need it.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(actors.router)
app.include_router(countries.router)


@app.exception_handler(APIError)
def supabase_error(request: Request, error: APIError):
    """Supabase did not carry out a request - for example deleting a country that still has actors."""
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
