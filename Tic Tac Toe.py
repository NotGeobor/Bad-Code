import time
import random
y = 3
x = 3
coords = {}
choices = []

for y_value in range(y):
    for x_value in range(x):
        coords[str(x_value) + str(y_value)] = "~"

for y_value in range(y):
    for x_value in range(x):
        choices.append(str(x_value) + str(y_value))


def show(x, y, x_value, y_value):
    print("  0 1 2")
    for y_value in range(y):
        print(y_value, end=" ")
        for x_value in range(x):
            print(coords[str(x_value) + str(y_value)], end=" ")
        print("\n", end="")


def win(x, y, coords):
    for y_number in range(y):
        if all(coords[str(value) + str(y_number)] == "o" for value in range(x)):
            return True
    for x_number in range(x):
        if all(coords[str(x_number) + str(value)] == "o" for value in range(y)):
            return True
    if coords["00"] == "o" and coords["11"] == "o" and coords["22"] == "o":
        return True
    if coords["20"] == "o" and coords["11"] == "o" and coords["02"] == "o":
        return True


def lose(x, y, coords):
    for y_number in range(y):
        if all(coords[str(value) + str(y_number)] == "x" for value in range(x)):
            return True
    for x_number in range(x):
        if all(coords[str(x_number) + str(value)] == "x" for value in range(y)):
            return True
    if coords["00"] == "x" and coords["11"] == "x" and coords["22"] == "x":
        return True
    if coords["20"] == "x" and coords["11"] == "x" and coords["02"] == "x":
        return True


while True:
    if len(choices) > 0:
        o = random.choice(choices)
        coords[o] = "x"
        choices.remove(o)
    else:
        print("Tie")
        break

    if lose(x, y, coords):
        show(x, y, x_value, y_value)
        print("ur gud")
        break

    show(x, y, x_value, y_value)

    move = input("Enter move (xy): ")

    if coords[move] == "x" or coords[move] == "o":
        print("ur gay")
        break
    else:
        coords[move] = "o"
        choices.remove(move)

    if win(x, y, coords):
        show(x, y, x_value, y_value)
        print("ur bad")
        break

    show(x, y, x_value, y_value)

    time.sleep(0.5)
