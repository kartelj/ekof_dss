"""
Branching: the statement match compares one value with several cases.
"""

import math

from fastapi import APIRouter, Request

from templating import templates

router = APIRouter()


def render(request: Request, shape: str, x: float, y: float, circumference: float, area: float):
    return templates.TemplateResponse(
        request,
        "geometry_2.html",
        {"shape": shape, "x": x, "y": y, "circumference": circumference, "area": area},
    )


@router.get("/geometry-2")
def show(request: Request, shape: str = "square", x: float = 1, y: float = 2):
    """Shows the page. It is also called when another shape is selected in the list."""
    return render(request, shape, x, y, circumference=0, area=0)


@router.get("/geometry-2/calculate")
def circumference_area(request: Request, shape: str, x: float, y: float = 2):
    pi = math.pi

    print(f"Shape: {shape}. x: {x}.")
    match shape:
        case "circle":
            circumference = 2 * pi * x
            area = pi * x * x
        case "square":
            circumference = 4 * x
            area = x * x
        case "rectangle":
            circumference = 2 * (x + y)
            area = x * y
        case "ellipse":
            area = x * y * pi
            # the circumference of an ellipse has no simple formula - this is an approximation
            circumference = 2 * pi * math.sqrt((x * x + y * y) / 2)
        case _:
            # we can not calculate area or circumference for this shape
            circumference = -math.inf
            area = -math.inf
    print(f"Area: {area}. Circumference: {circumference}.")
    print()

    return render(request, shape, x, y, circumference, area)
