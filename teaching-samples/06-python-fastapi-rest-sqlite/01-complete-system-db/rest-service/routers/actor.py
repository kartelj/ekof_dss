from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Response, status

from database import get_actor_repository, get_country_repository
from dtos.actor_dto import ActorCreateDTO, ActorDTO, ActorUpdateDTO
from models.actor import Actor
from models.country import Country
from repositories.actor_repository import ActorRepository
from repositories.country_repository import CountryRepository

router = APIRouter(prefix="/api/actors", tags=["actors"])

# the repositories are handed over by FastAPI (dependency injection)
ActorRepo = Annotated[ActorRepository, Depends(get_actor_repository)]
CountryRepo = Annotated[CountryRepository, Depends(get_country_repository)]


def to_dto(actor: Actor) -> ActorDTO:
    """Makes the object that is sent to the client from a row of the table."""
    return ActorDTO(
        id=actor.actor_id,
        last_name=actor.last_name,
        first_name=actor.first_name,
        country_code=actor.country.code,
        date_of_birth=actor.date_of_birth,
    )


def find_country(country_repo: CountryRepository, code: str) -> Country:
    country = country_repo.get_by_code(code)
    if country is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"There is no country with the code {code}"
        )
    return country


@router.get("")
def get_all(actor_repo: ActorRepo) -> list[ActorDTO]:
    actors = actor_repo.get_all()
    # a list comprehension: the list of the results of to_dto(a), for every a in actors
    return [to_dto(a) for a in actors]


@router.get("/{id}")
def get_by_id(id: int, actor_repo: ActorRepo) -> ActorDTO:
    actor = actor_repo.get_by_id(id)
    if actor is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Actor not found")
    return to_dto(actor)


@router.post("", status_code=status.HTTP_201_CREATED)
def create(
    model: ActorCreateDTO, actor_repo: ActorRepo, country_repo: CountryRepo, response: Response
) -> ActorDTO:
    country = find_country(country_repo, model.country_code)
    actor = actor_repo.create(model, country)

    response.headers["Location"] = f"/api/actors/{actor.actor_id}"
    return to_dto(actor)


@router.put("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def update(id: int, model: ActorUpdateDTO, actor_repo: ActorRepo, country_repo: CountryRepo) -> None:
    if id != model.id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The id in the address and the id in the body are different",
        )
    actor = actor_repo.get_by_id(id)
    if actor is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Actor not found")

    country = find_country(country_repo, model.country_code)
    actor_repo.update(actor, model, country)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, actor_repo: ActorRepo) -> None:
    actor = actor_repo.get_by_id(id)
    if actor is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Actor not found")

    actor_repo.delete(actor)
