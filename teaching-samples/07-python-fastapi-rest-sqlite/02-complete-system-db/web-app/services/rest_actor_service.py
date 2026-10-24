import datetime

import httpx2

from models.actor import Actor
from services.actor_service import ActorService
from services.messaging_service import MessagingService


class RestActorService(ActorService):
    """
    Obtains the actors from the RESTful service, and sends the changes to it.

    This class is a client of the service: it sends HTTP requests with the library
    httpx2, in the same way a browser sends them - only the answers are JSON, not HTML.
    The application keeps no actors of its own: the data lives in the service.
    """

    def __init__(self, request_uri: str, messaging_service: MessagingService):
        self._request_uri = request_uri  # the address of the resource: http://localhost:8001/api/actors
        self._messaging_service = messaging_service

    def get_actors(self) -> list[Actor]:
        # sending request for reading to the server
        response = httpx2.get(self._request_uri)
        response.raise_for_status()  # an answer such as 404 or 500 becomes an exception
        self._messaging_service.add("ActorService: sent request for read")

        actors = []
        for item in response.json():  # the JSON array has become a list of dictionaries
            date_of_birth = None
            if item["date_of_birth"] is not None:
                date_of_birth = datetime.date.fromisoformat(item["date_of_birth"])
            actor = Actor(
                id=item["id"],
                first_name=item["first_name"],
                last_name=item["last_name"],
                country_id=item["country_id"],
                country_code=item["country_code"],
                country_name=item["country_name"],
                date_of_birth=date_of_birth,
            )
            actors.append(actor)
        return actors

    def add(self, first_name: str, last_name: str, country_id: int) -> bool:
        # sending request for adding to the server; the dictionary is sent as JSON
        actor_add = {
            "first_name": first_name,
            "last_name": last_name,
            "country_id": country_id,
        }
        response = httpx2.post(self._request_uri, json=actor_add)
        return self._report(response, "add")

    def delete(self, actor: Actor) -> bool:
        # sending request for deleting to the server
        response = httpx2.delete(f"{self._request_uri}/{actor.id}")
        return self._report(response, "delete")

    def update(self, actor: Actor) -> bool:
        # sending request for updating to the server
        actor_upd = {
            "id": actor.id,
            "first_name": actor.first_name,
            "last_name": actor.last_name,
            "country_id": actor.country_id,
            "date_of_birth": actor.date_of_birth.isoformat() if actor.date_of_birth else None,
        }
        response = httpx2.put(f"{self._request_uri}/{actor.id}", json=actor_upd)
        return self._report(response, "update")

    def search(self, fn: str, ln: str, c: str) -> list[Actor]:
        result = []
        for actor in self.get_actors():
            if (
                fn.lower() in actor.first_name.lower()
                or ln.lower() in actor.last_name.lower()
                or c.lower() in actor.country_code.lower()
            ):
                result.append(actor)
        return result

    def _report(self, response: httpx2.Response, operation: str) -> bool:
        """Adds a message that tells whether the service has accepted the request; returns True if it has."""
        if response.is_success:  # the status code is 2xx
            self._messaging_service.add(f"ActorService: sent request for {operation}")
        else:
            self._messaging_service.add(
                f"ActorService: error in {operation} - {response.status_code} {response.text}"
            )
        return response.is_success
