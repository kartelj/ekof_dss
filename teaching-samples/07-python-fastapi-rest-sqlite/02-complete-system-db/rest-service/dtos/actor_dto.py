import datetime

from pydantic import BaseModel


class ActorDTO(BaseModel):
    """
    The data about an actor as the clients of the service see it (a data transfer object).

    It does not look like a row of the table actor: next to the key country_id
    it also carries the code and the name of the country, taken from the table country.
    When a client sends an ActorDTO (to add or to change an actor), only country_id
    is used - the code and the name of the country are ignored.
    """

    id: int | None = None
    last_name: str
    first_name: str
    country_id: int
    country_code: str | None = None
    country_name: str | None = None
    date_of_birth: datetime.date | None = None
