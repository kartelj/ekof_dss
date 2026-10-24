"""
Programming in Python, shown through the pages of a small web application.

Start the application with      python main.py
and then open                   http://localhost:8000

Everything that the pages write with print() appears in the terminal
in which the application was started.
"""

import uvicorn
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.staticfiles import StaticFiles

from pages import (
    actors_show,
    actors_show_module,
    append_clear,
    decrementer,
    do_while_loop_factorial,
    do_while_loop_power,
    fetch_data,
    for_loop_factorial,
    for_loop_power,
    function_factorial,
    function_guessing,
    function_power,
    geometry,
    geometry_2,
    hello_world,
    inc_dec,
    incrementer,
    index,
    list_indexing,
    list_iteration,
    list_iteration_function,
    list_iteration_module,
    list_min_max_5,
    min_max,
    module_namespace_power,
    operations,
    while_loop_factorial,
    while_loop_power,
)
from templating import BASE_DIR, templates

app = FastAPI(title="DSS - Python and FastAPI")

# files that are sent to the browser unchanged (styles, images ...)
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

# every page of the application is added here
app.include_router(index.router)

# basics
app.include_router(hello_world.router)
app.include_router(append_clear.router)
app.include_router(incrementer.router)
app.include_router(decrementer.router)
app.include_router(inc_dec.router)

# branches
app.include_router(operations.router)
app.include_router(min_max.router)
app.include_router(geometry.router)
app.include_router(geometry_2.router)

# loops
app.include_router(while_loop_factorial.router)
app.include_router(while_loop_power.router)
app.include_router(do_while_loop_factorial.router)
app.include_router(do_while_loop_power.router)
app.include_router(for_loop_factorial.router)
app.include_router(for_loop_power.router)

# functions
app.include_router(function_factorial.router)
app.include_router(function_power.router)
app.include_router(function_guessing.router)
app.include_router(module_namespace_power.router)

# lists
app.include_router(list_indexing.router)
app.include_router(list_iteration.router)
app.include_router(list_iteration_function.router)
app.include_router(list_iteration_module.router)
app.include_router(list_min_max_5.router)

# classes
app.include_router(actors_show.router)
app.include_router(actors_show_module.router)
app.include_router(fetch_data.router)


@app.exception_handler(RequestValidationError)
def invalid_input(request: Request, error: RequestValidationError):
    """Shown when a value from a form can not be converted (e.g. the text "abc" into a number)."""
    problems = []
    for e in error.errors():
        name = e["loc"][-1]  # the name of the field in the form
        problems.append(f"{name}: {e['msg']}")
    return templates.TemplateResponse(
        request, "error.html", {"title": "Invalid input", "problems": problems}, status_code=422
    )


@app.exception_handler(Exception)
def program_error(request: Request, error: Exception):
    """Shown when the program stops with an error; the details are written in the terminal."""
    problems = [f"{type(error).__name__}: {error}"]
    return templates.TemplateResponse(
        request, "error.html", {"title": "An error has occurred", "problems": problems}, status_code=500
    )


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
