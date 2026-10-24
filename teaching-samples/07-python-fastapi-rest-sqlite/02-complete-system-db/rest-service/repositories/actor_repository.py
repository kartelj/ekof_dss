from sqlmodel import Session, select

from dtos.actor_dto import ActorDTO
from models.actor import Actor


def to_dto(actor: Actor) -> ActorDTO:
    """Makes the object that is sent to the clients from a row of the table (and its country)."""
    return ActorDTO(
        id=actor.actor_id,
        last_name=actor.last_name,
        first_name=actor.first_name,
        country_id=actor.country.country_id,
        country_name=actor.country.name,
        country_code=actor.country.code,
        date_of_birth=actor.date_of_birth,
    )


class ActorRepository:
    """Reads and writes the table actor. The rest of the service sees only ActorDTO objects."""

    def __init__(self, session: Session):
        self._session = session

    def get_all(self) -> list[ActorDTO]:
        actors = self._session.exec(select(Actor)).all()
        # a list comprehension: the list of the results of to_dto(a), for every a in actors
        return [to_dto(a) for a in actors]

    def get_by_id(self, id: int) -> ActorDTO | None:
        actor = self._session.get(Actor, id)
        if actor is None:
            return None
        return to_dto(actor)

    def create(self, actor_dto: ActorDTO) -> ActorDTO:
        new_actor = Actor(
            first_name=actor_dto.first_name,
            last_name=actor_dto.last_name,
            country_id=actor_dto.country_id,
            date_of_birth=actor_dto.date_of_birth,
        )
        self._session.add(new_actor)
        self._session.commit()
        self._session.refresh(new_actor)  # reads the new row back, with its actor_id
        return to_dto(new_actor)

    def update(self, actor_dto: ActorDTO) -> bool:
        """Returns False if there is no actor with the given id."""
        actor_to_update = self._session.get(Actor, actor_dto.id)
        if actor_to_update is None:
            return False
        actor_to_update.first_name = actor_dto.first_name
        actor_to_update.last_name = actor_dto.last_name
        actor_to_update.country_id = actor_dto.country_id
        actor_to_update.date_of_birth = actor_dto.date_of_birth
        self._session.add(actor_to_update)
        self._session.commit()
        return True

    def delete(self, id: int) -> bool:
        """Returns False if there is no actor with the given id."""
        actor_to_delete = self._session.get(Actor, id)
        if actor_to_delete is None:
            return False
        self._session.delete(actor_to_delete)
        self._session.commit()
        return True
