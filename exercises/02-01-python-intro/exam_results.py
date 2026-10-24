"""
The assignment of the lecture "Introduction to Python": the results of an exam.

The program asks for the name and the points of every student (an empty name ends the input),
and then writes a table with the grades, how many students passed, the average and the best student.

    python exam_results.py
"""


def read_points(prompt):
    """Asks for the points until the user types a whole number from 0 to 100."""
    while True:
        try:
            points = int(input(prompt))
        except ValueError:
            points = -1                 # not a whole number: a value that is surely wrong
        if points >= 0 and points <= 100:
            return points               # a good value: return ends the function, and the loop with it
        print("Points are a whole number from 0 to 100.")


def grade(points):
    """Returns the grade (5 to 10) for the points of an exam (0 to 100)."""
    if points >= 91:
        return 10
    if points >= 81:
        return 9
    if points >= 71:
        return 8
    if points >= 61:
        return 7
    if points >= 51:
        return 6
    return 5


results = []        # every result is a dictionary: {"name": ..., "points": ...}

while True:
    name = input("Name: ").strip()
    if name == "":
        break                           # an empty name: the input is over
    points = read_points("Points: ")
    results.append({"name": name, "points": points})

print()
if len(results) == 0:
    print("No results.")
else:
    passed = 0
    total = 0
    best = results[0]
    for result in results:
        print(f"{result['name']:15} {result['points']:5} {grade(result['points']):5}")
        if grade(result["points"]) >= 6:
            passed = passed + 1
        total = total + result["points"]
        if result["points"] > best["points"]:
            best = result
    print(f"Passed: {passed} of {len(results)}")
    print(f"Average: {total / len(results):.1f} points")
    print(f"Best: {best['name']} ({best['points']} points)")
