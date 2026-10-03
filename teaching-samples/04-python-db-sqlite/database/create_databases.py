"""
Creates the SQLite databases of the course from the SQL scripts in this folder.

    python create_databases.py

The result are the files VanityFair01/VanityFair01.db and VanityFair02/VanityFair02.db.
A SQLite database is a single file: to start again from scratch, just run this program again.
"""

import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).parent

# the scripts of each database, in the order in which they have to be executed
DATABASES = {
    "VanityFair01": ["create-tables.sql", "insert-table-data.sql"],
    "VanityFair02": ["create-tables.sql", "create-views.sql", "insert-table-data.sql"],
}


def create_database(name: str, scripts: list[str]) -> None:
    folder = BASE_DIR / name
    database_file = folder / f"{name}.db"
    database_file.unlink(missing_ok=True)  # remove the old database, if there is one

    connection = sqlite3.connect(database_file)
    for script in scripts:
        sql = (folder / script).read_text(encoding="utf-8")
        connection.executescript(sql)
        print(f"{name}: executed {script}")
    connection.close()

    print(f"{name}: created {database_file}")


if __name__ == "__main__":
    for name, scripts in DATABASES.items():
        create_database(name, scripts)
