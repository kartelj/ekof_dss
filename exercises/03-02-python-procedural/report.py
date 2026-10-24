"""
The assignment of the lecture "Python: procedural programming": a report of the sales.

The journal of the sales is a list of texts (as if it had been read from a file). The program skips the
lines that are not valid, and writes how much of every product was sold, the total and the best seller.

    python report.py
"""

import sales

journal = [
    "2026-10-01;notebook;3;1250.00",
    "2026-10-01;pen;10;120.50",
    "2026-10-02;backpack;1;4500.00",
    "2026-10-02;notebook;two;1250.00",
    "2026-10-02;pen;4",
    "2026-10-03;notebook;2;1250.00",
]

valid = []
for number, line in enumerate(journal, start=1):      # start=1: the lines are numbered from 1
    sale = sales.parse(line)
    if sale is None:                                    # "is None": parse found the line not valid
        print(f"Skipped line {number}: {line}")
    else:
        valid.append(sale)

quantities = sales.quantities(valid)
amounts = sales.amounts(valid)

print()
total = 0
for product in sorted(quantities):      # sorted() of a dictionary: its keys, in alphabetical order
    print(f"{product:12} {quantities[product]:5} {amounts[product]:12,.2f}")
    total += amounts[product]
print(f"{'Total:':18} {total:12,.2f}")

best = ""
for product in quantities:
    if best == "" or quantities[product] > quantities[best]:
        best = product
print(f"Most sold: {best} ({quantities[best]} pieces)")
