# Introduction to REST APIs

Developing Software Solutions

---

## What is an API?

- **API** stands for *Application Programming Interface*: the operations that a program offers to **other programs**, and the rules for using them.
- A **web API** offers its operations over HTTP: a program sends a request to an address and gets data in the response.

| | A web page | A web API |
|---|---|---|
| The response is read by | a person | a program |
| The body contains | HTML: the data, arranged for reading | only the data, usually as JSON |
| Example | `http://localhost:8000/actors-show` | `http://localhost:8001/api/actors` |

Sample: `03-python-fastapi/pages/actors_show.py` - a page for people.

Note:
An API does not have to be on the web. The functions of the file helpers/mathematics.py (module 03) are its API: to call mathematics.power(2, 10) we only have to know what goes in and what comes out, not how the result is calculated.

The address of the API in the table belongs to the service that we build in the next lecture.

---

## One service, many clients

![Three kinds of clients talk JSON over HTTP to one REST service, which talks to a database](images/rest-clients-service.svg)

- A program that offers a web API is a **web service** - in this lecture simply *the service*. The programs that call it are its **clients**.
- The clients need the data in a strict format, not a page designed for reading.
- All clients use the same API. Only the service talks to the database.

Note:
Do not confuse a web service with the service objects of the actors application (ActorService). Those are objects inside one program; a web service is a separate program. A REST service is a web service built in the REST style, which the next slides explain.

Browser application: JavaScript code in a page asks for data and shows it without loading a new page.

Mobile application: the same data, shown on a phone.

Another server: a program on a server can be a client too. At the end of the course (module 07) our own web application gets its data from such a service.

None of the clients has to know which database is used, or how its tables look.

---

## JSON: the format of the data

```json
{
  "actor_id": 3,
  "last_name": "De Niro",
  "first_name": "Robert",
  "country_id": 1,
  "date_of_birth": "1943-08-17"
}
```

- **JSON** (*JavaScript Object Notation*) is plain text that describes data. Practically every programming language can read and write it.
- An **object** is written in braces: pairs `"name": value`, separated by commas. The order of the pairs has no meaning.
- A value is a **string** in double quotes, a **number**, `true`, `false`, `null` (no value), another object, or an **array**: `[1, 2, 3]`.
- There is no type for dates. A date travels as a string: `"1943-08-17"`.

---

## JSON: an array of objects

![A JSON text: an array in square brackets holds three objects in braces, one for every actor. Each object consists of pairs of a name and a value - here a number and a string - separated by commas.](images/json-anatomy.svg)

- `GET /api/actors` answers with such an array: one object for every actor.
- The colours only help reading: JSON itself is plain text.

---

## JSON and Python

| JSON | Python |
|---|---|
| object `{"code": "US"}` | dictionary `{"code": "US"}` |
| array `[1, 2, 3]` | list `[1, 2, 3]` |
| string `"US"` | string `"US"` or `'US'` |
| number `3` or `8.5` | `int` or `float` |
| `true`, `false`, `null` | `True`, `False`, `None` |

- JSON looks like Python, but it is only **text**. `json.loads(text)` turns the text into dictionaries and lists; `json.dumps(value)` does the opposite.
- JSON is stricter: only double quotes, no comma after the last item, no comments.

Sample: `03-python-fastapi/pages/fetch_data.py` reads the file `sample-data/weather.json`.

---

<!-- .slide: class="exercise" -->
## Exercise 1: repair the JSON

This text should describe a film, but it is not valid JSON:

```text
{'title': "Fargo", "year": 1996, "actors": ["Frances McDormand", "William H. Macy",], "sequel": None}
```

1. Find the three mistakes.
2. Write the corrected text into a Python program, as a string, and read it with `json.loads`.
3. Print `type(film["actors"])`, `len(film["actors"])`, `film["year"] + 10` and `film["sequel"]`.

The program prints `<class 'list'> 2 2006 None`. *About 10 minutes.*

<details><summary>Solution</summary>

