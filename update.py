import settings
import get_info

def check_for_updates(mode):
    if mode=="manual":
        try:
            settings.configure(state="disabled",text="Checking")
            response = requests.get("https://api.github.com/repos/ctih1/Happy-Button/releases/latest")
            a = response.json()["name"]
            b = a.rsplit(" ",1)
            
            if float(b[1]) > float(get_info.application_ver):
                check_for_updates_.configure(state="normal",text="Updates available.")
                webbrowser.open('github.com/ctih1/Happy-Button/releases/latest', new=2)
            else:
                check_for_updates_.configure(state="disabled",text="No Updates available.")
        except:
            print("ratelimited")