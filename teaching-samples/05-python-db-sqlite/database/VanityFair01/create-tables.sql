-- VanityFair01: everything that is known about a film is stored in ONE table.
--
-- This is the first, naive design. Notice that the genre and the state are written
-- as text in every row, and that the columns actors, directors and scenarists
-- hold several names in a single value. VanityFair02 improves the design.

CREATE TABLE movie (
    movie_id    INTEGER PRIMARY KEY,           -- the DBMS assigns 1, 2, 3 ... by itself
    title       TEXT    NOT NULL,
    genre       TEXT    NOT NULL,
    lasting     INTEGER NOT NULL DEFAULT 90,   -- in minutes
    states      TEXT    NOT NULL DEFAULT '',
    imdb_score  REAL    NOT NULL DEFAULT 0,
    year        INTEGER NULL,
    actors      TEXT    NULL,
    directors   TEXT    NULL,
    scenarists  TEXT    NULL,
    plot        TEXT    NULL,
    profit      NUMERIC NOT NULL DEFAULT 0
);
