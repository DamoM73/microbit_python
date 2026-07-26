from microbit import *

# --- SETUP
# start sensors

# store variables

# --- RUNNING
while True:
    # read sensor data
    field = compass.get_field_strength()
    
    # process data
    
    # output data
    display.scroll(field)
    
    sleep(500)
