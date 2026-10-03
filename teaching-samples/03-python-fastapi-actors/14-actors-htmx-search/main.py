"""
Step 14 (an extra step): searching while the user is typing.

Until now the browser asked for a whole new page after every click. Here the small
JavaScript library htmx asks the server only for a PIECE of the page - the list of
the actors found - and puts it into the page that is already shown. We do not write
any JavaScript: htmx is controlled by attributes in the HTML (hx-get, hx-trigger,
hx-target), see templates/components/app_actor_search.html.

Start it with      python main.py
and then open      http://localhost:8000
"""

import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from pages import actor_detail, actors, dashboard, messages
from templating import BASE_DIR

app = FastAPI(title="Vanity Fair")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

app.include_router(dashboard.router)
app.include_router(actors.router)
app.include_router(actor_detail.router)
app.include_router(messages.router)


@app.get("/")
def index():
    """The application starts with the dashboard."""
    return RedirectResponse("/dashboard")


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
