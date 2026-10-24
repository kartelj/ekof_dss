-- A view is a stored query. It is used in the same way as a table,
-- and it shows the current data of the tables it is built from.

CREATE VIEW vw_movie_profit
AS
SELECT movie.movie_id, movie.title, genre.short_name, state.code, movie.year, movie.profit
FROM genre
     INNER JOIN movie ON genre.genre_id = movie.genre_id
     INNER JOIN state ON movie.state_id = state.state_id;
