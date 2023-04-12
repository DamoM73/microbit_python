# display image ex3

from microbit import *

while True:
    display.show(Image.SQUARE_SMALL)
    sleep(500)
    display.show((Image.DIAMOND_SMALL))
    sleep(500)