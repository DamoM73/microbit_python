# movement exrecise 1

from microbit import *

while True:
    y_reading = accelerometer.get_y()
    display.scroll(y_reading)