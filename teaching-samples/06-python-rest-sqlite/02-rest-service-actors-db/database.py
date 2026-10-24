"""
The connection with the database.

The database is the SQLite file actors.db in this folder. It is created, with a few
countries and actors in it, the first time the service is started. To start again
from scratch, stop the service and delete the file.
"""

import datetime
from pathlib import Path
from typing import Annotated

from fastapi import Depends
from sqlalchemy import event
from sqlmodel import Session, SQLModel, create_engine, select

from models.actor import Actor
from models.country import Country

DATABASE_FILE = Path(__file__).parent / "actors.db"

# The engine knows where the database is, and how to talk to it.
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


# the functions of the service declare the session as a parameter of this type
SessionDep = Annotated[Session, Depends(get_session)]


def create_database() -> None:
    """Creates the tables (if they do not exist), and fills the empty tables with data."""
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        if session.exec(select(Country)).first() is not None:
            return  # there is data already

        usa = Country(name="United States of America", code="US")
        serbia = Country(name="Serbia", code="RS")
        australia = Country(name="Australia", code="AU")
        italy = Country(name="Italy", code="IT")
        france = Country(name="France", code="FR")
        session.add_all([usa, serbia, australia, italy, france])
        session.commit()  # after the commit every country has its country_id

        d = datetime.date
        session.add_all(
            [
                Actor(first_name="Bata", last_name="Živojinović", country_id=serbia.country_id, date_of_birth=d(1933, 6, 5)),
                Actor(first_name="Julia", last_name="Roberts", country_id=usa.country_id, date_of_birth=d(1967, 10, 28)),
                Actor(first_name="Robert", last_name="De Niro", country_id=usa.country_id, date_of_birth=d(1943, 8, 17)),
                Actor(first_name="Al", last_name="Pacino", country_id=usa.country_id, date_of_birth=d(1940, 4, 25)),
                Actor(first_name="Tom", last_name="Cruise", country_id=usa.country_id, date_of_birth=d(1962, 7, 3)),
                Actor(first_name="Morgan", last_name="Freeman", country_id=usa.country_id, date_of_birth=d(1937, 6, 1)),
                Actor(first_name="Robert", last_name="Downey Jr.", country_id=usa.country_id, date_of_birth=d(1965, 4, 4)),
                Actor(first_name="Brad", last_name="Pitt", country_id=usa.country_id, date_of_birth=d(1963, 12, 18)),
                Actor(first_name="Tom", last_name="Hanks", country_id=usa.country_id, date_of_birth=d(1956, 7, 9)),
                Actor(first_name="Jack", last_name="Nicholson", country_id=usa.country_id, date_of_birth=d(1937, 4, 22)),
                Actor(first_name="Nicole", last_name="Kidman", country_id=australia.country_id, date_of_birth=d(1967, 6, 20)),
                Actor(first_name="Harrison", last_name="Ford", country_id=usa.country_id, date_of_birth=d(1942, 7, 13)),
                Actor(first_name="Denzel", last_name="Washington", country_id=usa.country_id, date_of_birth=d(1954, 12, 28)),
            ]
        )
        session.commit()
