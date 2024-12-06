from microbit import *

# --- SETUP
# start sensors

# store variables

# --- RUNNING
while True:
    # read sensor data
    light_level = display.read_light_level()
    
    # process data
    
    # output data
    display.scroll(light_level)
    
    sleep(500)
    