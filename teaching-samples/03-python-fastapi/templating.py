"""
The template engine shared by all the pages of the application.

A page is produced by combining an HTML template (from the `templates` folder)
with the values calculated by the Python code of that page.
"""

from pathlib import Path

from fastapi.templating import Jinja2Templates

BASE_DIR = Path(__file__).parent

templates = Jinja2Templates(directory=BASE_DIR / "templates")

# The navigation menu: sections, and the (title, address) of each page in a section.
# The template `nav_menu.html` goes through this list and creates the links.
MENU = [
    ("Basics", [
        ("Hello world", "/hello-world"),
        ("Append-clear", "/append-clear"),
        ("Incrementer", "/incrementer"),
        ("Decrementer", "/decrementer"),
        ("Incr-decr", "/inc-dec"),
    ]),
    ("Branches", [
        ("Operations", "/operations"),
        ("Min Max 5", "/min-max"),
        ("Geometry if", "/geometry"),
        ("Geometry match", "/geometry-2"),
    ]),
    ("Loops", [
        ("Factorial W", "/while-loop-factorial"),
        ("Power W", "/while-loop-power"),
        ("Factorial DW", "/do-while-loop-factorial"),
        ("Power DW", "/do-while-loop-power"),
        ("Factorial F", "/for-loop-factorial"),
        ("Power F", "/for-loop-power"),
    ]),
    ("Functions", [
        ("Factorial", "/function-factorial"),
        ("Power", "/function-power"),
        ("Guessing", "/function-guessing"),
        ("Power module", "/module-namespace-power"),
    ]),
    ("Lists", [
        ("Indexing", "/list-indexing"),
        ("Iteration", "/list-iteration"),
        ("Iteration function", "/list-iteration-function"),
        ("Iteration module", "/list-iteration-module"),
        ("Min Max 5", "/list-min-max-5"),
    ]),
    ("Classes", [
        ("Actors", "/actors-show"),
        ("Actors module", "/actors-show-module"),
        ("Fetch data", "/fetch-data"),
    ]),
]

# values placed here are visible in every template
templates.env.globals["menu"] = MENU
