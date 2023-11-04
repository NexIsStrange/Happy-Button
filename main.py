import customtkinter as ctk
import logger as l
import sys
import gui as g
import platform
import os

#TODO:
fil = []
exclude = set(["__pycache__",".git"])
ctk.set_appearance_mode("Dark")

with open("log.txt","w") as f:
    f.write("")
    
if __name__ == "__main__":
    for (root, dirs,files) in os.walk('.',topdown=True):
        [dirs.remove(d) for d in list(dirs) if d in exclude]
        fil.append(f"{root} {files}")
    l.log(type="INFO",message="Game Started!")
    l.save_info(info=f"Python version: {sys.version}\nFiles: {fil}\nWindows Version: {platform.platform()}\nArchitecture: {platform.machine()}")
    g.GUI()
else:
    print(__name__)