from pypresence import Presence
import time
import logger as l
import get_info
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
    except Exception as e:
        l.log(type="ERROR",message=f"RPC Encountered an error. {e}")
        turned_on = False
    
def update(state: str, details: str):
    if turned_on == True:
        RPC.update(large_text=f"{get_info.application_ver()} ({get_info.release_type()})",
                details=details,
                state=state,
                start=time_started,
                large_image="logo_1",
                buttons=[{"label":"Download","url":"https://github.com/ctih1/Happy-Button/releases/latest"}]
        )