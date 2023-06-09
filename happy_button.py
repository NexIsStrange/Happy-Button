# I have no idea what I was thinking when coding this.

import customtkinter as ctk
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
ctk.set_appearance_mode("Dark")

scaling = False

mixer.init()




def create_save():
    if os.path.isfile("save.json"):
        return False
    else:
        with open("save.json","w") as f:
            f.write('{\n    "score": 0\n}')


create_save()
def main():
    def show_results(x,y):
        with open("save.json","r") as f:
            settings = json.load(f)
        theme = settings.get("settings",{}).get("theme","default").lower()
        global correct_list
        global average_time
        global reaction_click
        global reaction_start
     
        def focus_(n):
            thing.destroy()

    
        thing = ctk.CTk()
        thing.geometry(f"225x175+{x}+{y}")
        thing_frame = ctk.CTkFrame(thing,width=225,height=150)
        thing.title("Reaction Time")
        thing_frame.place(relx=0.5,rely=0.5,anchor=ctk.CENTER)
        try:
            min_time_ =  round(min(average_time),4)
        except:
            min_time_ = 0
        
        try:
            percentage = (sum(correct_list) / len(correct_list)) * 100
        except:
            precentage = 0

        #print(correct_list)
        accuracy_out_label = ctk.CTkLabel(thing_frame,text=f"{sum(correct_list)}/{len(correct_list)}\n({round(percentage, 2)}%)",font=("Helvetica",14))
        accuracy_out_label.place(relx=0.5,rely=0.85,anchor=ctk.CENTER)
        try:
            average_time_ = round(numpy.mean(average_time),4)
        except:
            average_time_ = 0
        average_label_label = ctk.CTkLabel(thing_frame,text="Average",font=("Helvetica",14))
        average_label_label.place(relx=0.7,rely=0.15,anchor=ctk.CENTER)
        min_label_label = ctk.CTkLabel(thing_frame,text="Minimum",font=("Helvetica",14))
        min_label_label.place(relx=0.3,rely=0.15,anchor=ctk.CENTER)
        average_label = ctk.CTkButton(thing_frame,text=f"{round(average_time_*1000,4)}\nms",width=75,height=75,font=("Helvetica",14))
        average_label.place(relx=0.7,rely=0.5,anchor=ctk.CENTER)
        min_label = ctk.CTkButton(thing_frame,text=f"{round(min_time_*1000,4)}\nms",width=75,height=75,font=("Helvetica",14))
        min_label.place(relx=0.3,rely=0.5,anchor=ctk.CENTER)


        correct_list = []
        average_time = []
        reaction_click = None
        reaction_start = None

        with open("save.json","r") as f:
            s = json.load(f)
        a = s.get("settings",{}).get("autohide",True)
        if a == True:
            thing.bind("<FocusOut>", focus_)
            
        if theme == "green":
            thing_frame.configure(fg_color="#142C06")
            thing.configure(fg_color="#0E1F04",hover_color="#254B0F")
            average_label.configure(fg_color="#4BA516",hover_color="#4BA516")
            min_label.configure(fg_color="#4BA516",hover_color="#4BA516")
        if theme == "purple":
            min_label.configure(fg_color="#1a001a",hover_color="#1a001a")
            average_label.configure(fg_color="#1a001a",hover_color="#1a001a")
            thing_frame.configure(fg_color="#330033")
            thing.configure(fg_color="#1a001a")
        if theme == "red":
            average_label.configure(fg_color="#1a0000",hover_color="#1a0000")
            min_label.configure(fg_color="#1a0000",hover_color="#1a0000")
            thing_frame.configure(fg_color="#330000")
            thing.configure(fg_color="#1a0000")
        if theme == "blue":
            average_label.configure(fg_color="#00131a",hover_color="#00131a")
            min_label.configure(fg_color="#00131a",hover_color="#00131a")
            thing_frame.configure(fg_color="#002533")
            thing.configure(fg_color="#00131a")
        if theme == "custom":
            button_c = settings.get("settings",{}).get("custom_theme",{}).get("hover","gray18")
            frame_c = settings.get("settings",{}).get("custom_theme",{}).get("frame_bg","gray18")
            average_label.configure(fg_color=button_c,hover_color=button_c)
            min_label.configure(fg_color=button_c,hover_color=button_c)
            thing_frame.configure(fg_color=frame_c)
            thing.configure(fg_color=button_c)
            
        thing.mainloop()
    
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
    if theme == "custom":
        with open("save.json","r") as f:
            settings = json.load(f)
        opac = settings.get("settings",{}).get("custom_theme",{}).get("opacity",1)
        window.attributes("-a",float(opac)) # I guess it changes the window to a certain opacity, not sure if it works :)
    frame = ctk.CTkFrame(window,width=450,height=200)
    frame.place(relx=0.5,rely=0.5,anchor=ctk.CENTER)        
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
        if old_score < score:  # I guess it checks if the old score is more than the score you just got.
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
            correct_list.append(1)
            a = time.time() - reaction_start
            average_time.append(a)
            start_time += 0.2
            score += 1
            if sound == True:
                mixer.Channel(1).play(mixer.Sound(sound_loc))
            score_label.configure(text=f"{score}/{get_save()}")
            random_button()
        else:
            correct_list.append(0)
            start_time -= 1
            if sound == True:
                mixer.Channel(2).play(mixer.Sound(wrong_loc))
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
            correct_list.append(1)
            a = time.time() - reaction_start
            average_time.append(a)
            start_time += 0.2
            if sound == True:
                mixer.Channel(1).play(mixer.Sound(sound_loc))
            score += 1
            score_label.configure(text=f"{score}/{get_save()}")
            random_button()
        else:
            if sound == True:
                mixer.Channel(2).play(mixer.Sound(wrong_loc))
            correct_list.append(0)
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
            correct_list.append(1)
            a = time.time() - reaction_start
            average_time.append(a)
            start_time += 0.2
            if sound == True:
                mixer.Channel(1).play(mixer.Sound(sound_loc))
            score += 1
            score_label.configure(text=f"{score}/{get_save()}")
            random_button()
        else:
            correct_list.append(0)
            if sound == True:
                mixer.Channel(2).play(mixer.Sound(wrong_loc))
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
            correct_list.append(1)
            if reaction_start != None:
                a = time.time() - reaction_start
                average_time.append(a)
            if sound == True:
                mixer.Channel(1).play(mixer.Sound(sound_loc))
            start_time += 0.2
            score += 1
            score_label.configure(text=f"{score}/{get_save()}")
            random_button()
        else:
            correct_list.append(0)
            if sound == True:
                mixer.Channel(2).play(mixer.Sound(wrong_loc))
            start_time -= 1
            return
    def get_theme(color):
        global reaction_start
        reaction_start = time.time()
        if theme == "green":
            return "#61B62F"
        if theme == "default":
            return "#ffffff"
        if theme == "purple":
            return "#ff00ff"
        if theme == "red":
            return "#ff0000"
        if theme == "blue":
            return "#004d99"
        if theme == "custom":
            with open("save.json","r") as f:
                settings = json.load(f)
            a = settings ["settings"]["custom_theme"]["button_color"]
            return a
    def restore(): # damn thats alot of code *sigh*, prob could used a more efficent way, but couldn't care less
        if theme == "default":
            button1.configure(fg_color="#1c1c1c",hover_color="#1c1c1c")
            button2.configure(fg_color="#1c1c1c",hover_color="#1c1c1c")
            button3.configure(fg_color="#1c1c1c",hover_color="#1c1c1c")
            button4.configure(fg_color="#1c1c1c",hover_color="#1c1c1c")
        if theme == "green":
            button1.configure(fg_color="#254B0F",hover_color="#254B0F")
            button2.configure(fg_color="#254B0F",hover_color="#254B0F")
            button3.configure(fg_color="#254B0F",hover_color="#254B0F")
            button4.configure(fg_color="#254B0F",hover_color="#254B0F")
            frame.configure(fg_color="#142C06")
            window.configure(fg_color="#0E1F04",hover_color="#254B0F")
            start.configure(fg_color="#4BA516",hover_color="#254B0F")
            settings_.configure(fg_color="#4BA516",hover_color="#254B0F")
        if theme == "purple":
            button1.configure(fg_color="#1a001a",hover_color="#1a001a")
            button2.configure(fg_color="#1a001a",hover_color="#1a001a")
            button3.configure(fg_color="#1a001a",hover_color="#1a001a")
            button4.configure(fg_color="#1a001a",hover_color="#1a001a")
            start.configure(fg_color="#1a001a",hover_color="#4d004d")
            settings_.configure(fg_color="#1a001a",hover_color="#4d004d")
            frame.configure(fg_color="#330033")
            window.configure(fg_color="#1a001a")
        if theme == "red":
            button1.configure(fg_color="#1a0000",hover_color="#1a0000")
            button2.configure(fg_color="#1a0000",hover_color="#1a0000")
            button3.configure(fg_color="#1a0000",hover_color="#1a0000")
            button4.configure(fg_color="#1a0000",hover_color="#1a0000")
            start.configure(fg_color="#1a0000",hover_color="#3d0101")
            settings_.configure(fg_color="#1a0000",hover_color="#3d0101")
            frame.configure(fg_color="#330000")
            window.configure(fg_color="#1a0000")
        if theme == "blue":
            button1.configure(fg_color="#00131a",hover_color="#00131a")
            button2.configure(fg_color="#00131a",hover_color="#00131a")
            button3.configure(fg_color="#00131a",hover_color="#00131a")
            button4.configure(fg_color="#00131a",hover_color="#00131a")
            start.configure(fg_color="#00131a",hover_color="#013245")
            settings_.configure(fg_color="#00131a",hover_color="#013245")
            frame.configure(fg_color="#002533")
            window.configure(fg_color="#00131a")
        if theme == "custom":
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
                
            if theme__=="Default":
                button_1.configure(fg_color="#1c1c1c",hover_color="#1c1c1c")
                button_2.configure(fg_color="#1c1c1c",hover_color="#1c1c1c")
                button_3.configure(fg_color="#ffffff",hover_color="#ffffff")
                button_4.configure(fg_color="#1c1c1c",hover_color="#1c1c1c")
                frame_.configure(fg_color="gray17")
                root.configure(fg_color="gray14")
            if theme__ == "Green":
                button_1.configure(fg_color="#254B0F",hover_color="#254B0F")
                button_2.configure(fg_color="#254B0F",hover_color="#254B0F")
                button_3.configure(fg_color="#61B62F",hover_color="#61B62F")
                button_4.configure(fg_color="#254B0F",hover_color="#254B0F")
                frame_.configure(fg_color="#142C06")
                root.configure(fg_color="#0E1F04")
            if theme__ == "Purple":
                button_1.configure(fg_color="#1a001a",hover_color="#1a001a")
                button_2.configure(fg_color="#1a001a",hover_color="#1a001a")
                button_3.configure(fg_color="#ff00ff",hover_color="#ff00ff")
                button_4.configure(fg_color="#1a001a",hover_color="#1a001a")
                frame_.configure(fg_color="#330033")
                root.configure(fg_color="#1a001a")
            if theme__ == "Red":
                button_1.configure(fg_color="#1a0000",hover_color="#1a0000")
                button_2.configure(fg_color="#1a0000",hover_color="#1a0000")
                button_3.configure(fg_color="#ff0000",hover_color="#ff0000")
                button_4.configure(fg_color="#1a0000",hover_color="#1a0000")
                frame_.configure(fg_color="#330000")
                root.configure(fg_color="#1a0000")
            if theme__ == "Blue":
                button_1.configure(fg_color="#00131a",hover_color="#00131a")
                button_2.configure(fg_color="#00131a",hover_color="#00131a")
                button_3.configure(fg_color="#004d99",hover_color="#004d99")
                button_4.configure(fg_color="#00131a",hover_color="#00131a")
                frame_.configure(fg_color="#002533")
                root.configure(fg_color="#00131a")
                
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
        
    def setting():
        try:
            mixer.music.pause()
        except:
            pass
        create_settings()
        root = ctk.CTk()
        root.title("Settings")
        root.geometry("500x500")
        def check_manual():
            mode = "manual"
            check_for_updates(mode=mode)
        frame_ = ctk.CTkFrame(root,width=450,height=450)
        frame_.place(relx=0.5,rely=0.5,anchor=ctk.CENTER)
        check_for_updates_ = ctk.CTkButton(frame_,text="Check For Updates",command=check_manual)
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
        
        def mus():
            mode_ = music_switch.get()
            music_option_change = change_setting(setting="music",mode=mode_)
            mus_ = mode_
        def hid():
            mode_ = auto_hide.get()
            hide_option_change = change_setting(setting="autohide",mode=mode_)
            ah = mode_
        scaling_option = ctk.CTkSwitch(frame_,onvalue=True,offvalue=False,text="",switch_width=50,switch_height=25,width=50,height=25,command=sca)
        scaling_option.place(relx=0.1,rely=0.2,anchor=ctk.CENTER)
        
        scaling_label = ctk.CTkLabel(frame_,text="Dynamic Scaling",font=("Helvetica",18))
        scaling_label.place(relx=0.31,rely=0.2,anchor=ctk.CENTER)
        
        switch = ctk.CTkSwitch(master=frame_, onvalue=True, offvalue=False,text="",switch_width=50,switch_height=25,width=50,height=25,command=sou)
        switch.place(relx=0.1,rely=0.3,anchor=ctk.CENTER)
        
        switch_label = ctk.CTkLabel(frame_,text="SFX",font=("Helvetica",18))
        switch_label.place(relx=0.2,rely=0.3,anchor=ctk.CENTER)
        
        auto_hide = ctk.CTkSwitch(frame_,text="",onvalue=True,offvalue=False,switch_width=50,switch_height=25,width=50,height=25,command=hid)
        auto_hide.place(relx=0.9,rely=0.3,anchor=ctk.CENTER)
        
        auto_close_label = ctk.CTkLabel(frame_,text="Auto hide results",font=("Helvetica",18))
        auto_close_label.place(relx=0.67,rely=0.3,anchor=ctk.CENTER)
    
        check_for_updates_switch = ctk.CTkSwitch(frame_,text="",onvalue=True,offvalue=False,switch_width=50,switch_height=25,command=che,width=50,height=25)
        check_for_updates_switch.place(relx=0.1,rely=0.4,anchor=ctk.CENTER)
        
        check_for_updates_label = ctk.CTkLabel(frame_,text="Automatically check for updates",font=("Helvetica",18))
        check_for_updates_label.place(relx=0.45,rely=0.4,anchor=ctk.CENTER)
    
        music_switch = ctk.CTkSwitch(frame_,text="",command=mus,switch_width=50,switch_height=25,width=50,height=25,onvalue=True,offvalue=False)
        music_switch.place(relx=0.9,rely=0.2,anchor=ctk.CENTER)
        
        music_label = ctk.CTkLabel(frame_,text="Music",font=("Helvetica",18))
        music_label.place(relx=0.765,rely=0.2,anchor=ctk.CENTER)
    
        warn = ctk.CTkLabel(frame_,text="",text_color="#cc3300",font=("Helvetica",24))
        warn.place(relx=0.5,rely=0.1,anchor=ctk.CENTER)
    
        keybinds = ctk.CTkButton(frame_,text="Change keybinds",command=change_keybind)
        keybinds.place(relx=0.83,rely=0.08,anchor=ctk.CENTER)
    
        #share_button = ctk.CTkButton(frame_,text="Share",command=share)
        #share_button.place(relx=0.5,rely=0.94,anchor=ctk.CENTER)
    
        sc = settings.get("settings",{}).get("scaling",False)
        so = settings.get("settings",{}).get("sound",True)
        cfu = settings.get("settings",{}).get("check",True)
        mus_ = settings.get("settings",{}).get("music",False)
        ah = settings.get("settings",{}).get("autohide",True)
        theme_button = ctk.CTkButton(frame_,text="Theme",command=custom_theme)
        theme_button.place(relx=0.5,rely=0.7,anchor=ctk.CENTER)
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
            

        version_label = ctk.CTkLabel(frame_,text=f"{version}",font=("Helvetica",12))
        version_label.place(relx=0.05,rely=0.95,anchor=ctk.CENTER)
        if sc == True:
            scaling_option.select()
        if cfu == True:
            check_for_updates_switch.select()
        else:
            check_for_updates_.place(relx=0.5,rely=0.08,anchor=ctk.CENTER)
        if so == True:
            switch.select()
        if mus_ == True:
            music_switch.select()
        if ah == True:
            auto_hide.select()
        def quit__():
            try:
                window.destroy()
            except:
                root.destroy()
            root.destroy()
            main()
        with open("save.json","r") as f:
            settings = json.load(f)
        theme = settings.get("settings",{}).get("theme","default").lower()
        if theme == "green":
            button_c="#4BA516"
            frame_.configure(fg_color="#142C06")
            root.configure(fg_color="#0E1F04",hover_color="#254B0F")
            keybinds.configure(fg_color="#4BA516",hover_color="#4BA516")
            theme_button.configure(fg_color="#4BA516",hover_color="#4BA516")
            check_for_updates_switch.configure(progress_color=button_c,fg_color="#0E1F04")
            scaling_option.configure(progress_color=button_c,fg_color="#0E1F04")
            switch.configure(progress_color=button_c,fg_color="#0E1F04")
            auto_hide.configure(progress_color=button_c,fg_color="#0E1F04")
            music_switch.configure(progress_color=button_c,fg_color="#0E1F04")
        if theme == "purple":
            button_c = "#1a001a"
            keybinds.configure(fg_color="#1a001a",hover_color="#1a001a")
            check_for_updates_switch.configure(progress_color=button_c,fg_color="#1a001a")
            scaling_option.configure(progress_color=button_c,fg_color="#1a001a")
            switch.configure(progress_color=button_c,fg_color="#1a001a")
            auto_hide.configure(progress_color=button_c,fg_color="#1a001a")
            music_switch.configure(progress_color=button_c,fg_color="#1a001a")
            theme_button.configure(fg_color="#1a001a",hover_color="#1a001a")
            frame_.configure(fg_color="#330033")
            root.configure(fg_color="#1a001a")
        if theme == "red":
            button_c = "#1a0000"
            keybinds.configure(fg_color="#1a0000",hover_color="#1a0000")
            theme_button.configure(fg_color="#1a0000",hover_color="#1a0000")
            check_for_updates_switch.configure(progress_color=button_c,fg_color="#1a0000")
            scaling_option.configure(progress_color=button_c,fg_color="#1a0000")
            switch.configure(progress_color=button_c,fg_color="#1a0000")
            auto_hide.configure(progress_color=button_c,fg_color="#1a0000")
            music_switch.configure(progress_color=button_c,fg_color="#1a0000")
            frame_.configure(fg_color="#330000")
            root.configure(fg_color="#1a0000")
        if theme == "blue":
            button_c = "#00131a"
            keybinds.configure(fg_color="#00131a",hover_color="#00131a")
            theme_button.configure(fg_color="#00131a",hover_color="#00131a")
            check_for_updates_switch.configure(progress_color=button_c,fg_color="#00131a")
            scaling_option.configure(progress_color=button_c,fg_color="#00131a")
            switch.configure(progress_color=button_c,fg_color="#00131a")
            auto_hide.configure(progress_color=button_c,fg_color="#00131a")
            music_switch.configure(progress_color=button_c,fg_color="#00131a")
            frame_.configure(fg_color="#002533")
            root.configure(fg_color="#00131a")
        if theme == "custom":
            button_c = settings.get("settings",{}).get("custom_theme",{}).get("hover","gray18")
            frame_c = settings.get("settings",{}).get("custom_theme",{}).get("frame_bg","gray18")
            keybinds.configure(fg_color=button_c,hover_color=button_c)
            theme_button.configure(fg_color=button_c,hover_color=button_c)
            check_for_updates_switch.configure(progress_color=button_c)
            scaling_option.configure(progress_color=button_c)
            switch.configure(progress_color=button_c)
            auto_hide.configure(progress_color=button_c)
            music_switch.configure(progress_color=button_c)
            frame_.configure(fg_color=frame_c)
            root.configure(fg_color=button_c)
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
        
    start = ctk.CTkButton(frame,width=100,height=25,text="Start",command=start_,font=("Helvetica",18.75))
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
            
            
    def clock():
        global start_time
        global elapsed_time
        global score
        global started
        print(average_time)
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
            show_results(x=window.winfo_pointerx()-112,y=window.winfo_pointery()-87)
            return
        _time = int(elapsed_time*-1)
        time_.configure(text=(_time))
        window.after(100,clock)
    def open_settings(n):
        setting()
    window.bind("<Escape>",open_settings)
    
    restore()
    window.after(1,play)
    create_settings()
    window.mainloop()
    
    
if __name__ == "__main__":
    main()
else:
    print(__name__)

    
# Probably could have gotten it to 250 lines if I actually knew what I was doing, I did not.
