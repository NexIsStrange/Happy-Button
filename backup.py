import json
import logger as l
from repair import repair

def backup():
    l.log(type="INFO",message="Backing up save...")
    repair()
    with open("save.json","r") as f:
        data = json.load(f)
    with open("save.backup.json","w") as b:
        json.dump(data,b,indent=2)