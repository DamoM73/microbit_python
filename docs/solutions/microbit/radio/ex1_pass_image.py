from microbit import *
import radio

# Setup
radio.config(group=7)
radio.on()
has_image = False

# Main loop
while True:
    if button_a.was_pressed():
        has_image = True
    if has_image:
        display.show(Image.DUCK)
        if accelerometer.was_gesture("shake"):
            radio.send("catch")
            has_image = False
            display.clear()
    if radio.receive() == "catch":
        has_image = True
