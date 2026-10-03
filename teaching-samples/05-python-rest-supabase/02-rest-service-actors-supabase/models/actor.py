import datetime

from pydantic import BaseModel


class Actor(BaseModel):
    """An actor: one row of the table actor, and the JSON that travels to and from the clients."""

    actor_id: int | None = None  # assigned by the DBMS

    last_name: str

    first_name: str | None = None

    country_id: int | None = None

    date_of_birth: datetime.date | None = None

    created_at: datetime.datetime | None = None  # assigned by the DBMS
