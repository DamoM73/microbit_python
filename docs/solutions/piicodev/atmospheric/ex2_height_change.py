from microbit import *
from PiicoDev_BME280 import PiicoDev_BME280

# Setup
sensor = PiicoDev_BME280()
last_height = sensor.altitude()

# Main loop
while True:
    if button_a.was_pressed():
        height = sensor.altitude()
        change = round(height - last_height, 1)
        display.scroll(change)
        last_height = height
