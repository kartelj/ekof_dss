"""
The complete system with Supabase, part 2: the web application.

    browser  <-- HTML -->  web application  <-- JSON -->  RESTful service  <-- JSON -->  Supabase
                           (this program)                 (the folder rest-service)      (the database)

The application shows and changes actors and countries. It has no data of its own:
its services call the RESTful service for everything. It knows nothing about Supabase -
for the application it makes no difference where the RESTful service keeps the data.
The pages are styled with Bootstrap.

Start the RESTful service first (python main.py in the folder rest-service), then
start this application with      python main.py
and open                         http://localhost:8000
"""

import httpx2
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from dependencies import REST_SERVICE_URL
from pages import actor_detail, actors, countries, country_detail, dashboard, messages
from templating import BASE_DIR, templates

app = FastAPI(title="Vanity Fair")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

app.include_router(dashboard.router)
app.include_router(actors.router)
app.include_router(actor_detail.router)
app.include_router(countries.router)
app.include_router(country_detail.router)
app.include_router(messages.router)


@app.get("/")
def index():
    """The application starts with the dashboard."""
    return RedirectResponse("/dashboard")


@app.exception_handler(httpx2.HTTPError)
def service_error(request: Request, error: httpx2.HTTPError):
    """Shown when the RESTful service does not answer, or answers with an error."""
    return templates.TemplateResponse(
        request,
        "error.html",
        {"service_url": REST_SERVICE_URL, "error": f"{type(error).__name__}: {error}"},
        status_code=503,
    )


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
