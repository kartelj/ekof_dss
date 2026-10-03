"""
Loops: the statement for takes the values of a sequence one by one.

range(1, n + 1) is the sequence 1, 2, ..., n       (the upper bound is not included)
range(n, 0, -1) is the sequence n, n - 1, ..., 1   (the third argument is the step)
"""

from fastapi import APIRouter, Request

from templating import templates

router = APIRouter()


def render(request: Request, num: int, result: int | None, error: str = ""):
    return templates.TemplateResponse(
        request, "for_loop_factorial.html", {"num": num, "result": result, "error": error}
    )


@router.get("/for-loop-factorial")
def show(request: Request):
    return render(request, num=0, result=1)


@router.get("/for-loop-factorial/count-forward")
def factorial_by_count_forward(request: Request, num: int):
    print("factorial_by_count_forward")
    n = num
    print("Argument:", n)
    if n < 0:
        print("Error - argument is negative.")
        return render(request, num, result=None, error="Error - argument is negative.")
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    result = fact
    print("Result:", result)
    print()
    return render(request, num, result)


@router.get("/for-loop-factorial/count-backward")
def factorial_by_count_backward(request: Request, num: int):
    print("factorial_by_count_backward")
    n = num
    print("Argument:", n)
    if n < 0:
        print("Error - argument is negative.")
        return render(request, num, result=None, error="Error - argument is negative.")
    fact = 1
    for i in range(n, 0, -1):
        fact *= i
    result = fact
    print("Result:", result)
    print()
    return render(request, num, result)
