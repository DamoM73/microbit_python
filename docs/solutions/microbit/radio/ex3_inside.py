from microbit import *
import radio

# Setup
radio.config(group=42)
radio.on()
outside = "?"

# Main loop
while True:
    message = radio.receive()
    if message:
        outside = message
    if button_a.was_pressed():
        display.scroll(temperature())
    if button_b.was_pressed():
        display.scroll(outside)
