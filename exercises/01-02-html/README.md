# Assignment of the lecture *Introduction to HTML* - a solution

The task: a small site of a film festival, three pages in a folder of their own -

- `index.html` - the name of the festival, a paragraph with bold and italic words, a picture,
  a list of films, and links to the other two pages;
- `program.html` - a table of the screenings with a caption, a row of headings, a cell that spans
  two columns and one that spans two rows, and a link *Back to the top*;
- `register.html` - a registration form, sent with `post` to `/process-form`, with text fields,
  radio buttons, check boxes, a drop-down list, a text area and a button.

This is one possible solution; yours may look different and still be correct.

## How to open it

The form needs the server of the samples, so copy this folder into the folder `wwwroot`
of the samples, under the name `festival`:

```text
01-html-css-bootstrap/wwwroot/festival/
```

Start the server (`python main.py` in the folder `01-html-css-bootstrap`) and open
`http://localhost:8000/festival/index.html`.

## What to check

- The links lead from every page to the others, and *Back to the top* jumps to the heading.
- In the table, *Opening, and then Raising Arizona* is as wide as two cells, and
  *Talk with the audience* is as high as two rows.
- After *Register*, the page of `/process-form` shows the method `POST`, nothing in the address,
  and all the fields in the body: `name`, `email`, `day`, the ticked films, `city` and `comment`.
  A check box that is not ticked is not sent; an empty text field is sent with an empty value.

The picture `lake.jpg` is `lake2.jpg` from the samples (`01-html/03-images`).
