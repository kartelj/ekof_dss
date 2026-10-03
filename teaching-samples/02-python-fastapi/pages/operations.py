"""
Branching: the statement if, written in several ways.

The page keeps one number. Every button changes the number,
and then the number is compared with 100.
"""

from fastapi import APIRouter, Request, status
from fastapi.responses import RedirectResponse

from templating import templates

router = APIRouter()

number = 17

comparison_result = "17 less than 100!"

# string that represents the output
message = "17"


@router.get("/operations")
def show(request: Request):
    return templates.TemplateResponse(
        request, "operations.html", {"comparison_result": comparison_result, "message": message}
    )


@router.post("/operations/plus-2")
def plus_2():
    global number, comparison_result, message

    number += 2  # number is incremented by 2
    message += "\n" + str(number)

    # three separate statements: all three conditions are always checked
    if number < 100:
        comparison_result = str(number) + " less than 100!"
    if number == 100:
        comparison_result = str(number) + " equal to 100!"
    if number > 100:
        comparison_result = str(number) + " greater than 100!"

    return RedirectResponse("/operations", status_code=status.HTTP_303_SEE_OTHER)


@router.post("/operations/multiply-2")
def multiply_2():
    """
    The function doubles the number, and the value
    of the doubled number is appended to the message.
    """
    global number, comparison_result, message

    number *= 2

    # an expression can be spread over several lines if it is written inside parentheses
    message += (
        "\n"
        +
        str(number)
    )

    # if - elif - else: conditions are checked in order, and exactly one branch is executed
    if number < 100:
        comparison_result = str(number) + " less than 100!"
    elif number == 100:
        comparison_result = str(number) + " equal to 100!"
    else:
        comparison_result = str(number) + " greater than 100!"

    return RedirectResponse("/operations", status_code=status.HTTP_303_SEE_OTHER)


@router.post("/operations/minus-2")
def minus_2():
    global number, comparison_result, message

    number -= 2
    message += f"\n{number}"  # f-string: the value of the variable is inserted into the text

    if number < 100:
        comparison_result = f"{number} less than 100!"
    elif number == 100:
        comparison_result = f"{number} equal to 100!"
    else:
        comparison_result = f"{number} greater than 100!"

    return RedirectResponse("/operations", status_code=status.HTTP_303_SEE_OTHER)


@router.post("/operations/divide-2")
def divide_2():
    global number, comparison_result, message

    # // is integer division: 17 // 2 is 8 (while 17 / 2 is 8.5)
    number = number // 2
    message += f"\n{number}"

    # conditional expression: the whole if - else is written as one value
    relation = "less than" if number < 100 else "equal to" if number == 100 else "greater than"
    comparison_result = f"{number} {relation} 100!"

    return RedirectResponse("/operations", status_code=status.HTTP_303_SEE_OTHER)
