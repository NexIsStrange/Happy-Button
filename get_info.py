import json

with open("info.json","r") as f:
    data = json.load(f)
    
def application_ver():
    return float(data["application_version"])
def theme_ver():
    return data["theme_version"]
def save_ver():
    return data["save_version"]
def release_type():
    return data["publish_type"]