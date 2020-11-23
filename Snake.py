import random
import os
import time
length = 5
snake = []
coords = {}
lose = 0

x = int(input("How wide? "))
y = int(input("How tall? "))

for y_value in range(y):
    for x_value in range(x):
        coords[str(x_value) + str(y_value)] = "[]"

position = (str(random.randint(0, (x - 1))) + str(random.randint(0, (y - 1))))

apple = (str(random.randint(0, (x - 1))) + str(random.randint(0, (y - 1))))

snake.append(position)

coords[position] = "s "

coords[apple] = "a "

os.system("clear")

for y_value in range(y):
    for x_value in range(x):
        print(coords[str(x_value) + str(y_value)] + " ", end="")
    print("\n", end="")
while True:
    move = input("Direction? ")
    if move == "w":
        position = (position[0] + str(int(position[1]) - 1))
        if len(position) > 2:
            print("ur gay")
            break
        for value in snake:
            if value == position:
                lose = 1
                break
        if position == apple:
            length += 2
        if len(snake) < length:
            snake.append(position)
        elif len(snake) == length:
            snake.append(position)
            coords[snake[0]] = "[]"
            snake.remove(snake[0])
    if move == "a":
        position = (str(int(position[0]) - 1) + position[1])
        if len(position) > 2:
            print("ur gay")
            break
        for value in snake:
            if value == position:
                lose = 1
                break
        if position == apple:
            length += 2
        if len(snake) < length:
            snake.append(position)
        elif len(snake) == length:
            snake.append(position)
            coords[snake[0]] = "[]"
            snake.remove(snake[0])
    if move == "s":
        position = (position[0] + str(int(position[1]) + 1))
        if len(position) > 2:
            print("ur gay")
            break
        for value in snake:
            if value == position:
                lose = 1
                break
        if position == apple:
            length += 2
        if len(snake) < length:
            snake.append(position)
        elif len(snake) == length:
            snake.append(position)
            coords[snake[0]] = "[]"
            snake.remove(snake[0])
    if move == "d":
        position = (str(int(position[0]) + 1) + position[1])
        if len(position) > 2:
            print("ur gay")
            break
        for value in snake:
            if value == position:
                lose = 1
                break
        if position == apple:
            length += 2
        if len(snake) < length:
            snake.append(position)
        elif len(snake) == length:
            snake.append(position)
            coords[snake[0]] = "[]"
            snake.remove(snake[0])
    if lose == 1:
        print("ur gay")
        break
    for value in snake:
        coords[snake[snake.index(value)]] = "s "
    win = 0
    for value in coords:
        if coords[value] == "s ":
            win += 1
        if win == (x * y):
            os.system("clear")
            for y_value in range(y):
                for x_value in range(x):
                    print(coords[str(x_value) + str(y_value)], end=" ")
                print("\n", end="")
            print("ur ungay")
            break
    while coords[apple] == "s ":
        apple = (str(random.randint(0, (x - 1))) +
                 str(random.randint(0, (y - 1))))
    coords[apple] = "a "
    os.system("clear")
    for y_value in range(y):
        for x_value in range(x):
            print(coords[str(x_value) + str(y_value)], end=" ")
        print("\n", end="")
