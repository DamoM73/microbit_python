from microbit import *
from PiicoDev_RGB import PiicoDev_RGB

# Setup
leds = PiicoDev_RGB()
red = [255, 0, 0]
amber = [255, 100, 0]
green = [0, 255, 0]

# Main loop
while True:
    leds.clear()
    leds.setPixel(2, green)
    leds.show()
    sleep(3000)
    leds.clear()
    leds.setPixel(1, amber)
    leds.show()
    sleep(1000)
    leds.clear()
    leds.setPixel(0, red)
    leds.show()
    sleep(3000)
