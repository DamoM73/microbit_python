# display.custom exercise 2

from microbit import *

display.clear()

while True:
    for y in range(5):
        for x in range(5):
            for level in range(0,10):
                display.set_pixel(x,y,level)
                sleep(10)
            for level in range(9,-1,-1):
                display.set_pixel(x,y,level)
                sleep(10)