# movement exrecise 2

from microbit import *

while True:
    z_reading = accelerometer.get_z()
    display.scroll(z_reading)
