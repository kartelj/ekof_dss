# 06 - RESTful services, with the data in Supabase

The same as `06-python-rest-sqlite`, with one difference: the service keeps the actors in a Supabase project
(a PostgreSQL database in the cloud) instead of a SQLite file.

| Sample | What it is |
|---|---|
| `01-rest-service-new` | the smallest service: one resource, the weather forecast (it does not use a database) |
| `02-rest-service-actors-supabase` | a service for actors, with the data in Supabase |

Before the first run of the second sample, prepare your Supabase project and the file `.env` as described in
[05-python-db-supabase/README.md](https://github.com/kartelj/ekof_dss/blob/main/teaching-samples/05-python-db-supabase/README.md); the file `.env.example` is in the main folder of these samples.

```text
cd 02-rest-service-actors-supabase
python main.py
```

Then open <http://localhost:8001/docs>.

For the clients nothing is different: the addresses, the methods and the status codes are those of the SQLite version.
Inside, the functions in `routers/actors.py` do not use SQLModel - they call the Python client of Supabase
(`supabase_client.py`), which sends HTTP requests to the Data API of the project. The service is therefore
a server for its own clients, and a client of Supabase at the same time.
