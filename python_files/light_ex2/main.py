# light exercise 2

from microbit import *

while True:
    light_level = display.read_light_level()
    
    if light_level< 100:
        for row in range(5):
            for column in range(5):
                display.set_pixel(row, column, 9)