from microbit import *
from PiicoDev_RGB import PiicoDev_RGB

# Setup
leds = PiicoDev_RGB()

# Main loop
while True:
    leds.fill([255, 0, 255])
