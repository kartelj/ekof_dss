# Assignment: a report of the sales

The assignment at the end of the lecture *Python: procedural programming*
(`presentations/03-02-python-procedural.md`), and its solution: `sales.py` and `report.py`.

## The task

A shop writes every sale into a journal, one line per sale - the date, the product, the quantity and the
price of one piece, separated by semicolons:

```text
2026-10-01;notebook;3;1250.00
```

In the program the journal is a list of texts (as if it had been read from a file); two of its lines are
not valid:

```python
journal = [
    "2026-10-01;notebook;3;1250.00",
    "2026-10-01;pen;10;120.50",
    "2026-10-02;backpack;1;4500.00",
    "2026-10-02;notebook;two;1250.00",
    "2026-10-02;pen;4",
    "2026-10-03;notebook;2;1250.00",
]
```

1. The module `sales.py` has three functions, with type hints and docstrings:
   - `parse(line)` returns a tuple (date, product, quantity, price) - the quantity as an `int`, the price as a
     `Decimal` - or `None` if the line does not have four parts, or if its quantity is not a whole number;
   - `quantities(sales)` returns a dictionary: product - the number of pieces sold;
   - `amounts(sales)` returns a dictionary: product - quantity times price, added up.
2. The program `report.py` imports the module, reads the journal line by line, and writes every line that
   is not valid, with its number.
3. Then it writes a table of the products in alphabetical order - the quantity, and the amount with two
   decimals and a separator of thousands - the total of all the amounts, and the product with the most
   pieces sold.

## Running the solution

```text
python report.py
```

```text
Skipped line 4: 2026-10-02;notebook;two;1250.00
Skipped line 5: 2026-10-02;pen;4

backpack         1     4,500.00
notebook         5     6,250.00
pen             10     1,205.00
Total:                11,955.00
Most sold: pen (10 pieces)
```

The solution uses what the lecture shows: strings and `split()`, `int()` and `Decimal`, `for` with
`enumerate()`, tuples and their unpacking, dictionaries, functions with type hints, a module of our own,
and f-strings with widths and formats (`:12`, `:12,.2f`). Catching the error of `int()` with `try` - `except`
comes from the introduction to Python.
