# 04 - The actors application, step by step

One web application - *Vanity Fair*, a list of actors - built in small steps.
Every folder is a complete application: it contains everything from the previous step, plus one new idea.

```text
cd 06-actors-click
python main.py
```

Then open <http://localhost:8000>. Only one step can run at a time (they all use the same port).

| Step | What is new |
|---|---|
| `01-actors-new` | a new application: a home page, a counter, data from a file, a menu |
| `02-actors-display` | displaying data; the first component (a Jinja2 macro in `templates/components`) |
| `03-actors-model` | the model: the class `Actor` (`models/actor.py`) |
| `04-actors-edit` | a form that changes the actor |
| `05-actors-list` | a list of actors, read from `sample-data/actors.json` |
| `06-actors-click` | selecting an actor from the list (`/?selected=3`) |
| `07-actors-decomposition` | the component is split into two: `Actors` and `ActorDetail` |
| `08-actors-service-data` | a service that obtains the data, and dependency injection (`services/`, `dependencies.py`) |
| `09-actors-service-msg` | a second service, for messages; the component `AppMessages`; listeners |
| `10-actors-navigation` | several pages with their own addresses: `/dashboard`, `/actors`, `/actordetail/3` |
| `11-actors-service-add` | adding an actor |
| `12-actors-service-delete` | deleting an actor |
| `13-actors-service-search` | searching |
| `14-actors-htmx-search` | an extra step: searching while typing, with the library htmx |

To see what a step has changed, compare its folder with the previous one, for example with
`diff -r 10-actors-navigation 11-actors-service-add` (or with the folder comparison of your editor).

The actors are kept in the memory of the program: changes are lost when the application is restarted.
In module 07 the same application gets its data from a RESTful service with a database.
