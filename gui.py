import customtkinter as ctk
import result
import theme
import sound
import importlib
import logger as l
import settings
import sys
import time
import update

buttons = []
current_button = None
start_time = None

def GUI():
    global logic
    logic = importlib.import_module("logic")
    l.log(type="INFO",message="Starting GUI")
    print(theme.get_colors())
    global max_score
    max_score = 0

    global window
    window = ctk.CTk()
    window.configure(fg_color=theme.get_colors()["root_color"])
    window.geometry("500x250")
    window.title("Happy Button")
    window.minsize(500,250)
    
    global frame
    frame = ctk.CTkFrame(window,width=450,height=200)
    frame.configure(fg_color=theme.get_colors()["frame_color"])
    frame.place(relx=0.5,rely=0.5,anchor=ctk.CENTER)
    create_elements()
    
    def toggle_resize():
        if settings.get_setting("scaling") == True:
            import scaling
            window.bind("<Configure>",scaling.resize)

    window.after(1000,toggle_resize)
    sound.init()
    window.protocol("WM_DELETE_WINDOW",on_closing)
    bind_buttons()
    if settings.get_setting("check") == True:
        update.check_for_updates()
    window.mainloop()

def reset_buttons():
    for i in buttons:
        i.configure(fg_color=theme.get_colors()["button_color"],hover_color=theme.get_colors()["button_color"])
    
def create_elements():
    l.log(type="DEBUG",message="Creating elements...")
    global start
    global score_label
    global settings_button
    global time_label
    global start
    global warning_label
    
    warning_label = ctk.CTkLabel(frame,font=("Helvetica",11),text_color="#FF0000",text="")
    warning_label.place(relx=0.75,rely=0.1,anchor=ctk.CENTER)
    
    start = ctk.CTkButton(frame,width=100,height=25,text="Start",fg_color=theme.get_colors()["button_color"],hover_color=theme.get_colors()["hover_color"],font=("Helvetica",18.75),command=start_game)
    start.place(relx=0.5,rely=0.125,anchor=ctk.CENTER)

    button1 = ctk.CTkButton(frame,width=100,height=100,text="",corner_radius=50,fg_color=theme.get_colors()["button_color"],hover_color=theme.get_colors()["button_color"],command=lambda m=1:logic.button_click(m))
    button1.place(relx=0.13,rely=0.5,anchor=ctk.CENTER)

    button2 = ctk.CTkButton(frame,width=100,height=100,text="",corner_radius=50,fg_color=theme.get_colors()["button_color"],hover_color=theme.get_colors()["button_color"],command=lambda m=2:logic.button_click(m))
    button2.place(relx=0.38,rely=0.5,anchor=ctk.CENTER)
    
    button3 = ctk.CTkButton(frame,width=100,height=100,text="",corner_radius=50,fg_color=theme.get_colors()["button_color"],hover_color=theme.get_colors()["button_color"],command=lambda m=3:logic.button_click(m))
    button3.place(relx=0.63,rely=0.5,anchor=ctk.CENTER)
    
    button4 = ctk.CTkButton(frame,width=100,height=100,text="",corner_radius=50,fg_color=theme.get_colors()["button_color"],hover_color=theme.get_colors()["button_color"],command=lambda m=4:logic.button_click(m))
    button4.place(relx=0.87,rely=0.5,anchor=ctk.CENTER)
    
    buttons.append(button1)
    buttons.append(button2)
    buttons.append(button3)
    buttons.append(button4)
    
    settings_button = ctk.CTkButton(frame,width=100,height=25,fg_color=theme.get_colors()["button_color"],hover_color=theme.get_colors()["hover_color"],text="Settings",font=("Helvetica",18.75),command=settings.gui)
    settings_button.place(relx=0.5,rely=0.9,anchor=ctk.CENTER)
    
    time_label = ctk.CTkLabel(frame,text="Time",font=("Helvetica",20))
    time_label.place(rely=0.9,relx=0.09,anchor=ctk.CENTER)
    
    score_label = ctk.CTkLabel(frame,text=f"0/0",font=("Helvetica",20))
    score_label.place(relx=0.03,rely=0.03)
    
    l.log(type="DEBUG",message="Done creating elements")
    
    
def highlight_button(index: int):
    buttons[index-1].configure(fg_color=theme.get_colors()["hover_color"],hover_color=theme.get_colors()["hover_color"])
        
def move_buttons_away():
    if l.level <= 0:
        l.log(type="DEBUG",message=f"Moving buttons away")
    start.place(relx=12,rely=12)
    settings_button.place(relx=12,rely=12)
 
def update_score(score):
    score_label.configure(text=f"{score}/{max_score}")
 
def restore_buttons():
    if l.level <= 0:
        l.log(type="DEBUG",message=f"Moved buttons back")
    start.place(rely=0.1,relx=0.5,anchor=ctk.CENTER)
    settings_button.place(relx=0.5,rely=0.9,anchor=ctk.CENTER)
    start.configure(text="Retry")

def show_result(score: int, max_score: int, clicks: int,correct_clicks: int, percentage: float, min_time: float, average_time: float):
    update_score(score=score)
    if l.level <= 0:
        l.log(type="DEBUG",message=f"Showing results")
    result.show(x=window.winfo_pointerx()-112,y=window.winfo_pointery()-87,clicks=clicks,correct_clicks=correct_clicks,percent=percentage, min_time=min_time,average_time=average_time)

def update_time(elapsed_time):
    _time = round(float(elapsed_time*-1),1)
    time_label.configure(text=(_time))

def start_game():
    if l.level <= 0:
        l.log(type="DEBUG",message=f"GUI: Starting game")
    logic.start()
    logic.random_button()

def refresh_theme_():
    if l.level <= 0:
        l.log(type="DEBUG",message=f"Refreshed theme")
    for button in buttons:
        button.configure(fg_color=theme.get_colors()["button_color"],hover_color=theme.get_colors()["button_color"])
    window.configure(fg_color=theme.get_colors()["root_color"])
    frame.configure(fg_color=theme.get_colors()["frame_color"])
    settings_button.configure(fg_color=theme.get_colors()["button_color"],hover_color=theme.get_colors()["button_color"])
    start.configure(fg_color=theme.get_colors()["button_color"],hover_color=theme.get_colors()["button_color"])
    l.log(type="DEBUG",message="Refreshed theme succesfully")

def refresh_theme():
    l.log(type="DEBUG",message="Refreshing theme in 200ms...")
    window.after(200,refresh_theme_)
    
def on_closing():
    l.log(type="DEBUG",message="Exiting with 'on_closing()'")
    for i in range(100)[::-1]:
        window.attributes("-alpha",i/100)
        time.sleep(0.005)
    sys.exit(0)

def bind_buttons():
    for i in range(4):
        l.log(type="DEBUG",message=f"Binding standard button {i+1} to {i+1}...")
        window.bind(f"{i+1}",lambda event,m=i+1: logic.button_click(m))
    for i in range(4):
        keybind = settings.get_setting(f"{i+1}")
        l.log(type="DEBUG",message=f"Binding custom button {i+1} to {keybind}...")
        window.bind(f"{keybind}", lambda event, m=i+1: logic.button_click(m))
        
if __name__ == "__main__":
    l.log(type="WARNING",message="It looks like you are running the 'gui.py' script as main, this is not adviced, and might lead to unexpected behaviour")
    input = input("Do you want to proceed? (Y/N)")
    if input.lower() not in ["yes","y","yeah"]:
        quit()
    else:
        GUI()