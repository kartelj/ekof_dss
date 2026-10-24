"""
The services of the application, and the functions that hand them over.

Compare this file with the one in the last step of the actors application
(04-python-fastapi-actors): there the actors came from a file, here they come
from the RESTful service. The pages know only the abstract classes ActorService
and CountryService.
"""

import os

from services.actor_service import ActorService
from services.country_service import CountryService
from services.messaging_service import MessagingService
from services.rest_actor_service import RestActorService
from services.rest_country_service import RestCountryService

# the address of the RESTful service (it can be changed with an environment variable)
REST_SERVICE_URL = os.environ.get("REST_SERVICE_URL", "http://localhost:8001/api")


def write_message_to_console(messages: list[str]) -> None:
    """A listener: it is called by the messaging service whenever the messages change."""
    if messages:
        print("Message:", messages[-1])  # the last message of the list
    else:
        print("Messages are cleared.")


# one object of each service for the whole application
_messaging_service = MessagingService()
_messaging_service.on_messages_changed.append(write_message_to_console)

_actor_service = RestActorService(REST_SERVICE_URL + "/actors", _messaging_service)
_country_service = RestCountryService(REST_SERVICE_URL + "/countries", _messaging_service)


def get_messaging_service() -> MessagingService:
    return _messaging_service


def get_actor_service() -> ActorService:
    return _actor_service


def get_country_service() -> CountryService:
    return _country_service
