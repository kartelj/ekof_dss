"""
Step 2: displaying data.

The home page shows a title and the name of an actor. The part of the page that
shows the actor is a component: a piece of a template that is written once, in a
file of its own (templates/components/actors.html), and used wherever it is needed.

Start it with      python main.py
and then open      http://localhost:8000
"""

from pathlib import Path

import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

BASE_DIR = Path(__file__).parent

app = FastAPI(title="Vanity Fair")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")

title = "Vanity Fair"

actor = "Robert De Niro"


@app.get("/")
def index(request: Request):
    # the values that the template needs are passed to it in a dictionary
    return templates.TemplateResponse(request, "index.html", {"title": title, "actor": actor})


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
