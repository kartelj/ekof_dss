"""
Loops: the statement while repeats its block as long as the condition is true.

The factorial of n (written n!) is the product 1 * 2 * ... * n.
"""

from fastapi import APIRouter, Request

from templating import templates

router = APIRouter()


def render(request: Request, num: int, result: int | None, error: str = ""):
    return templates.TemplateResponse(
        request, "while_loop_factorial.html", {"num": num, "result": result, "error": error}
    )


@router.get("/while-loop-factorial")
def show(request: Request):
    return render(request, num=0, result=1)


@router.get("/while-loop-factorial/count-forward")
def factorial_by_count_forward(request: Request, num: int):
    print("factorial_by_count_forward")
    n = num
    print("Argument:", n)
    if n < 0:
        print("Error - argument is negative.")
        return render(request, num, result=None, error="Error - argument is negative.")
    i = 1
    fact = 1
    while i <= n:
        fact = fact * i
        i += 1  # i = i + 1
    result = fact
    print("Result:", result)
    print()
    return render(request, num, result)


@router.get("/while-loop-factorial/count-backward")
def factorial_by_count_backward(request: Request, num: int):
    print("factorial_by_count_backward")
    n = num
    print("Argument:", n)
    if n < 0:
        print("Error - argument is negative.")
        return render(request, num, result=None, error="Error - argument is negative.")
    i = n
    fact = 1
    while i >= 1:
        fact *= i  # fact = fact * i
        i -= 1
    result = fact
    print("Result:", result)
    print()
    return render(request, num, result)


@router.get("/while-loop-factorial/decrementing")
def factorial_by_decrementing(request: Request, num: int):
    print("factorial_by_decrementing")
    n = num
    print("Argument:", n)
    if n < 0:
        print("Error - argument is negative.")
        return render(request, num, result=None, error="Error - argument is negative.")
    fact = 1
    while n > 0:
        fact *= n
        n -= 1
    result = fact
    print("Result:", result)
    print()
    return render(request, num, result)
