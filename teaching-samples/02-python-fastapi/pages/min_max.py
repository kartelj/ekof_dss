"""
Branching: the smallest and the largest of five numbers.

This page does not remember anything: the numbers travel from the form to the
server in the address of the request (e.g. /min-max/minimum?x=0&y=-1.5&...),
the server calculates the result and sends back the page that shows it.
"""

from fastapi import APIRouter, Request

from templating import templates

router = APIRouter()


def render(request: Request, x: float, y: float, z: float, w: float, t: float, result: float):
    """Produces the page that shows the five numbers and the result."""
    return templates.TemplateResponse(
        request, "min_max.html", {"x": x, "y": y, "z": z, "w": w, "t": t, "result": result}
    )


@router.get("/min-max")
def show(request: Request):
    return render(request, x=0, y=-1.5, z=1.5, w=2, t=-0.7, result=0)


@router.get("/min-max/minimum")
def minimum(request: Request, x: float, y: float, z: float, w: float, t: float):
    smallest = x
    if y < smallest:
        smallest = y
    if z < smallest:
        smallest = z
    if w < smallest:
        smallest = w
    if t < smallest:
        smallest = t
    return render(request, x, y, z, w, t, result=smallest)


@router.get("/min-max/maximum")
def maximum(request: Request, x: float, y: float, z: float, w: float, t: float):
    largest = x
    if y > largest:
        largest = y
    if z > largest:
        largest = z
    if w > largest:
        largest = w
    if t > largest:
        largest = t
    return render(request, x, y, z, w, t, result=largest)


@router.get("/min-max/sum")
def sum_of_numbers(request: Request, x: float, y: float, z: float, w: float, t: float):
    return render(request, x, y, z, w, t, result=x + y + z + w + t)


@router.get("/min-max/product")
def product(request: Request, x: float, y: float, z: float, w: float, t: float):
    return render(request, x, y, z, w, t, result=x * y * z * w * t)
