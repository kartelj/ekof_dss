import datetime
import json
from pathlib import Path

from models.actor import Actor
from services.actor_service import ActorService
from services.messaging_service import MessagingService


class FileActorService(ActorService):
    """Obtains the actors from a file in the JSON format."""

    def __init__(self, file: Path, messaging_service: MessagingService):
        # a service can use another service: it receives it when it is created
        self._file = file
        self._messaging_service = messaging_service
        self._actors: list[Actor] | None = None  # the actors are not read yet

    def get_actors(self) -> list[Actor]:
        # the file is read only the first time; after that the same list is returned
        if self._actors is None:
            text = self._file.read_text(encoding="utf-8")
            self._actors = []
            for item in json.loads(text):
                actor = Actor(
                    id=item["id"],
                    first_name=item["first_name"],
                    last_name=item["last_name"],
                    country_code=item["country_code"],
                    date_of_birth=datetime.date.fromisoformat(item["date_of_birth"]),
                )
                self._actors.append(actor)
            self._messaging_service.add("ActorService: actors fetched")
        return self._actors
