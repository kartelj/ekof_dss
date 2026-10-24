import datetime

from sqlmodel import Field, Relationship, SQLModel

from models.country import Country


class Actor(SQLModel, table=True):
    """One object of this class is one row of the table actor."""

    actor_id: int | None = Field(default=None, primary_key=True)

    last_name: str = Field(max_length=255)

    first_name: str = Field(max_length=255)

    country_id: int = Field(foreign_key="country.country_id")

    date_of_birth: datetime.date | None = None

    # Not a column: the object of the class Country to which country_id refers.
    # It is read from the table country when it is used for the first time.
    country: Country = Relationship()
