from microbit import *
from PiicoDev_RGB import PiicoDev_RGB

# Setup
leds = PiicoDev_RGB()

# Main loop
while True:
    temp = temperature()
    if temp < 20:
        leds.fill([0, 0, 255])
    elif temp <= 25:
        leds.fill([0, 255, 0])
    else:
        leds.fill([255, 0, 0])
    sleep(1000)
