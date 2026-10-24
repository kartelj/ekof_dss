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

BASE_DIR = Path(__file__).parent

# one object for the whole application
_actor_service = FileActorService(BASE_DIR / "sample-data" / "actors.json")


def get_actor_service() -> ActorService:
    return _actor_service
