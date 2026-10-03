# 01 - HTML, CSS and Bootstrap

Static web pages: every sample is an `.html` file that the browser shows exactly as it is written.

```text
python main.py
```

Then open <http://localhost:8000> and browse the folders:

| Folder | Lecture | Content |
|---|---|---|
| `wwwroot/01-html` | Introduction to HTML | basic elements, text, images, links, tables, forms |
| `wwwroot/02-css` | Introduction to CSS | styles in an element, in a document, in a separate file |
| `wwwroot/03-bootstrap` | Introduction to Bootstrap | containers, grid, tables, components, forms |

To see how a page is written, open the same file in your editor, or use *View page source* in the browser.
Change a file, save it, and reload the page.

## What `main.py` does

It is a small web server:

- it sends the files of the folder `wwwroot` to the browser, and shows the content of a folder as a list of links;
- the forms of the samples are sent to the address `/process-form`, which answers with a page that shows
  what the server has received: the method (GET or POST) and the names and values of the fields.

You do not have to understand `main.py` at this point - it is written with the tools from the second part of the course.

Python also has a ready-made server for static files: `python -m http.server 8000 --directory wwwroot`
does the first of the two jobs.
