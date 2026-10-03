from typing import Annotated

from fastapi import APIRouter, Depends, Request

from dependencies import get_actor_service
from services.actor_service import ActorService
from templating import templates

router = APIRouter()


@router.get("/dashboard")
def show(
    request: Request,
    actor_service: Annotated[ActorService, Depends(get_actor_service)],
    search: str = "",
):
    """The parameter search is the text typed into the search box: /dashboard?search=tom"""
    actors = actor_service.get_actors()
    top_actors = actors[:4]  # the first four actors of the list

    filtered_actors = []
    if search != "":
        # the same text is looked for in the first name, in the last name and in the country
        filtered_actors = actor_service.search(search, search, search)

    return templates.TemplateResponse(
        request,
        "dashboard.html",
        {"actors": top_actors, "search": search, "filtered_actors": filtered_actors},
    )
