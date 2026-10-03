from typing import Annotated

from fastapi import APIRouter, Depends, Request

from dependencies import get_actor_service
from services.actor_service import ActorService
from templating import templates

router = APIRouter()


@router.get("/actors")
def show(
    request: Request,
    actor_service: Annotated[ActorService, Depends(get_actor_service)],
):
    actors = actor_service.get_actors()

    return templates.TemplateResponse(request, "actors.html", {"actors": actors})
