# piicodev atmospheric sensor exercise 2

from PiicoDev_BME280 import PiicoDev_BME280
from microbit import *

sensor = PiicoDev_BME280()
zero_altitude = sensor.altitude()

while True:
    # get reading
    if button_a.was_pressed():
        current_altitude = sensor.altitude()
        print(current_altitude, zero_altitude)
        display.scroll(str(current_altitude - zero_altitude))
        zero_altitude = current_altitude