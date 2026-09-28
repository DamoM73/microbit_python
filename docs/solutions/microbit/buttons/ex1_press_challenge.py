from microbit import *

import random

# Setup
target = random.randint(5, 15)

# Main loop
while True:
    display.scroll("Press A " + str(target) + " times")
    button_a.get_presses()
    display.show(Image.YES)
    sleep(5000)
    presses = button_a.get_presses()
    if presses >= target:
        display.show(Image.HAPPY)
    else:
        display.show(Image.SAD)
    sleep(2000)
    target = random.randint(5, 15)
