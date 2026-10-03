"""
Functions: the calculation is moved into a function of its own.

The function fact gets a value through its parameter, and gives the result
back with the statement return. It knows nothing about pages and requests,
so it can be called from anywhere.
"""

from fastapi import APIRouter, Request

from templating import templates

router = APIRouter()


def fact(n: int) -> int:
    """Calculates the factorial of n."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def render(request: Request, num: int, result: int | None, error: str = ""):
    return templates.TemplateResponse(
        request, "function_factorial.html", {"num": num, "result": result, "error": error}
    )


@router.get("/function-factorial")
def show(request: Request):
    return render(request, num=0, result=1)


@router.get("/function-factorial/calculate")
def factorial_by_function(request: Request, num: int):
    print("factorial_by_function")
    print("Argument:", num)
    if num < 0:
        print("Error - argument is negative.")
        return render(request, num, result=None, error="Error - argument is negative.")
    result = fact(num)
    print("Result:", result)
    print()
    return render(request, num, result)
