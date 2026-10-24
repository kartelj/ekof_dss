# The API of the films

A REST API for the films of the database VanityFair02 and their genres.
The service runs at `http://localhost:8001`.

## 1. The resources and their addresses

| Address | Resource |
|---|---|
| `/api/movies` | the collection: all films |
| `/api/movies/4` | one item: the film with id 4 |
| `/api/genres` | all genres |
| `/api/genres/4` | the genre with id 4 |

The addresses are nouns in the plural. The method says what to do with the resource.

## 2. The JSON of one film

```json
{"movie_id": 4, "title": "Fargo", "year": 1996, "lasting": 98, "genre_id": 4}
```

- `lasting` is the length of the film in minutes.
- The genre is given by its id; its name is in another resource: `/api/genres/4` gives `{"genre_id": 4, "name": "crime"}`.
- In a `POST` the client does not send `movie_id`: the service chooses it.

## 3. The operations

### Read all films

```http
GET /api/movies HTTP/1.1
Host: localhost:8001
```

```http
HTTP/1.1 200 OK
Content-Type: application/json

[{"movie_id": 1, "title": "Raising Arizona", "year": 1987, "lasting": 94, "genre_id": 1},
 {"movie_id": 2, "title": "Miller's Crossing", "year": 1990, "lasting": 115, "genre_id": 2},
 ...]
```

### Read one film

```http
GET /api/movies/4 HTTP/1.1
Host: localhost:8001
```

```http
HTTP/1.1 200 OK
Content-Type: application/json

{"movie_id": 4, "title": "Fargo", "year": 1996, "lasting": 98, "genre_id": 4}
```

Unsuccessful: `GET /api/movies/99` - there is no such film.

```http
HTTP/1.1 404 Not Found
Content-Type: application/json

{"detail": "Movie not found"}
```

### Create a film

The year is wrong on purpose (2006 instead of 2008); the next request corrects it.

```http
POST /api/movies HTTP/1.1
Host: localhost:8001
Content-Type: application/json

{"title": "Burn After Reading", "year": 2006, "lasting": 96, "genre_id": 5}
```

```http
HTTP/1.1 201 Created
Content-Type: application/json
Location: /api/movies/11

{"movie_id": 11, "title": "Burn After Reading", "year": 2006, "lasting": 96, "genre_id": 5}
```

Unsuccessful: the year is a text, not a number. Nothing is saved.

```http
POST /api/movies HTTP/1.1
Host: localhost:8001
Content-Type: application/json

{"title": "Burn After Reading", "year": "two thousand eight", "lasting": 96, "genre_id": 5}
```

```http
HTTP/1.1 422 Unprocessable Content
Content-Type: application/json

{"detail": [{"type": "int_parsing", "loc": ["body", "year"],
             "msg": "Input should be a valid integer, unable to parse string as an integer",
             "input": "two thousand eight"}]}
```

Also possible: a film of a genre that does not exist (`"genre_id": 99`) - `409 Conflict`.

### Update a film

The client sends the **whole** film, with the corrected year.

```http
PUT /api/movies/11 HTTP/1.1
Host: localhost:8001
Content-Type: application/json

{"movie_id": 11, "title": "Burn After Reading", "year": 2008, "lasting": 96, "genre_id": 5}
```

```http
HTTP/1.1 204 No Content
```

Unsuccessful: the id in the address (11) and `movie_id` in the body (12) differ.

```http
HTTP/1.1 400 Bad Request
Content-Type: application/json

{"detail": "The id in the address and the movie_id in the body are different"}
```

Also `404 Not Found` for `PUT /api/movies/99`, and `422` for invalid data, as with `POST`.

### Delete a film

```http
DELETE /api/movies/11 HTTP/1.1
Host: localhost:8001
```

```http
HTTP/1.1 204 No Content
```

Unsuccessful: the same request once more - the film does not exist any more.

```http
HTTP/1.1 404 Not Found
Content-Type: application/json

{"detail": "Movie not found"}
```

### The genres

`GET /api/genres` gives all seven genres, `GET /api/genres/4` one of them (`200`), and
`GET /api/genres/99` gives `404 Not Found` with `{"detail": "Genre not found"}`.

## 4. Safe and idempotent

| Request | Safe | Idempotent |
|---|---|---|
| `GET /api/movies`, `GET /api/movies/4`, `GET /api/genres` ... | yes | yes |
| `PUT /api/movies/11` | no | yes - the film gets the same values again |
| `DELETE /api/movies/11` | no | yes - the film stays deleted (the second answer is `404`) |
| `POST /api/movies` | no | no - two requests create two films, 11 and 12 |
