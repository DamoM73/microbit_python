from microbit import *
from PiicoDev_BME280 import PiicoDev_BME280
from PiicoDev_RGB import PiicoDev_RGB
import music

# Setup
sensor = PiicoDev_BME280()
leds = PiicoDev_RGB()
limit = 25

# Main loop
while True:
    # Input
    temp, pressure, humidity = sensor.values()

    # Process
    too_hot = temp > limit

    # Output
    if too_hot:
        leds.fill([255, 0, 0])
        display.show(Image.SAD)
        music.pitch(880, 200)
    else:
        leds.fill([0, 255, 0])
        display.show(Image.HAPPY)
    sleep(1000)
