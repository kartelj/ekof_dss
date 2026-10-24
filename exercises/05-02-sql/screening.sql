-- Assignment of the lecture "Introduction to SQL": the screenings of a cinema, in VanityFair02.
-- Part 1 and 2: the table and its rows.

PRAGMA foreign_keys = ON;

CREATE TABLE screening (
    screening_id  INTEGER PRIMARY KEY,
    movie_id      INTEGER NOT NULL REFERENCES movie (movie_id),
    hall          TEXT    NOT NULL CHECK (hall IN ('A', 'B', 'C')),
    starts_at     TEXT    NOT NULL,                   -- a moment as a text: 'YYYY-MM-DD HH:MM'
    price         NUMERIC NOT NULL CHECK (price > 0),
    sold          INTEGER NOT NULL DEFAULT 0 CHECK (sold >= 0),
    UNIQUE (hall, starts_at)                          -- one screening in a hall at a time
);

-- the films: 4 Fargo, 3 Amélie, 5 The Big Lebowski, 10 Who's Singin' Over There?, 8 Delicatessen
INSERT INTO screening (movie_id, hall, starts_at, price, sold)
VALUES (4, 'A', '2026-11-06 18:00', 400, 52),
       (4, 'B', '2026-11-06 20:30', 450, 80),
       (3, 'A', '2026-11-06 20:30', 450, 95),
       (5, 'C', '2026-11-07 19:00', 400, 40),
       (10, 'A', '2026-11-07 18:00', 350, 120);

-- no tickets sold yet: the column sold gets its default value, 0
INSERT INTO screening (movie_id, hall, starts_at, price)
VALUES (8, 'B', '2026-11-07 21:00', 400);

SELECT * FROM screening;
