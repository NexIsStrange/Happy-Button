import os
import json 

def create_save():
    if os.path.isfile("save.json"):
        return False
    else:
        with open("save.json","w") as f:
            f.write('{"score": 0,"settings":{}}')

def get_score():
    create_save()
    with open("save.json","r") as f:
        save = json.load(f)
    return save.get("score",0)

def save(score: int):
    create_save()
    with open("save.json","r") as f:
        save = json.load(f)
    old_score = save.get("score",0)
    if old_score < score: 
        save["score"] = score
        with open("save.json","w") as f:
            json.dump(save,f)
            