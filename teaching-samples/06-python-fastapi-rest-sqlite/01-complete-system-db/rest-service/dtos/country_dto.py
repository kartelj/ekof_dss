from pydantic import BaseModel


class CountryDTO(BaseModel):
    """The data about a country as the clients of the service see it."""

    id: int | None = None
    name: str
    code: str
