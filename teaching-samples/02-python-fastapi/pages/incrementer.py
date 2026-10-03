"""
Assignment: a variable gets a new value, calculated from its old value.
"""

from fastapi import APIRouter, Request, status
from fastapi.responses import RedirectResponse

from templating import templates

router = APIRouter()

current_count = 42  # an integer (type int)


@router.get("/incrementer")
def show(request: Request):
    return templates.TemplateResponse(request, "incrementer.html", {"current_count": current_count})


@router.post("/incrementer")
def increment_count():
    global current_count

    current_count = current_count + 1

    return RedirectResponse("/incrementer", status_code=status.HTTP_303_SEE_OTHER)
