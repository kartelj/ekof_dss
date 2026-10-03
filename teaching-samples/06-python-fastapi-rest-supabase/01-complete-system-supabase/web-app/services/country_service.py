from abc import ABC, abstractmethod

from models.country import Country


class CountryService(ABC):
    """
    What a page may ask for when it needs countries.

    The methods that change the data return True if the change has been carried out,
    and False if it has been refused.
    """

    @abstractmethod
    def get_countries(self) -> list[Country]:
        """Returns all the countries."""

    @abstractmethod
    def add(self, country_code: str, country_name: str) -> bool:
        """Adds a new country."""

    @abstractmethod
    def delete(self, country: Country) -> bool:
        """Removes the country."""

    @abstractmethod
    def update(self, country: Country) -> bool:
        """Stores the changed data of the country."""
