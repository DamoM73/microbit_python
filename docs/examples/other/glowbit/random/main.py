from microbit import *
import neopixel
import random

# Setup
rainbow = neopixel.NeoPixel(pin0, 13)

# Main loop
while True:
    pixel = random.randint(0, 12)
    colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    rainbow.clear()
    rainbow[pixel] = colour
    rainbow.show()
    sleep(200)
