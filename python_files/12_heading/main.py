from microbit import *

# --- SETUP
# start sensors

# store variables

# --- RUNNING
while True:
    # read sensor data
    heading = compass.heading()
    
    # process data
    
    # output data
    display.scroll(heading)
    
    sleep(500)