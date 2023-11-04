from pygame import mixer
import logger as l
import pathlib

wrong_loc = fr"{pathlib.Path.cwd()}\assets\wrong.wav"
correct_loc = fr"{pathlib.Path.cwd()}\assets\correct.wav"

def init():
    l.log(type="DEBUG",message="Initializing mixer, please wait")
    mixer.init()
def wrong():
    mixer.Channel(2).play(mixer.Sound(wrong_loc))
def correct():
    mixer.Channel(1).play(mixer.Sound(correct_loc))