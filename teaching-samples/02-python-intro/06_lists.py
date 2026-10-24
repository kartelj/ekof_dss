"""
Lists: several values under one name, in a fixed order.

    python 06_lists.py
"""

prices = [1250, 899, 2400, 650]

print(prices[0])        # the first element - the positions (indexes) start at 0
print(prices[-1])       # the last element
print(len(prices))      # the number of elements

prices.append(1100)     # a new element at the end of the list
print(prices)

total = 0
for price in prices:    # one element after another
    total = total + price
print("Total:", total)
print("Average:", total / len(prices))

# Python has functions for the usual calculations
print(sum(prices), min(prices), max(prices))
print(sorted(prices))   # a new, sorted list; prices stays as it was
print(899 in prices)    # True: the value is in the list
