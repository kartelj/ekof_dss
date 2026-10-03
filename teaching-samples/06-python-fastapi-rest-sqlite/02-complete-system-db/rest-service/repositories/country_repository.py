from sqlmodel import Session, select

from dtos.country_dto import CountryDTO
from models.country import Country


def to_dto(country: Country) -> CountryDTO:
    return CountryDTO(id=country.country_id, name=country.name, code=country.code)


class CountryRepository:
    """Reads and writes the table country. The rest of the service sees only CountryDTO objects."""

    def __init__(self, session: Session):
        self._session = session

    def get_all(self) -> list[CountryDTO]:
        countries = self._session.exec(select(Country)).all()
        return [to_dto(c) for c in countries]

    def get_by_id(self, id: int) -> CountryDTO | None:
        country = self._session.get(Country, id)
        if country is None:
            return None
        return to_dto(country)

    def create(self, country_dto: CountryDTO) -> CountryDTO:
        new_country = Country(name=country_dto.name, code=country_dto.code)
        self._session.add(new_country)
        self._session.commit()
        self._session.refresh(new_country)
        return to_dto(new_country)

    def update(self, country_dto: CountryDTO) -> bool:
        """Returns False if there is no country with the given id."""
        country_to_update = self._session.get(Country, country_dto.id)
        if country_to_update is None:
            return False
        country_to_update.code = country_dto.code
        country_to_update.name = country_dto.name
        self._session.add(country_to_update)
        self._session.commit()
        return True

    def delete(self, id: int) -> bool:
        """Returns False if there is no country with the given id."""
        country_to_delete = self._session.get(Country, id)
        if country_to_delete is None:
            return False
        self._session.delete(country_to_delete)
        self._session.commit()
        return True
