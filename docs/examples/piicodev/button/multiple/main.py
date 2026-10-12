from microbit import *
from PiicoDev_Switch import PiicoDev_Switch

# Setup
buttonA = PiicoDev_Switch(id=[0, 0, 0, 0])
buttonB = PiicoDev_Switch(id=[1, 0, 0, 0])

# Main loop
while True:
    if buttonA.is_pressed:
        display.show("A")
    elif buttonB.is_pressed:
        display.show("B")
    else:
        display.clear()
    sleep(100)
