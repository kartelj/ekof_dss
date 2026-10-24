# Assignment: the home page of Vanity Fair - a solution

The assignment of the lecture [Introduction to Bootstrap](../../presentations/01-04-bootstrap.md): a responsive page
made with Bootstrap 4.5.2 (`vanity-fair.html`) and a small style sheet of our own (`vanity-fair.css`).

The page has, from the top down:

1. a dark navbar - below 768 pixels its links hide behind the button;
2. an alert that the user can close;
3. a jumbotron;
4. six cards of actors - one in a line on a phone, two from 576 pixels, three from 992 pixels
   (`col-sm-6 col-lg-4`);
5. a striped table of films with a dark header and one yellow row;
6. a form with two required fields, checked at once (`was-validated`), sent to `/process-form`;
7. a footer - `vanity-fair.css` centres its text, and a media query moves it to the right from 768 pixels on.

The comments in the HTML follow the same numbers.

## How to open it

Copy the two files into your folder of the samples, `01-html-css-bootstrap/wwwroot/my`,
start the server of the samples (`python main.py` in the folder `01-html-css-bootstrap`) and open
`http://localhost:8000/my/vanity-fair.html`. Look at it 380, 800 and 1200 pixels wide - the device toolbar of
the developer tools sets the width exactly.

Or look at it on the web site of the course:
[kartelj.github.io/ekof_dss/exercises/01-04-bootstrap/vanity-fair.html](https://kartelj.github.io/ekof_dss/exercises/01-04-bootstrap/vanity-fair.html)
(there the form cannot be sent: only the server of the samples has the address `/process-form`).
