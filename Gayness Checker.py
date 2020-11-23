import time
import os
import random
dic = {}
listhex = ["F", "H", "0", "3", "9", "6", "X"]
load = 0
seed = 0
code = 0
codenumber = 0
percent = 0
length1 = ""
length2 = ""
gayletters = ["g", "a", "y", "h", "o", "i", "p", "q", "d", "f", "m"]
kindagayletters = ["u", "n"]
barelygayletters = ["r", "l", "x", "s", "t"]
wordletter = 0
gayness = 0
while load < 3:
    os.system("clear")
    print("Loading.")
    time.sleep(0.45)
    os.system("clear")
    print("Loading..")
    time.sleep(0.45)
    os.system("clear")
    print("Loading...")
    time.sleep(0.6)
    load += 1
os.system("clear")
print("Loading.")
time.sleep(0.45)
os.system("clear")
print("Loading..")
time.sleep(1)
os.system("clear")
print("Word Gayness Checker v0.0.8.43", end="")
print("         By Geobor Geobor")
time.sleep(1)
print("Copyright 2008")
time.sleep(1.7)
word = input("Input Word: ")
time.sleep(1)
os.system("clear")
print("Word Gayness Checker v0.0.8.43", end="")
print("         By Geobor Geobor")
print("Copyright 2008")
time.sleep(0.25)
os.system("clear")
print("computing...")
time.sleep(3)
os.system("clear")
time.sleep(3)
print("gathering vector values...")
time.sleep(0.4)
print("parsing integers...")
time.sleep(2)
print("converting to floating point...")
time.sleep(3)
print("generating fp32 keys")
print("[")
time.sleep(3)
for letter in word:
    seed = random.randint(0, 100)
    random.seed(seed)
    fp32key = random.random()
    dic[letter] = fp32key
    print(letter + " = " + str(fp32key))
    time.sleep(3)
print("]")
print("hashing memory sets...")
time.sleep(2)
print("searching in byte blocks")
time.sleep(3)
print("converting to hexadecimal using base [15]...")
time.sleep(4)
print("[")
for letter in word:
    print(str(dic[letter]) + " = " + "0x803" + random.choice(listhex) + random.choice(listhex) + random.choice(listhex) +
          random.choice(listhex) + random.choice(listhex) + random.choice(listhex) + random.choice(listhex) + "0")
    time.sleep(2)
print("]")
print("comparing...")
time.sleep(2)
print("reading memory values...")
time.sleep(4)
os.system("clear")
time.sleep(2)
print("[----------------------------------------------------------------------------------------------------]")
time.sleep(0.3)
os.system("clear")
time.sleep(0.1)
print("0% [----------------------------------------------------------------------------------------------------]")
while percent < 50:
    while code < 100:
        print(str(codenumber) + " = " + "0x803" + random.choice(listhex) + random.choice(listhex) + random.choice(listhex) +
              random.choice(listhex) + random.choice(listhex) + random.choice(listhex) + random.choice(listhex) + "0")
        codenumber += 1
        time.sleep(0.02)
        print(str(codenumber) + " = " + "0x803" + random.choice(listhex) + random.choice(listhex) + random.choice(listhex) +
              random.choice(listhex) + random.choice(listhex) + random.choice(listhex) + random.choice(listhex) + "0")
        code += 1
        codenumber += 1
        time.sleep(0.02)
    time.sleep(3)
    percent += 25
    code = 0
    codenumber = 0
    os.system("clear")
    time.sleep(2)
    print("[----------------------------------------------------------------------------------------------------]")
    time.sleep(0.3)
    os.system("clear")
    time.sleep(0.1)
    print("0% [----------------------------------------------------------------------------------------------------]")
    time.sleep(1)
    os.system("clear")
    while len(length1) < percent:
        length1 += "*"
    length2 = ""
    while len(length2) < (100 - len(length1)):
        length2 += "-"
    print(str(percent) + "% " + "[" + length1 + length2 + "]")
time.sleep(2)
print("[----------------------------------------------------------------------------------------------------]")
time.sleep(0.3)
os.system("clear")
time.sleep(0.1)
while percent < 98:
    percent += 1
    while len(length1) < percent:
        length1 += "*"
    length2 = ""
    while len(length2) < (100 - len(length1)):
        length2 += "-"
    print("parsing...")
    print(str(percent) + "% " + "[" + length1 + length2 + "]")
    time.sleep(0.2)
    os.system("clear")
percent += 1
while len(length1) < percent:
    length1 += "*"
length2 = ""
while len(length2) < (100 - len(length1)):
    length2 += "-"
print("cleaning up...")
print(str(percent) + "% " + "[" + length1 + length2 + "]")
time.sleep(10)
os.system("clear")
percent += 1
while len(length1) < percent:
    length1 += "*"
length2 = ""
while len(length2) < (100 - len(length1)):
    length2 += "-"
print("finishing...")
print(str(percent) + "% " + "[" + length1 + length2 + "]")
time.sleep(3)
os.system("clear")
time.sleep(2)
while wordletter < len(word):
    if word[wordletter] in gayletters:
        gayness += 1
    wordletter += 1
wordletter = 0
while wordletter < len(word):
    if word[wordletter] in kindagayletters:
        gayness += 0.6
    wordletter += 1
wordletter = 0
while wordletter < len(word):
    if word[wordletter] in barelygayletters:
        gayness += 0.25
    wordletter += 1
print(word + " is " + str((gayness / len(word)) * 100) + "% gay")
