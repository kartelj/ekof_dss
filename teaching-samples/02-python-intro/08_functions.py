"""
Functions: a named piece of a program, with parameters and a result.

    python 08_functions.py
"""


def price_with_vat(net_price, vat_rate=20):
    """Returns the price with the value added tax; the rate is given in percent."""
    return net_price * (1 + vat_rate / 100)


def grade(points):
    """Returns the grade (5 to 10) for the points of an exam (0 to 100)."""
    if points >= 91:
        return 10       # return ends the function and gives the result back
    if points >= 81:
        return 9
    if points >= 71:
        return 8
    if points >= 61:
        return 7
    if points >= 51:
        return 6
    return 5


# The body of a function is executed only when the function is called.
print(price_with_vat(1000))         # the rate is left out, so it is 20
print(price_with_vat(1000, 10))     # the rate is 10
for points in [45, 58, 77, 93]:
    print(points, "points - grade", grade(points))
