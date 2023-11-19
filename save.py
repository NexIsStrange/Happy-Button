import os
import json 
import logger as l
from repair import repair
import backup

def create_save():
    if os.path.isfile("save.json"):
        return False
    else:
        l.log(type="INFO",message="Creating a new save.")
        with open("save.json","w") as f:
            f.write('{"score": 0,"settings":{}}')

def get_score():
    create_save()
    repair()
    with open("save.json","r") as f:
        save = json.load(f)
    return save.get("score",0)

def save(score: int):
    l.log(type="DEBUG", message=f"Saving score: {score}")
    create_save()
    repair()
    with open("save.json","r") as f:
        save = json.load(f)
    old_score = save.get("score",0)
    if old_score < score: 
        save["score"] = score
        with open("save.json","w") as f:
            json.dump(save,f,indent=2)
    backup.backup()
    l.log(type="DEBUG",message="Saved score succesfully!")
    
def create_empty(save):
        if "settings" not in save:
            save["settings"] = {}
        if "custom_theme" not in save["settings"]:
            save["settings"]["custom_theme"] = {}
        backup.backup()
        with open("save.json","w") as f:
            json.dump(save,f,indent=2)
            
def theme(theme:str, button_color: str=None, frame_color: str=None, root_color: str=None, hover_color: str=None, opacity:float=1.0):
    repair()
    l.log(type="DEBUG",message="Saving theme...")
    with open("save.json","r") as f:
        save = json.load(f)
    if theme=="custom":
        l.log(type="DEBUG",message="Saving custom theme...")
        save["settings"]["custom_theme"]["button_color"] = button_color
        save["settings"]["custom_theme"]["frame_color"] = frame_color
        save["settings"]["custom_theme"]["root_color"] = root_color
        save["settings"]["custom_theme"]["hover_color"] = hover_color
        save["settings"]["custom_theme"]["opacity"] = opacity
    save["settings"]["theme"] = theme
    
    backup.backup()
    with open("save.json","w") as f:
        json.dump(save,f,indent=2)
    
