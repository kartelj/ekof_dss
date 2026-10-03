from sqlmodel import Session, select

from models.country import Country


class CountryRepository:
    """Reads the table country."""

    def __init__(self, session: Session):
        self._session = session

    def get_all(self) -> list[Country]:
        return self._session.exec(select(Country)).all()

    def get_by_code(self, code: str) -> Country | None:
        """Returns the country with the given code, or None if there is no such country."""
        # the same as: SELECT * FROM country WHERE code = ...   (the codes are stored in upper case)
        statement = select(Country).where(Country.code == code.upper())
        return self._session.exec(statement).first()
