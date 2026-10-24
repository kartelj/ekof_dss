import httpx2

from models.country import Country
from services.country_service import CountryService
from services.messaging_service import MessagingService


class RestCountryService(CountryService):
    """Obtains the countries from the RESTful service, and sends the changes to it."""

    def __init__(self, request_uri: str, messaging_service: MessagingService):
        self._request_uri = request_uri  # the address of the resource: http://localhost:8001/api/countries
        self._messaging_service = messaging_service

    def get_countries(self) -> list[Country]:
        # sending request for reading to the server
        response = httpx2.get(self._request_uri)
        response.raise_for_status()
        self._messaging_service.add("CountryService: sent request for read")

        countries = []
        for item in response.json():
            countries.append(Country(id=item["id"], name=item["name"], code=item["code"]))
        return countries

    def add(self, country_code: str, country_name: str) -> bool:
        # sending request for adding to the server
        country_add = {"code": country_code, "name": country_name}
        response = httpx2.post(self._request_uri, json=country_add)
        return self._report(response, "add")

    def delete(self, country: Country) -> bool:
        # sending request for deleting to the server
        response = httpx2.delete(f"{self._request_uri}/{country.id}")
        return self._report(response, "delete")

    def update(self, country: Country) -> bool:
        # sending request for updating to the server
        country_upd = {"id": country.id, "code": country.code, "name": country.name}
        response = httpx2.put(f"{self._request_uri}/{country.id}", json=country_upd)
        return self._report(response, "update")

    def _report(self, response: httpx2.Response, operation: str) -> bool:
        """Adds a message that tells whether the service has accepted the request; returns True if it has."""
        if response.is_success:  # the status code is 2xx
            self._messaging_service.add(f"CountryService: sent request for {operation}")
        else:
            self._messaging_service.add(
                f"CountryService: error in {operation} - {response.status_code} {response.text}"
            )
        return response.is_success
