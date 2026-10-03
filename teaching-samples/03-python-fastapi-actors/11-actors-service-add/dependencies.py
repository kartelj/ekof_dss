"""
The services of the application, and the functions that hand them over.

A function that needs a service does not create it. It only declares it as a parameter:

    def index(actor_service: Annotated[ActorService, Depends(get_actor_service)]):

Before FastAPI calls index(), it calls get_actor_service() and passes the result on.
This is called dependency injection. To use another kind of actor service in the
whole application, only this file has to be changed.
"""

from pathlib import Path

from services.actor_service import ActorService
from services.file_actor_service import FileActorService
from services.messaging_service import MessagingService

BASE_DIR = Path(__file__).parent


def write_message_to_console(messages: list[str]) -> None:
    """A listener: it is called by the messaging service whenever the messages change."""
    if messages:
        print("Message:", messages[-1])  # the last message of the list
    else:
        print("Messages are cleared.")


# one object of each service for the whole application
_messaging_service = MessagingService()
_messaging_service.on_messages_changed.append(write_message_to_console)

_actor_service = FileActorService(BASE_DIR / "sample-data" / "actors.json", _messaging_service)


def get_messaging_service() -> MessagingService:
    return _messaging_service


def get_actor_service() -> ActorService:
    return _actor_service
