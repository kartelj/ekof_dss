"""
Errors: a program stops with an error message - unless it catches the error with try - except.

    python 10_errors.py
"""

text = input("A whole number: ")

try:
    number = int(text)                  # fails when the text is not a whole number
    print("Its square is", number * number)
except ValueError:
    print(f"'{text}' is not a whole number.")

print("The program goes on.")

# Without try - except, this line would stop the program with the error ValueError:
# int("abc")
