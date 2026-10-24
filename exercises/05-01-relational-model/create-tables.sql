-- Assignment of the lecture "Introduction to databases and the relational model":
-- the physical model of the library, in the dialect of SQLite.

PRAGMA foreign_keys = ON;

CREATE TABLE member (
    member_id  INTEGER PRIMARY KEY,
    name       TEXT    NOT NULL,
    phone      TEXT    NOT NULL
);

CREATE TABLE book (
    book_id    INTEGER PRIMARY KEY,
    code       TEXT    NOT NULL,      -- the code on the book, e.g. B-101 (a natural key)
    title      TEXT    NOT NULL
);

CREATE TABLE author (
    author_id  INTEGER PRIMARY KEY,
    name       TEXT    NOT NULL
);

-- many-to-many: a book has one or more authors, an author writes many books
CREATE TABLE book_author (
    book_id    INTEGER NOT NULL,
    author_id  INTEGER NOT NULL,
    PRIMARY KEY (book_id, author_id),
    CONSTRAINT fk_book_author_book FOREIGN KEY (book_id) REFERENCES book (book_id),
    CONSTRAINT fk_book_author_author FOREIGN KEY (author_id) REFERENCES author (author_id)
);

CREATE TABLE loan (
    loan_id      INTEGER PRIMARY KEY,
    member_id    INTEGER NOT NULL,
    book_id      INTEGER NOT NULL,
    loaned_on    TEXT    NOT NULL,     -- a date: 'YYYY-MM-DD'
    returned_on  TEXT    NULL,         -- NULL: the book has not been returned yet
    CONSTRAINT fk_loan_member FOREIGN KEY (member_id) REFERENCES member (member_id),
    CONSTRAINT fk_loan_book FOREIGN KEY (book_id) REFERENCES book (book_id)
);
