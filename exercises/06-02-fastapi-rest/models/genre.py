from sqlmodel import Field, SQLModel


class GenreData(SQLModel):
    """The data about a genre, as it travels in the JSON of the answers."""

    genre_id: int | None = None

    name: str = Field(max_length=50)


class Genre(GenreData, table=True):
    """One object of this class is one row of the table genre."""

    genre_id: int | None = Field(default=None, primary_key=True)  # assigned by the DBMS
