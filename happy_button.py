import customtkinter as ctk
import random
import time
from playsound import playsound
import json
import requests
import os
import webbrowser

version = 1.2
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



def create_save():
    if os.path.isfile("save.json"):
        return False
    else:
        with open("save.json","w") as f:
            f.write('{\n    "score": 0\n}')


create_save()
def main():
    
    create_save()
    global scaling
    global sound
    global theme
    def check_value(setting,default,special=None):
        with open("save.json","r") as f:
            settings = json.load(f)
            a = settings.get("settings",{}).get(setting,default)
        return a
    with open("save.json","r") as f:
        settings = json.load(f)
    theme = settings.get("settings",{}).get("theme","default").lower()

    scaling = check_value(setting="scaling",default=False)
    sound = check_value(setting="sound",default=True)
    window = ctk.CTk()
    window.geometry("500x250")
    window.title("Happy Button")
    window.minsize(500,250)
    frame = ctk.CTkFrame(window,width=450,height=200)
    frame.place(relx=0.5,rely=0.5,anchor=ctk.CENTER)        
    def get_check():
        with open("save.json","r") as f:
            settings = json.load(f)

        cheforupd = settings.get("settings",{}).get("check",True)
        if cheforupd != True:
            return
        try:
            response = requests.get("https://api.github.com/repos/ctih1/Happy-Button/releases/latest")
            a = response.json()["name"]
            b = a.rsplit(" ",1)
            print("access")
            if float(b[1]) > version:
                download.place(relx=0.8,rely=0.1,anchor=ctk.CENTER)
                #webbrowser.open('github.com/ctih1/Happy-Button/releases/latest', new=2)
            else:
                print("Nothing")
        except:
            print("ratelimited")  
    def download_():
        webbrowser.open('github.com/ctih1/Happy-Button/releases/latest', new=2)
    download = ctk.CTkButton(frame,text="Updates Available",font=("Helvetica",12),width=90,height=10.0,command=download_)
    
    get_check()

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
                
    def create_settings():
        with open("save.json","r") as f:
            settings = json.load(f)
        settings_ = settings.get("settings",None)
        if settings_ == None:
            settings["settings"] = {}
        with open("save.json","w") as f:
            json.dump(settings,f)
    def change_setting(setting,mode):
        with open("save.json","r") as f:
            settings = json.load(f)
        if "settings" not in settings:
            settings["settings"] = {}
        if settings == "scaling":
            global scaling
            scaling = mode
        settings["settings"][setting] = mode
        if "custom_theme" not in settings["settings"]:
            settings["settings"]["custom_theme"] = {}
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
    def get_theme(color):
        if theme == "green":
            return "#61B62F"
        if theme == "default":
            return "#ffffff"
        if theme == "custom":
            with open("save.json","r") as f:
                settings = json.load(f)
            a = settings ["settings"]["custom_theme"]["button_color"]
            return a
    def restore():
        if theme == "default":
            button1.configure(fg_color="#1c1c1c",hover_color="#1c1c1c")
            button2.configure(fg_color="#1c1c1c",hover_color="#1c1c1c")
            button3.configure(fg_color="#1c1c1c",hover_color="#1c1c1c")
            button4.configure(fg_color="#1c1c1c",hover_color="#1c1c1c")
        elif theme == "green":
            button1.configure(fg_color="#254B0F",hover_color="#254B0F")
            button2.configure(fg_color="#254B0F",hover_color="#254B0F")
            button3.configure(fg_color="#254B0F",hover_color="#254B0F")
            button4.configure(fg_color="#254B0F",hover_color="#254B0F")
            frame.configure(fg_color="#142C06")
            window.configure(fg_color="#0E1F04")
            start.configure(fg_color="#4BA516")
            settings_.configure(fg_color="#4BA516")
        elif theme == "custom":
            with open("save.json","r") as f:
                settings = json.load(f)
            
            a = settings["settings"]["custom_theme"]["hover"]
            b = settings["settings"]["custom_theme"]["frame_bg"]
            c = settings["settings"]["custom_theme"]["main_bg"]
            d = settings["settings"]["custom_theme"]["button_color"]
            button1.configure(fg_color=a,hover_color=a)
            button2.configure(fg_color=a,hover_color=a)
            button3.configure(fg_color=a,hover_color=a)
            button4.configure(fg_color=a,hover_color=a)
            frame.configure(fg_color=b)
            window.configure(fg_color=c)
            start.configure(fg_color=d,hover_color=a)
            settings_.configure(fg_color=d,hover_color=a)
    def random_button():
        global c_button
        buttonnum = random.choice(["red","yellow","blue","green"])
        if buttonnum == c_button:
            random_button()
            return
        restore()
        if buttonnum == "red":
            button1.configure(fg_color=get_theme(color="red"),hover_color=get_theme(color="red"))
        elif buttonnum == "yellow":
            button2.configure(fg_color=get_theme(color="yellow"),hover_color=get_theme(color="yellow"))
        elif buttonnum == "blue":
            button3.configure(fg_color=get_theme(color="blue"),hover_color=get_theme(color="blue"))
        elif buttonnum == "green":
            button4.configure(fg_color=get_theme(color="green"),hover_color=get_theme(color="green"))
            
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
                    start.configure(width=(__width__-50)*0.2,height=(__height__-50)*0.05,font=("Helvetica",button_font))
                    button1.configure(width=__x__,height=__x__,corner_radius=rad)
                    button2.configure(width=__x__,height=__x__,corner_radius=rad)
                    button3.configure(width=__x__,height=__x__,corner_radius=rad)
                    button4.configure(width=__x__,height=__x__,corner_radius=rad)
                    time_.configure(font=("Helvetica",button_font))
                    score_label.configure(font=("Helvetica",button_font))
                    settings_.configure(width=(__width__-50)*0.2,height=(__height__-50)*0.05,font=("Helvetica",button_font))
                    download.configure(width=(__width__-50)*0.2,height=(__height__-50)*0.05,font=("Helvetica",button_font*0.6))
                    print(f"width={(__width__-50)*0.2},height={(__height__-50)*0.05}")

                
                    frame.configure(width=__width__-50,height=__height__-50)   
                    
    def setting():
        
        create_settings()
        window.destroy()
        root = ctk.CTk()
        root.title("Settings")
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
        
        def che():
            mode_ = check_for_updates_switch.get()
            check_for_updates_change = change_setting(setting="check",mode=mode_)
            cfu = mode_
            if mode_ == False:
                check_for_updates_.place(relx=0.5,rely=0.08,anchor=ctk.CENTER)
            else:
                check_for_updates_.place(relx=12,rely=0.08,anchor=ctk.CENTER)
        
        scaling_option = ctk.CTkSwitch(frame_,onvalue=True,offvalue=False,text="",switch_width=50,switch_height=25,width=50,height=25,command=sca)
        scaling_option.place(relx=0.2,rely=0.2,anchor=ctk.CENTER)
        
        scaling_label = ctk.CTkLabel(frame_,text="Dynamic Scaling",font=("Helvetica",18))
        scaling_label.place(relx=0.41,rely=0.2,anchor=ctk.CENTER)
        
        switch = ctk.CTkSwitch(master=frame_, onvalue=True, offvalue=False,text="",switch_width=50,switch_height=25,width=50,height=25,command=sou)
        switch.place(relx=0.2,rely=0.3,anchor=ctk.CENTER)
        
        switch_label = ctk.CTkLabel(frame_,text="SFX",font=("Helvetica",18))
        switch_label.place(relx=0.3,rely=0.3,anchor=ctk.CENTER)
    
        check_for_updates_switch = ctk.CTkSwitch(frame_,text="",onvalue=True,offvalue=False,switch_width=50,switch_height=25,command=che,width=50,height=25)
        check_for_updates_switch.place(relx=0.2,rely=0.4,anchor=ctk.CENTER)
        
        check_for_updates_label = ctk.CTkLabel(frame_,text="Automatically check for updates",font=("Helvetica",18))
        check_for_updates_label.place(relx=0.55,rely=0.4,anchor=ctk.CENTER)
    
        warn = ctk.CTkLabel(frame_,text="",text_color="#cc3300",font=("Helvetica",24))
        warn.place(relx=0.5,rely=0.1,anchor=ctk.CENTER)
    
        sc = settings.get("settings",{}).get("scaling",False)
        so = settings.get("settings",{}).get("sound",True)
        cfu = settings.get("settings",{}).get("check",True)
        
        def check_is_string(hover,frame,main,button): #CREDITS; https://www.geeksforgeeks.org/check-if-a-given-string-is-a-valid-hexadecimal-color-code-or-not/
            if hover[0] != "#":
                return "hover"
            if frame[0] != "#":
                return "frame"
            if main[0] != "#":
                return "main"
            if button[0] != "#":
                return "button"
            if (not(len(hover) == 4 or len(hover) == 7)):
                return "hover"
            if (not(len(frame) == 4 or len(frame) == 7)):
                return "frame"
            if (not(len(main) == 4 or len(main) == 7)):
                return "main"
            if (not(len(button) == 4 or len(button) == 7)):
                return "button"
            for i in range(1, len(hover)):
                if (not((hover[i] >= '0' and hover[i] <= '9') or (hover[i] >= 'a' and hover[i] <= 'f') or (hover[i] >= 'A' or hover[i] <= 'F'))):
                    return "hover"
            for i in range(1, len(frame)):
                if (not((frame[i] >= '0' and frame[i] <= '9') or (frame[i] >= 'a' and frame[i] <= 'f') or (frame[i] >= 'A' or frame[i] <= 'F'))):
                    return "frame"
            for i in range(1, len(main)):
                if (not((main[i] >= '0' and main[i] <= '9') or (main[i] >= 'a' and main[i] <= 'f') or (main[i] >= 'A' or main[i] <= 'F'))):
                    return "main"
            for i in range(1, len(button)):
                if (not((button[i] >= '0' and button[i] <= '9') or (button[i] >= 'a' and button[i] <= 'f') or (button[i] >= 'A' or button[i] <= 'F'))):
                    return "button"
            return True
        def save_custom():
            with open("save.json","r") as f:
                settings = json.load(f)

            if "custom_theme" not in settings["settings"]:
                settings["settings"]["custom_theme"] = {}

            settings["settings"]["custom_theme"]["hover"] = str(hover.get())
            settings["settings"]["custom_theme"]["frame_bg"] = str(frame_bg.get())
            settings["settings"]["custom_theme"]["main_bg"] = str(main_bg.get())
            settings["settings"]["custom_theme"]["button_color"] = str(button_color.get())
            a = check_is_string(hover=str(hover.get()),frame=str(frame_bg.get()),main=str(main_bg.get()),button=str(button_color.get()))
            if a != True:
                warn.configure(text=f"Invalid hex on {a}")
                return
            if theme_.get() == "Custom":
                if len(hover.get()) > 1 and len(frame_bg.get()) > 1 and len(main_bg.get()) > 1 and len(button_color.get()) > 1:
                    settings["settings"]["theme"] = "Custom"
                    with open("save.json","w") as f:
                        json.dump(settings,f)
            with open("save.json","w") as f:
                json.dump(settings,f)
                
        with open("save.json","r") as f:
            settings = json.load(f)
        def check_for_updates(mode):
            with open("save.json","r") as f:
                settings = json.load(f)
            if mode == "automatic":
                cheforupd = settings.get("settings",{}).get("check",True)
                if cheforupd != True:
                    return
            try:
                check_for_updates_.configure(state="disabled",text="Checking")
                response = requests.get("https://api.github.com/repos/ctih1/Happy-Button/releases/latest")
                a = response.json()["name"]
                b = a.rsplit(" ",1)
                
                if float(b[1]) > version:
                    check_for_updates_.configure(state="normal",text="Updates available.")
                    webbrowser.open('github.com/ctih1/Happy-Button/releases/latest', new=2)
                else:
                    check_for_updates_.configure(state="disabled",text="No Updates available.")
            except:
                print("ratelimited")
            
        hover_ = settings.get("settings",{}).get("custom_theme",{}).get("hover","")
        frame_bg_ = settings.get("settings",{}).get("custom_theme",{}).get("frame_bg","")
        main_bg_ = settings.get("settings",{}).get("custom_theme",{}).get("main_bg","")
        button_color_ = settings.get("settings",{}).get("custom_theme",{}).get("button_color","")
        hover = ctk.CTkEntry(frame_,placeholder_text="Color for Inactive")
        frame_bg = ctk.CTkEntry(frame_,placeholder_text="Color for Frame")
        main_bg = ctk.CTkEntry(frame_,placeholder_text="Color for Background")
        button_color = ctk.CTkEntry(frame_,placeholder_text="Color For Button")
        hover.insert(0,hover_)
        frame_bg.insert(0,frame_bg_)
        main_bg.insert(0,main_bg_)
        button_color.insert(0,button_color_)
        def check_manual():
            mode = "manual"
            check_for_updates(mode=mode)
        save = ctk.CTkButton(frame_,text="Apply",command=save_custom)
        check_for_updates_ = ctk.CTkButton(frame_,text="Check For Updates",command=check_manual)

        if theme == "custom":
            hover.place(relx=0.3,rely=0.7,anchor=ctk.CENTER)
            frame_bg.place(relx=0.7,rely=0.7,anchor=ctk.CENTER)
            main_bg.place(relx=0.3,rely=0.8,anchor=ctk.CENTER)
            button_color.place(relx=0.7,rely=0.8,anchor=ctk.CENTER)
            save.place(relx=0.5,rely=0.9,anchor=ctk.CENTER)
        def change_theme(choice):
            if choice == "Custom":
                hover.place(relx=0.3,rely=0.7,anchor=ctk.CENTER)
                frame_bg.place(relx=0.7,rely=0.7,anchor=ctk.CENTER)
                main_bg.place(relx=0.3,rely=0.8,anchor=ctk.CENTER)
                button_color.place(relx=0.7,rely=0.8,anchor=ctk.CENTER)
                save.place(relx=0.5,rely=0.9,anchor=ctk.CENTER)
            else:
                hover.place(relx=12)
                frame_bg.place(relx=12)
                main_bg.place(relx=12)
                button_color.place(relx=12)
            with open("save.json","r") as f:
                settings = json.load(f)
            if choice == "Custom":
                if len(hover.get()) > 1 and len(frame_bg.get()) > 1 and len(main_bg.get()) > 1 and len(button_color.get()) > 1:
                    settings["settings"]["theme"] = choice
                    with open("save.json","w") as f:
                        json.dump(settings,f)
                else:
                    return
            settings["settings"]["theme"] = choice
            with open("save.json","w") as f:
                json.dump(settings,f)
        theme_ = ctk.CTkOptionMenu(frame_,values=["Default","Green","Custom"],command=change_theme)
        theme_.place(relx=0.5,rely=0.5,anchor=ctk.CENTER)
        a = settings.get("settings",{}).get("theme","Default")
        theme_.set(a)
        if sc == True:
            scaling_option.select()
        if cfu == True:
            check_for_updates_switch.select()
        else:
            check_for_updates_.place(relx=0.5,rely=0.08,anchor=ctk.CENTER)
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
            restore()
            score_label.configure(text=f"{score}/{get_save()}")
            return
        _time = int(elapsed_time*-1)
        time_.configure(text=(_time))
        window.after(100,clock)
    def open_settings(n):
        setting()
    window.bind("<Escape>",open_settings)
    
    restore()
    create_settings()
    window.mainloop()
    
    
main()
