from microbit import *

# --- SETUP
# start sensors

# store variables

# --- RUNNING
while True:
    # read sensor data
    touched = pin_logo.is_touched()
    
    # process data
    
    # output data
    if touched:
        display.show(Image.HAPPY)
    else:
        display.show(Image.SAD)
    
    sleep(10)