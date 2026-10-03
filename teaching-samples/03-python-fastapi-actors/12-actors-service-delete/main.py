"""
Step 12: deleting an actor.

Every actor in the list has a button that deletes it. The button is a small form
that sends a POST request; the actor service removes the actor from its list.

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
