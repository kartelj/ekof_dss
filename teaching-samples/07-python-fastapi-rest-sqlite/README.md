# 07 - The complete system

Everything from the previous modules, put together:

```text
browser  <-- HTML -->  web application  <-- JSON -->  RESTful service  <-->  database
                       web-app                         rest-service           actors.db
                       localhost:8000                  localhost:8001
```

The system consists of two programs. Start them in two terminals, the service first:

```text
cd 02-complete-system-db/rest-service
python main.py
```

```text
cd 02-complete-system-db/web-app
python main.py
```

Then open <http://localhost:8000> (the application) and <http://localhost:8001/docs> (the service).
If the service is not running, the application shows a page that says so.

| Version | Content |
|---|---|
| `01-complete-system-db` | the actors application of module 04, with its data moved into a RESTful service; countries can only be read |
| `02-complete-system-db` | actors and countries, both with all the operations; an actor refers to its country by `country_id` |

## What to look at

- **The web application did not have to be rewritten.** Compare `01-complete-system-db/web-app` with the last
  step of module 04: the pages are almost the same. They know only the abstract class `ActorService`;
  the new class `RestActorService` (`services/rest_actor_service.py`) calls the RESTful service with the
  library `httpx2`, and `dependencies.py` hands it over to the pages.
- **The service is built in layers** (`rest-service`): `routers` receive the requests, `repositories` read and
  write the database, `models` are the classes mapped to the tables, and `dtos` describe the data that travels
  to the clients - which need not look like a row of a table.
- **Nothing is kept in the web application.** Add an actor, restart the web application, and the actor is still there:
  the data lives in the database of the service (`rest-service/actors.db`). Delete that file to start again.
- **Rules are checked by the service.** Try to delete a country that still has actors, and look at the messages.
