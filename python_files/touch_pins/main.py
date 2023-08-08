# pin touch example

from microbit import *

pin0.set_touch_mode(pin0.CAPACITIVE)

while True:
    display.clear()
    if pin0.is_touched():
        display.show(Image.HAPPY)
    sleep(10)