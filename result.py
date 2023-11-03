import customtkinter as ctk
import theme


def show(x,y, percent: float, min_time: float, average_time: float, clicks: int, correct_clicks: int): 
        """
        average_time = round(average_time*1000,4)
        correct_clicks = sum(correct_list)
        clicks=len(correct_list)
        percentage = round(percentage, 2) 
        min_time = round(min_time*1000,4)
        """
        global app
        
        app = ctk.CTk()
        app.title("Reaction Time")
        app.geometry(f"225x175+{x}+{y}")
        app.resizable(False,False)
        app.configure(fg_color=theme.get_colors()["root_color"])
        create_items_(average_time=average_time, correct_clicks=correct_clicks, clicks=clicks, percentage=percent, min_time = min_time)
        app.mainloop()
            
def create_items_(average_time,correct_clicks, clicks, percentage, min_time): # Creates elements for the result window        
        app_frame = ctk.CTkFrame(app,width=200,height=150,fg_color=theme.get_colors()["frame_color"])
        app_frame.place(relx=0.5,rely=0.5,anchor=ctk.CENTER)
        accuracy_out_label = ctk.CTkLabel(master=app,
                                fg_color=theme.get_colors()["frame_color"],
                                text=f"{correct_clicks}/{clicks}\n({percentage}%)",
                                font=("Helvetica",14))
        accuracy_out_label.place(relx=0.5,rely=0.825,anchor=ctk.CENTER)
        
        average_label_label = ctk.CTkLabel(master=app,
                                fg_color=theme.get_colors()["button_color"],
                                text="Average",
                                font=("Helvetica",14))
        average_label_label.place(relx=0.7,rely=0.175,anchor=ctk.CENTER)
        
        min_label_label = ctk.CTkLabel(master=app,
                                fg_color=theme.get_colors()["button_color"],
                                text="Minimum",
                                font=("Helvetica",14))
        min_label_label.place(relx=0.3,rely=0.175,anchor=ctk.CENTER)
        
        average_label = ctk.CTkButton(master=app,
                                fg_color=theme.get_colors()["button_color"],
                                hover_color=theme.get_colors()["button_color"],
                                text=f"{average_time}\nms",
                                width=75,height=75,
                                font=("Helvetica",14))
        average_label.place(relx=0.7,rely=0.5,anchor=ctk.CENTER)
        
        min_label = ctk.CTkButton(master=app,
                                fg_color=theme.get_colors()["button_color"],
                                hover_color=theme.get_colors()["button_color"],
                                text=f"{min_time}\nms",
                                width=75,height=75,
                                font=("Helvetica",14))
        min_label.place(in_=app,relx=0.3,rely=0.5,anchor=ctk.CENTER)

              
if __name__ == "__main__":
        print("DEBUG - Testing with example numbers")
        show(0,0,52.6,126.7,1742.5,67,1)