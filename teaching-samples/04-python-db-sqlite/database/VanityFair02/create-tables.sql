-- VanityFair02: genres and states are stored only once, in tables of their own.
-- A film does not repeat their names - it refers to them through foreign keys.

-- SQLite checks foreign keys only if this is switched on (for every connection).
PRAGMA foreign_keys = ON;

CREATE TABLE genre (
    genre_id    INTEGER PRIMARY KEY,
    name        TEXT    NOT NULL,
    short_name  TEXT    NOT NULL
);

CREATE TABLE state (
    state_id    INTEGER PRIMARY KEY,
    name        TEXT    NOT NULL,
    code        TEXT    NOT NULL
);

CREATE TABLE movie (
    movie_id    INTEGER PRIMARY KEY,
    title       TEXT    NOT NULL,
    genre_id    INTEGER NOT NULL,
    lasting     INTEGER NOT NULL DEFAULT 90,   -- in minutes
    state_id    INTEGER NOT NULL,
    imdb_score  REAL    NOT NULL DEFAULT 0,
    year        INTEGER NULL,
    actors      TEXT    NULL,
    directors   TEXT    NULL,
    scenarists  TEXT    NULL,
    plot        TEXT    NULL,
    profit      NUMERIC NOT NULL DEFAULT 0,

    -- the value of genre_id must exist in the table genre, and state_id in the table state
    CONSTRAINT fk_movie_genre FOREIGN KEY (genre_id) REFERENCES genre (genre_id),
    CONSTRAINT fk_movie_state FOREIGN KEY (state_id) REFERENCES state (state_id)
);

-- searching films by genre or by state is faster with an index on those columns
CREATE INDEX ix_movie_genre_id ON movie (genre_id);
CREATE INDEX ix_movie_state_id ON movie (state_id);
