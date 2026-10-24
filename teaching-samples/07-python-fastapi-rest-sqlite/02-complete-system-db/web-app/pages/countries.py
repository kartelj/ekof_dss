from typing import Annotated

from fastapi import APIRouter, Depends, Form, Request, status
from fastapi.responses import RedirectResponse

from dependencies import get_country_service, get_messaging_service
from services.country_service import CountryService
from services.messaging_service import MessagingService
from templating import templates

router = APIRouter()


@router.get("/countries")
def show(
    request: Request,
    country_service: Annotated[CountryService, Depends(get_country_service)],
):
    countries = country_service.get_countries()

    return templates.TemplateResponse(request, "countries.html", {"countries": countries})


@router.post("/countries")
def add(
    country_service: Annotated[CountryService, Depends(get_country_service)],
    messaging_service: Annotated[MessagingService, Depends(get_messaging_service)],
    country_code: Annotated[str, Form()] = "",
    country_name: Annotated[str, Form()] = "",
):
    # the service returns False if the change is refused; it reports the reason in the messages
    if country_service.add(country_code, country_name):
        messaging_service.add(f"Country added: {country_code} {country_name}")

    return RedirectResponse("/countries", status_code=status.HTTP_303_SEE_OTHER)


@router.post("/countries/{country_id}/delete")
def delete(
    country_id: int,
    country_service: Annotated[CountryService, Depends(get_country_service)],
    messaging_service: Annotated[MessagingService, Depends(get_messaging_service)],
):
    for country in country_service.get_countries():
        if country.id == country_id:
            # the RESTful service refuses to delete a country that still has actors
            if country_service.delete(country):
                messaging_service.add(f"Country deleted: {country.code} {country.name}")
            break

    return RedirectResponse("/countries", status_code=status.HTTP_303_SEE_OTHER)
