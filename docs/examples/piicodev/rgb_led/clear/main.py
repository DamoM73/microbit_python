from microbit import *
from PiicoDev_RGB import PiicoDev_RGB

# Setup
leds = PiicoDev_RGB()

# Main loop
while True:
    leds.fill([255, 255, 255])
    sleep(1000)
    leds.clear()
    sleep(1000)
