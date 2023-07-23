# current gestures

from microbit import *

sleep(5000)

if accelerometer.was_gesture("shake"):
    display.show(Image.YES)
else:
    display.show(Image.NO)