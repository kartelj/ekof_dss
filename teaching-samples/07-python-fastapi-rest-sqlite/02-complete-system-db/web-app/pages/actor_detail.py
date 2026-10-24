import datetime
from typing import Annotated

from fastapi import APIRouter, Depends, Form, HTTPException, Request, status
from fastapi.responses import RedirectResponse

from dependencies import get_actor_service, get_country_service, get_messaging_service
from models.actor import Actor
from services.actor_service import ActorService
from services.country_service import CountryService
from services.messaging_service import MessagingService
from templating import templates

router = APIRouter()


def find_actor(actors: list[Actor], actor_id: int) -> Actor:
    """Returns the actor with the given id; if there is no such actor, the answer is 404 Not Found."""
    for actor in actors:
        if actor.id == actor_id:
            return actor
    raise HTTPException(status_code=404, detail="Actor not found")


@router.get("/actordetail/{actor_id}")
def show(
    request: Request,
    actor_id: int,
    actor_service: Annotated[ActorService, Depends(get_actor_service)],
    country_service: Annotated[CountryService, Depends(get_country_service)],
    messaging_service: Annotated[MessagingService, Depends(get_messaging_service)],
    mode: str = "view",
):
    """
    The page has two modes: in the mode "view" it shows the data of the actor,
    in the mode "edit" (/actordetail/3?mode=edit) it shows the form for changing them.
    """
    selected_actor = find_actor(actor_service.get_actors(), actor_id)

    countries = []
    if mode == "edit":
        countries = country_service.get_countries()  # for the list of countries in the form
        messaging_service.add(
            f"ActorDetail: actor edited: {selected_actor.first_name} {selected_actor.last_name}"
        )

    return templates.TemplateResponse(
        request,
        "actor_detail.html",
        {"selected_actor": selected_actor, "mode": mode, "countries": countries},
    )


@router.post("/actordetail/{actor_id}")
def save(
    actor_id: int,
    actor_service: Annotated[ActorService, Depends(get_actor_service)],
    messaging_service: Annotated[MessagingService, Depends(get_messaging_service)],
    country_id: Annotated[int, Form()],
    first_name: Annotated[str, Form()] = "",
    last_name: Annotated[str, Form()] = "",
    date_of_birth: Annotated[datetime.date | None, Form()] = None,
):
    actor = find_actor(actor_service.get_actors(), actor_id)

    actor.first_name = first_name
    actor.last_name = last_name
    actor.country_id = country_id
    actor.date_of_birth = date_of_birth

    if actor_service.update(actor):
        messaging_service.add(f"ActorDetail: actor saved: {actor.first_name} {actor.last_name}")

    # back to the page of this actor, in the mode "view"
    return RedirectResponse(f"/actordetail/{actor.id}", status_code=status.HTTP_303_SEE_OTHER)
