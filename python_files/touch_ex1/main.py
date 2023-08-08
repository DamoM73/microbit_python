# touch exercise 1

from microbit import *

x = 2

pin0.set_touch_mode(pin0.CAPACITIVE)
pin2.set_touch_mode(pin2.CAPACITIVE)

while True:
    display.set_pixel(x, 2, 9)
    if pin0.is_touched() and x > 0:
        x -= 1
    elif pin2.is_touched() and x < 4:
        x += 1
    sleep(100)
    display.clear()