```python
import json

text = '{"title": "Fargo", "year": 1996, "actors": ["Frances McDormand", "William H. Macy"], "sequel": null}'
film = json.loads(text)
print(type(film["actors"]), len(film["actors"]), film["year"] + 10, film["sequel"])
```

- The mistakes: single quotes around `title`, a comma after the last item of the array, `None` instead of `null`.
- The Python string is written in single quotes, so the double quotes of the JSON can stay inside it.

</details>

Note:
With the wrong text, json.loads raises JSONDecodeError and names the place of the first mistake, e.g. Expecting property name enclosed in double quotes: line 1 column 2 (char 1). The students can repair the mistakes one after another, guided by the messages.

---

## What is REST?

- **REST** stands for *Representational State Transfer*.
- It is an **architectural style**: a set of rules (*constraints*) for building systems like the web. It is not a protocol, not a standard and not a library.
- The aim: systems that stay simple, serve many users, and have parts that can be changed independently.
- Roy Fielding described it in 2000, in his doctoral dissertation. He is also one of the authors of the HTTP specification.
- The style does not depend on HTTP, but in practice REST APIs use HTTP: it already has addresses, methods, status codes and headers.
- An API that follows the constraints is called **RESTful**.

Note:
The dissertation: Roy T. Fielding, "Architectural Styles and the Design of Network-based Software Architectures", University of California, Irvine, 2000. REST is described in chapter 5.

---

## Six constraints: 1 and 2

### 1. Client-server

- The service keeps and processes the data. The client decides what to do with it.
- They know each other only through the interface: addresses, methods, JSON.
- In practice: each side can be changed or replaced without changing the other.

### 2. Statelessness

- The service keeps the data, but it does not remember the conversation: who asked, and what was asked before.
- Every request carries everything that is needed to answer it. It cannot say "the actor that I read a moment ago" - it says `DELETE /api/actors/14`.
- In practice: any copy of the service can answer any request, so a busy service can run on many computers.

Note:
Statelessness is already known from the first lecture: HTTP itself is stateless. REST asks the application to keep it that way.

What the user is doing at the moment (which actor is being edited, what is typed into a form) is remembered by the client.

What a client does with the data is its own business: a browser application shows it to a person, another server may use it in a calculation.

---

## Six constraints: 3 and 4

### 3. Cacheability

- A response says whether it may be kept and used again (*cached*), and for how long. In HTTP this is written in a header: `Cache-Control: max-age=3600` allows 3600 seconds, one hour.
- In practice: the list of countries changes rarely, so a client does not have to ask for it every time. Fewer requests mean a faster application.

### 4. Layered system

- Between the client and the service there can be other programs: one that encrypts the traffic (HTTPS), one that divides the requests among several copies of the service.
- In practice: the client talks to one address and does not see what is behind it. Such layers are added and removed without changing the clients.

Note:
The service of this course does not send the header Cache-Control.

---

## Statelessness and layers at work

![Two clients send their requests through two layers, HTTPS and a load balancer, to three copies of the same service. The request of client A is answered by copy 1, the request of client B by copy 3, and all three copies use one database.](images/rest-copies-layers.svg)

- Every request carries everything that is needed to answer it, so **any copy** of the service can answer it (constraint 2).
- The clients see only one address. The layers behind it are added and removed without changing the clients (constraint 4).

Note:
A load balancer is a program that sends every request to one of the copies, e.g. to the one that is least busy at the moment.

The copies do not have to know each other. What they share is kept in the database.

---

## Six constraints: 5 and 6

### 5. Code on demand (optional)

- The server may send program code that the client runs. A web page with JavaScript does that. An API that sends JSON does not need it.

### 6. Uniform interface

- Every resource - an actor, a country, the list of all actors - has its own **address**.
- A resource is read and changed through its **representation**: a JSON text that describes it.
- Every message **describes itself**: method, status code and `Content-Type` show how to read it.
- Responses contain **links** to what the client can do next (rare in practice).

