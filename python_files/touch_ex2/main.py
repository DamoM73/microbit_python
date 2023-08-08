# touch exercise 2

from microbit import *

x = 2

pin0.set_touch_mode(pin0.CAPACITIVE)
pin2.set_touch_mode(pin2.CAPACITIVE)

while True:
    display.set_pixel(x, 2, 9)
    if pin0.is_touched():
        x -= 1
    elif pin2.is_touched():
        x += 1
    if x == -1:
        x = 4
    elif x == 5:
        x = 0
    sleep(100)
    display.clear()

