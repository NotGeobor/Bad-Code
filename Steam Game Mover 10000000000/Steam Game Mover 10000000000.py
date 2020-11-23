from tkinter import *
from shutil import copytree, copy
import time

font = "Comic Sans MS"
dis = {"bg": "#2c2f33", "fg": "white"}
game_keys = {"Battlefield 4": "1238860", "Besiege": "346010", "BloonsTD6": "960090", "Borderlands": "8980", "Borderlands 2": "49520", "BorderlandsGOTYEnhanced": "729040", "BorderlandsPreSequel": "261640", "Call of Duty Black Ops III": "311210", "Call of Duty World at War": "10090", "CLANNAD": "324160", "CLANNAD Side Stories": "420100", "Counter-Strike Global Offensive": "730", "Crusader Kings II": "203770", "Dark Souls II Scholar of the First Sin": " 	335300", "DARK SOULS III": "374320", "Dark Souls Prepare to Die Edition": "211420", "DARK SOULS REMASTERED": "570940", "Dead Cells": "588650", "Doki Doki Literature Club": "698780", "Duck Game": "312530", "Dying Light": "239140", "Enter the Gungeon": "311690", "Europa Universalis IV": "236850", "Factorio": "427520", "Fallout 4": "377160", "Fallout New Vegas": "22380", "FORTIFY": "505040", "GarrysMod": "4000", "Halo The Master Chief Collection": "976730", "Hearts of Iron IV": "000000000000",
             "Hollow Knight": "367520", "ILYCS": "1121910", "Katana ZERO": "460950", "Kerbal Space Program": "220200", "My Friend Pedro": "557340", "NieRAutomata": "524220", "Ori": "261570", "Ori DE": "387290", "PapersPlease": "239030", "PlagueInc": "246620", "Poly Bridge": "367450", "Portal": "400", "Portal 2": "620", "Rust": "252490", "Sid Meier's Civilization VI": "289070", "SlayTheSpire": "646570", "Soda Dungeon": "564710", "SpeedRunners": "207140", "Stardew Valley": "413150", "Super Meat Boy": "40800", "Terraria": "105600", "The Forest": "242760", "the witcher 2": "20920", "The Witcher 3": "292030", "The Witcher Enhanced Edition": "20900", "Tom Clancy's Rainbow Six Siege": "359550", "Tom Clancy's The Division": "365590", "Tomb Raider": "203160", "Tomoyo After ~It's a Wonderful Life~ English Edition": "462990", "Universe Sandbox 2": "230290", "Victoria 2": "42960", "War Thunder": "236390"}


def gay():
    if pv.get() == "Default Path (C Drive)":
        copytree(f"D:\Steam Backup\steamapps\common\{gv.get()}",
                 f"C:\Program Files (x86)\Steam\steamapps\common\{gv.get()}")
        copy(f"D:\Steam Backup\steamapps\\appmanifest_{game_keys[gv.get()]}.acf",
             f"C:\Program Files (x86)\Steam\steamapps\\appmanifest_{game_keys[gv.get()]}.acf")
    elif pv.get() == "Custom Path" and pe.get() == "(Custom Path)":
        exit()
    elif pv.get() == "Custom Path" and pe.get() == "":
        exit()
    else:
        copytree(
            f"D:\Steam Backup\steamapps\common\{gv.get()}", f"{pe.get()}\{gv.get()}")
        copy(f"D:\Steam Backup\steamapps\\appmanifest_{game_keys[gv.get()]}.acf",
             f"{pe.get()[:-6]}appmanifest_{game_keys[gv.get()]}.acf")
    e = Label(root, text="Finished", font=(font, 15), **dis)
    e.pack()


root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry("640x480" + "+" + str(int((screen_width / 2) - 320)
                                    ) + "+" + str(int((screen_height / 2) - 240)))
root.config(bg="#2c2f33")
root.title("Steam Game Mover 10000000000")
root.iconbitmap("Geobor.ico")

t = Label(root, text="Steam Game Mover 10000000000", font=(font, 20), **dis)
t.pack()

gl = Label(root, text="Game", font=(font, 15), **dis)
gl.pack()

gv = StringVar(root)
gv.set("Choose Game")
g = OptionMenu(root, gv, *game_keys.keys())
g.pack()

pl = Label(root, text="Location", font=(font, 15), **dis)
pl.pack()

pv = StringVar(root)
pv.set("Default Path (C Drive)")
p = OptionMenu(root, pv, "Default Path (C Drive)", "Custom Path")
p.pack()

pe = Entry(root)
pe.insert(0, "(Custom Path)")
pe.pack()

vd = Button(root, text="Move", font=(font, 15), command=gay, **dis)
vd.pack()

root.mainloop()
