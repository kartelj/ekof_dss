from typing import Annotated

from fastapi import APIRouter, Depends, Request

from dependencies import get_actor_service
from models.actor import Actor
from services.actor_service import ActorService
from templating import templates

router = APIRouter()


def find_actors(actor_service: ActorService, search: str) -> list[Actor]:
    """An empty text finds nothing; otherwise the text is looked for in the names and in the country."""
    if search == "":
        return []
    return actor_service.search(search, search, search)


@router.get("/dashboard")
def show(
    request: Request,
    actor_service: Annotated[ActorService, Depends(get_actor_service)],
    search: str = "",
):
    """The whole page. The parameter search is the text typed into the search box."""
    actors = actor_service.get_actors()
    top_actors = actors[:4]  # the first four actors of the list

    return templates.TemplateResponse(
        request,
        "dashboard.html",
        {
            "actors": top_actors,
            "search": search,
            "filtered_actors": find_actors(actor_service, search),
        },
    )


@router.get("/search")
def search_result(
    request: Request,
    actor_service: Annotated[ActorService, Depends(get_actor_service)],
    search: str = "",
):
    """Only a piece of the page: the list of the actors found. It is requested by htmx."""
    return templates.TemplateResponse(
        request, "search_result.html", {"filtered_actors": find_actors(actor_service, search)}
    )
