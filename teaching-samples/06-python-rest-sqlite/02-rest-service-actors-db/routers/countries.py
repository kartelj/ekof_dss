from fastapi import APIRouter, HTTPException, Response, status
from sqlmodel import select

from database import SessionDep
from models.country import Country, CountryData

router = APIRouter(prefix="/api/countries", tags=["countries"])


# GET: api/countries
@router.get("")
def get_countries(session: SessionDep) -> list[CountryData]:
    countries = session.exec(select(Country)).all()
    return [CountryData.model_validate(country) for country in countries]


# GET: api/countries/5
@router.get("/{country_id}")
def get_country(country_id: int, session: SessionDep) -> CountryData:
    country = session.get(Country, country_id)
    if country is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Country not found")
    return CountryData.model_validate(country)


# PUT: api/countries/5
@router.put("/{country_id}", status_code=status.HTTP_204_NO_CONTENT)
def put_country(country_id: int, data: CountryData, session: SessionDep) -> None:
    if country_id != data.country_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The id in the address and the country_id in the body are different",
        )

    country = session.get(Country, country_id)
    if country is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Country not found")

    country.name = data.name
    country.code = data.code
    session.add(country)
    session.commit()


# POST: api/countries
@router.post("", status_code=status.HTTP_201_CREATED)
def post_country(data: CountryData, session: SessionDep, response: Response) -> CountryData:
    country = Country.model_validate(data)
    country.country_id = None  # the key of a new row is always assigned by the DBMS
    session.add(country)
    session.commit()
    session.refresh(country)

    response.headers["Location"] = f"/api/countries/{country.country_id}"
    return CountryData.model_validate(country)


# DELETE: api/countries/5
@router.delete("/{country_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_country(country_id: int, session: SessionDep) -> None:
    country = session.get(Country, country_id)
    if country is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Country not found")

    session.delete(country)
    session.commit()
