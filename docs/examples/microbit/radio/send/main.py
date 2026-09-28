from microbit import *
import radio

# Setup
radio.config(group=7)
radio.on()

# Main loop
while True:
    if button_a.was_pressed():
        radio.send("happy")
