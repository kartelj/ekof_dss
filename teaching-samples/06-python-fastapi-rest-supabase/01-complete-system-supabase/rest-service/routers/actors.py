from fastapi import APIRouter, HTTPException, Response, status

from models.actor import Actor
from models.actor_country import ActorCountry
from supabase_client import SupabaseDep

router = APIRouter(prefix="/api/actors", tags=["actors"])


# GET: api/actors
@router.get("")
def get_actors(supabase: SupabaseDep) -> list[Actor]:
    response = supabase.table("actor").select("*").order("actor_id").execute()
    return response.data  # a list of dictionaries, one for every row


# GET: api/actors/with-country
# (this function must be written before get_actor: otherwise "with-country" would be taken as an actor_id)
@router.get("/with-country")
def get_actors_with_country(supabase: SupabaseDep) -> list[ActorCountry]:
    # rpc = remote procedure call: the function of the database is called, and its result is returned
    response = supabase.rpc("get_actors_with_country").execute()
    return response.data


# GET: api/actors/5
@router.get("/{actor_id}")
def get_actor(actor_id: int, supabase: SupabaseDep) -> Actor:
    response = supabase.table("actor").select("*").eq("actor_id", actor_id).execute()

    if not response.data:  # an empty list: there is no such row
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Actor not found")

    return response.data[0]


# PUT: api/actors/5
@router.put("/{actor_id}", status_code=status.HTTP_204_NO_CONTENT)
def put_actor(actor_id: int, new_data: Actor, supabase: SupabaseDep) -> None:
    if actor_id != new_data.actor_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The id in the address and the actor_id in the body are different",
        )

    # the values that the DBMS assigns by itself are not sent
    row = new_data.model_dump(mode="json", exclude={"actor_id", "created_at"})
    response = supabase.table("actor").update(row).eq("actor_id", actor_id).execute()

    if not response.data:  # no row was changed
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Actor not found")


# POST: api/actors
@router.post("", status_code=status.HTTP_201_CREATED)
def post_actor(actor: Actor, supabase: SupabaseDep, response: Response) -> Actor:
    row = actor.model_dump(mode="json", exclude={"actor_id", "created_at"})
    result = supabase.table("actor").insert(row).execute()
    new_actor = result.data[0]  # the new row, as it is stored in the table

    # the answer tells the address of the new resource
    response.headers["Location"] = f"/api/actors/{new_actor['actor_id']}"
    return new_actor


# DELETE: api/actors/5
@router.delete("/{actor_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_actor(actor_id: int, supabase: SupabaseDep) -> None:
    response = supabase.table("actor").delete().eq("actor_id", actor_id).execute()

    if not response.data:  # no row was deleted
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Actor not found")