In practice: all RESTful APIs look alike. The next slides show how.

Note:
The numbers of the constraints are ours: Fielding lists the uniform interface fourth.

A representation describes the current or the wanted state of a resource. The client and the service transfer representations.

The fourth point of the uniform interface is known as HATEOAS: hypermedia as the engine of application state. We come back to it on the slide "Reality check".

---

<!-- .slide: class="exercise" -->
## Exercise 2: which constraint is broken?

Each of these services breaks one of the six constraints. Which one?

1. A mobile application opens the database file of the service, and reads the table `actor` by itself.
2. `GET /api/actors/next` answers with the actor after the one that this client read last: the service keeps a note for every client.
3. The answers say nothing about how long they may be kept, so a client asks for the list of countries again before every page.
4. The service runs on three computers, and every client has to choose one of them by itself.
5. Every answer is `200 OK`. Whether the request succeeded is written only in the body: `{"ok": false}`.

*About 5 minutes.*

<details><summary>Solution</summary>

| | Broken constraint | Why |
|---|---|---|
| 1 | client-server | a client knows the service only through its interface - not its database |
| 2 | statelessness | the service remembers the conversation; the request should say which actor: `/api/actors/5` |
| 3 | cacheability | an answer should say whether, and how long, it may be kept |
| 4 | layered system | the clients should see one address; what is behind it is not their business |
| 5 | uniform interface | a message should describe itself: the status code tells how the request ended |

</details>

---

## Resources and their addresses

- A **resource** is anything that the API works with: an actor, a country, the list of all actors.
- Every resource has an address. The addresses are **nouns**, usually in the plural.

| Address | Resource |
|---|---|
| `/api/actors` | the **collection**: all actors |
| `/api/actors/3` | one **item**: the actor with id 3 |
| `/api/countries` | all countries |
| `/api/countries/1` | the country with id 1 |

- The HTTP method, not the address, says what to do with a resource. There is no `/api/getActors` and no `/api/deleteActor?id=3`.

Note:
The prefix /api is a common convention. It shows that the address belongs to an API and not to a page.

---

## Methods are the operations

Almost everything that is done with data is one of four operations: **c**reate, **r**ead, **u**pdate, **d**elete - in short, **CRUD**.

| Operation | HTTP method | Address | In SQL |
|---|---|---|---|
| Create | `POST` | `/api/actors` | `INSERT` |
| Read | `GET` | `/api/actors` or `/api/actors/3` | `SELECT` |
| Update | `PUT` | `/api/actors/3` | `UPDATE` |
| Delete | `DELETE` | `/api/actors/3` | `DELETE` |

- The address says **which** resource. The method says **what to do** with it.
- `POST` goes to the collection: the new actor has no id yet - the service chooses it.
- `PUT` replaces the whole item: the client sends all the values, not only the changed ones.

Note:
HTTP also has the method PATCH, which changes only a part of a resource. The service of this course does not use it.

---

## The address says which, the method says what

![The client sends GET /api/actors to the collection and gets all the actors. GET, PUT and DELETE /api/actors/3 go to one item of the collection. POST /api/actors goes to the collection and creates a new item, /api/actors/14, whose id is chosen by the service.](images/rest-methods-resources.svg)

- `GET`, `PUT` and `DELETE` go to the address of the item that they read, replace or delete.
- `POST` goes to the collection. The service chooses the address of the new item.

Note:
The answer to the POST tells the address of the new item in the header Location: /api/actors/14.

The colours of the methods are the colours of the page /docs, which is shown at the end of the lecture.

---

## Safe and idempotent methods

- A **safe** method only reads: it does not change the data.
- An **idempotent** method may be repeated: several identical requests have the same effect on the data as one request.

| Method | Safe | Idempotent | If the same request is sent twice |
|---|---|---|---|
| `GET` | yes | yes | the data is read twice; nothing changes |
| `PUT` | no | yes | the actor gets the same values again |
| `DELETE` | no | yes | the actor stays deleted (the second response is `404`) |
| `POST` | no | no | **two** new actors are created |

