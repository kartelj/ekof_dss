"""
Lists: going through all the elements with a loop.
"""

from fastapi import APIRouter, Request

from templating import templates

router = APIRouter()


def render(request: Request, message: str):
    return templates.TemplateResponse(request, "list_iteration.html", {"message": message})


@router.get("/list-iteration")
def show(request: Request):
    return render(request, message="")


@router.get("/list-iteration/execute")
def execute(request: Request):
    message = ""

    byt_a = bytearray(10)
    byt_a[2] = 45
    byt_a[7] = 42
    message += "byt_a: "
    for i in range(len(byt_a)):  # i takes the values 0, 1, ..., len(byt_a) - 1
        message += str(byt_a[i]) + " "
    message += "\n"

    spec = " special"
    seasons = [" spring", " autumn", spec + " winter", " summer"]
    message += "seasons: "
    for i in range(len(seasons)):
        message += "'" + seasons[i] + "' "
    message += "\n"

    arr = [24, 48, 96, 192, 36, 72, 144]
    message += "arr: "
    for x in arr:  # x takes the values of the elements, one after another
        message += str(x) + " "
    message += "\n"

    message += "arr with indexes: "
    for i, x in enumerate(arr):  # enumerate gives the index and the element together
        message += f"{i}:{x} "
    message += "\n"

    str_a = [""] * 40
    str_a[2] = "mickey"
    str_a[3] = "mouse"
    str_a[4] = "donald"
    str_a[5] = "duck"
    str_a[6] = "goofy"
    message += "str_a: "
    for s in str_a:
        message += "'" + s + "' "
    message += "\n"

    print(message)
    return render(request, message)
