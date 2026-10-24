from sqlmodel import Field, SQLModel


class MovieData(SQLModel):
    """
    The data about a film, as it travels in the JSON of requests and answers.

    A film without a year may be stored (the year is not always known), and a film
    without its length gets 90 minutes. The title and the genre are required.
    """

    movie_id: int | None = None

    title: str = Field(max_length=100)

    year: int | None = None

    lasting: int = 90  # in minutes

    genre_id: int


class Movie(MovieData, table=True):
    """One object of this class is one row of the table movie."""

    movie_id: int | None = Field(default=None, primary_key=True)  # assigned by the DBMS

    # a foreign key: the value must be the genre_id of a row of the table genre
    genre_id: int = Field(foreign_key="genre.genre_id")
