from fastapi import APIRouter, HTTPException, Response, status

from models.country import Country
from supabase_client import SupabaseDep

router = APIRouter(prefix="/api/countries", tags=["countries"])


# GET: api/countries
@router.get("")
def get_countries(supabase: SupabaseDep) -> list[Country]:
    response = supabase.table("country").select("*").order("country_id").execute()
    return response.data


# GET: api/countries/4
@router.get("/{country_id}")
def get_country(country_id: int, supabase: SupabaseDep) -> Country:
    response = supabase.table("country").select("*").eq("country_id", country_id).execute()

    if not response.data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Country not found")

    return response.data[0]


# PUT: api/countries/4
@router.put("/{country_id}", status_code=status.HTTP_204_NO_CONTENT)
def put_country(country_id: int, new_data: Country, supabase: SupabaseDep) -> None:
    if country_id != new_data.country_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The id in the address and the country_id in the body are different",
        )

    row = new_data.model_dump(mode="json", exclude={"country_id", "created_at"})
    response = supabase.table("country").update(row).eq("country_id", country_id).execute()

    if not response.data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Country not found")


# POST: api/countries
@router.post("", status_code=status.HTTP_201_CREATED)
def post_country(country: Country, supabase: SupabaseDep, response: Response) -> Country:
    row = country.model_dump(mode="json", exclude={"country_id", "created_at"})
    result = supabase.table("country").insert(row).execute()
    new_country = result.data[0]

    response.headers["Location"] = f"/api/countries/{new_country['country_id']}"
    return new_country


# DELETE: api/countries/4
@router.delete("/{country_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_country(country_id: int, supabase: SupabaseDep) -> None:
    """A country that still has actors can not be deleted: the database refuses it (409)."""
    response = supabase.table("country").delete().eq("country_id", country_id).execute()

    if not response.data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Country not found")
