"""
Using a database from Python through a model class - without writing SQL.

    python main.py

The library SQLModel translates the work with objects of the class Actor into
SQL statements (this is called object-relational mapping, ORM). With echo=True
the engine prints every SQL statement that it sends to the database.
"""

import datetime
from pathlib import Path

from sqlmodel import Session, SQLModel, create_engine, select

from actor import Actor

DATABASE_FILE = Path(__file__).parent / "actors.db"


def main():
    # init
    engine = create_engine(f"sqlite:///{DATABASE_FILE}", echo=True)
    SQLModel.metadata.create_all(engine)  # creates the table actor if it does not exist

    with Session(engine) as session:
        # A result can be fetched like so.
        actors = session.exec(select(Actor)).all()

        print(len(actors))

        model = Actor(
            first_name="Robert",
            last_name="De Niro",
            date_of_birth=datetime.date(1943, 8, 17),
            country_code="US",
            created_at=datetime.datetime.now(datetime.timezone.utc),  # moments in time are kept in UTC
        )

        session.add(model)
        session.commit()

        session.refresh(model)  # reads the row back, with the actor_id that the DBMS assigned
        print(model)


if __name__ == "__main__":
    main()
