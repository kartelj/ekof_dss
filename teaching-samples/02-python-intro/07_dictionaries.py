"""
Dictionaries: pairs key - value. A value is found by its key, not by its position.

    python 07_dictionaries.py
"""

price_list = {"notebook": 1250, "pen": 120, "backpack": 4500}

print(price_list["pen"])                # the value of the key "pen"
price_list["calculator"] = 2300         # a new pair
price_list["pen"] = 150                 # a new value for an existing key
print(len(price_list), "products")

product = input("Which product? ")
if product in price_list:               # is there such a key?
    print(f"{product}: {price_list[product]} RSD")
else:
    print(f"There is no {product} in the price list.")

for name, price in price_list.items():  # all the pairs, one after another
    print(f"{name:12} {price:6} RSD")
