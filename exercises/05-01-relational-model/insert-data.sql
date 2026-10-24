-- The four loans of the spreadsheet, moved into the tables of the model.
-- The rows that other rows refer to come first.

PRAGMA foreign_keys = ON;

INSERT INTO member (member_id, name, phone)
VALUES (1, 'Ana Petrović', '064 111 222'),
       (2, 'Marko Ilić', '065 333 444'),
       (3, 'Jelena Kostić', '063 555 666');

INSERT INTO book (book_id, code, title)
VALUES (1, 'B-101', 'Good Omens'),
       (2, 'B-102', 'Mort'),
       (3, 'B-103', 'Coraline');

INSERT INTO author (author_id, name)
VALUES (1, 'Pratchett'),
       (2, 'Gaiman');

INSERT INTO book_author (book_id, author_id)
VALUES (1, 1),      -- Good Omens: Pratchett
       (1, 2),      -- Good Omens: Gaiman
       (2, 1),      -- Mort: Pratchett
       (3, 2);      -- Coraline: Gaiman

INSERT INTO loan (loan_id, member_id, book_id, loaned_on, returned_on)
VALUES (1, 1, 1, '2026-10-01', '2026-10-15'),
       (2, 2, 2, '2026-10-03', NULL),
       (3, 1, 3, '2026-10-16', NULL),
       (4, 3, 1, '2026-10-20', NULL);
