# magnetic strength exercise 2

from microbit import *

while True:
    print("Here")
    if compass.get_field_strength() > 230000:
        display.show(Image.HAPPY)
    else:
        display.show(Image.ANGRY)
    sleep(500)
