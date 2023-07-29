# magnetic strength example

from microbit import *

while True:
    if button_a.was_pressed():
        field = compass.get_field_strength()
        display.scroll(str(field))
