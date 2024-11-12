from microbit import *
from PiicoDev_VL53L1X import PiicoDev_VL53L1X

# --- SETUP

# start sensors
distSensor = PiicoDev_VL53L1X()

# store variables

# --- RUNNING
while True:
    # read sensor data
    distance = distSensor.read()
    
    # process data
    distance = str(distance) + " mm"
    
    # output data
    print(distance)
