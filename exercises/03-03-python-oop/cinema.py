"""
The cinema - the solution of the assignment of the lecture "Python: object-oriented programming".

Start it in this folder with      python cinema.py
"""

import json
from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path

BASE_DIR = Path(__file__).parent


# ---------- the films: a data class, read from a JSON file ----------

@dataclass
class Film:
    title: str
    year: int
    minutes: int

    @property
    def duration(self) -> str:
        """The length as hours and minutes, e.g. 1h 38min."""
        return f"{self.minutes // 60}h {self.minutes % 60}min"


def read_films(file_name: str) -> list[Film]:
    films = []
    text = (BASE_DIR / file_name).read_text(encoding="utf-8")
    for item in json.loads(text):            # item is a dictionary
        films.append(Film(item["title"], item["year"], item["minutes"]))
    return films


def find_film(films: list[Film], title: str) -> Film | None:
    for film in films:
        if film.title == title:
            return film
    return None


# ---------- the tickets: an abstract base class and three derived classes ----------

class Ticket(ABC):
    base_price = 500                         # a class attribute: the same for all the tickets

    def __init__(self, film: Film):
        self.film = film

    @abstractmethod
    def price(self) -> int:
        ...

    def __str__(self) -> str:
        return f"{self.film.title} ({self.price()})"

    def __lt__(self, other) -> bool:         # sorted() compares tickets by their price
        return self.price() < other.price()


class RegularTicket(Ticket):
    def price(self) -> int:
        return self.base_price


class StudentTicket(Ticket):
    def price(self) -> int:
        return self.base_price // 2


class PremiereTicket(Ticket):
    def price(self) -> int:
        return self.base_price * 2


# ---------- the cinema: "private" data, a property, events and an exception of its own ----------

class SoldOutError(Exception):
    pass


class Cinema:
    capacity = 4                             # the number of seats in the hall

    def __init__(self):
        self._sold = []                      # the tickets sold so far - for internal use
        self._listeners = []                 # the functions called at every sale

    def on_sale(self, listener):
        self._listeners.append(listener)

    def sell(self, ticket: Ticket):
        if len(self._sold) >= self.capacity:
            raise SoldOutError(f"the hall has only {self.capacity} seats")
        self._sold.append(ticket)
        for listener in self._listeners:
            listener(ticket)

    @property
    def income(self) -> int:
        total = 0
        for ticket in self._sold:
            total += ticket.price()          # polymorphism: every ticket has its own price()
        return total

    def tickets(self) -> list[Ticket]:
        return list(self._sold)              # a copy: the caller cannot change our list

    def __len__(self) -> int:                # len(cinema)
        return len(self._sold)


# ---------- the program ----------

films = read_films("films.json")
for film in films:
    print(f"{film.title} ({film.year}), {film.duration}")

cinema = Cinema()
sold_titles = []
cinema.on_sale(lambda ticket: print("Sold:", ticket))
cinema.on_sale(lambda ticket: sold_titles.append(ticket.film.title))

orders = [
    (RegularTicket, "Fargo"),
    (StudentTicket, "Fargo"),
    (PremiereTicket, "Heat"),
    (RegularTicket, "Up"),
    (StudentTicket, "Amélie"),
    (RegularTicket, "Heat"),
]
for kind, title in orders:
    film = find_film(films, title)
    if film is None:
        print("No such film:", title)
        continue
    try:
        cinema.sell(kind(film))              # a class is called like a function
    except SoldOutError as error:
        print("Sold out:", error)

print("Tickets sold:", len(cinema))
prices = []
for ticket in sorted(cinema.tickets()):     # sorted() uses __lt__ of the tickets
    prices.append(ticket.price())
print("From the cheapest:", prices)
print("Income:", cinema.income)
print("Films:", sold_titles)
