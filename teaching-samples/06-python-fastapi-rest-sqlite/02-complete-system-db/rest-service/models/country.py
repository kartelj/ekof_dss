from sqlmodel import Field, SQLModel


class Country(SQLModel, table=True):
    """One object of this class is one row of the table country."""

    country_id: int | None = Field(default=None, primary_key=True)

    name: str = Field(max_length=255)

    code: str = Field(max_length=50)
