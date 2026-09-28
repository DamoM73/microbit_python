from microbit import *
import neopixel

# Setup
rainbow = neopixel.NeoPixel(pin0, 13)

# Main loop
while True:
    rainbow.fill((0, 50, 0))
    rainbow.show()
