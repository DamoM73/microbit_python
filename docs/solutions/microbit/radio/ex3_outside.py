from microbit import *
import radio

# Setup
radio.config(group=42)
radio.on()

# Main loop
while True:
    radio.send(str(temperature()))
    sleep(5000)
