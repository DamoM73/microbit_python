from microbit import *
from PiicoDev_Switch import PiicoDev_Switch

# Setup
button = PiicoDev_Switch()

# Main loop
while True:
    if button.was_double_pressed:
        display.show(Image.HAPPY)
    else:
        display.show(Image.SAD)
    sleep(1000)
