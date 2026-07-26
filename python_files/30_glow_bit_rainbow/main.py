from microbit import *
import neopixel
import random

# --- SETUP
# start components
rainbow = neopixel.NeoPixel(pin0, 13)

# store variables
red = 0
green = 0
blue = 0
pixel = 0

# --- RUNNING
while True:
    # read sensor data
    
    # process data
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    colour = (red, green, blue)
    pixel = random.randint(0,12)
    
    # output data
    rainbow.clear()    
    rainbow[pixel] = colour
    rainbow.show()
    sleep(200)