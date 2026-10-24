"""
Step 1: a new application.

This is the skeleton from which the application about actors will grow:
a home page, a page with a counter and a page that shows data from a file.

Start it with      python main.py
and then open      http://localhost:8000
"""

import json
from pathlib import Path

import uvicorn
from fastapi import FastAPI, Request, status
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

BASE_DIR = Path(__file__).parent

app = FastAPI(title="01-actors-new")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")

current_count = 0


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse(request, "index.html")


@app.get("/counter")
def counter(request: Request):
    return templates.TemplateResponse(request, "counter.html", {"current_count": current_count})


@app.post("/counter")
def increment_count():
    global current_count

    current_count += 1

    return RedirectResponse("/counter", status_code=status.HTTP_303_SEE_OTHER)


@app.get("/fetch-data")
def fetch_data(request: Request):
    text = (BASE_DIR / "sample-data" / "weather.json").read_text(encoding="utf-8")
    forecasts = json.loads(text)  # a list of dictionaries
    return templates.TemplateResponse(request, "fetch_data.html", {"forecasts": forecasts})


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
