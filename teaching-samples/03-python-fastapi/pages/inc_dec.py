"""
Two buttons on one page: each button has its own function.
"""

from fastapi import APIRouter, Request, status
from fastapi.responses import RedirectResponse

from templating import templates

router = APIRouter()

current_count = 42


@router.get("/inc-dec")
def show(request: Request):
    return templates.TemplateResponse(request, "inc_dec.html", {"current_count": current_count})


@router.post("/inc-dec/increment")
def increment_count():
    global current_count

    current_count += 1  # Python has no operator ++

    return RedirectResponse("/inc-dec", status_code=status.HTTP_303_SEE_OTHER)


@router.post("/inc-dec/decrement")
def decrement_count():
    global current_count

    current_count -= 1  # Python has no operator --

    return RedirectResponse("/inc-dec", status_code=status.HTTP_303_SEE_OTHER)
