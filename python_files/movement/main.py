# movement

from microbit import *

while True:
    x_reading = accelerometer.get_x()
    display.scroll(x_reading)
