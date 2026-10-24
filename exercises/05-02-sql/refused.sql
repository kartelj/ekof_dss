-- Part 3: three INSERTs that the DBMS refuses, each because of another constraint.
-- Execute them one by one; the answer of SQLite is written under each of them.

PRAGMA foreign_keys = ON;

-- a hall that does not exist
INSERT INTO screening (movie_id, hall, starts_at, price) VALUES (4, 'D', '2026-11-08 18:00', 400);
-- CHECK constraint failed: hall IN ('A', 'B', 'C')

-- hall A is already taken at this moment (Amélie)
INSERT INTO screening (movie_id, hall, starts_at, price) VALUES (5, 'A', '2026-11-06 20:30', 400);
-- UNIQUE constraint failed: screening.hall, screening.starts_at

-- a film that does not exist
INSERT INTO screening (movie_id, hall, starts_at, price) VALUES (99, 'C', '2026-11-08 18:00', 400);
-- FOREIGN KEY constraint failed

-- more refusals that are possible: price 0 (CHECK), sold -5 (CHECK), no price at all (NOT NULL)
