"""
Decisions: if - elif - else. The grade of an exam from its points.

    python 04_if.py
"""

points = int(input("Points (0-100): "))

# The conditions are checked from the top. Only the block of the first true condition
# is executed. A block is made of the indented lines below the line with the colon.
if points < 0 or points > 100:
    print("The points must be between 0 and 100.")
elif points >= 91:
    print("Grade: 10")
elif points >= 81:
    print("Grade: 9")
elif points >= 71:
    print("Grade: 8")
elif points >= 61:
    print("Grade: 7")
elif points >= 51:
    print("Grade: 6")
else:
    print("Grade: 5 - the exam is not passed.")
