"""
Using a database from Python by writing the SQL statements ourselves.

    python main.py

The module sqlite3 is a part of Python - nothing has to be installed.
Every run adds one row, so run the program several times and watch the table grow.
"""

from pathlib import Path

from sqlite_service import SqliteService

DATABASE_FILE = Path(__file__).parent / "actors.db"


def main():
    service = SqliteService(DATABASE_FILE)
    service.create_table()

    # Fetch data
    result = service.get_data()
    print("Data from table:")
    for row in result:
        print(dict(row))

    # Insert data
    new_id = service.insert_data("Franco", "Nero")
    print("Insert response:")
    print("actor_id of the new row:", new_id)

    service.close()


if __name__ == "__main__":
    main()
