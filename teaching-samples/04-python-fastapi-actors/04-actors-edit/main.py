"""
Step 4: editing.

Below the details of the actor there is a form. When the form is sent, the function
save() copies the values of its fields into the object, and the page is shown again -
this time with the new values.

Start it with      python main.py
and then open      http://localhost:8000
"""

import datetime
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


@app.post("/actor")
def save(
    first_name: Annotated[str, Form()] = "",
    last_name: Annotated[str, Form()] = "",
    country_code: Annotated[str, Form()] = "",
    date_of_birth: Annotated[datetime.date | None, Form()] = None,
):
    """Every parameter gets the value of the form field that has the same name."""
    actor.first_name = first_name
    actor.last_name = last_name
    actor.country_code = country_code
    actor.date_of_birth = date_of_birth

    return RedirectResponse("/", status_code=status.HTTP_303_SEE_OTHER)


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
