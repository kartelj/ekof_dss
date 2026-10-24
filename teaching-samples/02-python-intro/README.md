# 02 - Introduction to Python

Small programs for the terminal, one topic each, in the order of the lecture
*Introduction to Python* (`presentations/02-01-python-intro.md`).
They need only Python itself - no packages, no web server.

Open this folder in Visual Studio Code (*File - Open Folder...*) and its terminal (*Terminal - New Terminal*),
and start a program by its name:

```text
python 01_hello.py
```

On some systems the command is `python3` (macOS, Linux) or `py` (Windows) instead of `python`.

| Program | Topic |
|---|---|
| `01_hello.py` | the first program: `print()` and comments |
| `02_variables.py` | variables; the types `int`, `float`, `str` and `bool`; arithmetic; f-strings |
| `03_input.py` | reading what the user types with `input()`, and converting the text into a number |
| `04_if.py` | decisions with `if` - `elif` - `else`: the grade of an exam from its points |
| `05_loops.py` | loops: `while` and `for` with `range()` - a deposit with interest |
| `06_lists.py` | lists: indexes, `append`, a loop over a list, `sum`, `min`, `max`, `sorted` |
| `07_dictionaries.py` | dictionaries: a price list, looking up a key, a loop over all the pairs |
| `08_functions.py` | functions: parameters, a default value, `return` |
| `09_modules.py` | modules: `import` from the standard library and from our own file `shop.py` |
| `10_errors.py` | errors, and catching them with `try` - `except` |
| `11_shopping_list.py` | a complete program that uses all of the above: a shopping list |

The programs `03`, `04`, `07`, `10` and `11` ask the user for input - type the answer and press Enter.
`11_shopping_list.py` runs until you type `q`.

Try changing the programs: other numbers, other texts, a new `elif`, a new function. Save the file and start
it again. When something goes wrong, read the last line of the error message first.

The interactive prompt is useful for short experiments: type `python` without a file name, and every line is
executed as soon as you press Enter. `exit()` ends it.
