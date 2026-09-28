from microbit import *

# Setup
pin0.set_touch_mode(pin0.CAPACITIVE)

# Main loop
while True:
    if pin0.is_touched():
        display.show(Image.HAPPY)
    else:
        display.show(Image.SAD)
