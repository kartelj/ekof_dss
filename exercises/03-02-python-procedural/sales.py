"""
Functions for the sales journal: reading one line, and adding up the sales of every product.

A line of the journal has four parts, separated by semicolons:

    2026-10-01;notebook;3;1250.00        the date, the product, the quantity and the price of one piece
"""

from decimal import Decimal


def parse(line: str) -> tuple[str, str, int, Decimal] | None:
    """Returns the four parts of a line (date, product, quantity, price), or None if the line is not valid."""
    parts = line.split(";")
    if len(parts) != 4:
        return None                     # a part is missing, or there is one too many
    try:
        quantity = int(parts[2])
    except ValueError:
        return None                     # the quantity is not a whole number
    return parts[0], parts[1], quantity, Decimal(parts[3])


def quantities(sales: list[tuple[str, str, int, Decimal]]) -> dict[str, int]:
    """Returns how many pieces of every product were sold."""
    result = {}
    for date, product, quantity, price in sales:
        if product in result:
            result[product] += quantity
        else:
            result[product] = quantity
    return result


def amounts(sales: list[tuple[str, str, int, Decimal]]) -> dict[str, Decimal]:
    """Returns the money that every product has brought: the quantity times the price, added up."""
    result = {}
    for date, product, quantity, price in sales:
        if product in result:
            result[product] += quantity * price
        else:
            result[product] = quantity * price
    return result
