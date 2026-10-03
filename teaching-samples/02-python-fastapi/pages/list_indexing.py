"""
Lists: reaching the elements through their index.

A list keeps several values under one name. The elements are numbered
from 0: the first element of the list a is a[0], the last one is a[len(a) - 1].
"""

from fastapi import APIRouter, Request

from templating import templates

router = APIRouter()


def render(request: Request, message: str):
    return templates.TemplateResponse(request, "list_indexing.html", {"message": message})


@router.get("/list-indexing")
def show(request: Request):
    return render(request, message="")


@router.get("/list-indexing/execute")
def execute(request: Request):
    str_a = [None] * 40  # a list with 40 elements; None means "there is no value"
    str_a[2] = "mickey"
    str_a[3] = "mouse"
    message = f"type(str_a): {type(str_a)}\n"
    message += f"str_a[2]: {str_a[2]}\n"
    message += f"str_a[3]: {str_a[3]}\n"
    message += f"str_a[10]: {str_a[10]}\n"
    message += f"len(str_a): {len(str_a)}\n"
    message += "\n"

    byt_a = bytearray(10)  # 10 bytes; a byte is a whole number between 0 and 255
    byt_a[2] = 42
    byt_a[0] = 12
    message += f"type(byt_a): {type(byt_a)}\n"
    message += f"byt_a[0]: {byt_a[0]}\n"
    message += f"byt_a[1]: {byt_a[1]}\n"
    message += f"byt_a[2]: {byt_a[2]}\n"
    message += f"byt_a[2] + byt_a[0]: {byt_a[2] + byt_a[0]}\n"
    message += f"len(byt_a): {len(byt_a)}\n"
    message += "\n"

    s = " special "
    adj = [s, " very ", " much "]
    seasons = [" spring", " autumn", adj[0] + adj[1] + adj[2] + "winter", " summer"]
    message += f"seasons: {seasons}\n"
    message += f"len(seasons): {len(seasons)}\n"
    message += f"seasons[0]: {seasons[0]}\n"
    message += f"seasons[2]: {seasons[2]}\n"
    message += "\n"

    numbers = [24, 48, 96, 192, 36, 72, 144]
    message += f"numbers: {numbers}\n"
    message += f"len(numbers): {len(numbers)}\n"
    message += f"numbers[0]: {numbers[0]}\n"
    message += f"numbers[1] + numbers[2]: {numbers[1] + numbers[2]}\n"
    message += f"numbers[len(numbers) - 1]: {numbers[len(numbers) - 1]}\n"
    message += f"numbers[-1]: {numbers[-1]}\n"  # a negative index counts from the end
    index_expression = 15 - 12
    message += f"index_expression: {index_expression}\n"
    message += f"numbers[index_expression]: {numbers[index_expression]}\n"
    message += f"numbers[1:4]: {numbers[1:4]}\n"  # a slice: elements 1, 2 and 3
    message += "\n"

    print(message)
    return render(request, message)
