from PiicoDev_VL53L1X import PiicoDev_VL53L1X
from microbit import *

distSensor = PiicoDev_VL53L1X()

while True:
    if button_a.was_pressed():
        dist = distSensor.read() 
        message = str(dist) + " mm"
        display.scroll(message)
