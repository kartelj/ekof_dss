"""
Web server for the HTML, CSS and Bootstrap samples.

The server does two things:

  1. it sends the files stored in the `wwwroot` folder to the browser, and lets
     you browse the sub-folders of `wwwroot` (this is the job of every "static"
     web server, such as Apache or nginx);
  2. it shows what the browser has sent when one of the sample forms is submitted.

Start it with      python main.py
and then open      http://localhost:8000

You do not have to understand this file yet - we will come back to it once we
have learned Python and FastAPI.
"""

from pathlib import Path

import uvicorn
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse, RedirectResponse, Response
from fastapi.templating import Jinja2Templates

BASE_DIR = Path(__file__).parent
WWWROOT = (BASE_DIR / "wwwroot").resolve()

app = FastAPI(title="HTML, CSS and Bootstrap samples")
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/process-form")
@app.post("/process-form")
async def process_form(request: Request):
    """Shows the data that the browser sent when a form was submitted."""
    form = await request.form()
    return templates.TemplateResponse(
        request,
        "form_data.html",
        {
            "method": request.method,
            "url": str(request.url),
            "query_parameters": request.query_params.multi_items(),
            "form_fields": form.multi_items(),
        },
    )


@app.get("/favicon.ico")
def favicon():
    """Browsers ask for the small picture of the site by themselves. There is none: 204 means "no content"."""
    return Response(status_code=204)


@app.get("/{path:path}")
def browse(request: Request, path: str):
    """Sends the requested file, or lists the content of the requested folder."""
    target = (WWWROOT / path).resolve()

    # never send anything that is outside of wwwroot (e.g. "../main.py")
    if not target.is_relative_to(WWWROOT) or not target.exists():
        raise HTTPException(status_code=404, detail="There is nothing at this address.")

    if target.is_file():
        return FileResponse(target)

    # relative links on a page work only if the address of a folder ends with "/"
    if path and not path.endswith("/"):
        return RedirectResponse(request.url.path + "/")

    visible = [entry for entry in target.iterdir() if not entry.name.startswith(".")]
    folders = sorted(entry.name for entry in visible if entry.is_dir())
    files = sorted(entry.name for entry in visible if entry.is_file())
    return templates.TemplateResponse(
        request,
        "directory.html",
        {"path": "/" + path, "is_root": target == WWWROOT, "folders": folders, "files": files},
    )


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
