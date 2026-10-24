"""
Step 8: a service for the data.

The pages should not care where the actors come from. Reading the file is moved
into a service (the folder services), and the functions below receive the service
as a parameter (see dependencies.py).

Start it with      python main.py
and then open      http://localhost:8000
"""

import datetime
from pathlib import Path
from typing import Annotated

import uvicorn
from fastapi import Depends, FastAPI, Form, HTTPException, Request, status
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from dependencies import get_actor_service
from models.actor import Actor
from services.actor_service import ActorService

BASE_DIR = Path(__file__).parent

app = FastAPI(title="Vanity Fair")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")

title = "Vanity Fair"


def find_actor(actors: list[Actor], actor_id: int) -> Actor | None:
    """Returns the actor with the given id, or None if there is no such actor."""
    for actor in actors:
        if actor.id == actor_id:
            return actor
    return None


@app.get("/")
def index(
    request: Request,
    actor_service: Annotated[ActorService, Depends(get_actor_service)],
    selected: int | None = None,
):
    actors = actor_service.get_actors()

    selected_actor = None
    if selected is not None:
        selected_actor = find_actor(actors, selected)

    return templates.TemplateResponse(
        request,
        "index.html",
        {"title": title, "actors": actors, "selected_actor": selected_actor},
    )


@app.post("/actors/{actor_id}")
def save(
    actor_id: int,
    actor_service: Annotated[ActorService, Depends(get_actor_service)],
    first_name: Annotated[str, Form()] = "",
    last_name: Annotated[str, Form()] = "",
    country_code: Annotated[str, Form()] = "",
    date_of_birth: Annotated[datetime.date | None, Form()] = None,
):
    actor = find_actor(actor_service.get_actors(), actor_id)
    if actor is None:
        raise HTTPException(status_code=404, detail="Actor not found")

    actor.first_name = first_name
    actor.last_name = last_name
    actor.country_code = country_code
    actor.date_of_birth = date_of_birth

    return RedirectResponse(f"/?selected={actor.id}", status_code=status.HTTP_303_SEE_OTHER)


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
