from abc import ABC, abstractmethod

from models.actor import Actor


class ActorService(ABC):
    """
    What a page may ask for when it needs actors.

    This class only says WHAT can be done (it is an abstract class, an "interface").
    HOW it is done is written in a class that inherits from it - see RestActorService.

    The methods that change the data return True if the change has been carried out,
    and False if it has been refused.
    """

    @abstractmethod
    def get_actors(self) -> list[Actor]:
        """Returns all the actors."""

    @abstractmethod
    def add(self, first_name: str, last_name: str, country_id: int) -> bool:
        """Adds a new actor."""

    @abstractmethod
    def delete(self, actor: Actor) -> bool:
        """Removes the actor."""

    @abstractmethod
    def update(self, actor: Actor) -> bool:
        """Stores the changed data of the actor."""

    @abstractmethod
    def search(self, fn: str, ln: str, c: str) -> list[Actor]:
        """
        Returns the actors whose first name contains fn,
        or whose last name contains ln, or whose country code contains c.
        """
