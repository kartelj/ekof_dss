"""
Classes, objects and modules: the average is calculated by a function from the module list_helper.
"""

from fastapi import APIRouter, Request

from helpers import list_helper
from models.actor import Actor
from templating import templates

router = APIRouter()

movie_star_1 = Actor(first_name="John", last_name="Goodman", imdb_mark=9.7)

movie_star_2 = Actor(last_name="De Niro", imdb_mark=9.4, first_name="Robert")

movie_star_3 = Actor(last_name="Spacey", imdb_mark=9.6, first_name="Kevin")

film_crew = [movie_star_1, movie_star_2, movie_star_3]


def render(request: Request, show_result: bool, avg_imdb: float):
    return templates.TemplateResponse(
        request,
        "actors_show_module.html",
        {"film_crew": film_crew, "show_result": show_result, "avg_imdb": avg_imdb},
    )


@router.get("/actors-show-module")
def show(request: Request):
    return render(request, show_result=False, avg_imdb=0)


@router.get("/actors-show-module/average-imdb")
def average_imdb(request: Request):
    vals = [0.0] * len(film_crew)
    for i in range(len(vals)):
        vals[i] = film_crew[i].imdb_mark
    avg_imdb = list_helper.average(vals)
    return render(request, show_result=True, avg_imdb=avg_imdb)
