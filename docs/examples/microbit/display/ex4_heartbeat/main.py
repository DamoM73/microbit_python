# Exercise 4
# Can you change the animation so it looks more like an actual heartbeat?

from microbit import *

# Main loop
while True:
    display.show(Image.HEART)
    sleep(1000)
    display.show(Image.HEART_SMALL)
    sleep(1000)
