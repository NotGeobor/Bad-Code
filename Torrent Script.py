import os
import subprocess

series = "Clannad After Story"
season = "1"
episode = 1

for file in os.listdir("D:/s1/1"):
    episode_name = (series + " S" + season + "EP" +
                    str(episode) + ".mkv")
    episode += 1
    command = (
        f"\"C:\Progra~1\MKVToolNix\mkvmerge.exe\" -o \"D:\s1\output\{episode_name}\" --compression -1:none -a 3 -s 5 D:\s1\\1\{file} --compression -1:none")
    subprocess.call(command)
