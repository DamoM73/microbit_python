from microbit import *
from PiicoDev_BME280 import PiicoDev_BME280

# Setup
sensor = PiicoDev_BME280()

# Main loop
while True:
    print(sensor.values())
    sleep(1000)
