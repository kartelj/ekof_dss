-- Queries over the database VanityFair01 (one table: movie).
-- Execute them one by one, and look at the result of each.

-- all the columns of all the rows
SELECT * FROM movie;

-- only some columns
SELECT title, year, imdb_score FROM movie;

-- only the rows that satisfy a condition
SELECT title, year FROM movie WHERE states = 'France';

SELECT title, imdb_score FROM movie WHERE imdb_score >= 8;

SELECT title, year FROM movie WHERE year BETWEEN 1990 AND 1999;

-- several conditions
SELECT title, genre, year FROM movie WHERE states = 'USA' AND year < 2000;

SELECT title, genre FROM movie WHERE genre = 'comedy' OR genre = 'crime comedy';

-- patterns: % stands for any text, _ for exactly one character
SELECT title, genre FROM movie WHERE genre LIKE '%comedy%';

SELECT title, actors FROM movie WHERE actors LIKE '%John Goodman%';

-- the order of the rows in the result
SELECT title, imdb_score FROM movie ORDER BY imdb_score DESC;

SELECT title, states, year FROM movie ORDER BY states, year DESC;

-- only the first rows of the result
SELECT title, imdb_score FROM movie ORDER BY imdb_score DESC LIMIT 3;

-- expressions and names for the columns of the result
SELECT title, lasting / 60 AS hours, lasting % 60 AS minutes FROM movie;

SELECT title || ' (' || year || ')' AS film FROM movie;

-- different values only
SELECT DISTINCT states FROM movie;

-- aggregate functions: one row for the whole table ...
SELECT COUNT(*) AS films, AVG(imdb_score) AS average_score, MIN(year) AS oldest, MAX(year) AS newest
FROM movie;

-- ... or one row for every group
SELECT states, COUNT(*) AS films, AVG(lasting) AS average_lasting
FROM movie
GROUP BY states;

-- only the groups that satisfy a condition
SELECT genre, COUNT(*) AS films
FROM movie
GROUP BY genre
HAVING COUNT(*) > 1
ORDER BY films DESC;

-- a query inside a query: the films with the highest score
SELECT title, imdb_score FROM movie WHERE imdb_score = (SELECT MAX(imdb_score) FROM movie);

-- changing the data
UPDATE movie SET profit = 1000000 WHERE title = 'Fargo';

UPDATE movie SET lasting = lasting + 1 WHERE states = 'France';

INSERT INTO movie (title, genre, states, year) VALUES ('A film that will be deleted', 'test', 'Nowhere', 2026);

DELETE FROM movie WHERE genre = 'test';
