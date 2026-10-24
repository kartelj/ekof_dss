# Assignment: a cinema programme - a solution

The assignment at the end of the lecture [Introduction to SQL](../../presentations/05-02-sql.md):
a cinema keeps the screenings of the films of VanityFair02 in a new table, `screening`.

| File | Parts of the assignment |
|---|---|
| `screening.sql` | 1. the table `screening` with its constraints, 2. the six screenings |
| `refused.sql` | 3. three INSERTs that are refused, each by another constraint |
| `queries.sql` | 4. the programme of a day, 5. tickets and income per film, 6. the films without a screening, 7. the view `vw_programme`, 8. a transaction |

## How to run it

In your folder `05-python-db-sqlite` (the archive of the module), build a fresh VanityFair02 first - this also
removes the table `screening` of an earlier attempt:

```text
cd database
python create_databases.py
```

Then copy the three scripts of this solution into the folder `database/VanityFair02`, open the database there in
the shell `sqlite3`, and execute the scripts in order:

```text
cd VanityFair02
sqlite3 VanityFair02.db
.headers on
.mode column
.read screening.sql
.read refused.sql
.read queries.sql
```

`refused.sql` ends with three error messages - that is the point of it.

## The results

4 - the programme of 6 November:

| time | hall | title |
|---|---|---|
| 18:00 | A | Fargo |
| 20:30 | A | Amélie |
| 20:30 | B | Fargo |

5 - tickets and income:

| title | tickets | income |
|---|---|---|
| Fargo | 132 | 56800 |
| Amélie | 95 | 42750 |
| Who's Singin' Over There? | 120 | 42000 |
| The Big Lebowski | 40 | 16000 |
| Delicatessen | 0 | 0 |

6 - five films without a screening: Miller's Crossing, No Country for Old Men, O Brother, Where Art Thou?,
Raising Arizona, The City of Lost Children.

7 - the comedies in the programme: Who's Singin' Over There? (2026-11-07 18:00, hall A) and Delicatessen
(2026-11-07 21:00, hall B).

8 - after the transaction, Delicatessen is in hall C, for 350.

## Notes

- `UNIQUE (hall, starts_at)` is the rule "one screening in a hall at a time". It only compares equal
  moments: two screenings at 18:00 and 18:30 in the same hall are accepted, although the films overlap.
  To refuse those, the DBMS would need the length of the film - a trigger could check it.
- `starts_at` is a text in the ISO format, so `ORDER BY starts_at` sorts by time, and `LIKE '2026-11-06%'`
  chooses one day. `substr(starts_at, 12, 5)` cuts out the time.
- Part 6 can also be written with `NOT EXISTS`, or with `LEFT JOIN screening ... WHERE screening_id IS NULL`.
- In part 5, Delicatessen has the income 0, not NULL: it has a screening, with 0 tickets sold.
  A film without any screening is not in the result at all - the join is an `INNER JOIN`.
