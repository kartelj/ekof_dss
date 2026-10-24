-- Parts 4 to 8: queries over the screenings, a view and a transaction.

PRAGMA foreign_keys = ON;

-- 4. The programme of 6 November, sorted by the time and then by the hall.
SELECT substr(s.starts_at, 12, 5) AS time, s.hall, m.title
FROM screening AS s
     INNER JOIN movie AS m ON m.movie_id = s.movie_id
WHERE s.starts_at LIKE '2026-11-06%'
ORDER BY s.starts_at, s.hall;

-- 5. Tickets and income of every film that has screenings, the highest income first.
SELECT m.title, SUM(s.sold) AS tickets, SUM(s.price * s.sold) AS income
FROM screening AS s
     INNER JOIN movie AS m ON m.movie_id = s.movie_id
GROUP BY m.title
ORDER BY income DESC;

-- 6. The films that have no screening.
SELECT title
FROM movie
WHERE movie_id NOT IN (SELECT movie_id FROM screening)
ORDER BY title;

-- 7. A view of the programme, and the screenings of comedies from it.
CREATE VIEW vw_programme
AS
SELECT s.starts_at, s.hall, m.title, g.name AS genre, s.price
FROM screening AS s
     INNER JOIN movie AS m ON m.movie_id = s.movie_id
     INNER JOIN genre AS g ON g.genre_id = m.genre_id;

SELECT starts_at, hall, title FROM vw_programme WHERE genre = 'comedy' ORDER BY starts_at;

-- 8. Two changes that belong together: Delicatessen moves to hall C, and its price is 50 lower.
BEGIN TRANSACTION;
UPDATE screening SET hall = 'C' WHERE movie_id = 8 AND starts_at = '2026-11-07 21:00';
UPDATE screening SET price = price - 50 WHERE movie_id = 8 AND starts_at = '2026-11-07 21:00';
COMMIT;

SELECT * FROM vw_programme WHERE title = 'Delicatessen';
