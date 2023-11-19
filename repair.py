import logger as l
import json
def repair():
    l.log(type="DEBUG",message="Checking the validity of 'save.json'")
    try:
        with open("save.json","r") as f:
            data = json.load(f)
    except:
        try:
            l.log(type="WARNING",message="Failed to load 'save.json', trying to restore using 'save.backup.json'")
            with open("save.backup.json","r") as f:
                settings_file_backup = json.load(f)
            with open("save.json","w") as f:
                json.dump(settings_file_backup,f,indent=2)
            l.log(type="SUCCESS",message="Succesfully reverted save!")
        except Exception as e:
            with open("save.json","w") as f:
                l.log(type="ERROR",message=f"An error occured with opening 'save.json', and we couldn't restore the backup file. Rewriting a new save with example data... {e}")
                settings_file = {"settings":{"custom_theme":{"button_color":"#8b9cf6","frame_color":"#9cf5f9","root_color":"#abb1fd","hover_color":"#ecf69a","opacity":0.75}}}
                json.dump(settings_file,f)