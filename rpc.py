from pypresence import Presence
import time
import logger as l
turned_on = True
def init():
    global turned_on
    global time_started
    global RPC
    try:
        client_id ="1171834497466126386"
        time_started = time.time()
        RPC = Presence(client_id)
        RPC.connect()
    except:
        l.log(type="ERROR",message="RPC Encountered an error.")
        turned_on = False
    
def update(state: str, details: str):
    if turned_on == True:
        RPC.update(large_text="Playing Happy Button",
                details=details,
                state=state,
                start=time_started,
                large_image="logo_1",
                buttons=[{"label":"Download","url":"https://github.com/ctih1/Happy-Button/releases/latest"}]
        )