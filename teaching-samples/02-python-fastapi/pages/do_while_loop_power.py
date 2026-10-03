"""
Loops: raising a number to an integer power with a loop whose condition
is checked at the end of each repetition (while True ... break).
"""

from fastapi import APIRouter, Request

from templating import templates

router = APIRouter()


def render(request: Request, base_one: float, exponent: int, result: float):
    return templates.TemplateResponse(
        request,
        "do_while_loop_power.html",
        {"base_one": base_one, "exponent": exponent, "result": result},
    )


@router.get("/do-while-loop-power")
def show(request: Request):
    return render(request, base_one=2.5, exponent=0, result=1)


@router.get("/do-while-loop-power/count-forward")
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
    i = 1
    while True:
        res *= base_one
        i += 1
        if i > exp:  # the loop continues while i <= exp
            break
    if not exponent_is_negative:
        result = res
    else:
        result = 1 / res
    print("Result:", result)
    print()
    return render(request, base_one, exponent, result)


@router.get("/do-while-loop-power/count-backward")
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
    i = exp
    while True:
        res *= base_one
        i -= 1
        if i < 1:  # the loop continues while i >= 1
            break
    if not exponent_is_negative:
        result = res
    else:
        result = 1 / res
    print("Result:", result)
    print()
    return render(request, base_one, exponent, result)


@router.get("/do-while-loop-power/decrementing")
def power_by_decrementing(request: Request, base_one: float, exponent: int):
    print("power_by_decrementing")
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
    while True:
        res *= base_one
        exp -= 1
        if exp < 1:  # the loop continues while exp >= 1
            break
    if not exponent_is_negative:
        result = res
    else:
        result = 1 / res
    print("Result:", result)
    print()
    return render(request, base_one, exponent, result)
