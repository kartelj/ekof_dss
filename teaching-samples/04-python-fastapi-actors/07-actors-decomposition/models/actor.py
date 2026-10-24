import datetime
from dataclasses import dataclass


@dataclass
class Actor:
    """
    The model: the data that the application keeps about one actor.

    @dataclass writes the method __init__ for us, from the list of attributes below.
    """

    id: int
    last_name: str
    first_name: str
    country_code: str
    date_of_birth: datetime.date | None = None
