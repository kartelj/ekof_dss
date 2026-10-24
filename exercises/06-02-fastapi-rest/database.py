"""
The connection with the database.

The database is the SQLite file movies.db in this folder. It is created, with the genres and
the films of VanityFair02 in it, the first time the service is started. To start again
from scratch, stop the service and delete the file.
"""

from pathlib import Path
from typing import Annotated

from fastapi import Depends
from sqlalchemy import event
from sqlmodel import Session, SQLModel, create_engine, select

from models.genre import Genre
from models.movie import Movie

DATABASE_FILE = Path(__file__).parent / "movies.db"

engine = create_engine(f"sqlite:///{DATABASE_FILE}")


@event.listens_for(engine, "connect")
def switch_on_foreign_keys(connection, connection_record):
    """SQLite checks foreign keys only if it is asked to, on every new connection."""
    cursor = connection.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    cursor.close()


def get_session():
    """Hands over a session - a conversation with the database - and closes it afterwards."""
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]


def create_database() -> None:
    """Creates the tables (if they do not exist), and fills the empty tables with data."""
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        if session.exec(select(Genre)).first() is not None:
            return  # there is data already

        # the genres of VanityFair02, with the same ids
        names = ["crime comedy", "gangster", "romantic comedy", "crime", "comedy", "fantasy", "science fiction"]
        session.add_all([Genre(name=name) for name in names])
        session.commit()

        session.add_all(
            [
                Movie(title="Raising Arizona", year=1987, lasting=94, genre_id=1),
                Movie(title="Miller's Crossing", year=1990, lasting=115, genre_id=2),
                Movie(title="Amélie", year=2001, lasting=122, genre_id=3),
                Movie(title="Fargo", year=1996, lasting=98, genre_id=4),
                Movie(title="The Big Lebowski", year=1998, lasting=117, genre_id=1),
                Movie(title="O Brother, Where Art Thou?", year=2000, lasting=107, genre_id=5),
                Movie(title="No Country for Old Men", year=2007, lasting=122, genre_id=4),
                Movie(title="Delicatessen", year=1991, lasting=99, genre_id=5),
                Movie(title="The City of Lost Children", year=1995, lasting=112, genre_id=6),
                Movie(title="Who's Singin' Over There?", year=1980, lasting=86, genre_id=5),
            ]
        )
        session.commit()
