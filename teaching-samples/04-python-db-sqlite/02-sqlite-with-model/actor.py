import datetime

from sqlmodel import Field, SQLModel


class Actor(SQLModel, table=True):
    """
    The model: one object of this class is one row of the table actor,
    and every attribute of the class is one column of the table.
    """

    actor_id: int | None = Field(default=None, primary_key=True)  # assigned by the DBMS

    last_name: str

    first_name: str

    country_code: str | None = None

    date_of_birth: datetime.date | None = None

    created_at: datetime.datetime | None = None
