# 06 - RESTful services

A RESTful service does not send pages for people - it sends data, in the JSON format, for other programs.

| Sample | What it is |
|---|---|
| `01-rest-service-new` | the smallest service: one resource, the weather forecast |
| `02-rest-service-actors-db` | a service for actors and countries, with the data in a SQLite database |

```text
cd 02-rest-service-actors-db
python main.py
```

Then open <http://localhost:8001/docs> - the interactive documentation, which FastAPI makes from the code.
Every operation of the service can be tried there.

## The service for actors

| Request | Meaning | Answers |
|---|---|---|
| `GET /api/actors` | all the actors | `200` |
| `GET /api/actors/5` | the actor 5 | `200`, `404` |
| `POST /api/actors` | adds an actor | `201` (with the header `Location`), `409`, `422` |
| `PUT /api/actors/5` | changes the actor 5 | `204`, `400`, `404`, `409`, `422` |
| `DELETE /api/actors/5` | deletes the actor 5 | `204`, `404` |

The same operations exist for `/api/countries`.

The service can also be tried from the terminal, with the tool `curl`:

```text
curl http://localhost:8001/api/actors/3

curl -i -X POST http://localhost:8001/api/actors -H "Content-Type: application/json" -d "{\"last_name\": \"Streep\", \"first_name\": \"Meryl\", \"country_id\": 1}"

curl -i -X DELETE http://localhost:8001/api/actors/14
```

## The parts of the service

| File or folder | Purpose |
|---|---|
| `main.py` | creates the application, and adds the routers to it |
| `routers/` | the functions that answer the requests, one module per resource |
| `models/` | the classes for the data: what arrives in a request (`ActorData`), and the row of the table (`Actor`) |
| `database.py` | the connection with the database, and the first data |

The database is the file `actors.db`. It is created when the service starts for the first time;
delete the file to start again from the original data.
