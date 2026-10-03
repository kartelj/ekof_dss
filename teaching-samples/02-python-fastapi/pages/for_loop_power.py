"""
Loops: raising a number to an integer power with the statement for.
"""

from fastapi import APIRouter, Request

from templating import templates

router = APIRouter()


def render(request: Request, base_one: float, exponent: int, result: float):
    return templates.TemplateResponse(
        request,
        "for_loop_power.html",
        {"base_one": base_one, "exponent": exponent, "result": result},
    )


@router.get("/for-loop-power")
def show(request: Request):
    return render(request, base_one=2.5, exponent=0, result=1)


@router.get("/for-loop-power/count-forward")
def power_by_count_forward(request: Request, base_one: float, exponent: int):
    print("power_by_count_forward")
    print("Base:", base_one)
    print("Exponent:", exponent)
    exp = exponent
    res = 1.0
    if exp == 0:
        result = res
        print("Result:", result)
        print()
        return render(request, base_one, exponent, result)
    exponent_is_negative = False
    if exp < 0:
        exponent_is_negative = True
        exp = -exp
    for i in range(1, exp + 1):
        res *= base_one
    if not exponent_is_negative:
        result = res
    else:
        result = 1 / res
    print("Result:", result)
    print()
    return render(request, base_one, exponent, result)


@router.get("/for-loop-power/count-backward")
def power_by_count_backward(request: Request, base_one: float, exponent: int):
    print("power_by_count_backward")
    print("Base:", base_one)
    print("Exponent:", exponent)
    exp = exponent
    res = 1.0
    if exp == 0:
        result = res
        print("Result:", result)
        print()
        return render(request, base_one, exponent, result)
    exponent_is_negative = False
    if exp < 0:
        exponent_is_negative = True
        exp = -exp
    for i in range(exp, 0, -1):
        res *= base_one
    if not exponent_is_negative:
        result = res
    else:
        result = 1 / res
    print("Result:", result)
    print()
    return render(request, base_one, exponent, result)
