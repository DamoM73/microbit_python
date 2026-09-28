from microbit import *

import random

# Main loop
while True:
    pattern = ""
    for i in range(6):
        pattern = pattern + random.choice(["A", "B"])
    display.scroll(pattern)
    display.show("?")
    button_a.was_pressed()
    button_b.was_pressed()
    guess = ""
    while len(guess) < 6:
        if button_a.was_pressed():
            guess = guess + "A"
            display.show("A")
        if button_b.was_pressed():
            guess = guess + "B"
            display.show("B")
    if guess == pattern:
        display.show(Image.HAPPY)
    else:
        display.show(Image.SAD)
    sleep(2000)
