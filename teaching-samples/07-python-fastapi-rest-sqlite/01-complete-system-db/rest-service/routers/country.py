from typing import Annotated

from fastapi import APIRouter, Depends

from database import get_country_repository
from dtos.country_dto import CountryDTO
from repositories.country_repository import CountryRepository

router = APIRouter(prefix="/api/countries", tags=["countries"])

CountryRepo = Annotated[CountryRepository, Depends(get_country_repository)]


@router.get("")
def get_all(country_repo: CountryRepo) -> list[CountryDTO]:
    countries = country_repo.get_all()
    return [CountryDTO(id=c.country_id, name=c.name, code=c.code) for c in countries]
