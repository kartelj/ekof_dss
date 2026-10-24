"""
Sequence: statements are executed one after another, in the order in which they are written.
"""

from fastapi import APIRouter, Request, status
from fastapi.responses import RedirectResponse

from templating import templates

router = APIRouter()

# the text shown in the output box of the page
message = ""


@router.get("/hello-world")
def show(request: Request):
    """Produces the page: the template is filled with the current value of the variable."""
    return templates.TemplateResponse(request, "hello_world.html", {"message": message})


@router.post("/hello-world")
def execute():
    """Executed when the button "Do It!" is pressed."""
    global message  # the function changes the variable defined above, outside of the function

    message = message + "Hello world!!!" + "\n"
    message = message + "Hello World, again!" + "\n"
    message = message + "Hello World, once again!" + "\n"
    message = message + "Goodbye." + "\n"

    # the browser is sent back to the page, which now shows the new text
    return RedirectResponse("/hello-world", status_code=status.HTTP_303_SEE_OTHER)
