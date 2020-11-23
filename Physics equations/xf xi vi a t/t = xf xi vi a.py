import math
xf = float(input("xf? "))
xi = float(input("xi? "))
vi = float(input("vi? "))
a = float(input("a? "))
t = (((vi * -1) + math.sqrt((vi ** 2) - ((2 * a) * (xi - xf)))) / a)
print()
print(t)
print()