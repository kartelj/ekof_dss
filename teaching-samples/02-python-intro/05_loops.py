"""
Loops: while repeats its block as long as a condition holds; for goes through a sequence of values.

    python 05_loops.py
"""

deposit = 1000.0    # euros
rate = 0.05         # 5 % interest a year

# while: after how many years is the deposit doubled?
balance = deposit
years = 0
while balance < 2 * deposit:
    balance = balance * (1 + rate)
    years = years + 1
print(f"The deposit is doubled after {years} years: {balance:.2f} EUR")

# for: the balance at the end of each of the first five years
balance = deposit
for year in range(1, 6):        # year takes the values 1, 2, 3, 4, 5
    balance = balance * (1 + rate)
    print(f"Year {year}: {balance:.2f} EUR")
