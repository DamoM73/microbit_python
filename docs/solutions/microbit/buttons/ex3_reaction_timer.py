from microbit import *

import random

# Main loop
while True:
    target = random.choice(["A", "B"])
    for number in [3, 2, 1]:
        display.show(number)
        sleep(1000)
    display.show(target)
    button_a.was_pressed()
    button_b.was_pressed()
    start = running_time()
    while True:
        if target == "A" and button_a.was_pressed():
            break
        if target == "B" and button_b.was_pressed():
            break
    reaction = running_time() - start
    display.scroll(str(reaction) + "ms")
    sleep(1000)
