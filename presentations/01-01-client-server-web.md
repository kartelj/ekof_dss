# Introduction to web applications and the HTTP protocol

Developing Software Solutions

---

## What happens when you open a web page?

1. A **web client** (usually a web browser) sends a *request* to a **web server**.
2. The server receives the request and sends back a *response* - most often an HTML page.
3. The client looks at what it has received:
   - an HTML page is parsed and shown on the screen,
   - a file the browser understands (an image, a video, a PDF) is displayed or played,
   - any other file is offered for download.

One page usually needs many requests: one for the HTML, and one for every image, style sheet and script that the HTML mentions.

---

## Client and server

![A client sends a request to a server and gets a response back](images/client-server.svg)

---

## The protocol: HTTP

- HTTP stands for **HyperText Transfer Protocol**.
- A *protocol* is a set of rules that both sides of a conversation agree to follow.
- HTTP defines:
  - what a request looks like,
  - what a response looks like,
  - what the two sides may expect from each other.
- **HTTPS** is the same protocol, sent through an encrypted connection.

Because both sides follow the same rules, any browser can talk to any web server.

---

## The HTTP client

- The program that **starts** the conversation.
- It builds an HTTP request, sends it to a server, and interprets the response.
- The best known clients are web browsers: Chrome, Firefox, Safari, Edge.
- A browser is not the only kind of client:
  - command-line tools, such as `curl`,
  - mobile applications,
  - our own Python programs (we will write some later in the course).

---

## The HTTP server

- A **program**, not a computer - although the computer that runs it is usually called "the server" as well.
- The server program:
  - *listens* for incoming requests,
  - reads and interprets each request,
  - sends back a response.
- Well known server programs: nginx, Apache HTTP Server, Microsoft IIS.
- In this course the server is a Python program, run by **Uvicorn**.

---

## What do we need to publish a web site?

1. A computer that is always on and connected to the internet.
2. A web server program installed on it.
3. The files of the site (HTML pages, images, style sheets) copied to that computer.
4. An address by which the others can find it - a *domain name*.

A busy site uses many computers in several data centres. A site for a few visitors can run on a single small computer - or, while we are developing it, on our own laptop.

---

## A web server on your own computer

Python comes with a simple web server. In a folder that contains HTML files, type:

```text
python -m http.server 8000
```

and open `http://localhost:8000` in the browser.

- `localhost` is the name by which every computer calls **itself**.
- `8000` is the **port**: one computer can run several server programs, and the port tells which one we want.
- Only you can see this site. That is exactly what we want during development.

---

## Static and dynamic content

**Static content**: the server sends a file exactly as it is stored on the disk.

- HTML pages, images, style sheets
- every visitor gets the same thing

**Dynamic content**: a program on the server *creates* the response at the moment of the request.

- search results, a shopping basket, your bank account
- the response depends on who asks, on what they ask for, and on the data in a database

The first part of the course uses static content. From the second part on, we write the programs that create the pages.

---

## The request - response cycle

- The client always speaks first; the server only answers.
- One request, one response - then the conversation is over.
- HTTP is **stateless**: the server does not remember earlier requests. Every request has to carry everything the server needs in order to answer it.

Note:
Statelessness comes back twice in the course: when we keep the state of a page on the server, and as one of the REST constraints.

---

## The HTTP request

```http
GET /01-html/01-basic-elements/04-headers.html HTTP/1.1
Host: localhost:8000
User-Agent: Mozilla/5.0 (Macintosh) Chrome/154.0
Accept: text/html,application/xhtml+xml
Accept-Language: en,sr;q=0.8
```

- The **request line**: the method (`GET`), the path of the resource, the version of the protocol.
- The **headers**: additional information, one `Name: value` pair per line - who asks, what kinds of answers are welcome, in which language.
- An optional **body**: the data that the client sends, for example the values typed into a form.

---

## HTTP methods

The method tells the server what the client wants to do with the resource.

| Method | Meaning |
|---|---|
| `GET` | give me this resource; nothing changes on the server |
| `POST` | here is some data - create something, or carry out an action |
| `PUT` | replace the resource with the data I am sending |
| `DELETE` | remove the resource |

Typing an address or clicking a link always sends a `GET`. Forms can send `GET` or `POST`.

---

## The HTTP response

```http
HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 309
Last-Modified: Fri, 02 Oct 2026 10:15:02 GMT

<!DOCTYPE html>
<html>
...
```

- The **status line**: the version of the protocol and a status code with a short description.
- The **headers**: the type of the content (`Content-Type`), its length, the date ...
- An empty line, and then the **body**: the requested resource itself.

---

## Status codes

The first digit tells the kind of the answer.

| Code | Kind | Examples |
|---|---|---|
| `2xx` | success | `200 OK`, `201 Created`, `204 No Content` |
| `3xx` | look elsewhere | `301 Moved Permanently`, `303 See Other` |
| `4xx` | the client made a mistake | `400 Bad Request`, `404 Not Found` |
| `5xx` | the server failed | `500 Internal Server Error` |

---

## 404 Not Found

- The server understood the request, but it has nothing at that address.
- The usual cause is a mistake in the address:

```text
http://localhost:8000/01-html/01-basic-elements/04-headers.html    200 OK
http://localhost:8000/01-html/01-basic-elements/04-heders.html     404 Not Found
```

- A 404 is a perfectly valid answer: the conversation between the client and the server worked, only the resource is missing.

---

## Anatomy of a URL

A URL (*Uniform Resource Locator*) is the address of a resource on the web.

![The parts of a URL: scheme, host, port, path, query and fragment](images/url-anatomy.svg)

- If the port is left out, `http` uses port 80 and `https` uses port 443.
- The query is the usual way to send a few values with a `GET` request.

---

## See HTTP with your own eyes

**In the browser** - open the developer tools (F12) and choose the *Network* tab:

- every request made by the page, with its method and status code,
- the headers of the request and of the response.

**In the terminal** - the tool `curl` shows the whole conversation:

```text
curl -v http://localhost:8000/01-html/01-basic-elements/04-headers.html
```

**In the terminal of the server** - every request that arrives is written in one line:

```text
INFO:     127.0.0.1:52144 - "GET /01-html/ HTTP/1.1" 200 OK
```

---

## Try it

The samples for the first part of the course are in the folder `teaching-samples/01-html-css-bootstrap`.

```text
cd teaching-samples/01-html-css-bootstrap
python main.py
```

Then open `http://localhost:8000` and:

1. browse to one of the HTML samples and find its request in the *Network* tab;
2. change one letter in the address and look at the status code;
3. look at the terminal - which requests has the server received?

---

## Summary

- The web is a conversation between **clients** and **servers**.
- They speak **HTTP**: a request (method, path, headers, body) is answered by a response (status code, headers, body).
- HTTP is **stateless** - every request stands on its own.
- A **URL** tells which protocol to use, which server to ask, and which resource to ask for.
- During development the client and the server are on the same computer: `http://localhost:8000`.

---

# Thanks for your attention!
