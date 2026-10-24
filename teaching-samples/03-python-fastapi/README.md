# 03 - Python, shown through the pages of a web application

One web application with many small pages. Every page demonstrates one topic of programming in Python.

```text
python main.py
```

Then open <http://localhost:8000>. What the pages write with `print()` appears in the terminal.

| Section | Pages | Topics |
|---|---|---|
| Basics | Hello world, Append-clear, Incrementer, Decrementer, Incr-decr | sequence, variables, assignment, `int`, `Decimal` |
| Branches | Operations, Min Max 5, Geometry if, Geometry match | `if` / `elif` / `else`, conditional expression, `match` |
| Loops | Factorial and Power with W, DW and F | `while`, a loop with the condition at the end, `for` and `range` |
| Functions | Factorial, Power, Guessing, Power module | functions, parameters, `return`, modules |
| Lists | Indexing, Iteration, Iteration function, Iteration module, Min Max 5 | lists, indexes, slices, loops over lists |
| Classes | Actors, Actors module, Fetch data | classes and objects, reading JSON |

## How a page is made

Every page consists of two files with the same name:

- `pages/incrementer.py` - the Python code: a function that shows the page, and one function for every button;
- `templates/incrementer.html` - the HTML of the page, with places for the values (`{{ current_count }}`).

There are two kinds of pages:

- Pages that **calculate** (for example *Min Max 5*). The form uses the method GET: the values travel in the
  address, the function calculates the result and shows the page again. Nothing is remembered.
- Pages that **remember** (for example *Incrementer*). The value is kept in a variable of the module. The form uses
  the method POST, the function changes the variable and sends the browser back to the page.
  The variables live as long as the program runs, and they are shared by everybody who uses the application.

Other files:

| File or folder | Purpose |
|---|---|
| `main.py` | creates the application and adds all the pages to it |
| `templating.py` | the template engine and the content of the menu |
| `templates/layout.html`, `nav_menu.html` | the frame that is the same on every page |
| `helpers/` | functions used by several pages (the modules `mathematics` and `list_helper`) |
| `models/actor.py` | the class `Actor` |
| `static/` | the style sheet |

When a value in a form cannot be converted (a text where a number is expected), the application shows the page
*Invalid input*; when the program fails with an error, it shows the error - and the details are in the terminal.
