# Assignment: a service for films - a solution

The assignment of the lecture *RESTful services with FastAPI*: a RESTful service for the films of
VanityFair02 and their genres, with SQLModel and SQLite - the API that was designed in the assignment
of the lecture *Introduction to REST APIs* ([06-01-restful-api](../06-01-restful-api/)).

| Request | Answer |
|---|---|
| `GET /api/genres`, `GET /api/genres/4` | `200`, or `404` for a genre that does not exist |
| `GET /api/movies`, `GET /api/movies/4` | `200`, or `404` |
| `POST /api/movies` | `201` with `Location: /api/movies/11`, `422` for invalid data, `409` for a genre that does not exist |
| `PUT /api/movies/11` | `204`, `400` if the ids differ, `404`, `422`, `409` |
| `DELETE /api/movies/11` | `204`, or `404` |
| `GET /api/genres/5/movies` (the bonus) | `200` and the films of the genre, or `404` |

The files - built like the sample `teaching-samples/06-python-rest-sqlite/02-rest-service-actors-db`:

- `main.py` - creates the application, includes the routers, turns `IntegrityError` into `409`
- `database.py` - the engine, the session, and the data of the first start (7 genres, 10 films)
- `models/genre.py`, `models/movie.py` - `GenreData` / `Genre`, `MovieData` / `Movie`
- `routers/genres.py`, `routers/movies.py` - one function for every operation
- `client.py` - the bonus: a client that prints every film with the name of its genre

## Running it

```text
python main.py
```

Then open `http://localhost:8001/docs`. The client runs in a second terminal: `python client.py`.

The file `movies.db` is created at the first start. To start again with the original data,
stop the service and delete the file.
