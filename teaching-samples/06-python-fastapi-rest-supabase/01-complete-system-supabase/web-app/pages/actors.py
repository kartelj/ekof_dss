from typing import Annotated

from fastapi import APIRouter, Depends, Form, Request, status
from fastapi.responses import RedirectResponse

from dependencies import get_actor_service, get_country_service, get_messaging_service
from services.actor_service import ActorService
from services.country_service import CountryService
from services.messaging_service import MessagingService
from templating import templates

router = APIRouter()


@router.get("/actors")
def show(
    request: Request,
    actor_service: Annotated[ActorService, Depends(get_actor_service)],
    country_service: Annotated[CountryService, Depends(get_country_service)],
    sort: str = "id",
    descending: bool = False,
):
    """
    The table can be ordered by a column: a click on the title of a column leads to
    /actors?sort=last_name , and a second click to /actors?sort=last_name&descending=true
    """
    countries = country_service.get_countries()  # for the list in the row for a new actor
    actors = actor_service.get_actors()

    # sort() orders the list by the value that the function key gives for every element;
    # lambda is a short way to write such a small function in place
    if sort == "first_name":
        actors.sort(key=lambda a: (a.first_name or "").lower(), reverse=descending)
    elif sort == "last_name":
        actors.sort(key=lambda a: a.last_name.lower(), reverse=descending)
    elif sort == "country_name":
        actors.sort(key=lambda a: (a.country_name or "").lower(), reverse=descending)
    else:
        sort = "id"
        actors.sort(key=lambda a: a.id, reverse=descending)

    return templates.TemplateResponse(
        request,
        "actors.html",
        {"actors": actors, "countries": countries, "sort": sort, "descending": descending},
    )


@router.post("/actors")
def add(
    actor_service: Annotated[ActorService, Depends(get_actor_service)],
    messaging_service: Annotated[MessagingService, Depends(get_messaging_service)],
    country_id: Annotated[int, Form()],
    first_name: Annotated[str, Form()] = "",
    last_name: Annotated[str, Form()] = "",
):
    # the service returns False if the change is refused; it reports the reason in the messages
    if actor_service.add(first_name, last_name, country_id):
        messaging_service.add(f"ActorComponent: actor added: {first_name} {last_name}")

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
                messaging_service.add(
                    f"ActorComponent: actor deleted: {actor.first_name} {actor.last_name}"
                )
            break

    return RedirectResponse("/actors", status_code=status.HTTP_303_SEE_OTHER)
