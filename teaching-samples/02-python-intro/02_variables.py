"""
Variables, numbers and texts.

    python 02_variables.py
"""

price = 1250            # a whole number (int)
vat_rate = 0.2          # a number with a decimal point (float)
product = "notebook"    # a text (str)
in_stock = True         # a logical value (bool): True or False

vat = price * vat_rate  # the right side is calculated first, then the name gets the result
total = price + vat

print(product, "costs", total, "RSD")
print(type(price), type(vat_rate), type(product), type(in_stock))

# an f-string puts the values of the expressions in braces into the text;
# :.2f shows a number with two decimals
print(f"{product}: {price} + {vat} VAT = {total:.2f} RSD")

# the arithmetic operators
print(17 + 5, 17 - 5, 17 * 5)
print(17 / 5)           # division: the result is always a float
print(17 // 5)          # integer division: the whole part
print(17 % 5)           # the remainder of the integer division
print(2 ** 10)          # power
print((17 - 5) * 2)     # parentheses change the order
