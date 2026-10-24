"""
Takes the screenshots that the lectures show (the PNG files in presentations/images).

    pip install -r tools/requirements.txt
    python tools/take_screenshots.py                  all the screenshots
    python tools/take_screenshots.py 01-02-html       only the screenshots of these lectures

What to take is described in tools/screenshots/<lecture>.json - a list of shots like this one:

    {
        "file": "fastapi-incrementer.png",      the name of the picture in presentations/images
        "sample": "03-python-fastapi",          the sample that is started (a folder with main.py) ...
        "path": "/incrementer",                 ... and the address that is opened in it
        "steps": [{"click": "text=Increment"}]  what the user does before the picture is taken
    }

Instead of "sample" and "path", a shot can have
    "url": "https://..."     a page of another site (the address bar shows it without https://)
    "site": "index.html"     a page of the course site - this repository as GitHub Pages shows it
    "html": "<p>...</p>"     a piece of HTML, shown on an empty page ("bootstrap": true adds Bootstrap 4.5.2);
                             the picture is as high as the piece
    "terminal": "$ ..."      text, shown in a terminal window
and further
    "width", "height"        the size of the browser window in pixels (default 800 x 450)
    "full_page": true        the whole page, not only the part that fits into the window
    "element": "nav"         only this element (a CSS selector), without the browser window around it
    "frame": false           no browser window around the picture (the default for "html" and "element")
    "address": "..."         the address shown in the browser window (by default the address of the page,
                             with the port 8000 - or "port": 8001 for the RESTful services)
    "title": "..."           the title of the terminal window
The steps are {"fill": selector, "value": text}, {"select": selector, "value": option}, {"check": selector},
{"click": selector}, {"hover": selector}, {"scroll": selector}, {"press": key} and {"wait": milliseconds};
a selector is anything that Playwright understands, e.g. "#name", "text=Save" or "button >> nth=1".

The samples are copied to a temporary folder and run there, so nothing in the repository changes
(the databases that the samples create are thrown away). A web application of module 07 gets its
RESTful service as well. The browser is Google Chrome if it is installed, otherwise the Chromium of
Playwright (python -m playwright install chromium).
"""

import base64
import functools
import html
import http.server
import json
import os
import shutil
import socket
import socketserver
import struct
import subprocess
import sys
import tempfile
import threading
import time
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlsplit

from playwright.sync_api import Error as PlaywrightError
from playwright.sync_api import TimeoutError as PlaywrightTimeout
from playwright.sync_api import Page, sync_playwright

ROOT = Path(__file__).resolve().parent.parent
SHOTS = ROOT / "tools" / "screenshots"
IMAGES = ROOT / "presentations" / "images"
SCALE = 2  # pixels of the picture per pixel of the page: sharp on large screens and projectors
SITE = "kartelj.github.io/ekof_dss/"  # the address of the course site, shown for the pages of "site"

BOOTSTRAP = '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">'

# the window around a picture: the bar of a browser with the address, a terminal, or a plain border
FRAME_CSS = """
body { margin: 0; padding: 16px; background: transparent; font-family: Arial, Helvetica, sans-serif; }
.shot { display: inline-block; border: 1px solid #c4c4c4; border-radius: 8px; overflow: hidden; background: #fff; }
.shot img { display: block; }
.bar { display: flex; align-items: center; gap: 14px; height: 38px; padding: 0 12px; background: #ececec;
       border-bottom: 1px solid #d4d4d4; }
.dots { display: flex; gap: 7px; flex: none; }
.dots i { width: 12px; height: 12px; border-radius: 50%; background: #ff5f57; }
.dots i:nth-child(2) { background: #febc2e; }
.dots i:nth-child(3) { background: #28c840; }
.address { flex: 1; height: 24px; line-height: 24px; padding: 0 12px; border-radius: 12px; background: #fff;
           color: #333; font-size: 14px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.plain { padding: 10px; border-radius: 6px; }
.terminal { background: #1e1e1e; border-color: #444; }
.terminal .bar { background: #3a3a3a; border-bottom-color: #2a2a2a; }
.terminal .title { flex: 1; text-align: center; color: #ccc; font-size: 13px; margin-right: 50px; }
.terminal pre { margin: 0; padding: 14px 18px; color: #e8e8e8; font: 15px/1.45 Menlo, Consolas, monospace;
                white-space: pre-wrap; }
"""


