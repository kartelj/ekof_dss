"""
Variables and input: the text typed by the user is appended to the output.
"""

from typing import Annotated

from fastapi import APIRouter, Form, Request, status
from fastapi.responses import RedirectResponse

from templating import templates

router = APIRouter()

message = ""
user_input = ""


@router.get("/append-clear")
def show(request: Request):
    return templates.TemplateResponse(
        request, "append_clear.html", {"message": message, "user_input": user_input}
    )


@router.post("/append-clear/write")
def write(text: Annotated[str, Form()] = ""):
    """Executed when the button "Write" is pressed; `text` is the content of the input field."""
    global message, user_input

    user_input = text
    message = message + user_input + "\n"
    print("Text is appended to message. Text: " + user_input)

    return RedirectResponse("/append-clear", status_code=status.HTTP_303_SEE_OTHER)


@router.post("/append-clear/clear")
def clear():
    """Executed when the button "Clear" is pressed."""
    global message

    message = ""
    print("Message is cleared.")

    return RedirectResponse("/append-clear", status_code=status.HTTP_303_SEE_OTHER)
