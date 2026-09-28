from microbit import *

# Setup
count = 0

# Main loop
while True:
    if button_a.was_pressed():
        count = count + 1
    if button_b.was_pressed():
        count = 0
    display.show(count)
