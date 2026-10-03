from typing import Annotated

from fastapi import APIRouter, Depends, Form, Request, status
from fastapi.responses import RedirectResponse

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


@router.post("/actors")
def add(
    actor_service: Annotated[ActorService, Depends(get_actor_service)],
    first_name: Annotated[str, Form()] = "",
    last_name: Annotated[str, Form()] = "",
    country: Annotated[str, Form()] = "",
):
    actor_service.add(first_name, last_name, country)

    return RedirectResponse("/actors", status_code=status.HTTP_303_SEE_OTHER)


@router.post("/actors/reload")
def reload(actor_service: Annotated[ActorService, Depends(get_actor_service)]):
    """Reads the actors from the file again: all the changes made so far are forgotten."""
    actor_service.get_actors(reload=True)

    return RedirectResponse("/actors", status_code=status.HTTP_303_SEE_OTHER)


@router.post("/actors/{actor_id}/delete")
def delete(
    actor_id: int,
    actor_service: Annotated[ActorService, Depends(get_actor_service)],
):
    """
    An HTML form can send only GET and POST requests,
    so the request for deleting is a POST to an address that ends with /delete.
    """
    for actor in actor_service.get_actors():
        if actor.id == actor_id:
            actor_service.delete(actor)
            break

    return RedirectResponse("/actors", status_code=status.HTTP_303_SEE_OTHER)
