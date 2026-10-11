from microbit import *
from PiicoDev_Switch import PiicoDev_Switch

# Setup
left = PiicoDev_Switch(id=[0, 0, 0, 0])
right = PiicoDev_Switch(id=[1, 0, 0, 0])

# Main loop
while True:
    if left.is_pressed:
        display.show("L")
    elif right.is_pressed:
        display.show("R")
    else:
        display.clear()
    sleep(100)
