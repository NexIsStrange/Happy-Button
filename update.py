import settings
import get_info
import json
import logger as l
import requests
import webbrowser

def check_for_updates():
    try:
        l.log(type="DEBUG",message=f"Checking for updates. Current version: {get_info.application_ver()}")
        response = requests.get("https://api.github.com/repos/ctih1/Happy-Button/releases/latest")
        a = response.json()["name"]
        b = a.rsplit(" ",1)
        if float(b[1]) > float(get_info.application_ver()):
            l.log(type="INFO",message=f"Found a newer version ({float(b[1])})")
            webbrowser.open_new("https://github.com/ctih1/Happy-Button/releases/latest")
            return True
        else:
            return False
    except Exception as e:
        l.log(type="ERROR",message=f"Failed to check for updates, possibly ratelimited? {e}")