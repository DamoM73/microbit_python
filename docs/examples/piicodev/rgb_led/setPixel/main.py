from microbit import *
from PiicoDev_RGB import PiicoDev_RGB

# Setup
leds = PiicoDev_RGB()

# Main loop
while True:
    leds.setPixel(0, [255, 0, 0])
    leds.show()
