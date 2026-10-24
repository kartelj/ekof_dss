"""
Lists and functions: a list can be passed to a function as an argument.

The same function works for a list of numbers, a list of texts and an array
of bytes - Python does not ask of which type the argument is, it only needs
to be something that the statement for can go through.
"""

from fastapi import APIRouter, Request

from templating import templates

router = APIRouter()


def elements_to_string(arr) -> str:
    res = ""
    for x in arr:
        if isinstance(x, str):
            res += "'" + x + "' "  # texts are shown between quotes
        else:
            res += str(x) + " "
    return res


def render(request: Request, message: str):
    return templates.TemplateResponse(request, "list_iteration_function.html", {"message": message})


@router.get("/list-iteration-function")
def show(request: Request):
    return render(request, message="")


@router.get("/list-iteration-function/execute")
def execute(request: Request):
    message = ""

    byt_a = bytearray(30)
    byt_a[2] = 45
    for i in range(3, len(byt_a)):
        byt_a[i] = 2 * i
    message += "byt_a: " + elements_to_string(byt_a) + "\n"

    spec = " special"
    seasons = [" spring", " autumn", spec + " winter", " summer"]
    message += "seasons: " + elements_to_string(seasons) + "\n"

    arr = [24, 48, 96, 192, 36, 72, 144]
    message += "arr: " + elements_to_string(arr) + "\n"

    str_a = [""] * 40
    str_a[2] = "mickey"
    str_a[3] = "mouse"
    str_a[4] = "donald"
    str_a[5] = "duck"
    str_a[6] = "goofy"
    message += "str_a: " + elements_to_string(str_a) + "\n"

    print(message)
    return render(request, message)