- In practice: if the response does not arrive, a client may simply repeat a `GET`, a `PUT` or a `DELETE` - but not a `POST`.

---

## The same request, twice

Before the requests, actor 14 is *Streep Meril*. Before the `POST`, there is no actor 14 yet.

![Every request is sent twice. After GET, PUT and DELETE the data is the same after the second request as after the first; only the answer to the second DELETE is 404 instead of 204. After two POST requests there are two new actors, 14 and 15.](images/rest-same-request-twice.svg)

- The second `DELETE` gets another **answer**, but the **data** does not change. Idempotence is about the data.

---

<!-- .slide: class="exercise" -->
## Exercise 3: an API for films

The database VanityFair02 has the tables `movie` and `genre`. Write the method and the address of each request:

1. all the films;
2. the film with id 4;
3. a new film;
4. the film 4 gets another year;
5. the film 4 is deleted;
6. all the genres.

What is in the body of request 4? Which requests may a client simply send again if the answer does not arrive? *About 10 minutes.*

<details><summary>Solution</summary>

| | Request | | Request |
|---|---|---|---|
| 1 | `GET /api/movies` | 4 | `PUT /api/movies/4` |
| 2 | `GET /api/movies/4` | 5 | `DELETE /api/movies/4` |
| 3 | `POST /api/movies` | 6 | `GET /api/genres` |

- The body of request 4 holds the **whole** film - all its values, with the new year - because `PUT` replaces the item.
- All except the `POST`: `GET`, `PUT` and `DELETE` are idempotent. A second `POST` would create a second film.

</details>

---

## Status codes of an API

| Code | What it tells the client |
|---|---|
| `200 OK` | Success. The body contains the data that was asked for. |
| `201 Created` | Success. A new resource was created; the header `Location` holds its address. |
| `204 No Content` | Success. There is nothing to send back - the body is empty. |
| `400 Bad Request` | The request is wrong, e.g. the id in the address and the id in the body differ. |
| `404 Not Found` | There is no resource at this address. |
| `422 Unprocessable Content` | The data in the request is not valid, e.g. `"USA"` where a number is expected. |
| `500 Internal Server Error` | The service itself failed. The client did nothing wrong and cannot repair it. |

After `4xx` the client has to change the request. After `5xx` it can only try again later.

Note:
400 or 422? The border is not sharp. Our service sends 422 automatically when the body cannot be read as an actor (a value is missing or has a wrong type). It sends 400 from its own check, when a correct actor does not fit the address.

Our service also sends 409 Conflict when the database refuses a change, for example an actor with a country that does not exist.

422 is also known under its older name, Unprocessable Entity. With Python versions before 3.13 the server writes the older name in the status line.

---

## Example: read all actors

```http
GET /api/actors HTTP/1.1
Host: localhost:8001
```

```http
HTTP/1.1 200 OK
Content-Type: application/json

[
  {"actor_id": 1, "last_name": "Živojinović", "first_name": "Bata",
   "country_id": 2, "date_of_birth": "1933-06-05"},
  {"actor_id": 2, "last_name": "Roberts", "first_name": "Julia",
   "country_id": 1, "date_of_birth": "1967-10-28"},
  ...
]
```

- A request to the collection returns a JSON **array**: one object per actor.
- The slides show only the important headers. Long bodies are shortened and split into lines.
- The names of headers are not case-sensitive: our service writes `content-type`.

Note:
The service runs at http://localhost:8001. A real client also sends headers such as User-Agent and Accept, and Content-Length when the request has a body. The real response also has the headers date, server and content-length.

The service sends every body as one line, without spaces.

---

## Example: read one actor

```http
GET /api/actors/3 HTTP/1.1
Host: localhost:8001
```

```http
HTTP/1.1 200 OK
Content-Type: application/json

{"actor_id": 3, "last_name": "De Niro", "first_name": "Robert",
 "country_id": 1, "date_of_birth": "1943-08-17"}
```

