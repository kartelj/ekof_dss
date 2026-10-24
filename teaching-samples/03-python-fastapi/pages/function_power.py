"""
Functions: a function with two parameters.
"""

from fastapi import APIRouter, Request

from templating import templates

router = APIRouter()


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


def render(request: Request, base_one: float, exponent: int, result: float):
    return templates.TemplateResponse(
        request,
        "function_power.html",
        {"base_one": base_one, "exponent": exponent, "result": result},
    )


@router.get("/function-power")
def show(request: Request):
    return render(request, base_one=2.5, exponent=0, result=1)


@router.get("/function-power/calculate")
def power_by_function(request: Request, base_one: float, exponent: int):
    print("power_by_function")
    print("Base:", base_one)
    print("Exponent:", exponent)
    result = power(base_one, exponent)
    print("Result:", result)
    print()
    return render(request, base_one, exponent, result)
