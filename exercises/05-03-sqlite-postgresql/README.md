# Assignment: a film catalogue - a solution

The assignment at the end of the lecture [SQLite and PostgreSQL](../../presentations/05-03-sqlite-postgresql.md):
a program for the terminal that lists, searches, adds and deletes the films of VanityFair02 - like the shopping
list of the introduction to Python, but with the data in a database.

```text
[l]ist, [s]earch, [a]dd, [d]elete, [q]uit: s
A part of the title: the
 10  1980  Who's Singin' Over There?    comedy           YUG
  9  1995  The City of Lost Children    fantasy          FRA
  5  1998  The Big Lebowski             crime comedy     USA
  6  2000  O Brother, Where Art Thou?   comedy           USA
4 films
```

## How to run it

The program works next to the database of the course. In your folder `05-python-db-sqlite` (the archive of the
module), copy `film_catalogue.py` into the folder `database/VanityFair02`, build the databases, and start it there:

```text
cd database
python create_databases.py
cd VanityFair02
python film_catalogue.py
```

To start again with the ten films, run `create_databases.py` again.

## What to look at

| Requirement | Where |
|---|---|
| every value of a statement is a parameter - also the pattern of `LIKE` | `show_films`, `add_film`, `delete_film` |
| foreign keys are checked | `PRAGMA foreign_keys = ON` right after `connect` |
| a change is permanent only after `commit()` | `add_film`, `delete_film` |
| the genre and the state are given by their codes, and the program finds their keys | `find_one` |
| a year that is not a number is asked again; an unknown code adds nothing | `read_year`, `add_film` |
| a missing database file is reported - `connect` would quietly create an empty one | before `connect` |

## Notes

- One query serves both the list and the search: the pattern `%%` (an empty text between the two `%`)
  matches every title.
- `find_one` returns `None` when the query finds no row: `fetchone()` gives `None` then.
- The path of the database is built from the folder of the program (`Path(__file__).parent`), so the program
  works from whichever folder it is started.
- A possible extension: the same program with SQLModel and three model classes - `Movie`, `Genre` and `State`.