- A request to one item returns one JSON **object**.
- `Content-Type: application/json` tells the client how to read the body.
- The country is given only by its id. Its name is in another resource: `/api/countries/1`.

---

## Example: the actor does not exist

<div class="columns"><div>

```http
GET /api/actors/99 HTTP/1.1
Host: localhost:8001
```

```http
HTTP/1.1 404 Not Found
Content-Type: application/json

{"detail": "Actor not found"}
```

</div><div>

![The answer to GET /api/actors/99 on the page /docs of the service: the code 404, the body with the detail "Actor not found", and the headers](images/swagger-404.png)

The same answer on the page `/docs`.

</div></div>

- There is no actor with id 99. The conversation itself worked - this is a regular response.
- The **status code** is for the program: it has to check the code before it uses the body.
- The **body** is for the programmer: it describes the problem in words.

---

## Example: create an actor

```http
POST /api/actors HTTP/1.1
Host: localhost:8001
Content-Type: application/json

{"last_name": "Streep", "first_name": "Meril",
 "country_id": 1, "date_of_birth": "1949-06-22"}
```

```http
HTTP/1.1 201 Created
Content-Type: application/json
Location: /api/actors/14

{"actor_id": 14, "last_name": "Streep", "first_name": "Meril",
 "country_id": 1, "date_of_birth": "1949-06-22"}
```

- The client sends the new actor **without** `actor_id`: the service chooses it.
- `Location` holds the address of the new resource. The body is the actor as it was saved.

Note:
The first name is misspelled on purpose (Meril instead of Meryl). The mistake is corrected with PUT two slides later.

---

## Example: invalid data

```http
POST /api/actors HTTP/1.1
Host: localhost:8001
Content-Type: application/json

{"last_name": "Streep", "first_name": "Meril",
 "country_id": "USA", "date_of_birth": "1949-06-22"}
```

```http
HTTP/1.1 422 Unprocessable Content
Content-Type: application/json

{"detail": [{
    "type": "int_parsing",
    "loc": ["body", "country_id"],
    "msg": "Input should be a valid integer, unable to parse string as an integer",
    "input": "USA"
}]}
```

- The same request, but `country_id` is `"USA"` - a text, not a number. Nothing was saved.
- The body says where the problem is (`loc`) and what it is (`msg`).

---

## Example: update an actor

```http
PUT /api/actors/14 HTTP/1.1
Host: localhost:8001
Content-Type: application/json

{"actor_id": 14, "last_name": "Streep", "first_name": "Meryl",
 "country_id": 1, "date_of_birth": "1949-06-22"}
```

```http
HTTP/1.1 204 No Content
```

- The first name was misspelled. The client sends the **whole** actor again, with the corrected value.
- `204 No Content`: success. There is no body - the client already has the data.
- Other responses: `400 Bad Request` if the id in the address differs from `actor_id` in the body, `404 Not Found` if there is no actor 14.

---

## Example: delete an actor

```http
DELETE /api/actors/14 HTTP/1.1
Host: localhost:8001
```

```http
HTTP/1.1 204 No Content
```

- The actor is removed. Again there is nothing to send back.
- If the client sends the same request once more, the response is different:

```http
HTTP/1.1 404 Not Found
Content-Type: application/json

{"detail": "Actor not found"}
```

- After one request and after two, the data is the same: there is no actor 14. That is why `DELETE` is idempotent.

---

## The examples, one after another

![The client sends five requests to the service, and the table actor is shown after each answer. POST creates row 14 (201 Created); a POST with the country "USA" is refused with 422 and nothing is saved; PUT changes the first name to Meryl (204); DELETE removes row 14 (204); the same DELETE once more gets 404 Not Found, and the table does not change.](images/rest-actor14-story.svg)

Note:
One request, one answer: the client waits for the answer before it sends the next request.

---

<!-- .slide: class="exercise" -->
## Exercise 4: predict the answers

