"""
Step 3: the model.

An actor is not just a name any more - it is an object of the class Actor
(models/actor.py), and the component shows the details of that object.

Start it with      python main.py
and then open      http://localhost:8000
"""

import datetime
from pathlib import Path

import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from models.actor import Actor

BASE_DIR = Path(__file__).parent

app = FastAPI(title="Vanity Fair")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")

title = "Vanity Fair"

actor = Actor(
    id=3,
    first_name="Robert",
    last_name="De Niro",
    date_of_birth=datetime.date(1943, 8, 17),
    country_code="US",
)


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse(request, "index.html", {"title": title, "actor": actor})


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
