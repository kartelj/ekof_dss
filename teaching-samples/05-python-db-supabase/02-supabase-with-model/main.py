"""
Using a database in the cloud (Supabase) through its Python client and a model class.

    python main.py

The client hides the HTTP requests of the previous sample: we say what we want
(table, select, insert ...), and it sends the requests and reads the answers.
"""

import datetime
import os
import sys

from dotenv import load_dotenv
from supabase import create_client

from actor import Actor


def main():
    # init
    load_dotenv()  # reads the settings from the file .env into os.environ

    supabase_url = os.environ.get("SUPABASE_URL")
    supabase_key = os.environ.get("SUPABASE_SECRET_KEY")
    if not supabase_url or not supabase_key:
        sys.exit("SUPABASE_URL and SUPABASE_SECRET_KEY are not set - see the file .env.example")

    supabase = create_client(supabase_url, supabase_key)

    # A result can be fetched like so.
    result = supabase.table("actor").select("*").execute()
    actors = [Actor.model_validate(row) for row in result.data]  # result.data is a list of dictionaries

    print(len(actors))
    for actor in actors:
        print(actor)

    model = Actor(
        first_name="Robert",
        last_name="De Niro",
        date_of_birth=datetime.date(1943, 8, 17),
    )

    # the model is sent as JSON, without the values that the DBMS assigns by itself
    row = model.model_dump(mode="json", exclude={"actor_id", "created_at"})
    result = supabase.table("actor").insert(row).execute()

    print(Actor.model_validate(result.data[0]))  # the new row, as it is stored in the table


if __name__ == "__main__":
    main()