# replaces 127.0.0.1:<temporary port> in the text of the page: the port of the page itself becomes
# the usual port of the sample, any other one (a RESTful service called by the page) becomes 8001
SHOW_USUAL_PORTS = """([own, usual]) => {
    const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
    while (walker.nextNode()) {
        const node = walker.currentNode;
        node.nodeValue = node.nodeValue.replace(/127\\.0\\.0\\.1:(\\d+)/g,
            (_, port) => "localhost:" + (Number(port) === own ? usual : 8001));
    }
}"""


def free_port() -> int:
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


class Samples:
    """Starts the samples (each one once, on a free port) in a temporary copy of teaching-samples."""

    def __init__(self, folder: Path):
        self.folder = folder
        self.started: dict[str, tuple[subprocess.Popen, int]] = {}
        self.site = None  # the web server of the course site, started when a shot needs it

    def site_address(self) -> str:
        """The course site: the files of the repository, sent as they are - as GitHub Pages does."""
        if self.site is None:
            class Quiet(http.server.SimpleHTTPRequestHandler):
                def log_message(self, *args):
                    pass

            self.site = socketserver.ThreadingTCPServer(("127.0.0.1", 0), functools.partial(Quiet, directory=str(ROOT)))
            threading.Thread(target=self.site.serve_forever, daemon=True).start()
        return f"http://127.0.0.1:{self.site.server_address[1]}"

    def address(self, sample: str) -> str:
        if sample not in self.started:
            self.started[sample] = self.start(sample)
        return f"http://127.0.0.1:{self.started[sample][1]}"

    def start(self, sample: str) -> tuple[subprocess.Popen, int]:
        folder = self.folder / sample
        env = dict(os.environ)
        if folder.name == "web-app":
            # a web application of the complete system needs its RESTful service
            env["REST_SERVICE_URL"] = self.address(f"{Path(sample).parent}/rest-service") + "/api"
        port = free_port()
        process = subprocess.Popen(
            [sys.executable, "-m", "uvicorn", "main:app", "--port", str(port)],
            cwd=folder, env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        )
        for _ in range(50):
            time.sleep(0.2)
            try:
                urllib.request.urlopen(f"http://127.0.0.1:{port}/", timeout=2)
                return process, port
            except urllib.error.HTTPError:
                return process, port  # it answers, even if not with a page
            except OSError:
                if process.poll() is not None:
                    break
        process.kill()
        raise RuntimeError(f"the sample {sample} did not start")

    def stop(self) -> None:
        for process, _ in self.started.values():
            process.terminate()
            process.wait()
        if self.site is not None:
            self.site.shutdown()


def png_width(picture: bytes) -> int:
    """The width of a PNG picture in pixels (it is written in the header of the file)."""
    return struct.unpack(">I", picture[16:20])[0]


def shown_address(url: str, port: int) -> str:
    """The address as the reader of the lecture would see it: localhost and the usual port of the sample."""
    parts = urlsplit(url)
    address = f"localhost:{port}{parts.path}"
    if parts.query:
        address += "?" + parts.query
    if parts.fragment:
        address += "#" + parts.fragment
    return address


def do_steps(page: Page, steps: list[dict]) -> None:
    for step in steps:
        if "fill" in step:
            page.fill(step["fill"], step["value"])
        elif "select" in step:
            page.select_option(step["select"], step["value"])
        elif "check" in step:
            page.check(step["check"])
        elif "click" in step:
            page.click(step["click"])
            try:
                page.wait_for_load_state("networkidle", timeout=5000)
            except PlaywrightTimeout:
                pass  # big sites keep loading in the background
            page.wait_for_timeout(300)
        elif "hover" in step:
            page.hover(step["hover"])
        elif "scroll" in step:
            page.locator(step["scroll"]).first.evaluate("element => element.scrollIntoView()")
        elif "press" in step:
            page.keyboard.press(step["press"])
            page.wait_for_load_state("networkidle")
        elif "wait" in step:
            page.wait_for_timeout(step["wait"])
        else:
            raise ValueError(f"unknown step {step}")


