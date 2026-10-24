# Assignment of the lecture *Introduction to web applications and the HTTP protocol* - answers

The task was to watch the conversation between a client and the server of the samples with
`curl -v`, with the tab *Network* of the developer tools, and in the terminal of the server.
Start the server first:

```text
cd teaching-samples/01-html-css-bootstrap
python main.py
```

The answers below were written with this server. Your dates, sizes of headers and the order of some
lines may differ; the methods, status codes and types are the same.

## 1. An HTML page

```text
curl -v http://localhost:8000/01-html/01-basic-elements/04-headers.html
```

```text
> GET /01-html/01-basic-elements/04-headers.html HTTP/1.1
> Host: localhost:8000
> User-Agent: curl/8.7.1
> Accept: */*
>
< HTTP/1.1 200 OK
< date: Sat, 24 Oct 2026 06:36:36 GMT
< server: uvicorn
< content-type: text/html; charset=utf-8
< accept-ranges: bytes
< content-length: 309
< last-modified: Fri, 02 Oct 2026 10:15:02 GMT
< etag: "d9d7602d131818161f5e62153f7fa5a6"
<
<!DOCTYPE html>
...
```

- The request line: `GET /01-html/01-basic-elements/04-headers.html HTTP/1.1`.
- The status line: `HTTP/1.1 200 OK`.
- `content-type: text/html; charset=utf-8` - an HTML page, written in UTF-8.
- `content-length` is exactly the size of the file on the disk (309 bytes here): a static file is
  sent as it is.

## 2. A picture

```text
curl -v http://localhost:8000/01-html/03-images/lake2.jpg -o lake.jpg
```

- `200 OK`, `content-type: image/jpeg`, `content-length: 53834` - again the size of the file.
- Without `-o`, curl would write the bytes of the picture into the terminal. The browser knows from
  `content-type` that it has received a picture, and shows it.

## 3. An address without the slash at the end

```text
curl -v http://localhost:8000/01-html
```

```text
< HTTP/1.1 307 Temporary Redirect
< content-length: 0
< location: /01-html/
```

- The server answers with a `3xx` - *look elsewhere* - and says where: the header `location`.
- curl only shows this answer. The browser reads `location` and at once sends a second request,
  `GET /01-html/`, which gets `200 OK` and the list of the folder. In *Network* both requests are seen.
- `curl -v -L` follows the redirect as the browser does: it reports
  `Issue another request to this URL: 'http://localhost:8000/01-html/'` and gets `200 OK`.
- Why the server does it: the relative links of a page work only if the address of a folder
  ends with `/`.

## 4. A wrong address

```text
curl -v http://localhost:8000/01-html/01-basic-elements/04-heders.html
```

```text
< HTTP/1.1 404 Not Found
< content-length: 46
< content-type: application/json
<
{"detail":"There is nothing at this address."}
```

- `404 Not Found`; the body is not HTML but a short text in the format JSON (`application/json`),
  which the browser shows as it is. We will meet JSON again with RESTful services.

## 5. A form

Open `http://localhost:8000/01-html/06-forms/01-form-text-submit.html`, type a first and a last name,
and click *Submit*. In *Network*:

- method `GET`, status `200`;
- the address: `/process-form?first_name=Ana&last_name=Jovanovi%C4%87` - the values travel in the
  **query** of the address, as pairs `name=value` joined with `&`; letters such as `ć` are encoded.

## 6. Reloading a page

Open `http://localhost:8000/01-html/03-images/03-img-out-of-current-dir/index.html` and reload it
three times. The terminal of the server shows:

- the first time, five requests: the page and its four pictures (and `/favicon.ico`, the little
  icon of the site, which our server answers with `204 No Content`);
- after that, only the page (and `/favicon.ico`): the browser keeps the pictures in its *cache*
  and does not ask for them again. With *Disable cache* ticked in *Network*, all five come every time.

Every reload is a new conversation, and the server answers each request on its own, without
remembering the earlier ones: HTTP is stateless.

## 7. A real site

```text
curl -v https://example.com
```

- `Connected to example.com (...) port 443` - `https` without a port in the address uses 443.
- The lines start with `HTTP/2` (`> GET / HTTP/2`, `< HTTP/2 200`): a newer version of the
  protocol, with the same methods, status codes and headers. The connection is encrypted, so curl
  also reports the steps of the encryption (the lines with `TLS`).
