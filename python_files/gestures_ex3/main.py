# current_gestures exercise 3

from microbit import *

sensing = True

while sensing:
    if button_a.is_pressed():
        sensing = False

if accelerometer.was_gesture("3g"):
    display.show(Image.YES)
else:
    display.show(Image.NO)