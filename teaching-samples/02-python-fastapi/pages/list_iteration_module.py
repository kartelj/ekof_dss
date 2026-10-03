"""
Lists and modules: the function elements_to_string is imported from the module
list_helper of the package helpers.

The three import statements below show three ways of using a name from a module.
"""

from fastapi import APIRouter, Request

import helpers.list_helper
from helpers import list_helper
from helpers.list_helper import elements_to_string
from templating import templates

router = APIRouter()


def render(request: Request, message: str):
    return templates.TemplateResponse(request, "list_iteration_module.html", {"message": message})


@router.get("/list-iteration-module")
def show(request: Request):
    return render(request, message="")


@router.get("/list-iteration-module/execute")
def execute(request: Request):
    message = ""

    byt_a = bytearray(30)
    byt_a[2] = 45
    for i in range(3, len(byt_a)):
        byt_a[i] = 2 * i
    # the full name: package.module.function
    message += "byt_a: " + helpers.list_helper.elements_to_string(byt_a) + "\n"

    spec = " special"
    seasons = [" spring", " autumn", spec + " winter", " summer"]
    # the module was imported from the package: module.function
    message += "seasons: " + list_helper.elements_to_string(seasons) + "\n"

    arr = [24, 48, 96, 192, 36, 72, 144]
    message += "arr: " + list_helper.elements_to_string(arr) + "\n"

    str_a = [""] * 40
    str_a[2] = "mickey"
    str_a[3] = "mouse"
    str_a[4] = "donald"
    str_a[5] = "duck"
    str_a[6] = "goofy"
    # the function itself was imported from the module: function
    message += "str_a: " + elements_to_string(str_a) + "\n"

    print(message)
    return render(request, message)
