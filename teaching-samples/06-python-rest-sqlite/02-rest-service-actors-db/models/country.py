from sqlmodel import Field, SQLModel


class CountryData(SQLModel):
    """The data about a country, as it travels in the JSON of requests and answers."""

    country_id: int | None = None

    name: str

    code: str


class Country(CountryData, table=True):
    """One object of this class is one row of the table country."""

    country_id: int | None = Field(default=None, primary_key=True)  # assigned by the DBMS
