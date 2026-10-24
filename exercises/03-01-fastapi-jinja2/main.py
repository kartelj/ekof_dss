"""
A small film site - the solution of the assignment of the lecture
"Introduction to FastAPI and Jinja2".

Start the application with      python main.py
and then open                   http://localhost:8000
"""

from pathlib import Path
from typing import Annotated

import uvicorn
from fastapi import FastAPI, Form, HTTPException, Request, status
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

BASE_DIR = Path(__file__).parent

app = FastAPI(title="Films")
templates = Jinja2Templates(directory=BASE_DIR / "templates")

# files that are sent to the browser unchanged (the style sheet)
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

# the state of the application: the films, kept in a global variable
# (shared by all the users, and lost when the program restarts)
films = [
    {"title": "Fargo", "year": 1996, "director": "Joel Coen"},
    {"title": "The Big Lebowski", "year": 1998, "director": "Joel Coen"},
    {"title": "Amélie", "year": 2001, "director": "Jean-Pierre Jeunet"},
]


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(request, "index.html", {"films": films})


@app.get("/films")
def film_list(request: Request):
    return templates.TemplateResponse(request, "films.html", {"films": films})


@app.get("/films/add")
def add_form(request: Request):
    """Shows the empty form. This route is written before /films/{film_id}, which would take "add" too."""
    return templates.TemplateResponse(request, "add_film.html", {})


@app.post("/films/add")
def add_film(
    title: Annotated[str, Form()],
    year: Annotated[int, Form()],
    director: Annotated[str, Form()] = "",
):
    """Executed when the form is sent: adds the film, and sends the browser to the list (Post/Redirect/Get)."""
    films.append({"title": title, "year": year, "director": director})
    return RedirectResponse("/films", status_code=status.HTTP_303_SEE_OTHER)


@app.get("/films/{film_id}")
def film_detail(request: Request, film_id: int):
    """The details of one film; its number is its position in the list, counted from 0."""
    if film_id < 0 or film_id >= len(films):
        raise HTTPException(status_code=404, detail="Film not found")
    return templates.TemplateResponse(request, "film_detail.html", {"film": films[film_id]})


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
