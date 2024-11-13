from microbit import *

# --- SETUP
# start sensors
pin0.set_touch_mode(pin0.CAPACITIVE)

# store variables

# --- RUNNING
while True:
    # read sensor data
    touched = pin0.is_touched()
    
    # process data
    
    # output data
    if touched:
        display.show(Image.HAPPY)
    else:
        display.show(Image.SAD)
    
    sleep(10)