The service has 13 actors, with the ids 1 to 13; actor 9 is Tom Hanks. Write down the status code of every answer - and `Location`, where there is one:

```text
1. GET    /api/actors/9
2. GET    /api/actors/90
3. POST   /api/actors     {"last_name": "Cage", "first_name": "Nicolas", "country_id": 1,
                           "date_of_birth": "1964-01-07"}
4. PUT    /api/actors/14  {"actor_id": 15, "last_name": "Cage", "first_name": "Nicolas", "country_id": 1}
5. POST   /api/actors     the body of request 3, but with "date_of_birth": "7 January 1964"
6. DELETE /api/actors/14  - and then the same request once more
```

*About 10 minutes.* Exercise 5 checks the predictions on the real service.

<details><summary>Solution</summary>

| | Answer | Why |
|---|---|---|
| 1 | `200 OK` | the actor exists; the body is Tom Hanks |
| 2 | `404 Not Found` | there is no actor 90 |
| 3 | `201 Created`, `Location: /api/actors/14` | the service chooses the next id: 14 |
| 4 | `400 Bad Request` | the address says 14, the body says 15 |
| 5 | `422 Unprocessable Content` | the date is not written as year-month-day; nothing is saved |
| 6 | `204 No Content`, then `404 Not Found` | after both requests the data is the same: no actor 14 |

</details>

---

## Reality check

REST describes an ideal. Real APIs often differ from it in three ways.

1. **`GET` that changes data** - for example `GET /api/deleteActor?id=3`. It works, but programs expect `GET` to be safe: browsers and search engines follow links on their own.
2. **Documentation** - ideally, the responses tell the client what it can do next. In reality a programmer reads the documentation. In the best case it is generated from the code, like our page `/docs`.
3. **Authentication and state** - most real APIs must know who is calling. A stateless API expects proof of identity (a key or a token) in **every** request. Some APIs remember the client on the server instead.

Note:
The service of this course does not ask who is calling. That is acceptable only because it runs on our own computer.

---

## How to try an API

Start the service first (see below). Then use one of three tools.

1. **The browser** - type `http://localhost:8001/api/actors` into the address bar. The browser shows the JSON. Only `GET` can be tried this way.
2. **`curl`** - a program for the terminal that can send every kind of request.
3. **The documentation page** - `http://localhost:8001/docs` lists all the operations. Open one, click *Try it out*, fill in the values and click *Execute*: the page sends the request and shows the response.

Sample: `06-python-rest-sqlite/02-rest-service-actors-db` - start it with `python main.py`.

Note:
The service keeps its terminal busy. Type the curl commands in a second terminal.

The page /docs loads its scripts from the internet, so it needs a connection.

---

## The browser and the page `/docs`

<div class="columns"><div>

