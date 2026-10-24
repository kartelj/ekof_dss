# 05 - A database in the cloud: Supabase

[Supabase](https://supabase.com) is a cloud service built around the PostgreSQL DBMS. Besides the database,
it gives every project a RESTful service for its tables (the *Data API*), so a program can use the database
through HTTP requests.

The Supabase samples of the course (this folder, `06-python-rest-supabase` and `07-python-fastapi-rest-supabase`)
use one Supabase project. Prepare it once:

1. Create a project in the Supabase dashboard.
2. Open the **SQL Editor** of the project, paste the content of `database/create-tables.sql`, and run it.
   The script creates the tables `country` and `actor` with a few rows, and a function that joins them.
3. Find the address of the project and its **secret key** (the dialog **Connect**, or **Settings > API Keys**).
4. In the root folder of the course, copy the file `.env.example`, name the copy `.env`, and write the two values into it:

   ```text
   SUPABASE_URL=https://your-project.supabase.co
   SUPABASE_SECRET_KEY=sb_secret_...
   ```

The secret key gives full access to the data of the project. It is meant for programs that run on a server,
like the Python programs of this course. Never put it into a web page, into source code or into git -
the file `.env` is excluded from git for that reason.

## The samples

| Sample | How it works |
|---|---|
| `01-supabase-with-request` | the program sends HTTP requests to the Data API itself, with the library `httpx2` |
| `02-supabase-with-model` | the program uses the Python client of Supabase and the model class `Actor` |

```text
cd 01-supabase-with-request
python main.py
```

Both programs show the rows of the table `actor`, and add one row. Compare them with the two SQLite samples
in `05-python-db-sqlite`: the task is the same, only the database is somewhere else.
