# magnetic strength exercise 1

from microbit import *

while True:
    if button_a.was_pressed():
        field = round((compass.get_field_strength()) / 1000)
        display.scroll(str(field))
