from abc import ABC, abstractmethod

from models.actor import Actor


class ActorService(ABC):
    """
    What a page may ask for when it needs actors.

    This class only says WHAT can be done (it is an abstract class, an "interface").
    HOW it is done is written in a class that inherits from it - see FileActorService.
    The pages know only about ActorService, so the place where the actors come from
    can be changed later without changing the pages.
    """

    @abstractmethod
    def get_actors(self, reload: bool = False) -> list[Actor]:
        """Returns all the actors. With reload=True the actors are obtained again from their source."""

    @abstractmethod
    def add(self, first_name: str, last_name: str, country: str) -> list[Actor]:
        """Adds a new actor, and returns all the actors."""

    @abstractmethod
    def delete(self, actor: Actor) -> list[Actor]:
        """Removes the actor, and returns the remaining actors."""
