import os
import sys
import platform
import logger as l
exclude = set(["__pycache__",".git"])
fil = []
for (root, dirs,files) in os.walk('.',topdown=True):
    [dirs.remove(d) for d in list(dirs) if d in exclude]
    fil.append(f"{root} {files}")
l.save_info(info=f"Python version: {sys.version}\nFiles: {fil}\nWindows Version: {platform.platform()}\nArchitecture: {platform.machine()}")
import customtkinter as ctk
import gui as g
import rpc
#TODO:
ctk.set_appearance_mode("Dark")

with open("log.txt","w") as f:
    f.write("")
    
if __name__ == "__main__":
    rpc.init()
    rpc.update(state="Happy Button", details="Launching")
    l.log(type="INFO",message="Game Started!")
    g.GUI()
else:
    print(__name__)