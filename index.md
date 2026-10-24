# Developing Software Solutions

**Python edition** - lectures and teaching samples

How web applications work, and how to build one: from a single HTML page to a complete system
with a web application, a RESTful service and a database - all of it in Python.

The course is on GitHub, [github.com/kartelj/ekof_dss](https://github.com/kartelj/ekof_dss), where a click on a
lecture shows its slides as one page, and on the web site of the course,
[kartelj.github.io/ekof_dss](https://kartelj.github.io/ekof_dss/), where a click on a lecture opens it as slides.
A folder of samples shows its files and its description.
How to run the samples and how to show the lectures on your own computer is explained at the end of this page.

## Instructor

Aleksandar Kartelj, [aleksandar.kartelj@gmail.com](mailto:aleksandar.kartelj@gmail.com)

## Aim and objectives

The objective of the course is to develop and broaden student competences in the basic components of
information systems development, in development concepts in Python, in service oriented solutions and in
modern software architectures.

After the course, students are able to

- explain the basic components of information systems development and how the web works;
- write programs in Python;
- build dynamic web sites, applications and services with FastAPI, an open-source web framework for Python;
- use a programming model organized around objects, and apply modular programming;
- store data in a relational database and work with it from a program;
- implement a service oriented architecture: a web application that uses a RESTful service.

## The course

| Module | Topic | Lectures | Samples | Download |
|---|---|---|---|---|
| 01 | The web: HTTP, HTML, CSS, Bootstrap | 4 | [01-html-css-bootstrap](teaching-samples/01-html-css-bootstrap/) | [01-html-css-bootstrap.zip](https://kartelj.github.io/ekof_dss/downloads/01-html-css-bootstrap.zip) |
| 02 | Introduction to Python | 1 | [02-python-intro](teaching-samples/02-python-intro/) | [02-python-intro.zip](https://kartelj.github.io/ekof_dss/downloads/02-python-intro.zip) |
| 03 | Web applications with FastAPI, and the Python language in detail | 3 | [03-python-fastapi](teaching-samples/03-python-fastapi/) | [03-python-fastapi.zip](https://kartelj.github.io/ekof_dss/downloads/03-python-fastapi.zip) |
| 04 | One application, built step by step | - | [04-python-fastapi-actors](teaching-samples/04-python-fastapi-actors/) | [04-python-fastapi-actors.zip](https://kartelj.github.io/ekof_dss/downloads/04-python-fastapi-actors.zip) |
| 05 | Databases: the relational model, SQL, SQLite and PostgreSQL | 3 | [05-python-db-sqlite](teaching-samples/05-python-db-sqlite/), [05-python-db-supabase](teaching-samples/05-python-db-supabase/) | [05-python-db-sqlite.zip](https://kartelj.github.io/ekof_dss/downloads/05-python-db-sqlite.zip), [05-python-db-supabase.zip](https://kartelj.github.io/ekof_dss/downloads/05-python-db-supabase.zip) |
| 06 | RESTful services | 2 | [06-python-rest-sqlite](teaching-samples/06-python-rest-sqlite/), [06-python-rest-supabase](teaching-samples/06-python-rest-supabase/) | [06-python-rest-sqlite.zip](https://kartelj.github.io/ekof_dss/downloads/06-python-rest-sqlite.zip), [06-python-rest-supabase.zip](https://kartelj.github.io/ekof_dss/downloads/06-python-rest-supabase.zip) |
| 07 | The complete system: web application + RESTful service + database | - | [07-python-fastapi-rest-sqlite](teaching-samples/07-python-fastapi-rest-sqlite/), [07-python-fastapi-rest-supabase](teaching-samples/07-python-fastapi-rest-supabase/) | [07-python-fastapi-rest-sqlite.zip](https://kartelj.github.io/ekof_dss/downloads/07-python-fastapi-rest-sqlite.zip), [07-python-fastapi-rest-supabase.zip](https://kartelj.github.io/ekof_dss/downloads/07-python-fastapi-rest-supabase.zip) |

**Download** the archive of a module when the module starts: unzipped, it is one folder with everything that the
module needs - its samples and the list of the packages of the course. The column *Samples* shows the same files
here, on GitHub.

### 01 - The web

How a browser and a web server talk to each other, and the three languages of a web page: HTML for the content,
CSS for the look, and Bootstrap - a ready-made style sheet - for pages that adapt to every screen.

- Lectures:
  [Introduction to web applications and the HTTP protocol](presentations/01-01-client-server-web.md) ·
  [Introduction to HTML](presentations/01-02-html.md) ·
  [Introduction to CSS](presentations/01-03-css.md) ·
  [Introduction to Bootstrap](presentations/01-04-bootstrap.md)
- Samples: [01-html-css-bootstrap](teaching-samples/01-html-css-bootstrap/) - static pages, shown by a small
  Python web server; download: [01-html-css-bootstrap.zip](https://kartelj.github.io/ekof_dss/downloads/01-html-css-bootstrap.zip)

### 02 - Introduction to Python

The basics of the language, with small programs that run in the terminal: variables and types, input, decisions,
loops, lists, dictionaries, functions, modules and errors. No previous programming is assumed.

- Lecture: [Introduction to Python](presentations/02-01-python-intro.md)
- Samples: [02-python-intro](teaching-samples/02-python-intro/) - eleven short programs, one topic each, and a
  complete small program at the end; download: [02-python-intro.zip](https://kartelj.github.io/ekof_dss/downloads/02-python-intro.zip)

### 03 - Web applications with FastAPI

A web page made by a Python program, at the moment of the request: routes and functions with FastAPI,
HTML templates with Jinja2, forms, and the state of an application. Then the language in more detail -
procedural and object-oriented programming - shown through the pages of one sample application.

- Lectures:
  [Introduction to FastAPI and Jinja2](presentations/03-01-fastapi-jinja2.md) ·
  [Python: procedural programming](presentations/03-02-python-procedural.md) ·
  [Python: object-oriented programming](presentations/03-03-python-oop.md)
- Samples: [03-python-fastapi](teaching-samples/03-python-fastapi/) - one web application with many small pages,
  each page demonstrates one topic of the language; download: [03-python-fastapi.zip](https://kartelj.github.io/ekof_dss/downloads/03-python-fastapi.zip)

### 04 - One application, step by step

*Vanity Fair*, a list of actors, built in 14 small steps: from an empty application to pages with navigation,
components, services, adding, deleting and searching. Every step is a complete application.
The lectures of module 03 explain the ideas that the steps use.

- Samples: [04-python-fastapi-actors](teaching-samples/04-python-fastapi-actors/); download: [04-python-fastapi-actors.zip](https://kartelj.github.io/ekof_dss/downloads/04-python-fastapi-actors.zip)

### 05 - Databases

Why applications keep their data in a database, how the data is organized into tables, the language SQL,
and two database systems: SQLite (a file on our computer) and PostgreSQL (a server - here in the cloud, as Supabase).

- Lectures:
  [Introduction to databases and the relational model](presentations/05-01-relational-model.md) ·
  [Introduction to SQL](presentations/05-02-sql.md) ·
  [SQLite and PostgreSQL](presentations/05-03-sqlite-postgresql.md)
- Samples: [05-python-db-sqlite](teaching-samples/05-python-db-sqlite/) - the SQL scripts of the lectures, and
  Python programs that use a database; [05-python-db-supabase](teaching-samples/05-python-db-supabase/) - the same
  with a database in the cloud; download: [05-python-db-sqlite.zip](https://kartelj.github.io/ekof_dss/downloads/05-python-db-sqlite.zip), [05-python-db-supabase.zip](https://kartelj.github.io/ekof_dss/downloads/05-python-db-supabase.zip)

### 06 - RESTful services

A service that sends data, not pages: resources, HTTP methods, status codes and JSON, and a service written with
FastAPI and SQLModel, with its data in a database.

- Lectures:
  [Introduction to REST APIs](presentations/06-01-restful-api.md) ·
  [RESTful services with FastAPI](presentations/06-02-fastapi-rest.md)
- Samples: [06-python-rest-sqlite](teaching-samples/06-python-rest-sqlite/),
  [06-python-rest-supabase](teaching-samples/06-python-rest-supabase/); download: [06-python-rest-sqlite.zip](https://kartelj.github.io/ekof_dss/downloads/06-python-rest-sqlite.zip),
  [06-python-rest-supabase.zip](https://kartelj.github.io/ekof_dss/downloads/06-python-rest-supabase.zip)

### 07 - The complete system

Everything together: the browser talks to the web application of module 04, the web application gets its data
from the RESTful service of module 06, and only the service talks to the database.
The second half of the lecture [RESTful services with FastAPI](presentations/06-02-fastapi-rest.md) explains it.

- Samples: [07-python-fastapi-rest-sqlite](teaching-samples/07-python-fastapi-rest-sqlite/),
  [07-python-fastapi-rest-supabase](teaching-samples/07-python-fastapi-rest-supabase/); download:
  [07-python-fastapi-rest-sqlite.zip](https://kartelj.github.io/ekof_dss/downloads/07-python-fastapi-rest-sqlite.zip), [07-python-fastapi-rest-supabase.zip](https://kartelj.github.io/ekof_dss/downloads/07-python-fastapi-rest-supabase.zip)

## How the course is passed

The course is passed with two homeworks and a project during the semester, and a final exam.

| Part | What it is | Modules | Points |
|---|---|---|---|
| Homework 1 | a personal web presentation: a small site about yourself, made with HTML, CSS and Bootstrap, in a GitHub repository of your own and published with GitHub Pages | 01 | 15 |
| Homework 2 | a web application made with FastAPI and Jinja2 templates | 02 - 04 | 15 |
| Project | a complete system - a web application, a RESTful service and a database - in a GitHub repository | 05 - 07 | 30 |
| Final exam | in the computer room of the Faculty, at the computer | the whole course | 40 |

The exercises in the lectures and the assignments at their end are for practice: they are not graded, and their
solutions are public.

The homeworks and the project are the pre-exam obligations, together 60 points; the final exam brings the other 40.
The final grade comes from the sum of the points, out of 100:

| Points | 0 - 50 | 51 - 60 | 61 - 70 | 71 - 80 | 81 - 90 | 91 - 100 |
|---|---|---|---|---|---|---|
| Grade | 5 (failed) | 6 | 7 | 8 | 9 | 10 |

## Literature

The lectures, the samples and the exercises of the course are its main material. These books and pages go further.

**Books**

- Jon Duckett: *HTML and CSS: Design and Build Websites*, Wiley, 2011 - module 01.
- Eric Matthes: *Python Crash Course*, 3rd edition, No Starch Press, 2023 - modules 02 and 03.
- Bill Lubanovic: *FastAPI: Modern Python Web Development*, O'Reilly, 2023 - modules 03, 04 and 06.
- Alan Beaulieu: *Learning SQL*, 3rd edition, O'Reilly, 2020 - module 05.
- Leonard Richardson, Mike Amundsen, Sam Ruby: *RESTful Web APIs*, O'Reilly, 2013 - module 06.

**Free on the web**

- The web: [MDN - Learn web development](https://developer.mozilla.org/en-US/docs/Learn_web_development) (HTML and CSS),
  [MDN - HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP),
  [Bootstrap 4.5 documentation](https://getbootstrap.com/docs/4.5/getting-started/introduction/)
- Python: [The Python Tutorial](https://docs.python.org/3/tutorial/),
  Al Sweigart: [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) (a whole book, free to read online),
  [Python in Visual Studio Code](https://code.visualstudio.com/docs/python/python-tutorial)
- Web applications and services: [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/),
  [Jinja templates](https://jinja.palletsprojects.com/en/stable/templates/), [htmx](https://htmx.org/docs/),
  [SQLModel](https://sqlmodel.tiangolo.com/)
- Databases: [SQLite](https://www.sqlite.org/docs.html), [PostgreSQL](https://www.postgresql.org/docs/),
  [Supabase](https://supabase.com/docs)
- REST, from its source: Roy Fielding,
  [Representational State Transfer](https://ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm)
  (chapter 5 of his dissertation, 2000) - for the curious

## Working with the course

**Getting started.** Install Python 3.12 or newer and Visual Studio Code, once. For every module, download the
archive of its samples (the column *Download* in the table above), unzip it, and open the folder in VS Code; in its
terminal install the packages of the course - once for every folder. The first lecture shows every step on its
slides (*The course on your computer*), and the [README](README.md) lists them too. A sample is then started with
`python main.py` in its folder (the programs of module 02 with `python` and the name of the file).

**The lectures as slides.** On GitHub a lecture is shown as one long page; as slides, the lectures are on the
web site of the course: [kartelj.github.io/ekof_dss/presentations](https://kartelj.github.io/ekof_dss/presentations/).
To show them from your own computer (e.g. without the internet, or after a change), start a web server in the folder
of the course and open the list of lectures:

```text
python -m http.server 8080
```

`http://localhost:8080/presentations/` - keys: arrows or space for the next slide, `Esc` for an overview of all the
slides, `F` for full screen, `S` for the speaker notes.

**Exercises.** The lectures and the practice go together: after every topic a lecture has an exercise on what it
has shown so far (the slides with a green title; the button *Solution* shows a solution, on GitHub it is a section
that opens with a click), and every lecture ends with a larger assignment. The solutions of the assignments are in
the folder [exercises](exercises/).

**The Supabase samples** (the folders whose names end with `-supabase`) need a free Supabase project of your own -
see [05-python-db-supabase](teaching-samples/05-python-db-supabase/). Everything else works without it.

## About

This is a Python edition of the course *Developing Software Solutions*, originally taught with C#, Blazor,
ASP.NET and SQL Server: [github.com/ekof-dss](https://github.com/ekof-dss) (by Vladimir Filipović).
The structure of the course follows the original; the lectures are written anew for Python.

The teaching samples are derived from the samples of the original course and are licensed under the
GNU General Public License v3.0 - see [LICENSE](LICENSE).
