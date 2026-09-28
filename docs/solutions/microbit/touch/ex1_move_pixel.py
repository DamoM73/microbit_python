from microbit import *

# Setup
pin0.set_touch_mode(pin0.CAPACITIVE)
pin2.set_touch_mode(pin2.CAPACITIVE)
x = 2

# Main loop
while True:
    if pin2.is_touched() and x < 4:
        x = x + 1
    if pin0.is_touched() and x > 0:
        x = x - 1
    display.clear()
    display.set_pixel(x, 2, 9)
    sleep(200)
