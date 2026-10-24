# Developing Software Solutions - Python edition

Lectures and teaching samples for the course **Developing Software Solutions**:
how web applications work and how to build one - from an HTML page to a complete system
with a web application, a RESTful service and a database.

**The course page - all the lectures and samples, readable here on GitHub: [index.md](index.md)**

This is a Python edition of the course that was originally taught with C#, Blazor,
ASP.NET and SQL Server ([github.com/ekof-dss](https://github.com/ekof-dss), by Vladimir Filipović).
The structure of the course is the same, with one addition: a short introduction to Python
(module 02) comes before the first web application. The technologies are:

| Topic | Original course | This edition |
|---|---|---|
| Web pages | HTML, CSS, Bootstrap | HTML, CSS, Bootstrap (unchanged) |
| Programming language | C# | Python |
| Interactive pages | Blazor (code runs in the browser) | FastAPI + Jinja2 templates (code runs on the server) |
| RESTful services | ASP.NET Web API | FastAPI |
| Working with the database | Entity Framework | SQLModel |
| Database | SQL Server, Supabase | SQLite, Supabase (PostgreSQL) |

## What is in this repository

| Part of the course | Lectures (`presentations/`) | Samples (`teaching-samples/`) |
|---|---|---|
| Web | `01-01-client-server-web`, `01-02-html`, `01-03-css`, `01-04-bootstrap` | `01-html-css-bootstrap` |
| Introduction to Python | `02-01-python-intro` | `02-python-intro` |
| Web applications in Python | `03-01-fastapi-jinja2`, `03-02-python-procedural`, `03-03-python-oop` | `03-python-fastapi`, `04-python-fastapi-actors` |
| Databases | `05-01-relational-model`, `05-02-sql`, `05-03-sqlite-postgresql` | `05-python-db-sqlite`, `05-python-db-supabase` |
| RESTful services | `06-01-restful-api`, `06-02-fastapi-rest` | `06-python-rest-sqlite`, `06-python-rest-supabase` |
| The complete system | | `07-python-fastapi-rest-sqlite`, `07-python-fastapi-rest-supabase` |

Other files: `index.md` is the home page of the course, `requirements.txt` lists the Python
packages, `.env.example` shows the settings of the Supabase samples, `tests/smoke_test.py`
checks that all the samples work, `tools/take_screenshots.py` takes the screenshots of the lectures.

## Getting started

You need **Python 3.12 or newer** (`python --version` shows which one you have;
you can download Python from [python.org](https://www.python.org/downloads/)).

Open a terminal in the folder of the course, create a virtual environment - a private
place for the packages of the course - and install the packages:

```text
python -m venv .venv
source .venv/bin/activate          (on Windows:  .venv\Scripts\activate)
pip install -r requirements.txt
```

The environment has to be activated (the second line) in every new terminal.
On some systems the command is `python3` instead of `python`.

## Running the samples

Every sample from module 03 on is a folder with a file `main.py`. Go to the folder, and start it:

```text
cd teaching-samples/03-python-fastapi
python main.py
```

Then open the address that the sample uses - `http://localhost:8000` for web applications,
`http://localhost:8001/docs` for RESTful services. Stop a program with `Ctrl+C`.
While a program is running, it restarts by itself whenever you change and save one of its files.

| Sample | What it is | Address |
|---|---|---|
| `01-html-css-bootstrap` | static pages: HTML, CSS and Bootstrap samples | `localhost:8000` |
| `02-python-intro` | small programs, started by name: `python 01_hello.py` | (programs for the terminal) |
| `03-python-fastapi` | Python, shown through the pages of a small web application | `localhost:8000` |
| `04-python-fastapi-actors/01...14` | one web application, built in 14 steps | `localhost:8000` |
| `05-python-db-sqlite` | SQL scripts, and Python programs that use a database | (programs for the terminal) |
| `06-python-rest-sqlite/01...02` | RESTful services | `localhost:8001/docs` |
| `07-python-fastapi-rest-sqlite/...` | a web application (`web-app`) that uses a RESTful service (`rest-service`) | `localhost:8000` and `localhost:8001/docs` |

The complete system of module 07 consists of two programs. Start the `rest-service` first,
and then, in a second terminal, the `web-app`.

Each module has its own `README.md` with the details.

### The Supabase samples

The folders whose names end with `-supabase` do the same things with a database in the cloud
([Supabase](https://supabase.com), a service built around PostgreSQL). They need a Supabase project of
your own: see `teaching-samples/05-python-db-supabase/README.md`. Everything else in the course
works without it.

## The lectures

The lectures are Markdown files (`presentations/*.md`), shown as slides in the browser.
The slides need a web server - Python has one. In the folder of the course type:

```text
python -m http.server 8080
```

and open `http://localhost:8080/presentations/`. Useful keys: arrows or space - next and previous slide,
`Esc` - overview of all the slides, `F` - full screen, `S` - speaker notes.

To get a lecture as a PDF, add `&print-pdf` to its address
(`.../presentations/slides.html?deck=01-02-html&print-pdf`) and print the page from the browser.

On GitHub the same files are shown as ordinary pages, one lecture per page.

The course is also a web site, published by GitHub Pages from the branch `main` (Settings - Pages - Deploy
from a branch - `main`, `/ (root)`): [kartelj.github.io/ekof_dss](https://kartelj.github.io/ekof_dss/).
The site is the repository as it is: `index.html` shows the course page `index.md`, with the lectures opening
as slides, and `presentations/` is the list of lectures. The empty file `.nojekyll` tells GitHub to publish the
files unchanged (without it, GitHub would turn the Markdown files into pages, and the slides could not load them).
Every push to `main` updates the site within a minute or two.

To change a lecture, edit its `.md` file: slides are separated by a line with three dashes
(`---`), and every slide starts with `## Title`. Code and the page it makes can stand side by side
in two columns - see the comment in `presentations/slides.css`.

The pictures are in `presentations/images`: the diagrams are SVG files written by hand, the
screenshots (PNG) are taken by a program that starts the samples and opens their pages in a browser.
What it takes is described in `tools/screenshots/<lecture>.json`. After a change of a sample,
take the screenshots of the lectures that show it again:

```text
pip install -r tools/requirements.txt
python tools/take_screenshots.py 03-01-fastapi-jinja2
```

It uses Google Chrome if it is installed; otherwise first run `python -m playwright install chromium`.

## Checking the samples

```text
python tests/smoke_test.py
```

starts every sample (in a temporary copy) and requests its pages. Use it after changing
the samples, or after changing the versions of the packages in `requirements.txt`.

## License

The teaching samples are derived from the samples of the original course, which are licensed
under the GNU General Public License v3.0; this repository uses the same license (see `LICENSE`).
