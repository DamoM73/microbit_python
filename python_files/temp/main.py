from microbit import *

# --- SETUP
# start sensors

# store variables

# --- RUNNING
while True:
    # read sensor data
    temp = temperature()
    
    # process data
    temp = str(temp) + "C"
    
    # output data
    display.scroll(temp)