# movement values example

from microbit import *

while True:
    values = accelerometer.get_values()
    display.scroll("x: " + str(values[0]) + " y: " + str(values[1]) + " z: " + str(values[2]))
    sleep(1000)