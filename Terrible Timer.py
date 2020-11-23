import time
import sys
import resource
sys.setrecursionlimit(10**6)
resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
digit = 0
digit1 = 0
digit2 = 0
digit3 = 0
digit4 = 0
startnumber = input("Start at what number (0-99999)? ")
while int(startnumber) > 99999 or int(startnumber) < 0:
    startnumber = input("Start number must be between 0 and 99999. ")
while len(str(startnumber)) == 5:
    startnumber = (int(startnumber) - 10000)
    digit += 1
while len(str(startnumber)) == 4:
    startnumber = (int(startnumber) - 1000)
    digit1 += 1
while len(str(startnumber)) == 3:
    startnumber = (int(startnumber) - 100)
    digit2 += 1
while len(str(startnumber)) == 2:
    startnumber = (int(startnumber) - 10)
    digit3 += 1
while len(str(startnumber)) == 1 and int(startnumber) > 0:
    startnumber = (int(startnumber) - 1)
    digit4 += 1
input("Press Enter to Go: ")
print(str(digit) + str(digit1) + str(digit2) + str(digit3) + str(digit4))


def digit4go(gamer, gamer1, gamer2, gamer3, gamer4):
    while gamer4 > 0:
        time.sleep(0.01)
        gamer4 -= 1
        print(str(gamer) + str(gamer1) + str(gamer2) + str(gamer3) + str(gamer4))
    return digit3go(gamer, gamer1, gamer2, gamer3, gamer4)


def digit3go(gamer, gamer1, gamer2, gamer3, gamer4):
    if gamer3 == 0:
        return digit2go(gamer, gamer1, gamer2, gamer3, gamer4)
    else:
        gamer4 = 9
        gamer3 -= 1
        print(str(gamer) + str(gamer1) + str(gamer2) + str(gamer3) + str(gamer4))
        return digit4go(gamer, gamer1, gamer2, gamer3, gamer4)


def digit2go(gamer, gamer1, gamer2, gamer3, gamer4):
    if gamer2 == 0:
        return digit1go(gamer, gamer1, gamer2, gamer3, gamer4)
    else:
        gamer4 = 9
        gamer3 = 9
        gamer2 -= 1
        print(str(gamer) + str(gamer1) + str(gamer2) + str(gamer3) + str(gamer4))
        return digit4go(gamer, gamer1, gamer2, gamer3, gamer4)


def digit1go(gamer, gamer1, gamer2, gamer3, gamer4):
    if gamer1 == 0:
        return digitgo(gamer, gamer1, gamer2, gamer3, gamer4)
    else:
        gamer4 = 9
        gamer3 = 9
        gamer2 = 9
        gamer1 -= 1
        print(str(gamer) + str(gamer1) + str(gamer2) + str(gamer3) + str(gamer4))
        return digit4go(gamer, gamer1, gamer2, gamer3, gamer4)


def digitgo(gamer, gamer1, gamer2, gamer3, gamer4):
    if gamer == 0:
        return print("Geobor")
    else:
        gamer4 = 9
        gamer3 = 9
        gamer2 = 9
        gamer1 = 9
        gamer -= 1
        print(str(gamer) + str(gamer1) + str(gamer2) + str(gamer3) + str(gamer4))
        return digit4go(gamer, gamer1, gamer2, gamer3, gamer4)


digit4go(digit, digit1, digit2, digit3, digit4)
