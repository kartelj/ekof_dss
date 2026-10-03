"""
Loops: a loop whose condition is checked at the END of each repetition.

Many languages have a special statement for this (do - while). Python does not:
we write an endless loop (while True) and leave it with the statement break.
The block of such a loop is always executed at least once.
"""

from fastapi import APIRouter, Request

from templating import templates

router = APIRouter()


def render(request: Request, num: int, result: int | None, error: str = ""):
    return templates.TemplateResponse(
        request, "do_while_loop_factorial.html", {"num": num, "result": result, "error": error}
    )


@router.get("/do-while-loop-factorial")
def show(request: Request):
    return render(request, num=0, result=1)


@router.get("/do-while-loop-factorial/count-forward")
def factorial_by_count_forward(request: Request, num: int):
    print("factorial_by_count_forward")
    n = num
    print("Argument:", n)
    if n < 0:
        print("Error - argument is negative.")
        return render(request, num, result=None, error="Error - argument is negative.")
    i = 1
    fact = 1
    while True:
        fact *= i
        i += 1
        if i > n:  # the loop continues while i <= n
            break
    result = fact
    print("Result:", result)
    print()
    return render(request, num, result)


@router.get("/do-while-loop-factorial/count-backward")
def factorial_by_count_backward(request: Request, num: int):
    print("factorial_by_count_backward")
    n = num
    print("Argument:", n)
    if n < 0:
        print("Error - argument is negative.")
        return render(request, num, result=None, error="Error - argument is negative.")
    fact = 1
    if n == 0:
        # the block of the loop below is executed at least once, which would be wrong for 0
        result = fact
        print("Result:", result)
        print()
        return render(request, num, result)
    i = n
    while True:
        fact *= i
        i -= 1
        if i < 1:  # the loop continues while i >= 1
            break
    result = fact
    print("Result:", result)
    print()
    return render(request, num, result)


@router.get("/do-while-loop-factorial/decrementing")
def factorial_by_decrementing(request: Request, num: int):
    print("factorial_by_decrementing")
    n = num
    print("Argument:", n)
    if n < 0:
        print("Error - argument is negative.")
        return render(request, num, result=None, error="Error - argument is negative.")
    fact = 1
    if n == 0:
        result = fact
        print("Result:", result)
        print()
        return render(request, num, result)
    while True:
        fact *= n
        n -= 1
        if n <= 0:  # the loop continues while n > 0
            break
    result = fact
    print("Result:", result)
    print()
    return render(request, num, result)
