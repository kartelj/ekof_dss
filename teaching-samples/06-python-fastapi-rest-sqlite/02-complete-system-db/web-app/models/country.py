from dataclasses import dataclass


@dataclass
class Country:
    """The data about one country, as the RESTful service sends it."""

    id: int
    name: str
    code: str
