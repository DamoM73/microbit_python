from microbit import *
import radio

# Setup
radio.config(group=7)
radio.on()

# Main loop
while True:
    message = radio.receive()
    if message == "happy":
        display.show(Image.HAPPY)
