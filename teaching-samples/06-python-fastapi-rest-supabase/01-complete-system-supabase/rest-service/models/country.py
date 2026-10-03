import datetime

from pydantic import BaseModel


class Country(BaseModel):
    """A country: one row of the table country, and the JSON that travels to and from the clients."""

    country_id: int | None = None  # assigned by the DBMS

    name: str

    code: str

    created_at: datetime.datetime | None = None  # assigned by the DBMS
