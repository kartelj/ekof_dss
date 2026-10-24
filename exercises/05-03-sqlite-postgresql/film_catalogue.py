"""
Assignment of the lecture "SQLite and PostgreSQL": a catalogue of the films of VanityFair02,
a program for the terminal.

    python film_catalogue.py

It works next to the database of the course: copy this file into the folder database/VanityFair02
of the samples 05-python-db-sqlite. Build the database first, in the folder database:

    python create_databases.py
"""

import sqlite3
from pathlib import Path

DATABASE_FILE = Path(__file__).parent / "VanityFair02.db"


def show_films(connection, text=""):
    """Writes the films whose title contains the text, sorted by year; an empty text: all the films."""
    rows = connection.execute(
        """
        SELECT m.movie_id, m.year, m.title, g.name AS genre, s.code AS state
        FROM movie AS m
             INNER JOIN genre AS g ON g.genre_id = m.genre_id
             INNER JOIN state AS s ON s.state_id = m.state_id
        WHERE m.title LIKE ?
        ORDER BY m.year
        """,
        (f"%{text}%",),  # the pattern is a value, so it is a parameter too
    ).fetchall()
    for row in rows:
        print(f"{row['movie_id']:3}  {row['year']}  {row['title']:28} {row['genre']:16} {row['state']}")
    print(f"{len(rows)} films")


def read_year():
    """Asks for a year until the user types a whole number."""
    while True:
        try:
            return int(input("Year: "))
        except ValueError:
            print("That is not a year. Type a whole number, e.g. 1995.")


def find_one(connection, sql, value):
    """Returns the first column of the row that the query finds, or None if there is no such row."""
    row = connection.execute(sql, (value,)).fetchone()
    if row is None:
        return None
    return row[0]


def add_film(connection):
    title = input("Title: ").strip()
    year = read_year()
    genre_id = find_one(connection, "SELECT genre_id FROM genre WHERE short_name = ?",
                       input("Genre (CRCOM, GANG, ROMCOM, CRIME, COM, FANT, SCIFI): ").strip().upper())
    state_id = find_one(connection, "SELECT state_id FROM state WHERE code = ?",
                       input("State (USA, FRA, YUG, ITA): ").strip().upper())
    if title == "" or genre_id is None or state_id is None:
        print("The title is empty, or there is no such genre or state. The film is not added.")
        return
    cursor = connection.execute(
        "INSERT INTO movie (title, year, genre_id, state_id) VALUES (?, ?, ?, ?)",
        (title, year, genre_id, state_id),
    )
    connection.commit()
    print(f"Added, with the number {cursor.lastrowid}.")


def delete_film(connection):
    try:
        movie_id = int(input("The number of the film: "))
    except ValueError:
        print("That is not a number.")
        return
    title = find_one(connection, "SELECT title FROM movie WHERE movie_id = ?", movie_id)
    if title is None:
        print("There is no film with this number.")
        return
    if input(f"Delete {title}? [y/n]: ").strip().lower() == "y":
        connection.execute("DELETE FROM movie WHERE movie_id = ?", (movie_id,))
        connection.commit()
        print("Deleted.")


if not DATABASE_FILE.exists():
    # connect() would create a new, empty database - and every query would fail
    raise SystemExit(f"There is no database {DATABASE_FILE} - run create_databases.py first.")

connection = sqlite3.connect(DATABASE_FILE)
connection.row_factory = sqlite3.Row
connection.execute("PRAGMA foreign_keys = ON")

while True:
    command = input("\n[l]ist, [s]earch, [a]dd, [d]elete, [q]uit: ").strip().lower()
    if command == "l":
        show_films(connection)
    elif command == "s":
        show_films(connection, input("A part of the title: "))
    elif command == "a":
        add_film(connection)
    elif command == "d":
        delete_film(connection)
    elif command == "q":
        print("Goodbye.")
        break
    else:
        print("Unknown command.")

connection.close()
