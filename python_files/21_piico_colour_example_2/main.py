from microbit import *
from PiicoDev_VEML6040 import PiicoDev_VEML6040

# --- SETUP
# start sensors
colourSensor = PiicoDev_VEML6040()

# store variables
COLOURS = {
    "Red": 0,
    "Yellow": 60,
    "Green": 120,
    "Cyan": 180,
    "Blue": 240,
    "Magenta": 300
    }

# --- RUNNING
while True:
    # read sensor data
    hsv_data = colourSensor.readHSV()
    
    # process data
    hue = hsv_data["hue"]
    colour = colourSensor.classifyHue(COLOURS)
    
    # output data
    print(colour, hue)
    sleep(500)