from microbit import *
from PiicoDev_BME280 import PiicoDev_BME280

# Setup
sensor = PiicoDev_BME280()

# Main loop
while True:
    temp, pressure, humidity = sensor.values()
    if button_a.was_pressed():
        display.scroll(round(temp))
    if button_b.was_pressed():
        display.scroll(round(humidity))
