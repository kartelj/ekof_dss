"""Mathematical functions."""


def power(the_base: float, exp: int) -> float:
    """Raises the_base to the power exp (exp may also be zero or negative)."""
    if exp == 0:
        return 1
    res = 1.0
    exponent_is_negative = False
    if exp < 0:
        exponent_is_negative = True
        exp = -exp
    for i in range(1, exp + 1):
        res *= the_base
    if not exponent_is_negative:
        return res
    else:
        return 1 / res


def factorial(num: int) -> int:
    """Calculates num! = 1 * 2 * ... * num."""
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result


def double_factorial(n: int) -> int:
    """Calculates n!! = n * (n - 2) * (n - 4) * ..."""
    r = 1
    i = n
    while i > 0:
        r *= i
        i -= 2
    return r
