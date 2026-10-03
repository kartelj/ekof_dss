"""
Reading data: the weather forecasts are read from a file in the JSON format.
"""

import datetime
import json

from fastapi import APIRouter, Request

from templating import BASE_DIR, templates

router = APIRouter()


class WeatherForecast:
    def __init__(self, date: datetime.date, temperature_c: int, summary: str):
        self.date = date
        self.temperature_c = temperature_c
        self.summary = summary

    @property
    def temperature_f(self) -> int:
        """A property is used like a variable (forecast.temperature_f), but its value is calculated."""
        return 32 + round(self.temperature_c * 9 / 5)


@router.get("/fetch-data")
def show(request: Request):
    text = (BASE_DIR / "sample-data" / "weather.json").read_text(encoding="utf-8")

    # json.loads turns the text into Python lists and dictionaries
    forecasts = []
    for item in json.loads(text):
        forecast = WeatherForecast(
            date=datetime.date.fromisoformat(item["date"]),
            temperature_c=item["temperature_c"],
            summary=item["summary"],
        )
        forecasts.append(forecast)

    return templates.TemplateResponse(request, "fetch_data.html", {"forecasts": forecasts})
