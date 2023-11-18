import json
import get_info
import keybind
import custom_theme
import logger as l

def get_setting(setting: str, default = False):
    with open("save.json","r") as f:
        settings_file = json.load(f)
    return settings_file.get("settings",{}).get(setting, default)

def change_setting(setting:str, value):
    l.log(f"Changing '{setting}' to '{value}'")
    with open("save.json","r") as f:
        setting_file = json.load(f)
    if "settings" not in setting_file:
        setting_file["settings"] = {}
    setting_file["settings"][setting] = value
    
    with open("save.json","w") as f:
        json.dump(setting_file,f,indent=2)

def get_custom_theme():
    """
    Returns dict
    Example: {"hover": "#30566E", "frame_bg": "#30566E", "main_bg": "#30566E", "button_color": "#30566E", "opacity": "1.0"}
    """
    with open("save.json","r") as f:
        settings_file = json.load(f)
    return settings_file.get("settings",{}).get("custom_theme")

def gui():
    l.log(type="DEBUG",message="Loading settings GUI")
    import customtkinter as ctk
    root = ctk.CTk()
    root.title("Settings")
    root.geometry("500x500")
    frame_ = ctk.CTkFrame(root,width=450,height=450)
    frame_.place(relx=0.5,rely=0.5,anchor=ctk.CENTER)
    check_for_updates_ = ctk.CTkButton(frame_,text="Check For Updates",command=None)
    def sca():
        mode_ = scaling_option.get()
        change_setting(setting="scaling",value=mode_)
    def sou():
        mode_ = switch.get()
        change_setting(setting="sound",value=mode_)
    
    def che():
        mode_ = check_for_updates_switch.get()
        change_setting(setting="check",value=mode_)
        cfu = mode_
        if mode_ == False:
            check_for_updates_.place(relx=0.5,rely=0.08,anchor=ctk.CENTER)
        else:
            check_for_updates_.place(relx=12,rely=0.08,anchor=ctk.CENTER)
    
    def mus():
        mode_ = music_switch.get()
        change_setting(setting="music",value=mode_)
        mus_ = mode_
    def hid():
        mode_ = auto_hide.get()
        change_setting(setting="autohide",value=mode_)
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

    keybinds = ctk.CTkButton(frame_,text="Change keybinds",command=keybind.GUI)
    keybinds.place(relx=0.83,rely=0.08,anchor=ctk.CENTER)
    
    update = ctk.CTkButton(frame_,text="Change keybinds",command=keybind.GUI)
    

    #share_button = ctk.CTkButton(frame_,text="Share",command=share)
    #share_button.place(relx=0.5,rely=0.94,anchor=ctk.CENTER)

    sc = get_setting("scaling")
    so = get_setting("sound")
    cfu = get_setting("check")
    mus_ = get_setting("music")
    ah = get_setting("auto_hide")
    theme_button = ctk.CTkButton(frame_,text="Theme",command=custom_theme.GUI)
    theme_button.place(relx=0.5,rely=0.7,anchor=ctk.CENTER)

    version_label = ctk.CTkLabel(frame_,text=f"Application: v{float(get_info.application_ver())}({get_info.release_type()}), Theme: v{float(get_info.theme_ver())}, Save: v{float(get_info.save_ver())} ",font=("Helvetica",12))
    version_label.place(relx=0.4,rely=0.95,anchor=ctk.CENTER)
    
    if sc == True: scaling_option.select()
    if cfu == True: check_for_updates_switch.select()
    else: check_for_updates_.place(relx=0.5,rely=0.08,anchor=ctk.CENTER)
    if so == True: switch.select()
    if mus_ == True: music_switch.select()
    if ah == True: auto_hide.select()
    root.mainloop()