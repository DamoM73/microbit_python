# Exercise 2
# Can you make the micro:bit show a happy face if it is face up, or an angry
# face if it isn't?

from microbit import *

# Main loop
while True:
    if accelerometer.is_gesture("face up"):
        display.show(Image.HAPPY)
    else:
        display.show(Image.ASLEEP)
