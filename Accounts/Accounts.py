import sys
from scrambler import user, encoder
import os
import json
import time
valid_create = ("create", "Create", "c", "L")
valid_login = ("login", "Login", "l", "L")

while True:
    os.system("clear")
    create_login = input("Create or Login: ")
    if create_login in valid_create or create_login in valid_login:
        pass
    else:
        exit("invalid input")

    if create_login in valid_login:
        break

    newuser = user
    newuser.username = input("New User Name: ")
    if input("Confirm User Name: ") == newuser.username:
        pass
    else:
        exit("User Names are not the same")

    newuser.password = input("New Password: ")
    if newuser.password == newuser.username:
        exit("User Name and Password cannot be the same")

    if input("Confirm Password: ") == newuser.password:
        pass
    else:
        exit("Passwords are not the same")

    try:
        newuser.key = int(input("New Key: "))
    except ValueError:
        exit("Key must be of type int")

    if int(input("Confirm Key: ")) == newuser.key:
        pass
    else:
        exit("Keys are not the same")

    save_user = user
    save_user.username = encoder(newuser.username, newuser.key)
    save_user.password = encoder(newuser.password, newuser.key)

    default_dic = {}

    try:
        open("users.json", "x").close
        with open("users.json", "w") as file:
            json.dump(default_dic, file, indent=4)
    except FileExistsError:
        pass

    with open("users.json", "r") as file:
        json_dic = dict(json.load(file))
        if save_user.username in json_dic.keys():
            exit("User already exists")
        json_dic[save_user.username] = save_user.password

    with open("users.json", "w") as file:
        json.dump(json_dic, file, indent=4)

    print("User Account Created Successfully")
    time.sleep(2.5)

currentuser = user
currentuser.username = input("User Name: ")
currentuser.password = input("Password: ")
currentuser.key = input("Key: ")

with open("users.json", "r") as file:
    json_dic = dict(json.load(file))

    if encoder(currentuser.username, currentuser.key) in json_dic.keys():
        pass
    else:
        exit("Incorrect User Name, Password, or Key")

    if json_dic[encoder(currentuser.username, currentuser.key)] == encoder(currentuser.password, currentuser.key):
        pass
    else:
        exit("Incorrect User Name, Password, or Key")

print("ur in")
