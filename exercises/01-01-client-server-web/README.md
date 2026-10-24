# Assignment of the lecture *Introduction to web applications and the HTTP protocol* - answers

The task: watch the conversation between the browser and the server of the samples - in the tab *Network*
of the developer tools (F12), and in the terminal of the server. Start the server first (the slides
*The course on your computer* show how):

```text
python main.py
```

in the folder `01-html-css-bootstrap` - the archive `01-html-css-bootstrap.zip` from the page of the course.

The answers below were written with this server and Chrome. In *Network* the column *Type* shows the type
of each request; *Status* its status code.

## 1. An HTML page

`http://localhost:8000/01-html/01-basic-elements/04-headers.html`

| Method | Address | Status | Type |
|---|---|---|---|
| `GET` | `/01-html/01-basic-elements/04-headers.html` | `200` | document |

In the terminal of the server:

```text
INFO:     127.0.0.1:57186 - "GET /01-html/01-basic-elements/04-headers.html HTTP/1.1" 200 OK
INFO:     127.0.0.1:57186 - "GET /favicon.ico HTTP/1.1" 204 No Content
```

The second line is the little icon of the site, which the browser asks for by itself. The samples have
none, and the server answers `204 No Content`. (*Network* usually does not show it.)

## 2. A page with pictures

`http://localhost:8000/01-html/03-images/03-img-out-of-current-dir/index.html`

| Method | Address | Status | Type |
|---|---|---|---|
| `GET` | `/01-html/03-images/03-img-out-of-current-dir/index.html` | `200` | document |
| `GET` | `/01-html/03-images/03-img-out-of-current-dir/images/lake.jpg` | `200` | jpeg |
| `GET` | `/01-html/03-images/03-img-out-of-current-dir/images/mountain.jpg` | `200` | jpeg |
| `GET` | `/01-html/03-images/03-img-out-of-current-dir/images/caste.jpg` | `200` | jpeg |
| `GET` | `/01-html/03-images/lake2.jpg` | `200` | jpeg |

Five requests, four of them pictures: the browser first gets the page, reads it, and then asks for every
picture that the page mentions - each in a request of its own.

If you reload the page, the pictures may come from the *cache* of the browser (the column *Size* says
*memory cache*), and the server sees only the page. Tick *Disable cache* in the tab *Network* to see all
five requests again.

## 3. A wrong address

`http://localhost:8000/01-html/01-basic-elements/04-heders.html`

| Method | Address | Status | Type |
|---|---|---|---|
| `GET` | `/01-html/01-basic-elements/04-heders.html` | `404` | document |

The page shows the answer of the server: `{"detail":"There is nothing at this address."}`.
`404 Not Found` - the conversation worked, but there is no resource at this address.

## 4. A form

`http://localhost:8000/01-html/06-forms/01-form-text-submit.html`, with the name *Ana Jovanovic*:

| Method | Address | Status | Type |
|---|---|---|---|
| `GET` | `/process-form?first_name=Ana&last_name=Jovanovic` | `200` | document |

The values are in the **address**, after the `?`: `first_name=Ana` and `last_name=Jovanovic`, each pair
*name=value*, joined by `&`. The form sends them with `GET`, so they travel in the address; the page that
comes back shows them too.

## 5. The server is stopped

After `Ctrl+C` in the terminal of the server, a reload of the page gives *This site can't be reached* -
*localhost refused to connect* (`ERR_CONNECTION_REFUSED`). In *Network* the request is marked as *(failed)*.

No program listens at port 8000 any more, so there is nobody to answer - not even with a `404`.
A client needs a server to talk to. Start it again with `python main.py`, and the page is back.

## Bonus: the same with curl

In a second terminal (*Terminal - New Terminal*), `curl -v` shows the whole conversation of step 1,
the headers included:

```text
curl -v http://localhost:8000/01-html/01-basic-elements/04-headers.html
```

The lines that begin with `>` were sent by curl, the lines with `<` are the answer of the server:
`HTTP/1.1 200 OK`, `content-type: text/html; charset=utf-8`, and `content-length` - exactly the size
of the file on the disk, because a static file is sent as it is.
