from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Response, status

from database import get_country_repository
from dtos.country_dto import CountryDTO
from repositories.country_repository import CountryRepository

router = APIRouter(prefix="/api/countries", tags=["countries"])

CountryRepo = Annotated[CountryRepository, Depends(get_country_repository)]


@router.get("")
def get_all(country_repo: CountryRepo) -> list[CountryDTO]:
    return country_repo.get_all()


@router.get("/{id}")
def get_by_id(id: int, country_repo: CountryRepo) -> CountryDTO:
    country = country_repo.get_by_id(id)
    if country is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Country not found")
    return country


@router.post("", status_code=status.HTTP_201_CREATED)
def create(model: CountryDTO, country_repo: CountryRepo, response: Response) -> CountryDTO:
    country = country_repo.create(model)

    response.headers["Location"] = f"/api/countries/{country.id}"
    return country


@router.put("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def update(id: int, model: CountryDTO, country_repo: CountryRepo) -> None:
    if id != model.id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The id in the address and the id in the body are different",
        )
    if not country_repo.update(model):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Country not found")


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, country_repo: CountryRepo) -> None:
    """A country that still has actors can not be deleted: the database refuses it (409)."""
    if not country_repo.delete(id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Country not found")
