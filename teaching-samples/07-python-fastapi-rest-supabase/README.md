# 07 - The complete system, with the data in Supabase

```text
browser  <-- HTML -->  web application  <-- JSON -->  RESTful service  <-- JSON -->  Supabase
                       web-app                         rest-service                   (PostgreSQL in the cloud)
                       localhost:8000                  localhost:8001
```

Before the first run, prepare your Supabase project and the file `.env` as described in
[05-python-db-supabase/README.md](https://github.com/kartelj/ekof_dss/blob/main/teaching-samples/05-python-db-supabase/README.md); the file `.env.example` is in the main folder of these samples.

The system consists of two programs. Start them in two terminals, the service first:

```text
cd 01-complete-system-supabase/rest-service
python main.py
```

```text
cd 01-complete-system-supabase/web-app
python main.py
```

Then open <http://localhost:8000> (the application) and <http://localhost:8001/docs> (the service).

## What to look at

- **The RESTful service** offers actors and countries with all the operations, and one more address:
  `GET /api/actors/with-country` returns the actors together with the name and the code of their country.
  The join is done by a function of the database (`get_actors_with_country` in
  `05-python-db-supabase/database/create-tables.sql`), which the service calls.
- **The web application** knows nothing about Supabase: it talks only to the RESTful service. Only the file `.env`
  of the service contains the key of the project.
- **The pages are styled with Bootstrap**: tables, forms, buttons and the menu use the classes from the lecture
  about Bootstrap. The table of actors can be ordered by a column - click the title of a column.