def take(browser, samples: Samples, shot: dict) -> bytes:
    """Opens the page, does the steps, and returns the picture of the page together with its window."""
    width, height = shot.get("width", 800), shot.get("height", 450)

    if "terminal" in shot:
        title = html.escape(shot.get("title", "Terminal"))
        inside = f'<div class="bar"><span class="dots"><i></i><i></i><i></i></span><span class="title">{title}</span></div>'
        inside += f'<pre>{html.escape(shot["terminal"])}</pre>'
        return frame(browser, f'<div class="shot terminal" style="width: {width}px">{inside}</div>', width)

    context = browser.new_context(viewport={"width": width, "height": height}, device_scale_factor=SCALE)
    page = context.new_page()
    try:
        if "sample" in shot:
            page.goto(samples.address(shot["sample"]) + shot.get("path", "/"), wait_until="networkidle")
        if "site" in shot:
            page.goto(f"{samples.site_address()}/{shot['site']}", wait_until="networkidle")
        if "url" in shot:
            # big sites keep loading in the background, so "networkidle" never comes
            page.goto(shot["url"], wait_until="load")
            page.wait_for_timeout(2000)
        if "html" in shot:
            head = '<meta charset="utf-8">' + (BOOTSTRAP if shot.get("bootstrap") else "")
            body = f'<div id="snippet" style="padding: 12px">{shot["html"]}</div>'
            page.set_content(f"<!DOCTYPE html><html><head>{head}</head><body>{body}</body></html>",
                             wait_until="networkidle")
            shot = {"element": "#snippet", **shot}
        do_steps(page, shot.get("steps", []))
        if "sample" in shot:
            # a page that shows an address (its own, or that of a RESTful service) shows the usual ports
            page.evaluate(SHOW_USUAL_PORTS, [urlsplit(page.url).port, shot.get("port", 8000)])
        if "element" in shot:
            picture = page.locator(shot["element"]).first.screenshot()
        else:
            picture = page.screenshot(full_page=shot.get("full_page", False))
        url = page.url
    finally:
        context.close()

    image = f'<img src="data:image/png;base64,{base64.b64encode(picture).decode()}" width="{png_width(picture) // SCALE}">'
    if not shot.get("frame", ("sample" in shot or "url" in shot or "site" in shot) and "element" not in shot and "html" not in shot):
        return frame(browser, f'<div class="shot plain">{image}</div>', width)
    if "url" in shot:
        default = url.removeprefix("https://")
    elif "site" in shot:
        default = SITE + shot["site"].removesuffix("index.html")
    else:
        default = shown_address(url, shot.get("port", 8000))
    address = html.escape(shot.get("address", default))
    bar = f'<div class="bar"><span class="dots"><i></i><i></i><i></i></span><div class="address">{address}</div></div>'
    return frame(browser, f'<div class="shot">{bar}{image}</div>', width)


def frame(browser, content: str, width: int) -> bytes:
    """Draws the window around the picture, and returns a picture of both (with transparent corners)."""
    context = browser.new_context(viewport={"width": width + 60, "height": 400}, device_scale_factor=SCALE)
    page = context.new_page()
    page.set_content(f"<!DOCTYPE html><html><head><style>{FRAME_CSS}</style></head><body>{content}</body></html>")
    picture = page.locator(".shot").screenshot(omit_background=True)
    context.close()
    return picture


def main() -> None:
    lectures = sys.argv[1:] or sorted(path.stem for path in SHOTS.glob("*.json"))
    failures = []
    with tempfile.TemporaryDirectory() as temporary, sync_playwright() as playwright:
        shutil.copytree(ROOT / "teaching-samples", Path(temporary) / "samples",
                        ignore=shutil.ignore_patterns("__pycache__", "*.db"))
        samples = Samples(Path(temporary) / "samples")
        try:
            browser = playwright.chromium.launch(channel="chrome")
        except PlaywrightError:
            browser = playwright.chromium.launch()
        try:
            for lecture in lectures:
                for shot in json.loads((SHOTS / f"{lecture}.json").read_text(encoding="utf-8")):
                    try:
                        (IMAGES / shot["file"]).write_bytes(take(browser, samples, shot))
                        print(f"{lecture}: {shot['file']}")
                    except Exception as error:
                        failures.append(shot["file"])
                        print(f"{lecture}: {shot['file']} FAILED - {error}")
        finally:
            browser.close()
            samples.stop()
    if failures:
        raise SystemExit(f"{len(failures)} screenshots failed: {', '.join(failures)}")


if __name__ == "__main__":
    main()
