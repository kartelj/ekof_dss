from fastapi import APIRouter, Request

from templating import templates

router = APIRouter()


@router.get("/")
def show(request: Request):
    return templates.TemplateResponse(request, "index.html")
