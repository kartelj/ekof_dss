# Assignment: a small film site

The solution of the assignment of the lecture
[Introduction to FastAPI and Jinja2](../../presentations/03-01-fastapi-jinja2.md).

The task in brief: a new application with

- a **layout** (the name of the site, a menu Home - Films - Add a film, a footer, the style sheet
  `static/css/site.css`) that every page extends;
- the page `/` with the number of films (`| length`);
- the page `/films`: the list of films, every film shown by the **component** `FilmItem` as a link to its page;
- the page `/films/{film_id}`: the details of one film - the number is its position in the list, from 0 -
  and `404 Not Found` for a number that does not exist;
- the page `/films/add`: a **POST** form (title, year, director). The film is added to a global list, and the
  browser is sent to `/films` (**Post/Redirect/Get**).

## Running it

In the folder of the solution, in a terminal with an activated virtual environment of the course - for example
the `.venv` of your folder `03-python-fastapi`:

```text
python main.py
```

Then open <http://localhost:8000>.

## How to check it

- Add the film *Heat*, 1995, Michael Mann: it appears at the end of the list, and its page is `/films/3`.
- Refresh the list (F5) after adding: the film is not added a second time.
- `/films/99` answers `{"detail":"Film not found"}` (404).
- The year `abc` is refused with the status 422.
- Restart the program: the list has the three films of the beginning again.

## Files

```text
main.py                          the application: the films and all the routes
templates/layout.html            the frame of every page
templates/components/film.html   the component FilmItem
templates/index.html             /
templates/films.html             /films
templates/film_detail.html       /films/{film_id}
templates/add_film.html          /films/add
static/css/site.css              the style sheet
```
