"""
A new RESTful service.

The service has one resource, the weather forecast. It does not send HTML pages:
its answers are data in the JSON format, meant to be read by other programs.

Start it with      python main.py
and then open      http://localhost:8001/weatherforecast     the data
                   http://localhost:8001/docs                the interactive documentation
"""

import datetime
import random

import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, computed_field

SUMMARIES = [
    "Freezing", "Bracing", "Chilly", "Cool", "Mild", "Warm", "Balmy", "Hot", "Sweltering", "Scorching",
]


class WeatherForecast(BaseModel):
    """The shape of the data that the service sends. FastAPI converts such objects into JSON."""

    date: datetime.date
    temperature_c: int
    summary: str | None = None

    @computed_field
    @property
    def temperature_f(self) -> int:
        return 32 + round(self.temperature_c * 9 / 5)


app = FastAPI(title="ActorsRestService")


@app.get("/weatherforecast")
def get_weather_forecast() -> list[WeatherForecast]:
    """Returns the forecast for the next five days (the values are random)."""
    forecasts = []
    for index in range(1, 6):
        forecast = WeatherForecast(
            date=datetime.date.today() + datetime.timedelta(days=index),
            temperature_c=random.randint(-20, 54),
            summary=random.choice(SUMMARIES),
        )
        forecasts.append(forecast)
    return forecasts


@app.get("/", include_in_schema=False)
def index():
    """The home address leads to the documentation of the service."""
    return RedirectResponse("/docs")


if __name__ == "__main__":
    uvicorn.run("main:app", port=8001, reload=True)
