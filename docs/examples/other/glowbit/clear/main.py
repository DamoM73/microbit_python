from microbit import *
import neopixel

# Setup
rainbow = neopixel.NeoPixel(pin0, 13)

# Main loop
while True:
    rainbow.fill((50, 0, 50))
    rainbow.show()
    sleep(1000)
    rainbow.clear()
    sleep(1000)
