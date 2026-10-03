from typing import Annotated

from fastapi import APIRouter, Depends, Form, HTTPException, Request, status
from fastapi.responses import RedirectResponse

from dependencies import get_country_service, get_messaging_service
from models.country import Country
from services.country_service import CountryService
from services.messaging_service import MessagingService
from templating import templates

router = APIRouter()


def find_country(countries: list[Country], country_id: int) -> Country:
    """Returns the country with the given id; if there is no such country, the answer is 404 Not Found."""
    for country in countries:
        if country.id == country_id:
            return country
    raise HTTPException(status_code=404, detail="Country not found")


@router.get("/countrydetail/{country_id}")
def show(
    request: Request,
    country_id: int,
    country_service: Annotated[CountryService, Depends(get_country_service)],
    messaging_service: Annotated[MessagingService, Depends(get_messaging_service)],
    mode: str = "view",
):
    selected_country = find_country(country_service.get_countries(), country_id)

    if mode == "edit":
        messaging_service.add(
            f"CountryDetail: country edited: {selected_country.name} ({selected_country.code})"
        )

    return templates.TemplateResponse(
        request, "country_detail.html", {"selected_country": selected_country, "mode": mode}
    )


@router.post("/countrydetail/{country_id}")
def save(
    country_id: int,
    country_service: Annotated[CountryService, Depends(get_country_service)],
    messaging_service: Annotated[MessagingService, Depends(get_messaging_service)],
    code: Annotated[str, Form()] = "",
    name: Annotated[str, Form()] = "",
):
    country = find_country(country_service.get_countries(), country_id)

    country.code = code
    country.name = name

    if country_service.update(country):
        messaging_service.add(f"CountryDetail: country saved: {country.name} ({country.code})")

    return RedirectResponse(f"/countrydetail/{country.id}", status_code=status.HTTP_303_SEE_OTHER)
