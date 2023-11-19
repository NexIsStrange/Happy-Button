from pygame import mixer
import logger as l
import pathlib
import os

wrong_loc = fr"{pathlib.Path.cwd()}\assets\wrong.wav"
correct_loc = fr"{pathlib.Path.cwd()}\assets\correct.wav"

def init():
    global wrong_loc, correct_loc
    l.log(type="DEBUG",message="Initializing mixer, please wait")
    mixer.init()
    if os.path.isfile(wrong_loc) == False:
        wrong_loc = fr"{pathlib.Path.cwd()}\_internal\assets\wrong.wav"
        correct_loc = fr"{pathlib.Path.cwd()}\_internal\assets\correct.wav"

def wrong():
    global wrong_loc
    try:
        mixer.Channel(2).play(mixer.Sound(wrong_loc))
    except Exception as e:
        l.log(type="ERROR",message=f"Failed to play sound. {e}")
def correct():
    global correct_loc
    try:
        mixer.Channel(1).play(mixer.Sound(correct_loc))
    except Exception as e:
        l.log(type="ERROR",message=f"Failed to play sound. {e}")
    