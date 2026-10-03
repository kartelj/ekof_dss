"""
Functions that work with lists.

Python already has built-in functions for most of these tasks
(min, max, sum, len ...). They are written here "by hand" to practise loops.
"""


def elements_to_string(arr) -> str:
    """Joins the elements of a list (or of any other sequence) into one text."""
    res = ""
    for x in arr:
        if isinstance(x, str):
            res += "'" + x + "' "  # texts are shown between quotes
        else:
            res += str(x) + " "
    return res


def average(arr: list[float]) -> float:
    r = 0
    for x in arr:
        r += x
    return r / len(arr)


def minimum(arr: list[float]) -> float:
    res = arr[0]
    for x in arr:
        if x < res:
            res = x
    return res


def maximum(arr: list[float]) -> float:
    res = arr[0]
    for x in arr:
        if x > res:
            res = x
    return res


def total(arr: list[float]) -> float:
    s = 0
    for x in arr:
        s += x
    return s


def product(arr: list[float]) -> float:
    prod = 1
    for i in range(len(arr)):
        prod *= arr[i]
    return prod
