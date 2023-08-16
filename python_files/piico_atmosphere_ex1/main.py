# piicodev atmospheric sensor exercise 1

from PiicoDev_BME280 import PiicoDev_BME280
from microbit import *

sensor = PiicoDev_BME280()

while True:
    # gather reading
    temp, pressure, humidity = sensor.values()
    temp = int(round(temp,0))
    humidity = int(round(humidity,0))
    
    # display reading
    if button_a.was_pressed():
        display.scroll(str(temp))
    if button_b.was_pressed():
        display.scroll(str(humidity))