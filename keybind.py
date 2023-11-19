import settings
import customtkinter as ctk
import logger as l
import gui

def GUI():
    l.log(type="DEBUG", message="Loading keybind GUI")
    global frame
    global root
    
    root = ctk.CTk()
    root.geometry("500x500")
    root.title("Change Keybinds")
    frame = ctk.CTkFrame(root,width=450,height=450)
    frame.place(relx=0.5,rely=0.5,anchor=ctk.CENTER)
    create_items()
    root.mainloop()

def create_items():
    global entry1,entry2,entry3,entry4,save_button
    _1 = settings.get_setting("1","")
    _2 = settings.get_setting("2","")
    _3 = settings.get_setting("3","")
    _4 = settings.get_setting("3","")
    entry1 = ctk.CTkEntry(frame,placeholder_text="1",width=75,height=75,font=("Helvetica",28))
    entry1.insert(0,_1)
    entry2 = ctk.CTkEntry(frame,placeholder_text="2",width=75,height=75,font=("Helvetica",28))
    entry2.insert(0,_2)
    entry3 = ctk.CTkEntry(frame,placeholder_text="3",width=75,height=75,font=("Helvetica",28))
    entry3.insert(0,_3)
    entry4 = ctk.CTkEntry(frame,placeholder_text="4",width=75,height=75,font=("Helvetica",28))
    entry4.insert(0,_4)
    entry1.place(relx=0.2,rely=0.5,anchor=ctk.CENTER)
    entry2.place(relx=0.4,rely=0.5,anchor=ctk.CENTER)
    entry3.place(relx=0.6,rely=0.5,anchor=ctk.CENTER)
    entry4.place(relx=0.8,rely=0.5,anchor=ctk.CENTER)
    save_button = ctk.CTkButton(frame,text="Save",command=save)
    save_button.place(relx=0.5,rely=0.9,anchor=ctk.CENTER)
    root.after(10,limit_char_count)
    
def save():
    l.log(type="DEBUG",message="Saving keybinds...")
    disable_button()
    settings.change_setting("1",entry1.get())
    settings.change_setting("2",entry2.get())
    settings.change_setting("3",entry3.get())
    settings.change_setting("4",entry4.get())
    gui.bind_buttons()
    root.after(1000,enable_button)
    
def limit_char_count():
    if len(entry1.get()) > 1:
        entry1.delete(0,1)
    if len(entry2.get()) > 1:
        entry2.delete(0,1)
    if len(entry3.get()) > 1:
        entry3.delete(0,1)
    if len(entry4.get()) > 1:
        entry4.delete(0,1)
    root.after(10,limit_char_count)
    
def disable_button():
    save_button.configure(text="Saved!",state="disabled")
def enable_button():
    save_button.configure(text="Save",state="normal")
