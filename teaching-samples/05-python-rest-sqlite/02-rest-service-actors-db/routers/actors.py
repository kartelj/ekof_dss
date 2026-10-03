from fastapi import APIRouter, HTTPException, Response, status
from sqlmodel import select

from database import SessionDep
from models.actor import Actor, ActorData

router = APIRouter(prefix="/api/actors", tags=["actors"])


# GET: api/actors
@router.get("")
def get_actors(session: SessionDep) -> list[ActorData]:
    actors = session.exec(select(Actor)).all()
    # every row of the table becomes an ActorData object - the data that is sent to the client
    return [ActorData.model_validate(actor) for actor in actors]


# GET: api/actors/5
@router.get("/{actor_id}")
def get_actor(actor_id: int, session: SessionDep) -> ActorData:
    actor = session.get(Actor, actor_id)

    if actor is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Actor not found")

    return ActorData.model_validate(actor)


# PUT: api/actors/5
@router.put("/{actor_id}", status_code=status.HTTP_204_NO_CONTENT)
def put_actor(actor_id: int, data: ActorData, session: SessionDep) -> None:
    """The parameter data is made from the JSON in the body of the request."""
    if actor_id != data.actor_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The id in the address and the actor_id in the body are different",
        )

    actor = session.get(Actor, actor_id)
    if actor is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Actor not found")

    actor.last_name = data.last_name
    actor.first_name = data.first_name
    actor.country_id = data.country_id
    actor.date_of_birth = data.date_of_birth
    session.add(actor)
    session.commit()


# POST: api/actors
@router.post("", status_code=status.HTTP_201_CREATED)
def post_actor(data: ActorData, session: SessionDep, response: Response) -> ActorData:
    actor = Actor.model_validate(data)  # makes a row for the table from the received data
    actor.actor_id = None  # the key of a new row is always assigned by the DBMS
    session.add(actor)
    session.commit()
    session.refresh(actor)  # reads the new row back, with the actor_id assigned by the DBMS

    # the answer tells the address of the new resource
    response.headers["Location"] = f"/api/actors/{actor.actor_id}"
    return ActorData.model_validate(actor)


# DELETE: api/actors/5
@router.delete("/{actor_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_actor(actor_id: int, session: SessionDep) -> None:
    actor = session.get(Actor, actor_id)
    if actor is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Actor not found")

    session.delete(actor)
    session.commit()
