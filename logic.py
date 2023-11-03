import importlib
import random
import time
import sound
import save
import logger as l

current_button = None
start_time = None
started = False
score = 0
pressed = 0
correct = 0
max_score = save.get_score()

def start():
    gui = importlib.import_module("gui") 
    global started 
    global start_time
    gui.move_buttons_away()
    started = True
    start_time = time.time()
    clock()
    
def end():
    gui = importlib.import_module("gui")
    gui.restore_buttons()
    global started
    global start_time
    global score
    global pressed
    global correct
    global current_button
    correct = 0
    pressed = 0
    current_button = None
    score = 0
    started = False
    start_time = None
    
def button_click(m):
    """
    'm' is the variable used to tell what button is being pressed (1-4)
    """
    gui = importlib.import_module("gui")
    global correct
    global score
    global start_time
    
    if not started: return
    else:
        global pressed, correct
        global score
        global start_time
        pressed+=1
        if m!=current_button:
            sound.wrong()
            l.log(type="DEUBG",message="Subtracting 0.2s from user's time.")
            start_time = start_time - 0.5
        else:
            sound.correct()
            score+=1
            correct+=1
            l.log(type="DEUBG",message="Adding 0.2s from user's time.")
            start_time += 0.2
        gui.reset_buttons()
        gui.update_score(score=score)
        random_button()
        
def random_button():
    gui = importlib.import_module("gui")
    global current_button
    number: int = random.randint(1,4)
    while number==current_button:
        number: int = random.randint(1,4)
    current_button = number
    gui.highlight_button(index=current_button)

def clock():
    gui = importlib.import_module("gui")
    global start_time
    global elapsed_time
    global score
    global started
    limit = 15
    elapsed_time = time.time() - start_time - limit
    if elapsed_time >= 0:
        gui.reset_buttons()
        save.save(score=score)
        gui.restore_buttons()
        try:
            calc_percentage = round((correct/pressed)*100,4)
        except ZeroDivisionError:
            calc_percentage = 0.0
        gui.show_result(score=score,max_score=max_score,clicks=pressed,correct_clicks=correct,percentage=calc_percentage,min_time=0,average_time=0)
        end()
        return
    gui.update_time(elapsed_time)
    gui.window.after(100,clock)