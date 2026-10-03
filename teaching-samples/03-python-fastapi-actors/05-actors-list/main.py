"""
Step 5: a list.

The actors are read from the file sample-data/actors.json, and the component shows
all of them as a list. The details and the form still show one actor - the first one.

Start it with      python main.py
and then open      http://localhost:8000
"""

import datetime
import json
from pathlib import Path
from typing import Annotated

import uvicorn
from fastapi import FastAPI, Form, Request, status
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from models.actor import Actor

BASE_DIR = Path(__file__).parent

app = FastAPI(title="Vanity Fair")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")

title = "Vanity Fair"


def load_actors() -> list[Actor]:
    """Reads the file, and makes an object of the class Actor from every actor in it."""
    text = (BASE_DIR / "sample-data" / "actors.json").read_text(encoding="utf-8")

    result = []
    for item in json.loads(text):
        actor = Actor(
            id=item["id"],
            first_name=item["first_name"],
            last_name=item["last_name"],
            country_code=item["country_code"],
            date_of_birth=datetime.date.fromisoformat(item["date_of_birth"]),
        )
        result.append(actor)
    return result


# the file is read once, when the application starts
actors = load_actors()

actor = actors[0]


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse(
        request, "index.html", {"title": title, "actors": actors, "actor": actor}
    )


@app.post("/actor")
def save(
    first_name: Annotated[str, Form()] = "",
    last_name: Annotated[str, Form()] = "",
    country_code: Annotated[str, Form()] = "",
    date_of_birth: Annotated[datetime.date | None, Form()] = None,
):
    actor.first_name = first_name
    actor.last_name = last_name
    actor.country_code = country_code
    actor.date_of_birth = date_of_birth

    return RedirectResponse("/", status_code=status.HTTP_303_SEE_OTHER)


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
