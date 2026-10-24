"""
Modules: code from other files - from the standard library of Python, and from our own file shop.py.

    python 09_modules.py
"""

import math
import random
from datetime import date

import shop     # the file shop.py in the same folder

print(math.sqrt(2))                     # the name of the module, a dot, the name of the function
print(math.pi)
print(random.randint(1, 6))             # a random whole number from 1 to 6, like a die
print(date.today())                     # the date of today
print(shop.price_with_vat(1000))        # a function from our own module
print(shop.VAT_RATE)
