import datetime

from pydantic import BaseModel


class ActorCountry(BaseModel):
    """
    An actor together with the name and the code of its country.

    This is not a row of a table: it is a row of the result of the database function
    get_actors_with_country(), which joins the tables actor and country.
    """

    actor_id: int

    last_name: str

    first_name: str | None = None

    country_id: int | None = None

    country_name: str | None = None

    country_code: str | None = None

    date_of_birth: datetime.date | None = None
