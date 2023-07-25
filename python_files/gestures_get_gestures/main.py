# get_gestures example

from microbit import *

sleep(5000)

gestures = accelerometer.get_gestures()

for gesture in gestures:
    display.scroll(gesture)