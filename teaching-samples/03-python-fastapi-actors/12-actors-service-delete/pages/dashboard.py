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
):
    actors = actor_service.get_actors()
    top_actors = actors[:4]  # the first four actors of the list

    return templates.TemplateResponse(request, "dashboard.html", {"actors": top_actors})
