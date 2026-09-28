from microbit import *
from PiicoDev_VEML6040 import PiicoDev_VEML6040

# Setup
sensor = PiicoDev_VEML6040()

# Main loop
while True:
    data = sensor.readHSV()
    print(data["hue"], data["sat"], data["val"])
    sleep(500)
