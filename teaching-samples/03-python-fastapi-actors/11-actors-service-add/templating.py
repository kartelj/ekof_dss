"""The template engine, shared by all the pages of the application."""

from pathlib import Path

from fastapi.templating import Jinja2Templates

from dependencies import get_messaging_service

BASE_DIR = Path(__file__).parent

templates = Jinja2Templates(directory=BASE_DIR / "templates")

# a value placed here can be used in every template (the component AppMessages needs it)
templates.env.globals["messaging_service"] = get_messaging_service()
