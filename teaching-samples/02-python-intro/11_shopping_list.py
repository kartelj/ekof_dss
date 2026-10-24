"""
A complete small program: a shopping list with prices.

It uses everything from the lecture: variables, input, if, loops, a list of dictionaries,
functions and catching an error.

    python 11_shopping_list.py
"""


def read_price(prompt):
    """Asks for a price until the user types a number."""
    while True:
        text = input(prompt)
        try:
            return float(text)          # a number: return ends the function, and the loop with it
        except ValueError:
            print("That is not a number. Decimals are written with a point: 12.5")


def show(items):
    """Writes all the items and the total."""
    if len(items) == 0:
        print("The list is empty.")
        return
    total = 0
    for item in items:
        print(f"{item['name']:15} {item['price']:10.2f}")
        total = total + item["price"]
    print(f"{'Total':15} {total:10.2f}")


items = []      # every item is a dictionary: {"name": ..., "price": ...}

while True:
    # strip() removes the spaces at both ends of the text, lower() makes the letters small
    command = input("\n[a]dd, [s]how, [q]uit: ").strip().lower()
    if command == "a":
        name = input("Name: ")
        price = read_price("Price: ")
        items.append({"name": name, "price": price})
    elif command == "s":
        show(items)
    elif command == "q":
        print("Goodbye.")
        break                           # leaves the loop, and the program ends
    else:
        print("Unknown command.")
