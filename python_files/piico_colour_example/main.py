from microbit import *
from PiicoDev_VEML6040 import PiicoDev_VEML6040

# --- SETUP

# start sensors
colourSensor = PiicoDev_VEML6040()

# store variables


# --- RUNNING
while True:
    # read sensor data
    rgb_data = colourSensor.readRGB()
    hsv_data = colourSensor.readHSV()
    
    # process data
    red = str(rgb_data['red'])
    green = str(rgb_data['green'])
    blue = str(rgb_data['blue'])
    hue = str(hsv_data['hue'])
    sat = str(hsv_data['sat'])
    val = str(hsv_data['val'])
    
    print(red, green, blue, "|", hue, sat, val)

    sleep(500)
