

import random
import time
import json
import requests
import os
import webbrowser
from pygame import mixer
import numpy
version = 1.7
playing_music = False
starting = False
sound_loc = "button.wav"
wrong_loc = "wrong.wav"
song_loc = "song.mp3"
sound = False
music = False
c_button = None
started = False
average_time = []
correct_list = []
reaction_click = None
reaction_start = None
p = None
scale = 150
score = 0
start_time = None
elapsed_time = None
cube_mode = False
old_width = 500
old_height = 250


scaling = False

mixer.init()






def main():


        #print(correct_list)



        correct_list = []
        average_time = []
        reaction_click = None
        reaction_start = None
        
        



    scaling = check_value(setting="scaling",default=False)
    sound = check_value(setting="sound",default=True)

    # ABANDONED if theme == "custom":
    #    with open("save.json","r") as f:
    #        settings = json.load(f)
    #    opac = settings.get("settings",{}).get("custom_theme",{}).get("opacity",1)
    #    window.attributes("-a",float(opac)) # I guess it changes the window to a certain opacity, not sure if it works :)
        
    def get_check():
        with open("save.json","r") as f:
            settings = json.load(f)

        cheforupd = settings.get("settings",{}).get("check",True)
        if cheforupd != True:
            return
        try:
            response = requests.get("https://api.github.com/repos/ctih1/Happy-Button/releases/latest") # Shitty api request
            a = response.json()["name"]
            b = a.rsplit(" ",1)
            if float(b[1]) > version:
                download.place(relx=0.8,rely=0.1,anchor=ctk.CENTER)
            else:
                print("Nothing")
        except:
            print("ratelimited") # Shit
    def download_():
        webbrowser.open('github.com/ctih1/Happy-Button/releases/latest', new=2) # idc that it opens Edge instead of the default browser, could not be bothered to fix it.
    download = ctk.CTkButton(frame,text="Updates Available",font=("Helvetica",12),width=90,height=10.0,command=download_)

    def resize(n):
        global old_height
        global old_width # 589375th Global Variable
        
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
    def custom_theme():
        try:
            mixer.music.pause()
        except:
            pass
        root = ctk.CTk()
        root.title("Settings")
        root.geometry("500x500") # Another window, yay
        frame_ = ctk.CTkFrame(root,width=450,height=450)
        frame_.place(relx=0.5,rely=0.5,anchor=ctk.CENTER)
        with open("save.json","r") as f:
            settings = json.load(f)

        def check_is_string(hover,frame,main,button): #*adapted* from https://www.geeksforgeeks.org/check-if-a-given-string-is-a-valid-hexadecimal-color-code-or-not/
            if hover[0] != "#": # Dont know what it does.
                return "hover"
            if frame[0] != "#": # Dont know what it does.
                return "frame" 
            if main[0] != "#": # Dont know what it does.
                return "main"
            if button[0] != "#": # Dont know what it does.
                return "button"
            if (not(len(hover) == 4 or len(hover) == 7)): # Dont know what it does.
                return "hover"
            if (not(len(frame) == 4 or len(frame) == 7)): # Dont know what it does.
                return "frame"
            if (not(len(main) == 4 or len(main) == 7)): # Dont know what it does.
                return "main"
            if (not(len(button) == 4 or len(button) == 7)): # Dont know what it does.
                return "button"
            for i in range(1, len(hover)):
                if (not((hover[i] >= '0' and hover[i] <= '9') or (hover[i] >= 'a' and hover[i] <= 'f') or (hover[i] >= 'A' or hover[i] <= 'F'))): # Dont know what it does.
                    return "hover"
            for i in range(1, len(frame)):
                if (not((frame[i] >= '0' and frame[i] <= '9') or (frame[i] >= 'a' and frame[i] <= 'f') or (frame[i] >= 'A' or frame[i] <= 'F'))): # Dont know what it does.
                    return "frame"
            for i in range(1, len(main)):
                if (not((main[i] >= '0' and main[i] <= '9') or (main[i] >= 'a' and main[i] <= 'f') or (main[i] >= 'A' or main[i] <= 'F'))): # Dont know what it does.
                    return "main"
            for i in range(1, len(button)):
                if (not((button[i] >= '0' and button[i] <= '9') or (button[i] >= 'a' and button[i] <= 'f') or (button[i] >= 'A' or button[i] <= 'F'))): # Dont know what it does.
                    return "button"
            return True # Dont know what it does.
        def save_custom(): # I don't understand what I did in this. Only the giant rat in the sky knows.
            if "custom_theme" not in settings["settings"]:
                settings["settings"]["custom_theme"] = {}

            settings["settings"]["custom_theme"]["hover"] = str(hover.get())
            settings["settings"]["custom_theme"]["frame_bg"] = str(frame_bg.get())
            settings["settings"]["custom_theme"]["main_bg"] = str(main_bg.get())
            settings["settings"]["custom_theme"]["button_color"] = str(button_color.get())
            settings["settings"]["custom_theme"]["opacity"] = str(opacity_slider.get())
            a = check_is_string(hover=str(hover.get()),frame=str(frame_bg.get()),main=str(main_bg.get()),button=str(button_color.get()))
            if a != True:
                warn.configure(text=f"Invalid hex on {a}")
                return
            if theme_.get() == "Custom":
                if len(hover.get()) > 1 and len(frame_bg.get()) > 1 and len(main_bg.get()) > 1 and len(button_color.get()) > 1:
                    settings["settings"]["theme"] = "Custom"
                    with open("save.json","w") as f:
                        json.dump(settings,f)
            settings["settings"]["theme"] = theme_.get()
            with open("save.json","w") as f:
                json.dump(settings,f)
                
        def check_for_updates(mode):
            if mode == "automatic":
                cheforupd = settings.get("settings",{}).get("check",True) # A better name could have been nice.
                if cheforupd != True:
                    return
            try:
                check_for_updates_.configure(state="disabled",text="Checking")
                response = requests.get("https://api.github.com/repos/ctih1/Happy-Button/releases/latest") # Didn't we already do this?
                a = response.json()["name"]
                b = a.rsplit(" ",1)
                
                if float(b[1]) > version:
                    check_for_updates_.configure(state="normal",text="Updates available.")
                    webbrowser.open('github.com/ctih1/Happy-Button/releases/latest', new=2)  # "Didn't we already do this?" - Yes. I don't know why it isnt a function.
                else:
                    check_for_updates_.configure(state="disabled",text="No Updates available.")
            except:
                print("ratelimited")
            
        hover_ = settings.get("settings",{}).get("custom_theme",{}).get("hover",None)
        frame_bg_ = settings.get("settings",{}).get("custom_theme",{}).get("frame_bg",None)
        main_bg_ = settings.get("settings",{}).get("custom_theme",{}).get("main_bg",None)
        button_color_ = settings.get("settings",{}).get("custom_theme",{}).get("button_color",None)
        warn = ctk.CTkLabel(frame_,text="",text_color="#cc3300",font=("Helvetica",24))
        warn.place(relx=0.5,rely=0.1,anchor=ctk.CENTER)
        hover = ctk.CTkEntry(frame_,placeholder_text="Color for Inactive")
        frame_bg = ctk.CTkEntry(frame_,placeholder_text="Color for Frame")
        main_bg = ctk.CTkEntry(frame_,placeholder_text="Color for Background")
        button_color = ctk.CTkEntry(frame_,placeholder_text="Color For Button")
        
        def slider(value):
            root.attributes("-a",value)
            settings["settings"]["custom_theme"]["opacity"] = value
            with open("save.json","w") as f:
                json.dump(settings,f)     
        button_1 = ctk.CTkButton(frame_,width=100,height=100,text="",corner_radius=120) # I ain't explaining allat
        button_1.place(relx=0.13,rely=0.3,anchor=ctk.CENTER)
        button_2 = ctk.CTkButton(frame_,width=100,height=100,text="",corner_radius=120)
        button_2.place(relx=0.38,rely=0.3,anchor=ctk.CENTER)
        button_3 = ctk.CTkButton(frame_,width=100,height=100,text="",corner_radius=120)
        button_3.place(relx=0.63,rely=0.3,anchor=ctk.CENTER)
        button_4 = ctk.CTkButton(frame_,width=100,height=100,text="",corner_radius=120)
        button_4.place(relx=0.87,rely=0.3,anchor=ctk.CENTER)
        opacity_label = ctk.CTkLabel(frame_,text="Opacity",font=("Helvetica",12))
        opacity_slider = ctk.CTkSlider(frame_,from_=0.1, to=1,command=slider)
        opacity_value = settings.get("settings",{}).get("custom_theme",{}).get("opacity",1)
        opacity_slider.set(float(opacity_value))
        
        
        def update_():
            theme__ = theme_.get()
            
            hover_ = hover.get()
            frame_bg_ = frame_bg.get()
            main_bg_ = main_bg.get()
            button_color_ = button_color.get()
            if theme__ == "Custom":
                try:
                    button_1.configure(fg_color=hover_,hover_color=hover_)
                except Exception as e:
                    pass
                try:
                    button_2.configure(fg_color=hover_,hover_color=hover_)
                except Exception as e:
                    pass
                try:
                    button_3.configure(fg_color=button_color_,hover_color=button_color_)
                except Exception as e:
                    pass
                try:
                    button_4.configure(fg_color=hover_,hover_color=hover_)
                except Exception as e:
                    pass
                try:
                    frame_.configure(fg_color=frame_bg_)
                except Exception as e:
                    pass
                try:
                    root.configure(fg_color=main_bg_)
                except Exception as e:
                    pass
        
            window.after(250,update_) # Ran out of comments.
        if not all([hover_,frame_bg_,main_bg_,button_color_]): # Something with lists and trying not to make it crash. 
            pass
        else:
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
            opacity_label.place(relx=0.5,rely=0.05,anchor=ctk.CENTER)
            hover.place(relx=0.3,rely=0.7,anchor=ctk.CENTER)
            root.attributes("-a",float(opacity_value))
            frame_bg.place(relx=0.7,rely=0.7,anchor=ctk.CENTER)
            main_bg.place(relx=0.3,rely=0.8,anchor=ctk.CENTER)
            button_color.place(relx=0.7,rely=0.8,anchor=ctk.CENTER)
            save.place(relx=0.5,rely=0.9,anchor=ctk.CENTER)
            opacity_slider.place(relx=0.5,rely=0.1,anchor=ctk.CENTER)
        def change_theme(choice):
            settings["settings"]["theme"] = choice
            with open("save.json","w") as f:
                json.dump(settings,f)
            print(choice)
            if choice == "Custom":
                opacity_label.place(relx=0.5,rely=0.05,anchor=ctk.CENTER)
                root.attributes("-a",float(opacity_value))
                opacity_slider.place(relx=0.5,rely=0.1,anchor=ctk.CENTER)
                hover.place(relx=0.3,rely=0.7,anchor=ctk.CENTER)
                frame_bg.place(relx=0.7,rely=0.7,anchor=ctk.CENTER)
                main_bg.place(relx=0.3,rely=0.8,anchor=ctk.CENTER)
                button_color.place(relx=0.7,rely=0.8,anchor=ctk.CENTER)
                save.place(relx=0.5,rely=0.9,anchor=ctk.CENTER)
            else:
                opacity_label.place(relx=12,rely=12)
                root.attributes("-a",1)
                hover.place(relx=12)
                opacity_slider.place(relx=12,rely=12)
                frame_bg.place(relx=12)
                main_bg.place(relx=12)
                button_color.place(relx=12)
            if choice == "Custom":
                if len(hover.get()) > 1 and len(frame_bg.get()) > 1 and len(main_bg.get()) > 1 and len(button_color.get()) > 1: # I have a headdache.
                    settings["settings"]["theme"] = choice
                    #with open("save.json","w") as f:
                        #json.dump(settings,f)
                else:
                    return

        theme_ = ctk.CTkOptionMenu(frame_,values=["Default","Green","Purple","Red","Blue","Custom"],command=change_theme)
        theme_.place(relx=0.5,rely=0.60,anchor=ctk.CENTER)
        a = settings.get("settings",{}).get("theme","Default")
        version_label = ctk.CTkLabel(frame_,text=f"{version}",font=("Helvetica",12))
        version_label.place(relx=0.05,rely=0.95,anchor=ctk.CENTER)
        theme_.set(a)
        
        

            
        root.after(100,update_)
        root.mainloop()
        
    def change_keybind(): # Why did I do this
        root_ = ctk.CTk()
        root_.geometry("500x500")
        root_.title("Change Keybinds")
        frame__ = ctk.CTkFrame(root_,width=450,height=450)
        frame__.place(relx=0.5,rely=0.5,anchor=ctk.CENTER)
        with open("save.json","r") as f:
            settings = json.load(f)
        
        def deferr():
            save_button.configure(text="Save",state="normal")
        def chje():
            if len(entry1.get()) > 1:
                entry1.delete(0,1)
            if len(entry2.get()) > 1:
                entry2.delete(0,1)
            if len(entry3.get()) > 1:
                entry3.delete(0,1)
            if len(entry4.get()) > 1:
                entry4.delete(0,1)
            window.after(10,chje)
        def _save_():
            create_settings()
            with open("save.json","r") as f:
                settings = json.load(f)
            settings["settings"]["1"] = entry1.get()
            settings["settings"]["2"] = entry2.get()
            settings["settings"]["3"] = entry3.get()
            settings["settings"]["4"] = entry4.get()
            with open("save.json","w") as f:
                json.dump(settings,f)
            save_button.configure(text="Saved!",state="disabled")
            root_.after(2500,deferr)
        _1 = settings.get("settings",{}).get("1","")
        _2 = settings.get("settings",{}).get("2","")
        _3 = settings.get("settings",{}).get("3","")
        _4 = settings.get("settings",{}).get("4","")
        entry1 = ctk.CTkEntry(frame__,placeholder_text="1",width=75,height=75,font=("Helvetica",28))
        entry1.insert(0,_1)
        entry2 = ctk.CTkEntry(frame__,placeholder_text="2",width=75,height=75,font=("Helvetica",28))
        entry2.insert(0,_2)
        entry3 = ctk.CTkEntry(frame__,placeholder_text="3",width=75,height=75,font=("Helvetica",28))
        entry3.insert(0,_3)
        entry4 = ctk.CTkEntry(frame__,placeholder_text="4",width=75,height=75,font=("Helvetica",28))
        entry4.insert(0,_4)
        entry1.place(relx=0.2,rely=0.5,anchor=ctk.CENTER)
        entry2.place(relx=0.4,rely=0.5,anchor=ctk.CENTER)
        entry3.place(relx=0.6,rely=0.5,anchor=ctk.CENTER)
        entry4.place(relx=0.8,rely=0.5,anchor=ctk.CENTER)
        save_button = ctk.CTkButton(frame__,text="Save",command=_save_)
        save_button.place(relx=0.5,rely=0.9,anchor=ctk.CENTER)
        root_.after(10,chje)
        
        with open("save.json","r") as f:
            settings = json.load(f)
        theme = settings.get("settings",{}).get("theme","default").lower() # ""Didn't we already do this?"" - Yes
        if theme == "green":
            button_c="#4BA516"
            frame__.configure(fg_color="#142C06")
            root_.configure(fg_color="#0E1F04")
            entry1.configure(fg_color="#4BA516")
            entry2.configure(fg_color="#4BA516")
            entry3.configure(fg_color="#4BA516")
            entry4.configure(fg_color="#4BA516")
        if theme == "purple":
            button_c = "#1a001a"
            save_button.configure(fg_color=button_c,hover_color=button_c)
            entry1.configure(fg_color=button_c)
            entry2.configure(fg_color=button_c)
            entry3.configure(fg_color=button_c)
            entry4.configure(fg_color=button_c)
            frame__.configure(fg_color="#330033")
            root_.configure(fg_color=button_c)
        if theme == "red":
            button_c = "#1a0000"
            button_c = "#1a001a"
            save_button.configure(fg_color=button_c,hover_color=button_c)
            entry1.configure(fg_color=button_c)
            entry2.configure(fg_color=button_c)
            entry3.configure(fg_color=button_c)
            entry4.configure(fg_color=button_c)
            frame__.configure(fg_color="#330000")
            root_.configure(fg_color=button_c)
        if theme == "blue":
            button_c = "#1a0000"
            save_button.configure(fg_color=button_c,hover_color=button_c)
            entry1.configure(fg_color=button_c)
            entry2.configure(fg_color=button_c)
            entry3.configure(fg_color=button_c)
            entry4.configure(fg_color=button_c)
            frame__.configure(fg_color="#002533")
            root_.configure(fg_color=button_c)
        if theme == "custom":
            button_c = settings.get("settings",{}).get("custom_theme",{}).get("hover","gray18")
            frame_c = settings.get("settings",{}).get("custom_theme",{}).get("frame_bg","gray18")
            entry1.configure(fg_color=button_c)
            entry2.configure(fg_color=button_c)
            entry3.configure(fg_color=button_c)
            entry4.configure(fg_color=button_c)
            save_button.configure(fg_color=button_c,hover_color=button_c)
            frame__.configure(fg_color=frame_c)
            root_.configure(fg_color=button_c)

        root_.mainloop()
        
 
    
        root.protocol("WM_DELETE_WINDOW", quit__)
        root.mainloop()
        
    #1 = Red, 2 = Yellow, 3 = Blue, 4 = Green
    window.bind("<Configure>",resize)
    

   

    window.bind("1",lambda event: red_button())
    window.bind("2",lambda event: yellow_button())
    window.bind("3",lambda event: blue_button())
    window.bind("4",lambda event: green_button())
    
    window.bind("<Left>",lambda event: red_button())
    window.bind("<Down>",lambda event: yellow_button())
    window.bind("<Up>",lambda event: blue_button())
    window.bind("<Right>",lambda event: green_button())
    
    def bind_():
        with open("save.json","r") as f:
            settings = json.load(f)
        _1 = settings.get("settings",{}).get("1",1)
        _2 = settings.get("settings",{}).get("2",2)
        _3 = settings.get("settings",{}).get("3",3)
        _4 = settings.get("settings",{}).get("4",4)
        window.bind(_1,lambda event: red_button())
        window.bind(_2,lambda event: yellow_button())
        window.bind(_3,lambda event: blue_button())
        window.bind(_4,lambda event: green_button())
    bind_()
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
        
    
    start.place(rely=0.1,relx=0.5,anchor=ctk.CENTER)

    def song(mode):
        if mode == "play":
            mixer.Channel(0).play(mixer.Sound(song_loc))
        elif mode == "pause":
            mixer.pause()
        else:
            print(f"{mode}")
    def play():
        global playing_music
        global p
        with open("save.json","r") as f:
            settings = json.load(f)
        music_ = settings.get("settings",{}).get("music",False)
        print(music_)
        if music_ == True:
            song(mode="play")
        elif music_ == False:
            song(mode="pause")
            
            

    def open_settings(n):
        setting()
    window.bind("<Escape>",open_settings)
    
    restore()
    window.after(1,play)
    create_settings()
    window.mainloop()
    
    


    
# Probably could have gotten it to 250 lines if I actually knew what I was doing, I did not.
