-- Queries over the database VanityFair02 (tables: genre, state, movie; view: vw_movie_profit).
-- Execute them one by one, and look at the result of each.

PRAGMA foreign_keys = ON;

-- Joining tables: every film with the name of its genre and of its state.
SELECT movie.title, genre.name AS genre, state.name AS state
FROM movie
     INNER JOIN genre ON genre.genre_id = movie.genre_id
     INNER JOIN state ON state.state_id = movie.state_id;

-- The same query written with short names (aliases) for the tables.
SELECT m.title, g.name AS genre, s.name AS state
FROM movie AS m
     INNER JOIN genre AS g ON g.genre_id = m.genre_id
     INNER JOIN state AS s ON s.state_id = m.state_id
WHERE s.code = 'FRA'
ORDER BY m.year;

-- Without a condition every row of one table is combined with every row of the other
-- (the cartesian product): 10 films x 7 genres = 70 rows. This is almost never what we want.
SELECT movie.title, genre.name FROM movie, genre;

-- INNER JOIN shows only the genres that have films ...
SELECT g.name, COUNT(*) AS films
FROM genre AS g
     INNER JOIN movie AS m ON m.genre_id = g.genre_id
GROUP BY g.name;

-- ... LEFT JOIN keeps all the genres; for a genre without films the columns of movie are NULL.
SELECT g.name, COUNT(m.movie_id) AS films
FROM genre AS g
     LEFT JOIN movie AS m ON m.genre_id = g.genre_id
GROUP BY g.name
ORDER BY films DESC;

-- Groups: number of films and average score per state.
SELECT s.name AS state, COUNT(*) AS films, ROUND(AVG(m.imdb_score), 2) AS average_score
FROM movie AS m
     INNER JOIN state AS s ON s.state_id = m.state_id
GROUP BY s.name
HAVING COUNT(*) >= 2;

-- Subqueries: states that have no films, genres that have films.
SELECT name FROM state WHERE state_id NOT IN (SELECT state_id FROM movie);

SELECT name FROM genre AS g WHERE EXISTS (SELECT * FROM movie AS m WHERE m.genre_id = g.genre_id);

-- Union: the rows of two queries in one result.
SELECT name, 'genre' AS kind FROM genre
UNION
SELECT name, 'state' AS kind FROM state
ORDER BY kind, name;

-- The view is used as if it were a table.
SELECT * FROM vw_movie_profit;

SELECT code, COUNT(*) AS films FROM vw_movie_profit GROUP BY code;

-- Referential integrity: both statements below are REFUSED by the DBMS
-- (remove the two dashes in front of them and try).
-- INSERT INTO movie (title, genre_id, state_id) VALUES ('A film of an unknown genre', 99, 1);
-- DELETE FROM genre WHERE genre_id = 1;

-- A transaction: several changes that are accepted (COMMIT) or cancelled (ROLLBACK) together.
BEGIN TRANSACTION;
UPDATE movie SET profit = profit + 500000 WHERE state_id = 2;
SELECT title, profit FROM movie WHERE state_id = 2;     -- the change is visible inside the transaction
ROLLBACK;
SELECT title, profit FROM movie WHERE state_id = 2;     -- ... and it is gone after the rollback
