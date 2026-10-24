import httpx2


class SupabaseService:
    """
    Reads and writes the tables of a Supabase project by sending HTTP requests.

    Supabase puts a RESTful service in front of the database (the Data API):
    every table has an address,  <address of the project>/rest/v1/<name of the table> .
    """

    def __init__(self, supabase_url: str, supabase_key: str):
        # a client that remembers the address of the project and sends the key with every request
        self._client = httpx2.Client(
            base_url=supabase_url,
            headers={
                "apikey": supabase_key,
                "Authorization": f"Bearer {supabase_key}",
            },
        )

    def get_data(self, table_name: str) -> str:
        response = self._client.get(f"/rest/v1/{table_name}", params={"select": "*"})
        response.raise_for_status()  # an answer such as 401 or 404 becomes an exception
        return response.text

    def insert_data(self, table_name: str, data: dict) -> str:
        # the dictionary is sent as JSON; the header Prefer asks the service to send the new row back
        response = self._client.post(
            f"/rest/v1/{table_name}",
            json=data,
            headers={"Prefer": "return=representation"},
        )
        response.raise_for_status()
        return response.text

    def close(self) -> None:
        self._client.close()
