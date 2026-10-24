# Assignment: the results of an exam

The assignment at the end of the lecture *Introduction to Python* (`presentations/02-01-python-intro.md`),
and its solution: `exam_results.py`.

## The task

Write a program that collects the results of an exam:

1. It asks for the name and the points of every student. An empty name (just Enter) ends the input.
2. The points are a whole number from 0 to 100. For anything else the program says
   `Points are a whole number from 0 to 100.` and asks again - a function `read_points`, with `try` - `except`
   inside a loop.
3. A function `grade(points)` returns the grade: 51 points for a 6, 61 for a 7, 71 for an 8, 81 for a 9,
   91 for a 10, less than 51 is a 5.
4. At the end it writes a table - the name, the points and the grade of every student - then how many students
   passed (a grade of 6 or more), the average of the points with one decimal, and the best student.
   Without any student it writes `No results.`

## Running the solution

```text
python exam_results.py
```

An example run (the user types the names, the points, and at the end an empty name):

```text
Name: Ana
Points: 93
Name: Marko
Points: abc
Points are a whole number from 0 to 100.
Points: 47
Name: Ivana
Points: 78
Name:

Ana                93    10
Marko              47     5
Ivana              78     8
Passed: 2 of 3
Average: 72.7 points
Best: Ana (93 points)
```

The solution uses only what the lecture shows: `input()`, `int()`, `if`, `while` with `break`, `for`,
a list of dictionaries, functions, f-strings with a width (`:15`, `:5`) and `try` - `except`.
