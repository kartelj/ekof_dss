import datetime
from dataclasses import dataclass


@dataclass
class Actor:
    """The data about one actor, as the RESTful service sends it."""

    id: int
    last_name: str
    first_name: str
    country_id: int
    country_code: str
    country_name: str
    date_of_birth: datetime.date | None = None
