from pygame import mixer
import pathlib

wrong_loc = fr"{pathlib.Path.cwd()}\assets\wrong.wav"
correct_loc = fr"{pathlib.Path.cwd()}\assets\correct.wav"

def init():
    mixer.init()
def wrong():
    mixer.Channel(2).play(mixer.Sound(wrong_loc))
def correct():
    mixer.Channel(1).play(mixer.Sound(correct_loc))