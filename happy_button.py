import customtkinter as ctk
import random
import time
from playsound import playsound
import json
import os

starting = False
sound_loc = "button.wav"
wrong_loc = "wrong.wav"
sound = False
music = False
c_button = None
started = False
scale = 150
score = 0
start_time = None
elapsed_time = None
cube_mode = False
old_width = 500
old_height = 250
ctk.set_appearance_mode("Dark")

scaling = False



def main():
    global scaling
    global sound
    def check_value(setting,default):
        with open("save.json","r") as f:
            settings = json.load(f)
            a = settings.get("settings",{}).get(setting,default)
        return a
    scaling = check_value(setting="scaling",default=False)
    sound = check_value(setting="sound",default=True)
    
    window = ctk.CTk()
    window.geometry("500x250")
    window.title("Happy Button")
    window.minsize(500,250)
    frame = ctk.CTkFrame(window,width=450,height=200)
    frame.place(relx=0.5,rely=0.5,anchor=ctk.CENTER)        
        
    def create_save():
        if os.path.isfile("save.json"):
            return False
        else:
            with open("save.json","w") as f:
                f.write('{\n    "score": 0\n}')
    def get_save():
        create_save()
        with open("save.json","r") as f:
            save = json.load(f)
        a = save.get("score",0)
        return a
    def save():
        create_save()
        with open("save.json","r") as f:
            save = json.load(f)
        old_score = save.get("score",0)
        if old_score < score:
            save["score"] = score
            with open("save.json","w") as f:
                json.dump(save,f)

    def change_setting(setting,mode):
        with open("save.json","r") as f:
            settings = json.load(f)
        if "settings" not in settings:
            settings["settings"] = {}
        if settings == "scaling":
            global scaling
            scaling = mode
        settings["settings"][setting] = mode
        with open("save.json","w") as f:
            json.dump(settings,f)
            
    def red_button():
        global start_time
        global starting
        if starting == True:
            start_time = time.time()
            clock()
            starting = False
        global recent_button
        global score
        recent_button = "red"
        if started == False:
            return
        if recent_button == c_button:
            start_time += 0.2
            score += 1
            if sound == True:
                playsound(sound_loc,False)
            score_label.configure(text=f"{score}/{get_save()}")
            random_button()
        else:
            start_time -= 1
            if sound == True:
                playsound(wrong_loc,False)
            return
        
    def yellow_button():
        global starting
        global start_time
        if starting == True:
            start_time = time.time()
            clock()
            starting = False
        global score
        global recent_button
       
        if started == False:
            return
        recent_button = "yellow"
        if recent_button == c_button:
            start_time += 0.2
            if sound == True:
                playsound(sound_loc,False)
            score += 1
            score_label.configure(text=f"{score}/{get_save()}")
            random_button()
        else:
            if sound == True:
                playsound(wrong_loc,False)
            start_time -= 1
            return
    def blue_button():
        global starting
        global start_time
        if starting == True:
            start_time = time.time()
            clock()
            starting = False
        global score
        global recent_button
        recent_button = "blue"
        if started == False:
            return
        if recent_button == c_button:
            
            start_time += 0.2
            if sound == True:
                playsound(sound_loc,False)
            score += 1
            score_label.configure(text=f"{score}/{get_save()}")
            random_button()
        else:
            if sound == True:
                playsound(wrong_loc,False)
            start_time -= 1
            return
    def green_button():
        
        global starting
        global start_time
        if starting == True:
            start_time = time.time()
            clock()
            starting = False
        global score
        global recent_button
        
        if started == False:
            return
        recent_button = "green"
        if recent_button == c_button:
            if sound == True:
                playsound(sound_loc,False)
            start_time += 0.2
            score += 1
            score_label.configure(text=f"{score}/{get_save()}")
            random_button()
        else:
            if sound == True:
                playsound(wrong_loc,False)
            start_time -= 1
            return
    def restore():
        button1.configure(fg_color="#1c1c1c",hover_color="#1c1c1c")
        time.sleep(0.01)
        button2.configure(fg_color="#1c1c1c",hover_color="#1c1c1c")
        time.sleep(0.01)
        button3.configure(fg_color="#1c1c1c",hover_color="#1c1c1c")
        time.sleep(0.01)
        button4.configure(fg_color="#1c1c1c",hover_color="#1c1c1c")
        time.sleep(0.01)
        
    def random_button():
        global c_button
        buttonnum = random.choice(["red","yellow","blue","green"])
        if buttonnum == c_button:
            random_button()
            return
        restore()
        if buttonnum == "red":
            button1.configure(fg_color="#FFFFFF",hover_color="#FFFFFF")
        elif buttonnum == "yellow":
            button2.configure(fg_color="#FFFFFF",hover_color="#FFFFFF")
        elif buttonnum == "blue":
            button3.configure(fg_color="#FFFFFF",hover_color="#FFFFFF")
        elif buttonnum == "green":
            button4.configure(fg_color="#FFFFFF",hover_color="#FFFFFF")
        else:
            print(buttonnum)
        c_button = buttonnum
    def resize(n):
        global old_height
        global old_width
        
        __width__ = window.winfo_width()
        __height__ = window.winfo_height()
        if __width__ == old_width or __height__ == old_height:
            pass
        else:
            if scaling == True:
                    old_width = __width__
                    old_height = __height__
                    button_font = (__height__-50)*0.1
                    __x__ = (__width__-50)*0.22
                    f_w = __width__-50
                    f_h = __height__-50
                    rad = round(__x__ *0.5)
                    print(button_font)
                    start.configure(width=(__width__-50)*0.2,height=(__height__-50)*0.05,font=("Helvetica",button_font))
                    button1.configure(width=__x__,height=__x__,corner_radius=rad)
                    button2.configure(width=__x__,height=__x__,corner_radius=rad)
                    button3.configure(width=__x__,height=__x__,corner_radius=rad)
                    button4.configure(width=__x__,height=__x__,corner_radius=rad)
                    time_.configure(font=("Helvetica",button_font))
                    score_label.configure(font=("Helvetica",button_font))
                    settings_.configure(width=(__width__-50)*0.2,height=(__height__-50)*0.05,font=("Helvetica",button_font))


                
                    frame.configure(width=__width__-50,height=__height__-50)   
                    
    def setting():
        window.destroy()
        root = ctk.CTk()
        root.geometry("500x500")
        frame_ = ctk.CTkFrame(root,width=450,height=450)
        frame_.place(relx=0.5,rely=0.5,anchor=ctk.CENTER)
        with open("save.json","r") as f:
            settings = json.load(f)
        def sca( ):
            mode_ = scaling_option.get()
            scaling_option_change = change_setting(setting="scaling",mode=mode_)
        def sou():
            mode_ = switch.get()
            sound_option_change = change_setting(setting="sound",mode=mode_)
            
        scaling_option = ctk.CTkSwitch(frame_,onvalue=True,offvalue=False,text="",switch_width=50,switch_height=25,command=sca)
        scaling_option.place(relx=0.2,rely=0.2,anchor=ctk.CENTER)
        scaling_label = ctk.CTkLabel(frame_,text="Dynamic Scaling",font=("Helvetica",18))
        scaling_label.place(relx=0.37,rely=0.2,anchor=ctk.CENTER)
        
        switch = ctk.CTkSwitch(master=frame_, onvalue=True, offvalue=False,font=("Helvetica",16),text="",switch_width=50,switch_height=25,command=sou)
        switch.place(relx=0.09,rely=0.3)
        switch_label = ctk.CTkLabel(frame_,text="SFX",font=("Helvetica",18))
        switch_label.place(relx=0.23,rely=0.3)
    
        sc = settings.get("settings",{}).get("scaling",False)
        so = settings.get("settings",{}).get("sound",True)
        if sc == True:
            scaling_option.select()
        if so == True:
            switch.select()
        def quit__():
            root.destroy()
            main()
        root.protocol("WM_DELETE_WINDOW", quit__)
        root.mainloop()
        
    #1 = Red, 2 = Yellow, 3 = Blue, 4 = Green
    window.bind("<Configure>",resize)
    button1 = ctk.CTkButton(frame,width=100,height=100,text="",corner_radius=50,fg_color="#1c1c1c",hover_color="#1c1c1c",command=red_button)
    button1.place(relx=0.13,rely=0.5,anchor=ctk.CENTER)

    button2 = ctk.CTkButton(frame,width=100,height=100,text="",corner_radius=50,fg_color="#1c1c1c",hover_color="#1c1c1c",command=yellow_button)
    button2.place(relx=0.38,rely=0.5,anchor=ctk.CENTER)

    button3 = ctk.CTkButton(frame,width=100,height=100,text="",corner_radius=50,fg_color="#1c1c1c",hover_color="#1c1c1c",command=blue_button)
    button3.place(relx=0.63,rely=0.5,anchor=ctk.CENTER)
   
    settings_ = ctk.CTkButton(frame,width=100,height=25,text="Settings",font=("Helvetica",18.75),command=setting)
    settings_.place(relx=0.5,rely=0.9,anchor=ctk.CENTER)
    
    button4 = ctk.CTkButton(frame,width=100,height=100,text="",corner_radius=50,fg_color="#1c1c1c",hover_color="#1c1c1c",command=green_button)
    button4.place(relx=0.87,rely=0.5,anchor=ctk.CENTER)

    time_ = ctk.CTkLabel(frame,text="Time",font=("Helvetica",20))
    time_.place(rely=0.9,relx=0.09,anchor=ctk.CENTER)
    
    score_label = ctk.CTkLabel(frame,text=f"{score}/{get_save()}",font=("Helvetica",20))
    score_label.place(relx=0.03,rely=0.03)

    

    window.bind("1",lambda event: red_button())
    window.bind("2",lambda event: yellow_button())
    window.bind("3",lambda event: blue_button())
    window.bind("4",lambda event: green_button())
    
    window.bind("<Left>",lambda event: red_button())
    window.bind("<Down>",lambda event: yellow_button())
    window.bind("<Up>",lambda event: blue_button())
    window.bind("<Right>",lambda event: green_button())
    def start_():
        global started
        global starting
        global score
        score = 0
        score_label.configure(text=f"{score}/{get_save()}")
        started = True
        start.place(relx=12,rely=12)
        settings_.place(relx=12,rely=12)
        random_button()
        
        starting = True
        
    start = ctk.CTkButton(frame,width=100,height=25,text="Start",command=start_,font=("Helvetica",18.75))
    start.place(rely=0.1,relx=0.5,anchor=ctk.CENTER)
            
    def clock():
        global start_time
        global elapsed_time
        global score
        global started
        limit = 15
        
        elapsed_time = time.time() - start_time - limit
        if elapsed_time >= 0:
            started = False
            start_time = None
            
            start.place(rely=0.1,relx=0.5,anchor=ctk.CENTER)
            settings_.place(relx=0.5,rely=0.9,anchor=ctk.CENTER)
            start.configure(text="Retry")
            save()
            button1.configure(fg_color="#1c1c1c",hover_color="#1c1c1c")
            button2.configure(fg_color="#1c1c1c",hover_color="#1c1c1c")
            button3.configure(fg_color="#1c1c1c",hover_color="#1c1c1c")
            button4.configure(fg_color="#1c1c1c",hover_color="#1c1c1c")
            score_label.configure(text=f"{score}/{get_save()}")
            return
        _time = int(elapsed_time*-1)
        time_.configure(text=(_time))
        window.after(25,clock)
    def open_settings(n):
        setting()
    window.bind("<Escape>",open_settings)
    window.mainloop()
    
    
main()