from microbit import *

# Main loop
while True:
    if accelerometer.is_gesture("face up"):
        display.show(Image.HAPPY)
    else:
        display.show(Image.ANGRY)
