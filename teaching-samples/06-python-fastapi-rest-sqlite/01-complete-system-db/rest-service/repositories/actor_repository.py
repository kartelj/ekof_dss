from sqlmodel import Session, select

from dtos.actor_dto import ActorCreateDTO, ActorUpdateDTO
from models.actor import Actor
from models.country import Country


class ActorRepository:
    """Reads and writes the table actor."""

    def __init__(self, session: Session):
        self._session = session

    def get_all(self) -> list[Actor]:
        return self._session.exec(select(Actor)).all()

    def get_by_id(self, id: int) -> Actor | None:
        return self._session.get(Actor, id)

    def create(self, actor_dto: ActorCreateDTO, country: Country) -> Actor:
        new_actor = Actor(
            first_name=actor_dto.first_name,
            last_name=actor_dto.last_name,
            date_of_birth=actor_dto.date_of_birth,
            country_id=country.country_id,
        )
        self._session.add(new_actor)
        self._session.commit()
        self._session.refresh(new_actor)  # reads the new row back, with its actor_id
        return new_actor

    def update(self, actor_to_update: Actor, actor_dto: ActorUpdateDTO, country: Country) -> None:
        actor_to_update.first_name = actor_dto.first_name
        actor_to_update.last_name = actor_dto.last_name
        actor_to_update.date_of_birth = actor_dto.date_of_birth
        actor_to_update.country_id = country.country_id
        self._session.add(actor_to_update)
        self._session.commit()

    def delete(self, actor_to_delete: Actor) -> None:
        self._session.delete(actor_to_delete)
        self._session.commit()
