from typing import Annotated

from fastapi import APIRouter, Depends, Form, Request, status
from fastapi.responses import RedirectResponse

from dependencies import get_actor_service, get_messaging_service
from services.actor_service import ActorService
from services.messaging_service import MessagingService
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
    messaging_service: Annotated[MessagingService, Depends(get_messaging_service)],
    first_name: Annotated[str, Form()] = "",
    last_name: Annotated[str, Form()] = "",
    country: Annotated[str, Form()] = "",
):
    # the service returns False if the change is refused; it reports the reason in the messages
    if actor_service.add(first_name, last_name, country):
        messaging_service.add(f"Actor added: {first_name} {last_name}")

    return RedirectResponse("/actors", status_code=status.HTTP_303_SEE_OTHER)


@router.post("/actors/{actor_id}/delete")
def delete(
    actor_id: int,
    actor_service: Annotated[ActorService, Depends(get_actor_service)],
    messaging_service: Annotated[MessagingService, Depends(get_messaging_service)],
):
    """
    An HTML form can send only GET and POST requests, so the request for deleting is a
    POST to an address that ends with /delete. The actor service then sends a real
    DELETE request to the RESTful service.
    """
    for actor in actor_service.get_actors():
        if actor.id == actor_id:
            if actor_service.delete(actor):
                messaging_service.add(f"Actor deleted: {actor.first_name} {actor.last_name}")
            break

    return RedirectResponse("/actors", status_code=status.HTTP_303_SEE_OTHER)
