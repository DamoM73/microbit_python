# piicodev colour sensor exercise 1

from PiicoDev_VEML6040 import PiicoDev_VEML6040
from PiicoDev_Unified import sleep_ms

colourSensor = PiicoDev_VEML6040()

while True:
    data = colourSensor.readRGB()
    print(data)

    sleep_ms(1000)
