
old_width = 450
old_height = 200

def resize(n):
    import gui
    global old_height
    global old_width
    
    __width__ = gui.window.winfo_width()
    __height__ = gui.window.winfo_height()
    if __width__ == old_width or __height__ == old_height:
        pass
    else:
        if gui.scaling_setting == True:
            old_width = __width__
            old_height = __height__
            button_font = (__height__-50)*0.1
            __x__ = (__width__-50)*0.22
            f_w = __width__-50
            f_h = __height__-50
            rad = round(__x__ *0.5)
            gui.start.configure(width=(__width__-50)*0.2,height=(__height__-50)*0.05,font=("Helvetica",button_font))
            gui.button1.configure(width=__x__,height=__x__,corner_radius=rad)
            gui.button2.configure(width=__x__,height=__x__,corner_radius=rad)
            gui.button3.configure(width=__x__,height=__x__,corner_radius=rad)
            gui.button4.configure(width=__x__,height=__x__,corner_radius=rad)
            gui.time_label.configure(font=("Helvetica",button_font))
            gui.score_label.configure(font=("Helvetica",button_font))
            gui.settings_button.configure(width=(__width__-50)*0.2,height=(__height__-50)*0.05,font=("Helvetica",button_font))
            
            #gui.download.configure(width=(__width__-50)*0.2,height=(__height__-50)*0.05,font=("Helvetica",button_font*0.6))
            gui.frame.configure(width=__width__-50,height=__height__-50)   