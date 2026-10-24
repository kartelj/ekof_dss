# Assignment: the cinema

The solution of the assignment of the lecture
[Python: object-oriented programming](../../presentations/03-03-python-oop.md).

The task in brief - a program that sells cinema tickets:

- the **data class** `Film` (title, year, minutes) with the **property** `duration` (`1h 38min`);
  the films are read from the JSON file `films.json`, and `find_film` returns a film or `None`;
- the **abstract base class** `Ticket` with the class attribute `base_price = 500` and the abstract method
  `price()`, and three **derived classes**: `RegularTicket` (the base price), `StudentTicket` (half of it)
  and `PremiereTicket` (double); tickets can be **compared** with `<` by their price, and printed;
- the class `Cinema` with the "private" list of sold tickets, the class attribute `capacity = 4`,
  the method `sell(ticket)`, the property `income`, `len(cinema)`, **listeners** that are called at every sale,
  and **its own exception** `SoldOutError` when the hall is full.

## Running it

```text
python exercises/03-03-python-oop/cinema.py
```

## The expected output

```text
Fargo (1996), 1h 38min
Heat (1995), 2h 50min
Amélie (2001), 2h 2min
Sold: Fargo (500)
Sold: Fargo (250)
Sold: Heat (1000)
No such film: Up
Sold: Amélie (250)
Sold out: the hall has only 4 seats
Tickets sold: 4
From the cheapest: [250, 250, 500, 1000]
Income: 2000
Films: ['Fargo', 'Fargo', 'Heat', 'Amélie']
```
