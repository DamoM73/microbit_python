from microbit import *
from PiicoDev_VEML6040 import PiicoDev_VEML6040

# Setup
sensor = PiicoDev_VEML6040()

# Main loop
while True:
    print(sensor.readRGB())
    sleep(1000)
