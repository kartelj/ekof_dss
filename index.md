# Developing Software Solutions

**Python edition** - lectures and teaching samples

How web applications work, and how to build one: from a single HTML page to a complete system
with a web application, a RESTful service and a database - all of it in Python.

The course is on GitHub, [github.com/kartelj/ekof_dss](https://github.com/kartelj/ekof_dss), where a click on a
lecture shows its slides as one page, and on the web site of the course,
[kartelj.github.io/ekof_dss](https://kartelj.github.io/ekof_dss/), where a click on a lecture opens it as slides.
A folder of samples shows its files and its description.
How to run the samples and how to show the lectures on your own computer is explained at the end of this page.

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

| Module | Topic | Lectures | Samples |
|---|---|---|---|
| 01 | The web: HTTP, HTML, CSS, Bootstrap | 4 | [01-html-css-bootstrap](teaching-samples/01-html-css-bootstrap/) |
| 02 | Introduction to Python | 1 | [02-python-intro](teaching-samples/02-python-intro/) |
| 03 | Web applications with FastAPI, and the Python language in detail | 3 | [03-python-fastapi](teaching-samples/03-python-fastapi/) |
| 04 | One application, built step by step | - | [04-python-fastapi-actors](teaching-samples/04-python-fastapi-actors/) |
| 05 | Databases: the relational model, SQL, SQLite and PostgreSQL | 3 | [05-python-db-sqlite](teaching-samples/05-python-db-sqlite/), [05-python-db-supabase](teaching-samples/05-python-db-supabase/) |
| 06 | RESTful services | 2 | [06-python-rest-sqlite](teaching-samples/06-python-rest-sqlite/), [06-python-rest-supabase](teaching-samples/06-python-rest-supabase/) |
| 07 | The complete system: web application + RESTful service + database | - | [07-python-fastapi-rest-sqlite](teaching-samples/07-python-fastapi-rest-sqlite/), [07-python-fastapi-rest-supabase](teaching-samples/07-python-fastapi-rest-supabase/) |

### 01 - The web

How a browser and a web server talk to each other, and the three languages of a web page: HTML for the content,
CSS for the look, and Bootstrap - a ready-made style sheet - for pages that adapt to every screen.

- Lectures:
  [Introduction to web applications and the HTTP protocol](presentations/01-01-client-server-web.md) ·
  [Introduction to HTML](presentations/01-02-html.md) ·
  [Introduction to CSS](presentations/01-03-css.md) ·
  [Introduction to Bootstrap](presentations/01-04-bootstrap.md)
- Samples: [01-html-css-bootstrap](teaching-samples/01-html-css-bootstrap/) - static pages, shown by a small
  Python web server

### 02 - Introduction to Python

The basics of the language, with small programs that run in the terminal: variables and types, input, decisions,
loops, lists, dictionaries, functions, modules and errors. No previous programming is assumed.

- Lecture: [Introduction to Python](presentations/02-01-python-intro.md)
- Samples: [02-python-intro](teaching-samples/02-python-intro/) - eleven short programs, one topic each, and a
  complete small program at the end

### 03 - Web applications with FastAPI

A web page made by a Python program, at the moment of the request: routes and functions with FastAPI,
HTML templates with Jinja2, forms, and the state of an application. Then the language in more detail -
procedural and object-oriented programming - shown through the pages of one sample application.

- Lectures:
  [Introduction to FastAPI and Jinja2](presentations/03-01-fastapi-jinja2.md) ·
  [Python: procedural programming](presentations/03-02-python-procedural.md) ·
  [Python: object-oriented programming](presentations/03-03-python-oop.md)
- Samples: [03-python-fastapi](teaching-samples/03-python-fastapi/) - one web application with many small pages,
  each page demonstrates one topic of the language

### 04 - One application, step by step

*Vanity Fair*, a list of actors, built in 14 small steps: from an empty application to pages with navigation,
components, services, adding, deleting and searching. Every step is a complete application.
The lectures of module 03 explain the ideas that the steps use.

- Samples: [04-python-fastapi-actors](teaching-samples/04-python-fastapi-actors/)

### 05 - Databases

Why applications keep their data in a database, how the data is organized into tables, the language SQL,
and two database systems: SQLite (a file on our computer) and PostgreSQL (a server - here in the cloud, as Supabase).

- Lectures:
  [Introduction to databases and the relational model](presentations/05-01-relational-model.md) ·
  [Introduction to SQL](presentations/05-02-sql.md) ·
  [SQLite and PostgreSQL](presentations/05-03-sqlite-postgresql.md)
- Samples: [05-python-db-sqlite](teaching-samples/05-python-db-sqlite/) - the SQL scripts of the lectures, and
  Python programs that use a database; [05-python-db-supabase](teaching-samples/05-python-db-supabase/) - the same
  with a database in the cloud

### 06 - RESTful services

A service that sends data, not pages: resources, HTTP methods, status codes and JSON, and a service written with
FastAPI and SQLModel, with its data in a database.

- Lectures:
  [Introduction to REST APIs](presentations/06-01-restful-api.md) ·
  [RESTful services with FastAPI](presentations/06-02-fastapi-rest.md)
- Samples: [06-python-rest-sqlite](teaching-samples/06-python-rest-sqlite/),
  [06-python-rest-supabase](teaching-samples/06-python-rest-supabase/)

### 07 - The complete system

Everything together: the browser talks to the web application of module 04, the web application gets its data
from the RESTful service of module 06, and only the service talks to the database.
The second half of the lecture [RESTful services with FastAPI](presentations/06-02-fastapi-rest.md) explains it.

- Samples: [07-python-fastapi-rest-sqlite](teaching-samples/07-python-fastapi-rest-sqlite/),
  [07-python-fastapi-rest-supabase](teaching-samples/07-python-fastapi-rest-supabase/)

## Working with the course

**Getting started.** The course needs Python 3.12 or newer. The [README](README.md) explains how to install the
packages of the course, and how to start the samples: every sample is started with `python main.py` in its folder
(the programs of module 02 with `python` and the name of the file).

**The lectures as slides.** On GitHub a lecture is shown as one long page; as slides, the lectures are on the
web site of the course: [kartelj.github.io/ekof_dss/presentations](https://kartelj.github.io/ekof_dss/presentations/).
To show them from your own computer (e.g. without the internet, or after a change), start a web server in the folder
of the course and open the list of lectures:

```text
python -m http.server 8080
```

`http://localhost:8080/presentations/` - keys: arrows or space for the next slide, `Esc` for an overview of all the
slides, `F` for full screen, `S` for the speaker notes.

**The Supabase samples** (the folders whose names end with `-supabase`) need a free Supabase project of your own -
see [05-python-db-supabase](teaching-samples/05-python-db-supabase/). Everything else works without it.

## About

This is a Python edition of the course *Developing Software Solutions*, originally taught with C#, Blazor,
ASP.NET and SQL Server: [github.com/ekof-dss](https://github.com/ekof-dss) (by Vladimir Filipović).
The structure of the course follows the original; the lectures are written anew for Python.

The teaching samples are derived from the samples of the original course and are licensed under the
GNU General Public License v3.0 - see [LICENSE](LICENSE).
