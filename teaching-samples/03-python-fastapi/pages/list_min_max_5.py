"""
Lists: the five numbers typed into the form arrive to the server as one list.

All five input fields of the form have the same name (elements), so their
values are collected into the list elements.
"""

from typing import Annotated

from fastapi import APIRouter, Query, Request

from helpers import list_helper
from templating import templates

router = APIRouter()


def render(request: Request, elements: list[float], result: float):
    return templates.TemplateResponse(
        request, "list_min_max_5.html", {"elements": elements, "result": result}
    )


@router.get("/list-min-max-5")
def show(request: Request):
    return render(request, elements=[-1.5, 1.5, 2, 0.7, 5], result=0)


@router.get("/list-min-max-5/minimum")
def minimum(request: Request, elements: Annotated[list[float], Query()]):
    return render(request, elements, result=list_helper.minimum(elements))


@router.get("/list-min-max-5/maximum")
def maximum(request: Request, elements: Annotated[list[float], Query()]):
    return render(request, elements, result=list_helper.maximum(elements))


@router.get("/list-min-max-5/sum")
def sum_of_elements(request: Request, elements: Annotated[list[float], Query()]):
    return render(request, elements, result=list_helper.total(elements))


@router.get("/list-min-max-5/product")
def product(request: Request, elements: Annotated[list[float], Query()]):
    return render(request, elements, result=list_helper.product(elements))
