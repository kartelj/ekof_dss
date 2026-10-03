import datetime
from dataclasses import dataclass


@dataclass
class Actor:
    """The data about one actor, together with its country, as the RESTful service sends it."""

    id: int
    last_name: str
    first_name: str | None = None
    country_id: int | None = None  # an actor does not have to have a country
    country_code: str | None = None
    country_name: str | None = None
    date_of_birth: datetime.date | None = None
