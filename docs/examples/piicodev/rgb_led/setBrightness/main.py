from microbit import *
from PiicoDev_RGB import PiicoDev_RGB

# Setup
leds = PiicoDev_RGB()
leds.fill([0, 0, 255])

# Main loop
while True:
    leds.setBrightness(10)
