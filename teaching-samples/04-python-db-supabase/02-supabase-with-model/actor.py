import datetime

from pydantic import BaseModel


class Actor(BaseModel):
    """
    The model: one object of this class is one row of the table actor.

    The class is based on BaseModel, so the values are checked and converted when an
    object is made from a row: the text "1943-08-17" becomes a date.
    """

    actor_id: int | None = None  # assigned by the DBMS

    last_name: str

    first_name: str | None = None

    country_id: int | None = None

    date_of_birth: datetime.date | None = None

    created_at: datetime.datetime | None = None  # assigned by the DBMS
