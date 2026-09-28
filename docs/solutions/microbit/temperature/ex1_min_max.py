from microbit import *

# Setup
lowest = temperature()
highest = temperature()

# Main loop
while True:
    temp = temperature()
    if temp < lowest:
        lowest = temp
    if temp > highest:
        highest = temp
    if button_a.was_pressed():
        display.scroll(lowest)
    if button_b.was_pressed():
        display.scroll(highest)
    sleep(2000)
