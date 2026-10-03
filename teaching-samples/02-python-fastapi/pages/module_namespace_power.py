"""
Modules: the function power is not written in this file - it is imported
from the module mathematics, which is in the package (folder) helpers.

A module is a file with Python code. The name of the module is in front of the
names it defines (mathematics.power), so the same name can be used in several
modules without a conflict.
"""

from fastapi import APIRouter, Request

from helpers import mathematics
from templating import templates

router = APIRouter()


def render(request: Request, base_one: float, exponent: int, result: float):
    return templates.TemplateResponse(
        request,
        "module_namespace_power.html",
        {"base_one": base_one, "exponent": exponent, "result": result},
    )


@router.get("/module-namespace-power")
def show(request: Request):
    return render(request, base_one=2.5, exponent=0, result=1)


@router.get("/module-namespace-power/calculate")
def power_by_function(request: Request, base_one: float, exponent: int):
    print("power_by_function")
    print("Base:", base_one)
    print("Exponent:", exponent)
    result = mathematics.power(base_one, exponent)
    print("Result:", result)
    print()
    return render(request, base_one, exponent, result)
