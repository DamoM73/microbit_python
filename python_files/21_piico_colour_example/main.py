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
    
    # process data
    red = str(rgb_data['red'])
    green = str(rgb_data['green'])
    blue = str(rgb_data['blue'])
    
    # output data
    print(red, green, blue)
    sleep(500)
