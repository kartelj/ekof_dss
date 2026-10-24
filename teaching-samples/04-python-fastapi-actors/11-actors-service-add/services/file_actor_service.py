import datetime
import json
from pathlib import Path

from models.actor import Actor
from services.actor_service import ActorService
from services.messaging_service import MessagingService


class FileActorService(ActorService):
    """
    Obtains the actors from a file in the JSON format, and keeps them in memory.

    The file itself is never changed: new actors live only in the memory of the
    application, and they are gone when the application is restarted.
    """

    def __init__(self, file: Path, messaging_service: MessagingService):
        self._file = file
        self._messaging_service = messaging_service
        self._actors: list[Actor] | None = None  # the actors are not read yet

    def get_actors(self, reload: bool = False) -> list[Actor]:
        if self._actors is None or reload:
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
            self._messaging_service.add("ActorService: actors reloaded")
        else:
            self._messaging_service.add("ActorService: actors already loaded")
        return self._actors

    def add(self, first_name: str, last_name: str, country: str) -> list[Actor]:
        actors = self.get_actors()

        # the new actor gets the id that is by one greater than the greatest id in the list
        new_id = max((actor.id for actor in actors), default=0) + 1
        new_actor = Actor(
            id=new_id,
            first_name=first_name,
            last_name=last_name,
            country_code=country,
        )
        actors.append(new_actor)
        return actors
