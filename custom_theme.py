import customtkinter as ctk
import theme
import settings
import save
import sound
import hex_color
import gui
import logger as l

buttons = []
i=0


denied = ["frame_color","button_color","root_color","hover_color"]
def GUI():
    l.log(type="INFO",message="Loading custom_theme GUI")
    global opacity_slider, opacity_label, theme_option, hover_color_entry, frame_color_entry,root_color_entry, button_color_entry,save_button
    global root,frame
    
    root = ctk.CTk()
    root.title("Settings")
    root.geometry("500x500") # Another window, yay
    frame = ctk.CTkFrame(root,width=450,height=450)
    frame.place(relx=0.5,rely=0.5,anchor=ctk.CENTER)
    button1 = ctk.CTkButton(frame,width=100,height=100,text="",corner_radius=120,command=sound.correct)
    button1.place(relx=0.13,rely=0.3,anchor=ctk.CENTER)
    button2 = ctk.CTkButton(frame,width=100,height=100,text="",corner_radius=120,command=sound.correct)
    button2.place(relx=0.38,rely=0.3,anchor=ctk.CENTER)
    button3 = ctk.CTkButton(frame,width=100,height=100,text="",corner_radius=120,command=sound.correct)
    button3.place(relx=0.63,rely=0.3,anchor=ctk.CENTER)
    button4 = ctk.CTkButton(frame,width=100,height=100,text="",corner_radius=120,command=sound.correct)
    button4.place(relx=0.87,rely=0.3,anchor=ctk.CENTER)
    save_button = ctk.CTkButton(frame,text="Save",command=save_theme)
    save_button.place(relx=0.5,rely=0.9,anchor=ctk.CENTER)
    buttons.append(button1)
    buttons.append(button2)
    buttons.append(button3)
    buttons.append(button4)
    
    for button in buttons:
        button.configure(fg_color=theme.get_colors()["button_color"],hover_color=theme.get_colors()["button_color"])
    
    opacity_label = ctk.CTkLabel(frame,text="Opacity",font=("Helvetica",12))
    opacity_slider = ctk.CTkSlider(frame,from_=0.1, to=1,command=slider_feedback)
    opacity_value = settings.get_setting("opacity")
    opacity_slider.set(float(opacity_value))
    theme_option = ctk.CTkOptionMenu(master=frame,values=["Default","Green","Purple","Red","Blue","Custom"],command=change_theme)
    theme_option.place(relx=0.5,rely=0.60,anchor=ctk.CENTER)
    hover_color_entry = ctk.CTkEntry(frame,placeholder_text="Actives button")
    frame_color_entry = ctk.CTkEntry(frame,placeholder_text="Frame")
    root_color_entry = ctk.CTkEntry(frame,placeholder_text="Root")
    button_color_entry = ctk.CTkEntry(frame,placeholder_text="Inactve button")
    root.mainloop()
   
def restore_save():
    save_button.configure(state="normal",text="Save")
    
def save_theme():
    l.log(type="DEBUG",message="Saving theme...")
    gui.refresh_theme()
    save_button.configure(state="disabled",text="Saved!")
    if theme_option.get().lower() != "custom":
        save.theme(theme=theme_option.get().lower())
    else:
        check = hex_color.check(
                {"button_color":button_color_entry.get(),
                "frame_color":frame_color_entry.get(),
                "root_color":root_color_entry.get(),
                "hover_color":hover_color_entry.get()}
        )
        print(check)
        if check not in denied:
            l.log(type="DEUBG",message="All hex-codes are valid.")
            save.theme(theme="custom",
                    button_color=button_color_entry.get(),
                    frame_color=frame_color_entry.get(),
                    root_color=root_color_entry.get(),
                    hover_color=hover_color_entry.get(),
                    opacity=opacity_slider.get()
            )
        else:
            l.log(type="DEBUG",message=f"Invalid hex-code: {check}")
            save_button.configure(text=f"Invalid: {check}")
    root.after(1000,restore_save)
def change_theme(element):
    l.log(type="DEBUG",message=f"Changed theme to {element}")
    global i
    i = 0
    update_buttons()
    print(element)
    if element.lower() == "custom":
        opacity_label.place(relx=0.5,rely=0.05,anchor=ctk.CENTER)
        opacity_slider.place(relx=0.5,rely=0.1,anchor=ctk.CENTER)
        hover_color_entry.place(relx=0.3,rely=0.7,anchor=ctk.CENTER)
        frame_color_entry.place(relx=0.7,rely=0.7,anchor=ctk.CENTER)
        root_color_entry.place(relx=0.3,rely=0.8,anchor=ctk.CENTER)
        button_color_entry.place(relx=0.7,rely=0.8,anchor=ctk.CENTER)
    else:
        opacity_label.place(relx=12,rely=12,anchor=ctk.CENTER)
        opacity_slider.place(relx=12,rely=12,anchor=ctk.CENTER)
        hover_color_entry.place(relx=12,rely=12,anchor=ctk.CENTER)
        frame_color_entry.place(relx=12,rely=12,anchor=ctk.CENTER)
        root_color_entry.place(relx=12,rely=12,anchor=ctk.CENTER)
        button_color_entry.place(relx=12,rely=12,anchor=ctk.CENTER)
        root.wm_attributes("-alpha",1)
    root.configure(fg_color=theme.get_colors(specify=element)["root_color"])
    frame.configure(fg_color=theme.get_colors(specify=element)["frame_color"])
def update_buttons():
    global i
    for button in buttons:
        print(i)
        try:
            button.configure(fg_color=theme.get_colors(specify=theme_option.get())["button_color"],hover_color=theme.get_colors(specify=theme_option.get())["hover_color"])
        except:
            pass
        
def slider_feedback(value):
    root.wm_attributes("-alpha",value)