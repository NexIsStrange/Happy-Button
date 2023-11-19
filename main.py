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

def start():
    l.log(type="INFO",message="Game Started!")
    try:
        l.log(type="DEBUG", message="Initializing RPC")
        rpc.init()
        rpc.update(state="Happy Button", details="Launching")
    except Exception as e:
        l.log(type="ERROR",message=f"Failed initializing RPC. {e}")
    g.GUI()



with open("log.txt","w") as f:
    f.write("")
    
if __name__ == "__main__":
    start()
    
    
else:
    print(__name__)