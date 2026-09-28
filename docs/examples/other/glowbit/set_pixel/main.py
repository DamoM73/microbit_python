from microbit import *
import neopixel

# Setup
rainbow = neopixel.NeoPixel(pin0, 13)

# Main loop
while True:
    rainbow[0] = (255, 0, 0)
    rainbow.show()