![The browser shows the answer to http://localhost:8001/api/actors: the JSON array of all the actors, as one long line of text](images/rest-browser-json.png)

**The browser**: the body, as it is.

</div><div>

![The page http://localhost:8001/docs: the title ActorsRestService and the operations of the resource actors - GET, POST, GET, PUT and DELETE - each with its address](images/swagger-actors-operations.png)

**The page `/docs`**: all the operations.

</div></div>

Note:
Newer versions of Chrome show a check box Pretty print above the JSON: it shows the same data in many indented lines.

The picture shows only a part of the page /docs: the operations of the resource actors. The title of the service is above them, the operations of the resource countries below.

The answer 404 on the slide "Example: the actor does not exist" was made on this page: GET /api/actors/{actor_id}, Try it out, 99, Execute.

---

## Requests with curl

**Read** - without options `curl` sends a `GET` and prints the body of the response:

```bash
curl http://localhost:8001/api/countries/1
```

```text
{"country_id":1,"name":"United States of America","code":"US"}
```

**Create** - the file `actor.json` in the current folder holds the JSON text of the new actor:

```bash
curl -i -X POST http://localhost:8001/api/actors \
     -H "Content-Type: application/json" \
     -d "@actor.json"
```

- `-X` sets the method, `-H` adds a header, `-d` sends the body. `-i` also shows the status line and the headers.
- On Windows, write the command in one line, without the `\` characters. In PowerShell, type `curl.exe`, not `curl`.

Note:
The header Content-Type is necessary: without it curl says that the body is the data of a form, and the service answers 422.

With -d, curl sends a POST by itself. -X POST is written only to make the method visible; with the option -v curl remarks that it is unnecessary. The option -v shows the request as well.

In Windows PowerShell the word curl alone starts another command (Invoke-WebRequest), so we type curl.exe. The backslash at the end of a line continues the command only in the terminals of macOS and Linux.

---

<!-- .slide: class="exercise" -->
## Exercise 5: check your predictions

1. Start the service `06-python-rest-sqlite/02-rest-service-actors-db`. If you have added actors already, stop it, delete the file `actors.db` in its folder, and start it again: it starts with 13 actors.
2. Write the bodies of the requests 3, 4 and 5 of exercise 4 into the files `cage.json`, `cage14.json` and `cage-wrong.json`.
3. Send the requests of exercise 4 with `curl -i` - or on the page `/docs` - and compare the status codes with your predictions.

*About 15 minutes.*

<details><summary>Solution</summary>

```bash
curl -i http://localhost:8001/api/actors/9
curl -i http://localhost:8001/api/actors/90
curl -i -X POST http://localhost:8001/api/actors -H "Content-Type: application/json" -d "@cage.json"
curl -i -X PUT http://localhost:8001/api/actors/14 -H "Content-Type: application/json" -d "@cage14.json"
curl -i -X POST http://localhost:8001/api/actors -H "Content-Type: application/json" -d "@cage-wrong.json"
curl -i -X DELETE http://localhost:8001/api/actors/14
curl -i -X DELETE http://localhost:8001/api/actors/14
```

- The body of the `400`: `{"detail":"The id in the address and the actor_id in the body are different"}`.
- The `422` says where the problem is: `"loc":["body","date_of_birth"]`.

</details>

Note:
The curl commands must be typed in the folder of the JSON files, because of "@cage.json".
With Python 3.12 the status line of the 422 says Unprocessable Entity, the older name of the same code.
On Windows: every command in one line, and curl.exe in PowerShell.

---

## Summary

- A **web API** is for programs: requests and responses over HTTP, with the data as **JSON**.
- **REST** is an architectural style with six constraints: client-server, statelessness, cacheability, layered system, code on demand (optional), uniform interface.
- A **resource** has an address (`/api/actors`, `/api/actors/3`). The HTTP **method** says what to do with it: `POST`, `GET`, `PUT`, `DELETE` - create, read, update, delete.
- The **status code** says how the request ended: `200`, `201`, `204` - `400`, `404`, `422` - `500`.
- An API can be tried without writing a program: the browser, `curl`, the page `/docs`.

Next lecture: we write such a service in Python, with FastAPI.

---

<!-- .slide: class="exercise" -->
## Assignment: the API of the films

Design a REST API for the films of the database VanityFair02, and write it down in a text file:

1. The resources and their addresses: the films and the genres.
2. The JSON of one film - *Fargo* - with the fields `movie_id`, `title`, `year`, `lasting` and `genre_id`.
3. For each of the five operations on the films: the request (method, address, body) and the successful answer (status code, `Location`, body), in the form of the example slides of this lecture.
4. For every operation at least one unsuccessful answer (`400`, `404` or `422`), and its reason.
5. A table: which of the requests are safe, and which are idempotent?

*About 40 minutes.* The next lecture builds this API. A solution: [exercises/06-01-restful-api](https://github.com/kartelj/ekof_dss/tree/main/exercises/06-01-restful-api)

Note:
The films of VanityFair02 are in teaching-samples/05-python-db-sqlite/database/VanityFair02/insert-table-data.sql. Fargo has the id 4, it is 98 minutes long, and its genre is 4 (crime).

---

# Thanks for your attention!
