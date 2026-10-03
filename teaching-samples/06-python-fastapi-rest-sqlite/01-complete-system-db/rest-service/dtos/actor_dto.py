"""
The data about actors as the clients of the service see it.

A data transfer object (DTO) does not have to look like a row of a table:
here the clients get the code of the country (US) instead of the key country_id.
"""

import datetime

from pydantic import BaseModel


class ActorDTO(BaseModel):
    """An actor, as it is sent to the clients."""

    id: int
    last_name: str
    first_name: str
    country_code: str
    date_of_birth: datetime.date | None = None


class ActorCreateDTO(BaseModel):
    """What a client sends in order to add an actor (the id is chosen by the database)."""

    last_name: str
    first_name: str
    country_code: str
    date_of_birth: datetime.date | None = None


class ActorUpdateDTO(BaseModel):
    """What a client sends in order to change an actor."""

    id: int
    last_name: str
    first_name: str
    country_code: str
    date_of_birth: datetime.date | None = None
