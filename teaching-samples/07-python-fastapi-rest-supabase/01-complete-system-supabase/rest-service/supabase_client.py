"""
The connection with the Supabase project.

The address and the secret key of the project are read from the file .env
(see the file .env.example in the main folder of the samples).
"""

import os
from typing import Annotated

from dotenv import load_dotenv
from fastapi import Depends
from supabase import Client, create_client

load_dotenv()  # reads the settings from the file .env into os.environ

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_SECRET_KEY = os.environ.get("SUPABASE_SECRET_KEY")
if not SUPABASE_URL or not SUPABASE_SECRET_KEY:
    raise SystemExit("SUPABASE_URL and SUPABASE_SECRET_KEY are not set - see the file .env.example")

# one client for the whole service
_supabase = create_client(SUPABASE_URL, SUPABASE_SECRET_KEY)


def get_supabase() -> Client:
    return _supabase


# the functions of the service declare the client as a parameter of this type
SupabaseDep = Annotated[Client, Depends(get_supabase)]
