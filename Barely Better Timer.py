import time


def start():
    startnumber = input("Start at what number (HH:MM:SS)? ")
    if startnumber[-3] == ":" and startnumber[-6] == ":" and int(startnumber[-2:]) <= 59 and int(startnumber[-5:-3]) <= 59 and int(startnumber[-2:]) >= 0 and int(startnumber[-5:-3]) >= 0 and int(startnumber[:-6]) >= 0:
        return startnumber
    else:
        return startagain()


def startagain():
    startnumber = input("Must Be correct format (HH:MM:SS). ")
    if startnumber[-3] == ":" and startnumber[-6] == ":":
        return startnumber
    else:
        return startagain()


startnumber = start()
hours = int(startnumber[:-6])
minutes = int(startnumber[-5:-3])
seconds = int(startnumber[-2:])
print(str(hours) + ":" + str(minutes) + ":" + str(seconds))


def scount(seconds, minutes, hours):
    while seconds > 0:
        time.sleep(1)
        seconds = (seconds - 1)
        print(str(hours) + ":" + str(minutes) + ":" + str(seconds))
    return mcount(seconds, minutes, hours)


def mcount(seconds, minutes, hours):
    if minutes == 0:
        return hcount(seconds, minutes, hours)
    else:
        time.sleep(1)
        seconds = 59
        minutes = (minutes - 1)
        print(str(hours) + ":" + str(minutes) + ":" + str(seconds))
        return scount(seconds, minutes, hours)


def hcount(seconds, minutes, hours):
    if hours == 0:
        return print("Geobor")
    else:
        time.sleep(1)
        seconds = 59
        minutes = 59
        hours = (hours - 1)
        print(str(hours) + ":" + str(minutes) + ":" + str(seconds))
        return mcount(seconds, minutes, hours)


scount(seconds, minutes, hours)
