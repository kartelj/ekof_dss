"""
Reading what the user types. input() always gives a text, so a number has to be converted.

    python 03_input.py
"""

name = input("Your name: ")
quantity = int(input("How many notebooks? "))     # the text "3" becomes the whole number 3
price = float(input("Price of one notebook: "))   # the text "1250" becomes the number 1250.0

total = quantity * price
print(f"{name}, you pay {total:.2f} RSD.")
