# microphone example 2

from microbit import *

while True:
    sound_level = microphone.sound_level()
    display.scroll(sound_level)
    sleep(500)