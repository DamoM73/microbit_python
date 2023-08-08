# touch sensor example

from microbit import *

while True:
    display.clear()
    if pin_logo.is_touched():
        display.show(Image.HAPPY)
    sleep(10)