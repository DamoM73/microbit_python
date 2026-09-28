from microbit import *
from PiicoDev_RGB import PiicoDev_RGB, wheel

# Setup
leds = PiicoDev_RGB()

# Main loop
while True:
    leds.fill(wheel(0.5))
