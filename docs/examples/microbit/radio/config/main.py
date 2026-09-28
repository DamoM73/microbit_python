from microbit import *
import radio

# Setup
radio.config(group=7)
radio.on()

# Main loop
while True:
    display.show(7)
