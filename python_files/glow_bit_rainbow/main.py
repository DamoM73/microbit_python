# glowbit example

from microbit import *
import neopixel
import random

# Setup the Rainbow as a Neopixel strip on pin0 with a length of 13
rainbow = neopixel.NeoPixel(pin0, 13)

while True:
    rainbow.clear()
    pixel = random.randint(0,12)
    colour = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    
    rainbow[pixel] = colour
    
    rainbow.show()
    sleep(200)