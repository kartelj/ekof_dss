"""
Numeric types: besides int and float, Python has the type Decimal for exact decimal numbers.
"""

from decimal import Decimal

from fastapi import APIRouter, Request, status
from fastapi.responses import RedirectResponse

from templating import templates

router = APIRouter()

current_count = Decimal("-42")  # an exact decimal number (important e.g. for money)


@router.get("/decrementer")
def show(request: Request):
    return templates.TemplateResponse(request, "decrementer.html", {"current_count": current_count})


@router.post("/decrementer")
def decrement_count():
    global current_count

    current_count -= Decimal("0.5")  # the same as: current_count = current_count - Decimal("0.5")

    return RedirectResponse("/decrementer", status_code=status.HTTP_303_SEE_OTHER)
