import sqlite3
from pathlib import Path


class SqliteService:
    """Reads and writes the table actor by sending SQL statements to a SQLite database."""

    def __init__(self, database_file: Path):
        # the database is one file; it is created if it does not exist yet
        self._connection = sqlite3.connect(database_file)
        # with this setting the columns of a row can be reached by their names
        self._connection.row_factory = sqlite3.Row

    def create_table(self) -> None:
        self._connection.execute(
            """
            CREATE TABLE IF NOT EXISTS actor (
                actor_id       INTEGER PRIMARY KEY,
                last_name      TEXT NOT NULL,
                first_name     TEXT NOT NULL,
                country_code   TEXT NULL,
                date_of_birth  TEXT NULL,
                created_at     TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

    def get_data(self) -> list[sqlite3.Row]:
        cursor = self._connection.execute("SELECT * FROM actor")
        return cursor.fetchall()

    def insert_data(self, first_name: str, last_name: str) -> int:
        # The values are NOT glued into the text of the statement. Each question mark
        # is replaced by the DBMS with one value from the tuple - safely, whatever the
        # value contains.
        cursor = self._connection.execute(
            "INSERT INTO actor (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name),
        )
        self._connection.commit()  # without commit the change would be lost
        return cursor.lastrowid

    def close(self) -> None:
        self._connection.close()
