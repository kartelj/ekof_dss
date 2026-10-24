"""
Classes and objects: a list of actors, shown as a table.
"""

from fastapi import APIRouter, Request

from models.actor import Actor
from templating import templates

router = APIRouter()

movie_star_1 = Actor(first_name="John", last_name="Goodman", imdb_mark=9.7)

# when the arguments are named, they can be written in any order
movie_star_2 = Actor(last_name="De Niro", imdb_mark=9.4, first_name="Robert")

movie_star_3 = Actor(last_name="Spacey", imdb_mark=9.6, first_name="Kevin")

movie_star_4 = Actor(last_name="Nero", imdb_mark=9.9, first_name="Franco")

film_crew = [movie_star_1, movie_star_2, movie_star_3, movie_star_4]


def render(request: Request, show_result: bool, avg_imdb: float):
    return templates.TemplateResponse(
        request,
        "actors_show.html",
        {"film_crew": film_crew, "show_result": show_result, "avg_imdb": avg_imdb},
    )


@router.get("/actors-show")
def show(request: Request):
    return render(request, show_result=False, avg_imdb=0)


@router.get("/actors-show/average-imdb")
def average_imdb(request: Request):
    total = 0
    for a in film_crew:
        total += a.imdb_mark
    avg_imdb = total / len(film_crew)
    return render(request, show_result=True, avg_imdb=avg_imdb)
