"""
Step 10: navigation.

The application now has several pages, each with its own address:

    /dashboard          the top actors
    /actors             the list of all the actors
    /actordetail/3      the details of the actor with the id 3

Every page has its Python module in the folder pages, and its template.
The layout shows the title, the menu with the links, the page, and the messages.

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
