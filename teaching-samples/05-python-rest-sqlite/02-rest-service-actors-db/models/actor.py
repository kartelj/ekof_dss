import datetime

from sqlmodel import Field, SQLModel


class ActorData(SQLModel):
    """
    The data about an actor, as it travels in the JSON of requests and answers.

    When the data arrives, FastAPI checks every value against the type written here,
    and converts it (for example the text "1949-06-22" into a date). If a value is
    missing or has a wrong type, the answer is 422 and the function is not called at all.
    """

    actor_id: int | None = None

    last_name: str = Field(max_length=50)

    first_name: str = Field(max_length=50)

    country_id: int

    date_of_birth: datetime.date | None = None


class Actor(ActorData, table=True):
    """One object of this class is one row of the table actor."""

    actor_id: int | None = Field(default=None, primary_key=True)  # assigned by the DBMS

    # a foreign key: the value must be the country_id of a row of the table country
    country_id: int = Field(foreign_key="country.country_id")
