"""
Using a database in the cloud (Supabase) by sending HTTP requests to it.

    python main.py

Before the first run: create the tables with database/create-tables.sql, and write
the address and the secret key of your Supabase project into the file .env
(see the file .env.example in the root folder of the course).
Every run adds one row, so run the program several times and watch the table grow.
"""

import os
import sys

from dotenv import load_dotenv

from supabase_service import SupabaseService


def main():
    load_dotenv()  # reads the settings from the file .env into os.environ

    supabase_url = os.environ.get("SUPABASE_URL")
    supabase_key = os.environ.get("SUPABASE_SECRET_KEY")
    if not supabase_url or not supabase_key:
        sys.exit("SUPABASE_URL and SUPABASE_SECRET_KEY are not set - see the file .env.example")

    service = SupabaseService(supabase_url, supabase_key)

    # Fetch data
    result = service.get_data("actor")
    print("Data from table:")
    print(result)

    # Insert data
    data = {"first_name": "Franco", "last_name": "Nero"}
    insert_result = service.insert_data("actor", data)
    print("Insert response:")
    print(insert_result)

    service.close()


if __name__ == "__main__":
    main()
