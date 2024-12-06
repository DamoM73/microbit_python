from microbit import *

# --- SETUP
# start sensors

# store variables

# --- RUNNING
while True:
    display.show(Image.YES)
    sleep(3000)
    
    # read sensor data
    did_shake = accelerometer.was_gesture("shake")

    # process data
    
    # output data
    if did_shake:
        display.show(Image.HAPPY)
    else:
        display.show(Image.SAD)
        
    sleep(500)
