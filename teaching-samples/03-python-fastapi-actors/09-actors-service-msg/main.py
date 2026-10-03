"""
Step 9: a service for messages.

The application now tells what it is doing. Messages are collected by a second
service, MessagingService, which is used by the pages and by the actor service.
The component AppMessages shows the messages at the bottom of the page.

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

from dependencies import get_actor_service, get_messaging_service
from models.actor import Actor
from services.actor_service import ActorService
from services.messaging_service import MessagingService

BASE_DIR = Path(__file__).parent

app = FastAPI(title="Vanity Fair")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")

# a value placed here can be used in every template (the component AppMessages needs it)
templates.env.globals["messaging_service"] = get_messaging_service()

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
    messaging_service: Annotated[MessagingService, Depends(get_messaging_service)],
    selected: int | None = None,
):
    actors = actor_service.get_actors()

    selected_actor = None
    if selected is not None:
        selected_actor = find_actor(actors, selected)
        if selected_actor is not None:
            messaging_service.add(
                f"Actor selected: {selected_actor.first_name} {selected_actor.last_name}"
            )

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


@app.post("/messages/clear")
def clear_messages(
    request: Request,
    messaging_service: Annotated[MessagingService, Depends(get_messaging_service)],
):
    messaging_service.clear()

    # back to the page on which the button was pressed (the browser sends its address)
    return RedirectResponse(request.headers.get("referer", "/"), status_code=status.HTTP_303_SEE_OTHER)


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
