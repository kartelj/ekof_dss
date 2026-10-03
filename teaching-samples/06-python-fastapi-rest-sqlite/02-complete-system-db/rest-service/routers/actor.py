from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Response, status

from database import get_actor_repository, get_country_repository
from dtos.actor_dto import ActorDTO
from repositories.actor_repository import ActorRepository
from repositories.country_repository import CountryRepository

router = APIRouter(prefix="/api/actors", tags=["actors"])

# the repositories are handed over by FastAPI (dependency injection)
ActorRepo = Annotated[ActorRepository, Depends(get_actor_repository)]
CountryRepo = Annotated[CountryRepository, Depends(get_country_repository)]


def check_country(country_repo: CountryRepository, country_id: int) -> None:
    """An actor can belong only to a country that exists."""
    if country_repo.get_by_id(country_id) is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"There is no country with the id {country_id}",
        )


@router.get("")
def get_all(actor_repo: ActorRepo) -> list[ActorDTO]:
    return actor_repo.get_all()


@router.get("/{id}")
def get_by_id(id: int, actor_repo: ActorRepo) -> ActorDTO:
    actor = actor_repo.get_by_id(id)
    if actor is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Actor not found")
    return actor


@router.post("", status_code=status.HTTP_201_CREATED)
def create(
    model: ActorDTO, actor_repo: ActorRepo, country_repo: CountryRepo, response: Response
) -> ActorDTO:
    check_country(country_repo, model.country_id)
    actor = actor_repo.create(model)

    response.headers["Location"] = f"/api/actors/{actor.id}"
    return actor


@router.put("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def update(id: int, model: ActorDTO, actor_repo: ActorRepo, country_repo: CountryRepo) -> None:
    if id != model.id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The id in the address and the id in the body are different",
        )
    check_country(country_repo, model.country_id)

    if not actor_repo.update(model):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Actor not found")


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, actor_repo: ActorRepo) -> None:
    if not actor_repo.delete(id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Actor not found")
