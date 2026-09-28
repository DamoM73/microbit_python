from microbit import *
from PiicoDev_VEML6040 import PiicoDev_VEML6040

# Setup
sensor = PiicoDev_VEML6040()

# Main loop
while True:
    colour = sensor.classifyHue()
    if colour:
        display.show(colour[0].upper())
    sleep(500)
